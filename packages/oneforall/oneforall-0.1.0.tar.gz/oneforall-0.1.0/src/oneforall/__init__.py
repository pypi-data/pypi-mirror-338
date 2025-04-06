# src/oneforall/__init__.py
"""
OneForAll: A tool to pack and unpack project files into a single file
for easy sharing and LLM interaction.
"""
__version__ = "0.1.0" # Initial version

from .bundler import pack
from .unbundler import unpack

__all__ = ["pack", "unpack", "__version__"]