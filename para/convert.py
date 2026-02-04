"""Rule-based Zawgyi to Unicode conversion."""

from __future__ import annotations

import re
from typing import Iterable

from para.detect import detect_encoding, is_zawgyi
from para.normalize import normalize_unicode
from para.rules import ZAWGYI_TO_UNICODE_RULES


def _compile_rules(rules: Iterable[tuple[str, str]]) -> list[tuple[re.Pattern[str], str]]:
    compiled: list[tuple[re.Pattern[str], str]] = []
    for pattern, replacement in rules:
        compiled.append((re.compile(pattern), replacement))
    return compiled


_COMPILED_RULES = _compile_rules(ZAWGYI_TO_UNICODE_RULES)


def zg_to_unicode(text: str, *, normalize: bool = True, force: bool = False) -> str:
    """
    Convert Zawgyi text to Unicode using ordered regex rules.

    Args:
        text: Input text that may be Zawgyi.
        normalize: Whether to apply Unicode normalization and basic reordering.
        force: When False, conversion only runs if the detector believes the text is Zawgyi.
    """
    if not text:
        return ""

    # Hard guard: never modify non-Zawgyi input (contract guarantee).
    if not force and detect_encoding(text) != "zawgyi":
        return text

    converted = text
    for pattern, repl in _COMPILED_RULES:
        converted = pattern.sub(repl, converted)

    if normalize:
        converted = normalize_unicode(converted)

    return converted
