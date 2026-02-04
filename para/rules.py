"""Minimal, testable regex rules for Zawgyi-to-Unicode conversion.

Each rule is intentionally small and has a dedicated unit test. This is a
foundational subset, not full coverage.
"""

ZAWGYI_TO_UNICODE_RULES = [
    # Core kinzi and kinzi-with-vowel.
    (r"\u1064", "\u1004\u103A\u1039"),
    (r"\u108B", "\u1004\u103A\u1039\u102D"),

    # Common consonant and vowel forms.
    (r"\u106A", "\u1009"),
    (r"\u1033", "\u102F"),
    (r"\u1034", "\u1030"),
    (r"\u105A", "\u102B\u103A"),

    # Reorder prefix E vowel relative to medials.
    (r"\u1031([\u103B-\u103E])", "\\1\u1031"),

    # Swap asat + dot order.
    (r"\u103A\u1037", "\u1037\u103A"),

    # Move dot after tall U.
    (r"\u1036\u102F", "\u102F\u1036"),

    # Basic stacked consonant KA.
    (r"\u1060", "\u1039\u1000"),
]
