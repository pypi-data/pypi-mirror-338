"""Top-level package for t-proxy."""

__author__ = """Thoughtful"""
__email__ = "support@thoughtful.ai"
__version__ = "0.2.1"

from .t_proxy import (
    BrowserProxy,
    RequestsProxy,
)

__all__ = ["BrowserProxy", "RequestsProxy"]
