import json
import logging
import random
import tarfile
import warnings
from collections import Counter, defaultdict
from copy import deepcopy
from functools import partial
from typing import Dict, List, Union, Tuple, Any

import torch
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


from pie import utils, torch_utils, constants
from . import preprocessors

logger = logging.getLogger(__name__)

# Typing utilities
Sentence = List[str]
TaskName = str
Label = str
DictGT = Dict[TaskName, List[Label]]


class LabelEncoder(object):
    """
    Label encoder
    """
    def __init__(self, level='token', name=None, target=None,
                 lower=False, utfnorm=False, utfnorm_type='NFKD', drop_diacritics=False,
                 preprocessor=None, max_size=None, min_freq=1,
                 pad=True, eos=False, bos=False, reserved=(), **meta):

        if level.lower() not in ('token', 'char'):
            raise ValueError("`level` must be 'token' or 'char'. Got ", level)

        self.meta = meta  # dictionary with other task-relevant information
        self.pad = constants.PAD if pad else None
        self.eos = constants.EOS if eos else None
        self.bos = constants.BOS if bos else None
        self.lower = lower
        self.utfnorm = utfnorm
        self.utfnorm_type = utfnorm_type
        self.drop_diacritics = drop_diacritics
        self.text_preprocess_fn = None
        if lower or utfnorm or drop_diacritics:
            self.text_preprocess_fn = self._get_text_preprocess_fn(
                lower, utfnorm, utfnorm_type, drop_diacritics)
        self.preprocessor = preprocessor
        self.preprocessor_fn = \
            getattr(preprocessors, preprocessor) if preprocessor else None
        self.max_size = max_size
        self.min_freq = min_freq
        self.level = level.lower()
        self.target = target
        self.name = name
        self.reserved = reserved + (constants.UNK,)  # always use <unk>
        self.reserved += tuple([sym for sym in [self.eos, self.pad, self.bos] if sym])
        self.freqs = Counter()
        self.known_tokens = set()  # for char-level dicts, keep word-level known tokens
        self.table = None
        self.inverse_table = None
        self.fitted = False

    def _get_text_preprocess_fn(self, lower, utfnorm, utfnorm_type, drop_diacritics):
        fns = []
        if lower:
            fns.append(utils.lower_str)
        if utfnorm:
            fns.append(partial(utils.apply_utfnorm, form=utfnorm_type))
        if drop_diacritics:
            fns.append(utils.drop_diacritics)

        return utils.compose(*fns)

    def __len__(self):
        if not self.fitted:
            raise ValueError("Cannot get length of unfitted LabelEncoder")

        return len(self.table)

    def __eq__(self, other):
        if type(other) != LabelEncoder:
            return False

        return self.pad == other.pad and \
            self.eos == other.eos and \
            self.bos == other.bos and \
            self.preprocessor == other.preprocessor and \
            self.max_size == other.max_size and \
            self.level == other.level and \
            self.lower == other.lower and \
            self.utfnorm == other.utfnorm and \
            self.drop_diacritics == other.drop_diacritics and \
            self.target == other.target and \
            self.freqs == other.freqs and \
            self.table == other.table and \
            self.inverse_table == other.inverse_table and \
            self.fitted == other.fitted

    def __repr__(self):
        try:
            length = len(self)
        except Exception:
            length = 0

        return (
            '<LabelEncoder name="{}" lower="{}" utfnorm="{}" utfnorm_type="{}" ' +
            'target="{}" vocab="{}" level="{}" fitted="{}"/>'
        ).format(
            self.name, self.lower, self.utfnorm, self.utfnorm_type,
            self.target, self.level, length, self.fitted)

    def get_type_stats(self):
        """
        Compute number of known types, total number of types and ratio
        """
        if not self.fitted:
            raise ValueError("Vocabulary hasn't been computed yet")

        total_types = len(self.freqs)
        known_types = len(self) - len(self.reserved)
        return known_types, total_types, known_types / total_types

    def get_token_stats(self):
        """
        Compute number of known tokens, total number of types and ratio
        """
        if not self.fitted:
            raise ValueError("Vocabulary hasn't been computed yet")

        total_tokens = sum(self.freqs.values())
        known_tokens = sum(self.freqs[w] for w in self.table)
        return known_tokens, total_tokens, known_tokens / total_tokens

    def add(self, seq, rseq=None):
        if self.fitted:
            raise ValueError("Already fitted")

        postseq = self.preprocess(seq, rseq)

        if self.level == 'token':
            self.freqs.update(postseq)
        else:
            self.freqs.update(c for tok in postseq for c in tok)
            # always use original sequence for known tokens
            self.known_tokens.update(seq)

    def compute_vocab(self):
        if self.fitted:
            raise ValueError("Cannot compute vocabulary, already fitted")

        if len(self.freqs) == 0:
            logger.warning("Computing vocabulary for empty encoder {}"
                            .format(self.name))

        # Sort freqs by order of frequency, and alphabetically in case of ties
        vocab = sorted(self.freqs.most_common(), key=lambda x: (-x[1], x[0]))

        # Apply min_freq
        if self.min_freq:
            vocab = [it for it in vocab if it[1] >= self.min_freq]

        # Apply max_size
        if self.max_size:
            vocab = vocab[:self.max_size-len(self.reserved)]
        
        # Remove frequencies
        vocab = [sym for sym, _ in vocab]

        self.inverse_table = list(self.reserved) + vocab
        self.table = {sym: idx for idx, sym in enumerate(self.inverse_table)}
        self.fitted = True

    def expand_vocab(self):
        if self.fitted:
            raise ValueError("Cannot expand vocabulary, already fitted")
        
        # Check if there is room to add new symbols
        # size_original_vocab_noreserved = len(self.inverse_table) - len(self.reserved)
        logger.info(f"Original '{self.name}' vocab contains {len(self.inverse_table) - len(self.reserved)} "
                    "entries (reserved not included)")
        if self.max_size:
            nb_indexes_left = self.max_size - len(self.inverse_table)
            if nb_indexes_left == 0:
                logger.warning(
                    f"No room left for new vocab entries in label_encoder '{self.name}', "
                    f"Consider increasing max_size (currently {self.max_size}) to be able "
                    f"to expand the vocabulary with new symbols."
                )
                self.fitted = True
                return
            elif nb_indexes_left < 0:
                nb_indexes_to_remove = -nb_indexes_left
                logger.warning(
                    f"Size of the original vocabulary (incl. reserved) is larger than max_size "
                    f"({len(self.inverse_table)} > {self.max_size}: "
                    f"removing {nb_indexes_to_remove} entries to the vocabulary"
                )
                self.inverse_table = self.inverse_table[:self.max_size]
                self.table = {
                    sym: idx for i, (sym, idx) in enumerate(self.table.items())
                    if i < self.max_size
                }
                self.fitted = True
                return
        else:
            nb_indexes_left = None

        # Get all new symbols, ordered by frequency
        set_original_vocab = set(self.inverse_table)
        new_symbols = [
            (s, freq) for s, freq in self.freqs.most_common() 
            if s not in set_original_vocab
            and freq >= (self.min_freq or 0)
        ]
        # Extract only the desired number of new symbols
        if nb_indexes_left:
            new_symbols = new_symbols[:nb_indexes_left]
        # Append new symbols to the LabelEncoder's vocab attributes
        cur_table_idx = max(self.table.values())
        for sym, _ in new_symbols:
            self.inverse_table.append(sym)
            cur_table_idx += 1
            self.table[sym] = cur_table_idx

        self.fitted = True
        logger.info(f"Added {len(new_symbols)} new entries to the vocabulary of label_encoder '{self.name}'")
    
    def register_upper(self):
        """ Params registers the same vocabulary but in full uppercase

        Important when using the upper strategy
        """
        # Get all new uppercase chars of lowercase chars in the vocab
        inp = self.inverse_table[len(self.reserved):]
        new_chars = list(map(
            lambda x: x.upper(),
            filter(
                lambda x: x.islower() and x.upper() not in inp,
                inp
            )
        ))

        # Remove duplicates (in rare cases, multiple lowercase chars can have the same uppercasing)
        new_chars = list(dict.fromkeys(new_chars))

        # Reduce list of new chars to the number of available slots
        if self.max_size:
            slots_left = self.max_size - len(self.inverse_table)
            if slots_left > 0:                
                if slots_left < len(new_chars):
                    logger.info(f"Could not register all available uppercase {self.name} vocab entries "
                                f"({slots_left} slots < {len(new_chars)} upper chars)")
                else:
                    logger.info(f"All uppercase ({self.name}) vocab registered ({len(new_chars)} new entries)")
                new_chars = new_chars[:min(len(new_chars), slots_left)]
            else:
                if len(new_chars) > 0:
                    logger.info(f"Could not register all available uppercase vocab entries "
                                f"({len(new_chars)} upper {self.name} entries not registered)")
                return # We have too much in the vocab already
        
        # Add new chars to the vocabulary
        self.inverse_table.extend(new_chars)
        self.table = {sym: idx for idx, sym in enumerate(self.inverse_table)}

    def preprocess_text(self, seq):
        """
        Apply surface level preprocessing such as lowering, unicode normalization
        """
        if self.text_preprocess_fn:
            seq = list(map(self.text_preprocess_fn, seq))
        return seq

    def preprocess(self, tseq, rseq=None):
        """
        Full preprocessing pipeline including possible token-level transformations
        """
        tseq = self.preprocess_text(tseq)

        if self.preprocessor_fn is not None:
            if rseq is None:
                raise ValueError("Expected ref sequence for preprocessor")

            return [self.preprocessor_fn.transform(t, r) for t, r in zip(tseq, rseq)]

        return tseq

    def transform(self, seq, rseq=None):
        if not self.fitted:
            raise ValueError("Vocabulary hasn't been computed yet")

        def transform_seq(s):
            output = []
            if self.bos:
                output.append(self.get_bos())

            for tok in s:
                output.append(self.table.get(tok, self.table[constants.UNK]))

            if self.eos:
                output.append(self.get_eos())

            return output

        # preprocess
        seq = self.preprocess(seq, rseq)

        if self.level == 'token':
            output = transform_seq(seq)
        else:
            output = [transform_seq(w) for w in seq]

        return output

    def inverse_transform(self, seq):
        if not self.fitted:
            raise ValueError("Vocabulary hasn't been computed yet")

        return [self.inverse_table[i] for i in seq]

    def stringify(self, seq, length=None):
        if not self.fitted:
            raise ValueError("Vocabulary hasn't been computed yet")

        eos, bos = self.get_eos(), self.get_bos()
        if length is not None:
            if eos is not None or bos is not None:
                warnings.warn("Length was passed to stringify but LabelEncoder "
                              "has <eos> and/or <bos> tokens")
            seq = seq[:length]
        else:
            if eos is None:
                raise ValueError("Don't know how to compute input length")
            try:
                # some generations might fail to produce the <eos> symbol
                seq = seq[:seq.index(eos)]
            except ValueError:
                pass

            # eventually remove <bos> if required
            if bos is not None:
                if len(seq) > 0 and seq[0] == bos:
                    seq = seq[1:]

        return self.inverse_transform(seq)

    def _get_sym(self, sym):
        if not self.fitted:
            raise ValueError("Vocabulary hasn't been computed yet")

        return self.table.get(sym)

    def get_pad(self):
        return self._get_sym(constants.PAD)

    def get_eos(self):
        return self._get_sym(constants.EOS)

    def get_bos(self):
        return self._get_sym(constants.BOS)

    def get_unk(self):
        return self._get_sym(constants.UNK)

    def jsonify(self):
        if not self.fitted:
            raise ValueError("Attempted to serialize unfitted encoder")

        return {'name': self.name,
                'eos': self.eos,
                'bos': self.bos,
                'pad': self.pad,
                'meta': self.meta,
                'level': self.level,
                'preprocessor': self.preprocessor,
                'lower': self.lower,
                'utfnorm': self.utfnorm,
                'utfnorm_type': self.utfnorm_type,
                'drop_diacritics': self.drop_diacritics,
                'target': self.target,
                'max_size': self.max_size,
                'min_freq': self.min_freq,
                'freqs': dict(self.freqs),
                'table': dict(self.table),
                'inverse_table': self.inverse_table,
                'known_tokens': list(self.known_tokens)}

    @classmethod
    def from_json(cls, obj):
        inst = cls(pad=obj['pad'], eos=obj['eos'], bos=obj['bos'],
                   level=obj['level'], target=obj['target'], lower=obj['lower'],
                   max_size=obj['max_size'], min_freq=obj['min_freq'],
                   drop_diacritics=obj.get('drop_diacritics', False),
                   utfnorm=obj.get('utfnorm', False),
                   utfnorm_type=obj.get('utfnorm_type', False),
                   preprocessor=obj.get('preprocessor'),
                   name=obj['name'], meta=obj.get('meta', {}))
        inst.freqs = Counter(obj['freqs'])
        inst.table = dict(obj['table'])
        inst.inverse_table = list(obj['inverse_table'])
        inst.known_tokens = set(obj['known_tokens'])
        inst.fitted = True

        return inst


class MultiLabelEncoder(object):
    """
    Complex Label encoder for all tasks.
    """
    def __init__(self, word_max_size=None, word_min_freq=1, word_lower=False,
                 char_max_size=None, char_min_freq=None, char_lower=False,
                 char_eos=True, char_bos=True, utfnorm=False, utfnorm_type='NFKD',
                 drop_diacritics=False, noise_strategies = None):
        self.word = LabelEncoder(max_size=word_max_size, min_freq=word_min_freq,
                                 lower=word_lower, utfnorm=utfnorm,
                                 utfnorm_type=utfnorm_type,
                                 drop_diacritics=drop_diacritics, name='word')
        self.char = LabelEncoder(max_size=char_max_size, min_freq=char_min_freq,
                                 level='char', lower=char_lower, name='char',
                                 eos=char_eos, bos=char_bos, utfnorm_type=utfnorm_type,
                                 utfnorm=utfnorm, drop_diacritics=drop_diacritics)
        self.tasks = {}
        self.nsents = None
        self.noise_strategies = noise_strategies or {}

    @property
    def all_label_encoders(self):
        return [self.word, self.char] + list(self.tasks.values())

    def __repr__(self):
        return (
            '<MultiLabelEncoder>\n\t' +
            '\n\t'.join(map(str, [self.word, self.char] + list(self.tasks.values()))) +
            '\n</MultiLabelEncoder>')

    def __eq__(self, other):
        if not (self.word == other.word and self.char == other.char):
            return False

        for task in self.tasks:
            if task not in other.tasks:
                return False
            if self.tasks[task] != other.tasks[task]:
                return False

        return True

    def add_task(self, name, **meta):
        self.tasks[name] = LabelEncoder(name=name, **meta)

        # check <eos> <bos> (not suitable for linear models)
        if meta['level'].lower() != 'char' and (meta.get('eos') or meta.get('bos')):
            raise ValueError(
                ('[Task: {task}] => `bos` and `eos` options are '
                 'only compatible with char-level tasks but got '
                 'level: "{level}". Aborting!!!').format(
                    task=name, level=meta['level']))

        return self

    @classmethod
    def from_settings(cls, settings, tasks=None):
        le = cls(word_max_size=settings.word_max_size,
                 word_min_freq=settings.word_min_freq,
                 word_lower=settings.word_lower,
                 char_max_size=settings.char_max_size,
                 char_min_freq=settings.char_min_freq,
                 char_lower=settings.char_lower,
                 char_eos=settings.char_eos,
                 char_bos=settings.char_bos,
                 utfnorm=settings.utfnorm,
                 utfnorm_type=settings.utfnorm_type,
                 drop_diacritics=settings.drop_diacritics,
                 noise_strategies=settings.noise_strategies)

        for task in settings.tasks:
            if tasks is not None and task['settings']['target'] not in tasks:
                raise ValueError("No available data for task [{}]".format(
                    task['settings']['target']))
            le.add_task(task['name'], level=task['level'], **task['settings'])

        return le

    def fit(self, lines, expand_mode=False, skip_fitted=False):
        """
        Fit all LabelEncoder objects contained in this instance on the given data to create their label-to-id tables

        Parameters
        ===========
        lines (iterator): tuples of (Input, Tasks)
        expand_mode (bool): True to continue fitting all LabelEncoders with new data,
            keeping all labels already assigned and adding new ones as seen in the new data.
        skip_fitted (bool): True to skip already fitted label encoders instead of raising an error.
            skip_fitted and expand_mode are exclusive.
        """
        assert not (expand_mode and skip_fitted), "parameters expand_mode and skip_fitted are exclusive"
        lencs_to_update = self.all_label_encoders
        if expand_mode is True:
            lencs_to_expand = [le for le in lencs_to_update if le.fitted is True]
            lencs_to_fit = [le for le in lencs_to_update if le not in lencs_to_expand]
            if lencs_to_fit:
                logger.warning(
                    f"Expanding only the label encoders {lencs_to_expand} "
                    f"and fitting the rest from scratch {lencs_to_fit}")
            for le in lencs_to_expand:
                le.fitted = False
        else:
            if skip_fitted:
                lencs_to_update = [le for le in lencs_to_update if le.fitted is False]
                if not lencs_to_update:
                    logger.info("All label encoders have been fitted already !")
                    return self
            lencs_to_expand = []
            lencs_to_fit = lencs_to_update

        for inp in lines:
            tasks = None
            if isinstance(inp, tuple):
                inp, tasks = inp

            # input
            if self.word in lencs_to_update:
                self.word.add(inp)
            if self.char in lencs_to_update:
                self.char.add(inp)

            for le in self.tasks.values():
                if le not in lencs_to_update:
                    continue
                le.add(tasks[le.target], inp)

        for le in lencs_to_fit:
            le.compute_vocab()
        
        for le in lencs_to_expand:
            le.expand_vocab()

        if self.noise_strategies["uppercase"]["apply"]:
            self.word.register_upper()
            self.char.register_upper()

        return self

    def fit_reader(self, reader, expand_mode=False, skip_fitted=False):
        """
        fit reader in a non verbose way (to warn about parsing issues)
        """
        return self.fit(
            (line for (_, line) in reader.readsents(silent=False)),
            expand_mode=expand_mode,
            skip_fitted=skip_fitted)

    def transform(self, sents: Union[List[Sentence], List[Tuple[Sentence, DictGT]]]):
        """
        Parameters
        ===========
        sents : list of Example's

        Returns
        ===========
        tuple of (word, char), task_dict

            - word: list of integers
            - char: list of integers where each list represents a word at the
                character level
            - task_dict: Dict to corresponding integer output for each task
        """
        word, char, tasks_dict = [], [], defaultdict(list)

        for inp in sents:
            tasks = None

            # task might not be passed
            if isinstance(inp, tuple):
                inp, tasks = inp

            # input data
            word.append(self.word.transform(inp))
            char.extend(self.char.transform(inp))

            # task data
            if tasks is None:
                # during inference there is no task data (pass None)
                continue

            for le in self.tasks.values():
                task_data = le.transform(tasks[le.target], inp)
                # add data
                if le.level == 'char':
                    tasks_dict[le.name].extend(task_data)
                else:
                    tasks_dict[le.name].append(task_data)

        return (word, char), tasks_dict

    def jsonify(self):
        return {'word': self.word.jsonify(),
                'char': self.char.jsonify(),
                'tasks': {le.name: le.jsonify() for le in self.tasks.values()}}

    def save(self, path):
        with open(path, 'w+') as f:
            yaml.dump(self.jsonify(), f, Dumper=Dumper)

    @staticmethod
    def _init(inst, obj):
        inst.word = LabelEncoder.from_json(obj['word'])
        inst.char = LabelEncoder.from_json(obj['char'])

        for task, le in obj['tasks'].items():
            inst.tasks[task] = LabelEncoder.from_json(le)

        return inst

    @classmethod
    def load_from_string(cls, string):
        inst = cls()
        try:
            obj = json.loads(string)
        except ValueError:      # use yaml
            obj = yaml.load(string, Loader=Loader)
        return cls._init(inst, obj)

    @classmethod
    def load_from_file(cls, path):
        with open(path, 'r+') as f:
            return cls.load_from_string(f.read())

    @classmethod
    def load_from_pretrained_model(cls, path, new_settings=None, tasks=None):

        def copy_pretrained_le(pretrained_le, new_le):
            new_attrs_to_keep = deepcopy({
                "lower": new_le.lower,
                "utfnorm": new_le.utfnorm,
                "utfnorm_type": new_le.utfnorm_type,
                "drop_diacritics": new_le.drop_diacritics,
                "text_preprocess_fn": new_le.text_preprocess_fn,
                "preprocessor": new_le.preprocessor,
                "preprocessor_fn": new_le.preprocessor_fn,
                "max_size": new_le.max_size,
                "min_freq": new_le.min_freq,
                "target": new_le.target
            })
            new_le = deepcopy(pretrained_le)
            for attr_key, attr_val in new_attrs_to_keep.items():
                setattr(new_le, attr_key, attr_val)
            
            return new_le

        with tarfile.open(utils.ensure_ext(path, 'tar'), 'r') as tar:
            label_encoder_pretrained = cls.load_from_string(utils.get_gzip_from_tar(tar, 'label_encoder.zip'))
        
        if not new_settings:
            return label_encoder_pretrained
        else:
            # Create another MultiLabelEncoder to import the new settings
            # As the saved pretrained MultiLabelEncoder doesn't contain all settings,
            # for instance noise strategies
            new_multilabel_encoder = MultiLabelEncoder.from_settings(new_settings, tasks=tasks)

            new_multilabel_encoder.word = copy_pretrained_le(
                label_encoder_pretrained.word, new_multilabel_encoder.word)
            new_multilabel_encoder.char = copy_pretrained_le(
                label_encoder_pretrained.char, new_multilabel_encoder.char)

            for tname in tasks:
                task_name = tname
                if task_name in label_encoder_pretrained.tasks:
                    new_multilabel_encoder.tasks[task_name] = copy_pretrained_le(
                        label_encoder_pretrained.tasks[task_name], new_multilabel_encoder.tasks[task_name])
                else:
                    # search with lowercased tasks
                    found_normalized_task = False
                    for pretrained_task_name, pretrained_task_le in label_encoder_pretrained.tasks.items():
                        if task_name.lower() == pretrained_task_name.lower():
                            new_multilabel_encoder.tasks[task_name] = copy_pretrained_le(
                                pretrained_task_le, new_multilabel_encoder.tasks[task_name])
                            new_multilabel_encoder.tasks[task_name].name = task_name
                            found_normalized_task = True
                            logger.warning(
                                f"Task {task_name} not found in the pretrained label encoder, "
                                f"but {pretrained_task_name} was found and will be loaded in "
                                f"task {task_name}.")
                            break
                    if not found_normalized_task:
                        logger.warning(f"Task {task_name} not found in the pretrained label encoder.")
            
            return new_multilabel_encoder


class Dataset(object):
    """
    Dataset class to encode files into integers and compute batches.

    Settings
    ===========
    buffer_size : int, maximum number of sentences in memory at any given time.
       The larger the buffer size the more memory instensive the dataset will
       be but also the more effective the shuffling over instances.
    batch_size : int, number of sentences per batch
    device : str, target device to put the processed batches on
    shuffle : bool, whether to shuffle items in the buffer
    minimize_pad : bool, whether to pack batches with sentences of similar length
       in order to minimize padding.

    Parameters
    ===========
    input_path : str (optional), either a path to a directory, a path to a file
        or a unix style pathname pattern expansion for glob. If given, the
        input_path in settings will be overwritten by the new value
    label_encoder : optional, prefitted LabelEncoder object
    """
    def __init__(self, settings, reader, label_encoder):

        if settings.batch_size > settings.buffer_size:
            raise ValueError("Not enough buffer capacity {} for batch_size of {}"
                             .format(settings.buffer_size, settings.batch_size))

        # attributes
        self.buffer_size = settings.buffer_size
        self.batch_size = settings.batch_size
        self.device = settings.device
        self.shuffle = settings.shuffle
        self.minimize_pad = settings.minimize_pad
        self.cache_dataset = settings.cache_dataset

        # data
        self.reader = reader
        self.label_encoder = label_encoder
        self.cached = []

    @staticmethod
    def get_nelement(batch):
        """
        Returns the number of elements in a batch (based on word-level length)
        """
        return batch[0][0][1].sum().item()

    def pack_batch(self, batch, device=None):
        """
        Transform batch data to tensors
        """
        return pack_batch(self.label_encoder, batch, device or self.device)

    def prepare_buffer(self, buf, return_raw=False, **kwargs):
        "Transform buffer into batch generator"

        def key(data):
            inp, tasks = data
            return len(inp)

        if self.minimize_pad:
            buf = sorted(buf, key=key, reverse=True)
        elif self.shuffle:
            random.shuffle(buf)

        batches = list(utils.chunks(buf, self.batch_size))

        if self.shuffle:
            random.shuffle(batches)

        for batch in batches:
            packed = self.pack_batch(batch, **kwargs)
            if return_raw:
                inp, tasks = zip(*batch)
                yield packed, (inp, tasks)
            else:
                yield packed

    def _batch_generator_cached(self, return_raw=False):
        """
        Generator over dataset batches. Each batch is a tuple of (input, tasks):
            * (word, char)
                - word : tensor(length, batch_size), padded lengths
                - char : tensor(length, batch_size * words), padded lengths
            * (tasks) dictionary with tasks
        """
        if self.cache_dataset:
            if not self.cached:
                self.cache_batches()
            if self.shuffle:
                random.shuffle(self.cached)

            for batch, raw in self.cached:
                # move to device
                batch = tuple(list(wrap_device(batch, self.device)))
                if return_raw:
                    yield batch, raw
                else:
                    yield batch
        else:
            yield from self.batch_generator_(return_raw=return_raw)

    def _get_noised_batch(self, raw_words, raw_targets, apply_noise: Dict[str, Dict[str, Any]]):
        """

        """
        raw_words = list(raw_words)  # Was a Tuple before

        # Run N strategies per N sentences rand on the range [0.00:1.00(
        apply_strategies = torch.rand(len(apply_noise), len(raw_words))

        # Iterate over strategies
        for strat_id, (strat_name, strategy) in enumerate(apply_noise.items()):
            targets = (apply_strategies[strat_id] < strategy.get("ratio", 0)).nonzero(as_tuple=True)

            if not len(targets):
                continue

            changed_index = targets[0].tolist()

            for index, sent, truth in zip(
                    changed_index,
                    map(raw_words.__getitem__, changed_index),
                    map(raw_targets.__getitem__, changed_index)
            ):
                raw_words[index] = getattr(NoiseStrategies, strat_name)(
                    sent,
                    tasks=changed_index,
                    **strategy.get("params", {})
                )

        # Recreate a batch
        return self.pack_batch(list(zip(raw_words, raw_targets)), device=self.device)

    def batch_generator(self, return_raw=False, apply_noise=None):
        """
        Generator over dataset batches. Each batch is a tuple of (input, tasks):
            * (word, char)
                - word : tensor(length, batch_size), padded lengths
                - char : tensor(length, batch_size * words), padded lengths
            * (tasks) dictionary with tasks
        """
        if apply_noise or return_raw:
            for batch, raw in self._batch_generator_cached(return_raw=True):
                if apply_noise:  # If we need to apply noise
                    batch = self._get_noised_batch(*raw, apply_noise=apply_noise)
                if return_raw:
                    # Batch = ((word, wlen), (char, clen)), tasks
                    # Raw Tuple[List[words], Tuple[Dict[task, List[gold]]...]]
                    # For each strategy
                        # Index = list(range(0, len(raw[0])+1), get N random
                        # Then for each index, -> strategy(raw[0][1])
                        # Batch[0] -> apply on word and char reusing index
                    yield batch, raw
                else:
                    yield batch
        else:
            yield from self._batch_generator_cached(return_raw=False)

    def batch_generator_(self, return_raw=False):
        buf = []
        for (fpath, line_num), data in self.reader.readsents():

            # fill buffer
            buf.append(data)

            # check if buffer is full and yield
            if len(buf) == self.buffer_size:
                yield from self.prepare_buffer(buf, return_raw=return_raw)
                buf = []

        if len(buf) > 0:
            yield from self.prepare_buffer(buf, return_raw=return_raw)

    def cache_batches(self):
        if self.cached:
            return

        buf = [data for _, data in self.reader.readsents()]
        for batch, raw in self.prepare_buffer(buf, return_raw=True, device='cpu'):
            self.cached.append((batch, raw))


def pack_batch(label_encoder, batch, device=None):
    """
    Transform batch data to tensors
    """
    (word, char), tasks = label_encoder.transform(batch)

    word = torch_utils.pad_batch(word, label_encoder.word.get_pad(), device=device)
    char = torch_utils.pad_batch(char, label_encoder.char.get_pad(), device=device)

    output_tasks = {}
    for task, data in tasks.items():
        output_tasks[task] = torch_utils.pad_batch(
            data, label_encoder.tasks[task].get_pad(), device=device)

    return (word, char), output_tasks


def wrap_device(it, device):
    for i in it:
        if isinstance(i, torch.Tensor):
            yield i.to(device)
        elif isinstance(i, dict):
            yield {k: tuple(wrap_device(v, device)) for k, v in i.items()}
        else:
            yield tuple(wrap_device(i, device))


class device_wrapper(object):
    def __init__(self, batches, device):
        self.batches = batches
        self.device = device

    def __getitem__(self, idx):
        return tuple(wrap_device(self.batches[idx], self.device))

    def __len__(self):
        return len(self.batches)


class NoiseStrategies:
    @staticmethod
    def uppercase(inp: Sentence, tasks: DictGT = None, **kwargs) -> List[str]:
        return list(map(str.upper, inp))
