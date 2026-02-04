"""Batch-friendly I/O helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from para.convert import zg_to_unicode
from para.handlers import get_handler, is_supported, PlainTextHandler


DEFAULT_ENCODING = "utf-8"


def read_text(path: str, *, encoding: str = DEFAULT_ENCODING) -> str:
    """Read text from a file. For plain text files only."""
    return Path(path).read_text(encoding=encoding)


def write_text(path: str, data: str, *, encoding: str = DEFAULT_ENCODING) -> None:
    """Write text to a file. For plain text files only."""
    Path(path).write_text(data, encoding=encoding)


def convert_file(
    *,
    input_path: str,
    output_path: Optional[str] = None,
    assume_zawgyi: bool = False,
    normalize: bool = True,
    encoding: str = DEFAULT_ENCODING,
) -> str:
    """
    Convert a file from Zawgyi to Unicode and write the result.

    Supports multiple file formats:
    - Plain text files (.txt, .md, .csv, .json, .xml, .html, etc.)
    - Microsoft Word (.docx) - requires: pip install paraencoder[office]
    - Microsoft Excel (.xlsx) - requires: pip install paraencoder[office]
    - OpenDocument (.odt) - requires: pip install paraencoder[office]

    Returns the converted text. When ``output_path`` is None for plain text
    files, the caller can capture the returned string. For binary formats
    like .docx and .xlsx, output_path is required.
    """
    input_p = Path(input_path)
    handler = get_handler(input_p)

    # Create converter function
    def converter(text: str) -> str:
        return zg_to_unicode(text, normalize=normalize, force=assume_zawgyi)

    # For plain text, we can return the string
    if isinstance(handler, PlainTextHandler):
        data = handler.read(input_p, encoding=encoding)
        converted = converter(data)
        if output_path:
            Path(output_path).write_text(converted, encoding=encoding)
        return converted
    else:
        # Binary formats require output path
        if not output_path:
            output_path = input_path  # Overwrite in place

        handler.convert(input_p, Path(output_path), converter)

        # Return text content for display
        return handler.read(Path(output_path))

