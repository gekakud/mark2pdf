"""
Base class for PDF generation backends.
"""

from abc import ABC, abstractmethod


class PDFBackend(ABC):
    """Abstract base class for PDF generation backends."""
    
    @abstractmethod
    def html_to_pdf(self, html_content: str, output_path: str) -> None:
        """
        Convert HTML content to PDF.
        
        Args:
            html_content: The HTML content to convert.
            output_path: Path where the PDF will be saved.
        """
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of this backend."""
        pass
