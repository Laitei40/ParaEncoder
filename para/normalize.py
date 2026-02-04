"""Unicode-focused normalization helpers."""

from __future__ import annotations

# NOTE (v0.1.0): Normalization is intentionally disabled for safety.
# Previous reordering logic corrupted valid canonical Unicode text.
# Until a provably-safe implementation is available, this function is a
# strict no-op.  Unicode safety > clever normalization.


def normalize_unicode(text: str) -> str:
    """Return text unchanged (normalization disabled in v0.1.0 for safety).

    ParaEncoder must never modify valid Unicode text unless explicitly and
    provably necessary.  Reordering / NFC logic has been removed because it
    corrupted canonical input such as "မင်္ဂလာပါ".

    Future versions may re-introduce opt-in, test-backed normalization.
    """
    return text
