"""Deterministic detection for Zawgyi vs Unicode Burmese text."""

from __future__ import annotations

import re
from typing import Literal

Encoding = Literal["zawgyi", "unicode", "unknown"]

_MYANMAR_RANGE = re.compile(r"[\u1000-\u109F]")

# Patterns that strongly suggest Zawgyi encoding.
_ZG_PATTERNS = [
    (re.compile(r"[\u105A\u1060-\u1097]"), 4),
    (re.compile(r"\u1031[\u103B-\u103E]"), 3),
    (re.compile(r"\u1039[\u1000-\u1021]?\u1031"), 3),
    (re.compile(r"\u103A\u103A"), 2),
    (re.compile(r"\u1039[\u1000-\u109F]"), 2),
    (re.compile(r"\u1031\u108A"), 3),
]

# Patterns that indicate proper Unicode ordering or characters.
_UNI_PATTERNS = [
    (re.compile(r"\u1031[\u1000-\u1021]"), 3),
    (re.compile(r"\u102B\u103A"), 2),
    (re.compile(r"\u103B[\u103C\u103D]"), 2),
    (re.compile(r"\u103C[\u103E]"), 2),
    (re.compile(r"\u1037[\u103A]"), 2),
    (re.compile(r"\u1004\u103A\u1039"), 3),
    (re.compile(r"[\u1000-\u1021]\u103C"), 2),
]


def _score(text: str, patterns: list[tuple[re.Pattern[str], int]]) -> int:
    score = 0
    for pattern, weight in patterns:
        matches = pattern.findall(text)
        if matches:
            score += len(matches) * weight
    return score


def detect_encoding(text: str) -> Encoding:
    """Return "zawgyi", "unicode", or "unknown" based on heuristic scoring."""
    if not text:
        return "unknown"

    if not _MYANMAR_RANGE.search(text):
        return "unknown"

    zg_score = _score(text, _ZG_PATTERNS)
    uni_score = _score(text, _UNI_PATTERNS)

    if zg_score == uni_score:
        return "unknown"

    return "zawgyi" if zg_score > uni_score else "unicode"


def is_zawgyi(text: str) -> bool:
    """Convenience boolean: True when the detector prefers Zawgyi."""
    return detect_encoding(text) == "zawgyi"
