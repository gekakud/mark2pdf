"""
Playwright-based PDF backend for Windows.
"""

import tempfile
from pathlib import Path

from .base import PDFBackend


class PlaywrightBackend(PDFBackend):
    """PDF backend using Playwright with Chromium."""
    
    @property
    def name(self) -> str:
        return "playwright"
    
    def html_to_pdf(self, html_content: str, output_path: str) -> None:
        """
        Convert HTML to PDF using Playwright.
        
        Args:
            html_content: The HTML content to convert.
            output_path: Path where the PDF will be saved.
        """
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            raise ImportError(
                "Playwright is not installed. "
                "Install it with: pip install mark2pdf[windows]"
            )
        
        # Write HTML to a temp file
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".html",
            delete=False,
            encoding="utf-8"
        ) as tmp:
            tmp.write(html_content)
            tmp_path = tmp.name
        
        try:
            with sync_playwright() as p:
                # Use installed Chrome browser instead of downloading Chromium
                browser = p.chromium.launch(channel="chrome")
                page = browser.new_page()
                
                # Load the HTML file
                page.goto(f"file:///{tmp_path}")
                
                # Wait for content to render
                page.wait_for_load_state("networkidle")
                
                # Generate PDF
                page.pdf(
                    path=output_path,
                    format="A4",
                    print_background=True,
                    margin={
                        "top": "20mm",
                        "bottom": "20mm",
                        "left": "15mm",
                        "right": "15mm",
                    },
                )
                
                browser.close()
        finally:
            # Clean up temp file
            Path(tmp_path).unlink(missing_ok=True)
