"""
LlamaForge - Ultimate Language Model Command Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LlamaForge is a powerful command-line tool and Python library designed to streamline
working with large language models. It provides a unified interface for managing,
running, and optimizing various language models from different providers.

Basic usage:

    >>> from llamaforge import LlamaForge
    >>> forge = LlamaForge()
    >>> response = forge.generate("Explain quantum computing in simple terms")
    >>> print(response)

:copyright: (c) 2023 by LlamaSearch AI.
:license: MIT, see LICENSE for more details.
"""

__version__ = "0.2.0"

from .forge import LlamaForge
from .model import Model

__all__ = ["LlamaForge", "Model"] 