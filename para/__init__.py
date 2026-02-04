"""Para: Burmese text detection and conversion toolkit."""

__all__ = [
    "is_zawgyi",
    "detect_encoding",
    "zg_to_unicode",
    "normalize_unicode",
]

from para.detect import detect_encoding, is_zawgyi
from para.convert import zg_to_unicode
from para.normalize import normalize_unicode

__version__ = "0.1.0"
