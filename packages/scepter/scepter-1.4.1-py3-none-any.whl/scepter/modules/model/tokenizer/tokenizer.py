# -*- coding: utf-8 -*-
# Copyright (c) Alibaba, Inc. and its affiliates.
import open_clip
from transformers import CLIPTokenizer as transformer_clip_tokenizer

from scepter.modules.model.registry import TOKENIZERS
from scepter.modules.model.tokenizer import BaseTokenizer
from scepter.modules.model.tokenizer.tokenizer_component import (
    basic_clean, canonicalize, whitespace_clean)
from scepter.modules.utils.config import dict_to_yaml
from scepter.modules.utils.file_system import FS


@TOKENIZERS.register_class()
class HuggingfaceTokenizer(BaseTokenizer):
    para_dict = {
        'PRETRAINED_PATH': {
            'value': '',
            'description': "Huggingface tokenizer's pretrained path."
        },
        'LENGTH': {
            'value': 77,
            'description': "The input prompt's length."
        },
        'CLEAN': {
            'value': True,
            'description': 'Clean the special chars or not.'
        }
    }

    def __init__(self, cfg, logger=None):
        super().__init__(cfg, logger=logger)
        self.pretrained_path = cfg.get('PRETRAINED_PATH', 'xlm-roberta-large')
        self.length = cfg.get('LENGTH', 77)
        self.clean = cfg.get('CLEAN', 'whitespace')
        assert self.clean in (None, 'whitespace', 'lower', 'canonicalize')

        # init tokenizer
        from transformers import AutoTokenizer
        with FS.get_dir_to_local_dir(self.pretrained_path) as local_path:
            self.tokenizer = AutoTokenizer.from_pretrained(local_path)

        self.vocab_size = len(
            self.tokenizer)  # self.vocab_size = self.tokenizer.vocab_size

        # special tokens
        self.comma_token = self.tokenizer(',')['input_ids'][
            2]  # same as CN comma
        self.sos_token = self.tokenizer(
            self.tokenizer.bos_token)['input_ids'][1]
        self.eos_token = self.tokenizer(
            self.tokenizer.eos_token)['input_ids'][1]
        self.pad_token = self.tokenizer(
            self.tokenizer.pad_token)['input_ids'][1]

    def __call__(self, sequence, **kwargs):
        # arguments
        return_mask = kwargs.pop('return_mask', False)
        _kwargs = {'return_tensors': 'pt'}
        if self.length is not None:
            _kwargs.update({
                'padding': 'max_length',
                'truncation': True,
                'max_length': self.length
            })
        _kwargs.update(**kwargs)

        # tokenization
        if isinstance(sequence, str):
            sequence = [sequence]
        if self.clean:
            sequence = [self._clean(u) for u in sequence]
        tokens = self.tokenizer(sequence, **_kwargs)

        # output
        if return_mask:
            return tokens.input_ids, tokens.attention_mask
        else:
            return tokens.input_ids

    def _clean(self, text):
        if self.clean == 'whitespace':
            text = whitespace_clean(basic_clean(text))
        elif self.clean == 'lower':
            text = whitespace_clean(basic_clean(text)).lower()
        elif self.clean == 'canonicalize':
            text = canonicalize(basic_clean(text))
        return text

    @staticmethod
    def get_config_template():
        return dict_to_yaml('TOKENIZERS',
                            __class__.__name__,
                            HuggingfaceTokenizer.para_dict,
                            set_name=True)


@TOKENIZERS.register_class()
class ClipTokenizer(BaseTokenizer):
    para_dict = {
        'PRETRAINED_PATH': {
            'value': '',
            'description': "Huggingface tokenizer's pretrained path."
        },
        'LENGTH': {
            'value': 77,
            'description': "The input prompt's length."
        },
        'CLEAN': {
            'value': True,
            'description': 'Clean the special chars or not.'
        }
    }

    def __init__(self, cfg, logger=None):
        super().__init__(cfg, logger=logger)
        self.pretrained_path = cfg.get('PRETRAINED_PATH', 'xlm-roberta-large')
        self.length = cfg.get('LENGTH', 77)
        self.clean = cfg.get('CLEAN', True)
        with FS.get_dir_to_local_dir(self.pretrained_path,
                                     wait_finish=True) as local_path:
            self.tokenizer = transformer_clip_tokenizer.from_pretrained(
                local_path)
        self.vocab_size = len(self.tokenizer)
        # special tokens
        self.comma_token = self.tokenizer(',')['input_ids'][
            2]  # same as CN comma
        self.sos_token = self.tokenizer(
            self.tokenizer.bos_token)['input_ids'][1]
        self.eos_token = self.tokenizer(
            self.tokenizer.eos_token)['input_ids'][1]
        self.pad_token = self.tokenizer(
            self.tokenizer.pad_token)['input_ids'][1]

    def __call__(self, sequence, **kwargs):
        # arguments
        batch_encoding = self.tokenizer(sequence,
                                        truncation=True,
                                        max_length=self.length,
                                        return_length=True,
                                        return_overflowing_tokens=False,
                                        padding='max_length',
                                        return_tensors='pt')
        return batch_encoding['input_ids']

    @staticmethod
    def get_config_template():
        return dict_to_yaml('TOKENIZERS',
                            __class__.__name__,
                            ClipTokenizer.para_dict,
                            set_name=True)


@TOKENIZERS.register_class()
class OpenClipTokenizer(BaseTokenizer):
    para_dict = {
        'LENGTH': {
            'value': 77,
            'description': "The input prompt's length."
        }
    }

    def __init__(self, cfg, logger=None):
        super().__init__(cfg, logger=logger)
        self.length = cfg.get('LENGTH', 77)
        self.vocab_size = open_clip.tokenizer._tokenizer.vocab_size

    def __call__(self, sequence, **kwargs):
        # arguments
        tokens = open_clip.tokenize(sequence)
        return tokens

    @staticmethod
    def get_config_template():
        return dict_to_yaml('TOKENIZERS',
                            __class__.__name__,
                            OpenClipTokenizer.para_dict,
                            set_name=True)
