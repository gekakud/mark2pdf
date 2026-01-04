"""
WeasyPrint-based PDF backend for Linux.
"""

from .base import PDFBackend


class WeasyPrintBackend(PDFBackend):
    """PDF backend using WeasyPrint."""
    
    @property
    def name(self) -> str:
        return "weasyprint"
    
    def html_to_pdf(self, html_content: str, output_path: str) -> None:
        """
        Convert HTML to PDF using WeasyPrint.
        
        Args:
            html_content: The HTML content to convert.
            output_path: Path where the PDF will be saved.
        """
        try:
            from weasyprint import HTML
        except ImportError:
            raise ImportError(
                "WeasyPrint is not installed. "
                "Install it with: pip install mark2pdf[linux]"
            )
        
        # Convert HTML string to PDF
        html_doc = HTML(string=html_content)
        html_doc.write_pdf(output_path)
