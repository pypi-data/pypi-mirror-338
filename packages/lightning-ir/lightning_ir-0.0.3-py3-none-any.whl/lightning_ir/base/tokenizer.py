"""
Tokenizer module for Lightning IR.

This module contains the main tokenizer class for the Lightning IR library.
"""

import json
from os import PathLike
from typing import Dict, Sequence, Tuple, Type

from transformers import TOKENIZER_MAPPING, BatchEncoding, PreTrainedTokenizerBase

from .class_factory import LightningIRTokenizerClassFactory
from .config import LightningIRConfig
from .external_model_hub import CHECKPOINT_MAPPING


class LightningIRTokenizer(PreTrainedTokenizerBase):
    """Base class for Lightning IR tokenizers. Derived classes implement the tokenize method for handling query
    and document tokenization. It acts as mixin for a transformers.PreTrainedTokenizer_ backbone tokenizer.

    .. _transformers.PreTrainedTokenizer: \
https://huggingface.co/transformers/main_classes/tokenizer.htmltransformers.PreTrainedTokenizer
    """

    config_class: Type[LightningIRConfig] = LightningIRConfig
    """Configuration class for the tokenizer."""

    def __init__(self, *args, query_length: int = 32, doc_length: int = 512, **kwargs):
        """Initializes the tokenizer.

        :param query_length: Maximum number of tokens per query, defaults to 32
        :type query_length: int, optional
        :param doc_length: Maximum number of tokens per document, defaults to 512
        :type doc_length: int, optional
        """
        super().__init__(*args, **kwargs)
        self.query_length = query_length
        self.doc_length = doc_length

    def tokenize(
        self, queries: str | Sequence[str] | None = None, docs: str | Sequence[str] | None = None, **kwargs
    ) -> Dict[str, BatchEncoding]:
        """Tokenizes queries and documents.

        :param queries: Queries to tokenize, defaults to None
        :type queries: str | Sequence[str] | None, optional
        :param docs: Documents to tokenize, defaults to None
        :type docs: str | Sequence[str] | None, optional
        :raises NotImplementedError: Must be implemented by the derived class
        :return: Dictionary of tokenized queries and documents
        :rtype: Dict[str, BatchEncoding]
        """
        raise NotImplementedError

    @classmethod
    def from_pretrained(cls, model_name_or_path: str, *args, **kwargs) -> "LightningIRTokenizer":
        """Loads a pretrained tokenizer. Wraps the transformers.PreTrainedTokenizer.from_pretrained_ method to return a
        derived LightningIRTokenizer class. See :class:`.LightningIRTokenizerClassFactory` for more details.

        .. _transformers.PreTrainedTokenizer.from_pretrained: \
https://huggingface.co/docs/transformers/main_classes/tokenizer.html#transformers.PreTrainedTokenizer.from_pretrained

        .. highlight:: python
        .. code-block:: python

            >>> Loading using model class and backbone checkpoint
            >>> type(BiEncoderTokenizer.from_pretrained("bert-base-uncased"))
            ...
            <class 'lightning_ir.base.class_factory.BiEncoderBertTokenizerFast'>
            >>> Loading using base class and backbone checkpoint
            >>> type(LightningIRTokenizer.from_pretrained("bert-base-uncased", config=BiEncoderConfig()))
            ...
            <class 'lightning_ir.base.class_factory.BiEncoderBertTokenizerFast'>

        :param model_name_or_path: Name or path of the pretrained tokenizer
        :type model_name_or_path: str
        :raises ValueError: If called on the abstract class :class:`LightningIRTokenizer` and no config is passed
        :return: A derived LightningIRTokenizer consisting of a backbone tokenizer and a LightningIRTokenizer mixin
        :rtype: LightningIRTokenizer
        """
        # provides AutoTokenizer.from_pretrained support
        config = kwargs.pop("config", None)
        if config is not None:
            kwargs.update(config.to_tokenizer_dict())
        if cls is LightningIRTokenizer or all(issubclass(base, LightningIRTokenizer) for base in cls.__bases__):
            # no backbone models found, create derived lightning-ir tokenizer based on backbone model
            if config is not None:
                Config = config.__class__
            elif model_name_or_path in CHECKPOINT_MAPPING:
                _config = CHECKPOINT_MAPPING[model_name_or_path]
                Config = _config.__class__
                kwargs.update(_config.to_tokenizer_dict())
            elif cls is not LightningIRTokenizer and hasattr(cls, "config_class"):
                Config = cls.config_class
            else:
                Config = LightningIRTokenizerClassFactory.get_lightning_ir_config(model_name_or_path)
                if Config is None:
                    raise ValueError("Pass a config to `from_pretrained`.")
            Config = getattr(Config, "mixin_config", Config)
            BackboneConfig = LightningIRTokenizerClassFactory.get_backbone_config(model_name_or_path)
            BackboneTokenizers = TOKENIZER_MAPPING[BackboneConfig]
            if kwargs.get("use_fast", True):
                BackboneTokenizer = BackboneTokenizers[1]
            else:
                BackboneTokenizer = BackboneTokenizers[0]
            cls = LightningIRTokenizerClassFactory(Config).from_backbone_class(BackboneTokenizer)
            return cls.from_pretrained(model_name_or_path, *args, **kwargs)
        return super(LightningIRTokenizer, cls).from_pretrained(model_name_or_path, *args, **kwargs)

    def _save_pretrained(
        self,
        save_directory: str | PathLike,
        file_names: Tuple[str],
        legacy_format: bool | None = None,
        filename_prefix: str | None = None,
    ) -> Tuple[str]:
        # bit of a hack to change the tokenizer class in the stored tokenizer config to only contain the
        # lightning_ir tokenizer class (removing the backbone tokenizer class)
        save_files = super()._save_pretrained(save_directory, file_names, legacy_format, filename_prefix)
        config_file = save_files[0]
        with open(config_file, "r") as file:
            tokenizer_config = json.load(file)

        tokenizer_class = None
        backbone_tokenizer_class = None
        for base in self.__class__.__bases__:
            if issubclass(base, LightningIRTokenizer):
                if tokenizer_class is not None:
                    raise ValueError("Multiple Lightning IR tokenizer classes found.")
                tokenizer_class = base.__name__
                continue
            if issubclass(base, PreTrainedTokenizerBase):
                backbone_tokenizer_class = base.__name__

        tokenizer_config["tokenizer_class"] = tokenizer_class
        tokenizer_config["backbone_tokenizer_class"] = backbone_tokenizer_class

        with open(config_file, "w") as file:
            out_str = json.dumps(tokenizer_config, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
            file.write(out_str)
        return save_files
