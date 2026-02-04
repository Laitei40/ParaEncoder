"""Batch-friendly I/O helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from para.convert import zg_to_unicode


DEFAULT_ENCODING = "utf-8"


def read_text(path: str, *, encoding: str = DEFAULT_ENCODING) -> str:
    return Path(path).read_text(encoding=encoding)


def write_text(path: str, data: str, *, encoding: str = DEFAULT_ENCODING) -> None:
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

    Returns the converted text. When ``output_path`` is None, the caller can
    capture the returned string.
    """
    data = read_text(input_path, encoding=encoding)
    converted = zg_to_unicode(data, normalize=normalize, force=assume_zawgyi)

    if output_path:
        write_text(output_path, converted, encoding=encoding)

    return converted
