"""
Insider - Python Code Obfuscation Library
"""

from .core.obfuscator import Obfuscator
from .core.transformers import (
    VariableRenamer,
    StringObfuscator,
    ImportObfuscator, 
    CommentRemover,
    MarshallTransformer,
    ZlibTransformer
)
from .encryption import MarshallEncoder, ZlibCompressor

__version__ = "1.1.0"
__author__ = "exsarorrayzer"

__all__ = [
    'Obfuscator',
    'VariableRenamer',
    'StringObfuscator',
    'ImportObfuscator',
    'CommentRemover', 
    'MarshallTransformer',
    'ZlibTransformer',
    'MarshallEncoder',
    'ZlibCompressor'
]