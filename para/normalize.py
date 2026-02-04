"""Unicode-focused normalization helpers."""

from __future__ import annotations

import re
import unicodedata


def _reorder_myanmar(text: str) -> str:
    # Move kinzi to canonical position.
    text = re.sub(
        r"(\u1004\u103A\u1039)([\u1000-\u1021])",
        lambda m: m.group(2) + m.group(1),
        text,
    )
    # Place E vowel and medial RA before the base consonant.
    text = re.sub(r"([\u1000-\u1021])(\u1031)", r"\2\1", text)
    text = re.sub(r"([\u1000-\u1021])(\u103C)", r"\2\1", text)
    # Swap asat and dot if reversed.
    text = re.sub(r"\u103A\u1037", "\u1037\u103A", text)
    # Reorder medials to YA, RA, WA, HA.
    text = re.sub(
        r"([\u1000-\u1021])([\u103E])(\u103B)",
        lambda m: m.group(1) + "\u103B" + m.group(2),
        text,
    )
    text = re.sub(
        r"([\u1000-\u1021])([\u103E])(\u103C)",
        lambda m: m.group(1) + "\u103C" + m.group(2),
        text,
    )
    text = re.sub(
        r"([\u1000-\u1021])([\u103E])(\u103D)",
        lambda m: m.group(1) + "\u103D" + m.group(2),
        text,
    )
    return text


def normalize_unicode(text: str) -> str:
    """Normalize Unicode Burmese text with NFC and simple ordering fixes."""
    if not text:
        return ""
    normalized = unicodedata.normalize("NFC", text)
    normalized = _reorder_myanmar(normalized)
    return normalized
