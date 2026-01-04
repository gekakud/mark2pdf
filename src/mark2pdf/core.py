"""
Core module for Markdown to PDF conversion.
"""

import os
from pathlib import Path
from typing import Optional

import markdown

from .backends import get_backend


def get_default_css() -> str:
    """Load the default CSS stylesheet."""
    css_path = Path(__file__).parent / "styles" / "default.css"
    if css_path.exists():
        return css_path.read_text(encoding="utf-8")
    return ""


def md_to_html(md_content: str) -> str:
    """Convert Markdown content to HTML."""
    html_body = markdown.markdown(
        md_content,
        extensions=["tables", "fenced_code", "codehilite", "toc"],
    )
    
    css = get_default_css()
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
{css}
    </style>
</head>
<body>
{html_body}
</body>
</html>"""
    
    return html


def mark_convert(
    pdf_file_path: str,
    md_file_path: Optional[str] = None,
    md_content: Optional[str] = None,
    css_file_path: Optional[str] = None,
) -> None:
    """
    Convert Markdown to PDF.
    
    Args:
        pdf_file_path: Output PDF file path.
        md_file_path: Path to input Markdown file.
        md_content: Markdown content as string (alternative to md_file_path).
        css_file_path: Optional custom CSS file path.
    
    Raises:
        ValueError: If neither md_file_path nor md_content is provided.
        FileNotFoundError: If md_file_path doesn't exist.
    """
    if md_file_path is None and md_content is None:
        raise ValueError("Either md_file_path or md_content must be provided")
    
    if md_file_path is not None:
        md_path = Path(md_file_path)
        if not md_path.exists():
            raise FileNotFoundError(f"Markdown file not found: {md_file_path}")
        md_content = md_path.read_text(encoding="utf-8")
    
    # Convert Markdown to HTML
    html_content = md_to_html(md_content)
    
    # Inject custom CSS if provided
    if css_file_path:
        css_path = Path(css_file_path)
        if css_path.exists():
            custom_css = css_path.read_text(encoding="utf-8")
            html_content = html_content.replace(
                "</style>",
                f"\n{custom_css}\n    </style>"
            )
    
    # Get the appropriate backend and generate PDF
    backend = get_backend()
    backend.html_to_pdf(html_content, pdf_file_path)
