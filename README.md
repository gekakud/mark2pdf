# mark2pdf

A Python library for converting Markdown files to PDF with cross-platform support.

## Features

- **Cross-platform**: Automatically selects the best PDF rendering backend for your OS
- **Simple API**: One function to convert Markdown to PDF

## Installation

### Windows

```bash
pip install mark2pdf[windows]
```

This installs Playwright, which uses your installed Chrome browser for PDF generation.

### Linux

```bash
pip install mark2pdf[linux]
```

This installs WeasyPrint for PDF generation.

### All Platforms

```bash
pip install mark2pdf[all]
```

Installs both backends for maximum compatibility.

## Usage

### Basic Usage

```python
from mark2pdf import mark_convert

# Convert a Markdown file to PDF
mark_convert("output.pdf", md_file_path="document.md")
```

### From String Content

```python
from mark2pdf import mark_convert

md_content = """
# Hello World

This is a **Markdown** document.

- Item 1
- Item 2
- Item 3
"""

mark_convert("output.pdf", md_content=md_content)
```

### With Custom CSS

```python
from mark2pdf import mark_convert

mark_convert(
    "output.pdf",
    md_file_path="document.md",
    css_file_path="custom-styles.css"
)
```

## API Reference

### `mark_convert(pdf_file_path, md_file_path=None, md_content=None, css_file_path=None)`

Convert Markdown to PDF.

**Parameters:**
- `pdf_file_path` (str): Output PDF file path
- `md_file_path` (str, optional): Path to input Markdown file
- `md_content` (str, optional): Markdown content as string (alternative to md_file_path)
- `css_file_path` (str, optional): Path to custom CSS file

**Raises:**
- `ValueError`: If neither md_file_path nor md_content is provided
- `FileNotFoundError`: If md_file_path doesn't exist

## How It Works

mark2pdf uses platform-specific backends for PDF generation:

| Platform | Backend | Description |
|----------|---------|-------------|
| Windows | Playwright | Uses Chrome's PDF printing capabilities |
| Linux | WeasyPrint | Direct HTML-to-PDF conversion |
| macOS | Auto | Tries WeasyPrint first, then Playwright |

The conversion process:
1. Parse Markdown to HTML using Python's `markdown` library
2. Apply default CSS styling (or custom CSS if provided)
3. Generate PDF using the platform-appropriate backend

## Supported Markdown Features

- Headings
- Bold, italic, strikethrough
- Lists (ordered and unordered)
- Tables
- Fenced code blocks with syntax highlighting
- Links and images
- Blockquotes
- Table of contents (via `[TOC]` marker)

## Testing

Run the test script:

```bash
python test.py
```

This will convert a sample Markdown file to PDF using the default settings.

## Development

Install in development mode:

```bash
pip install -e .[all]
```

## License

MIT License
