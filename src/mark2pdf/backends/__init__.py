"""
Backend selection based on platform.
"""

import platform
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import PDFBackend


def get_backend() -> "PDFBackend":
    """
    Get the appropriate PDF backend for the current platform.
    
    Returns:
        PDFBackend: Platform-specific PDF backend instance.
        
    Raises:
        ImportError: If the required backend is not installed.
        RuntimeError: If the platform is not supported.
    """
    system = platform.system()
    
    if system == "Windows":
        from .playwright_backend import PlaywrightBackend
        return PlaywrightBackend()
    
    elif system == "Linux":
        from .weasyprint_backend import WeasyPrintBackend
        return WeasyPrintBackend()
    
    else:
        # For other platforms (macOS, etc.), try WeasyPrint first, then Playwright
        try:
            from .weasyprint_backend import WeasyPrintBackend
            # Verify it's actually installed
            import weasyprint  # noqa: F401
            return WeasyPrintBackend()
        except ImportError:
            pass
        
        try:
            from .playwright_backend import PlaywrightBackend
            import playwright  # noqa: F401
            return PlaywrightBackend()
        except ImportError:
            pass
        
        raise RuntimeError(
            f"No PDF backend available for {system}. "
            "Install with: pip install mark2pdf[windows] or pip install mark2pdf[linux]"
        )


__all__ = ["get_backend"]
