"""
mark2pdf - Markdown to PDF converter with platform-specific backends.

Uses Playwright on Windows, WeasyPrint on Linux.
"""

from .core import mark_convert

__version__ = "0.1.0"
__all__ = ["mark_convert"]
