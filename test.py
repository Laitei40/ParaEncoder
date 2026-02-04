#!/usr/bin/env python3
"""Manual test runner for the `para` package.

Run this script to perform a quick smoke check that imports
the main functions and exercises them on a couple of sample inputs.
"""
from para import detect_encoding, is_zawgyi, zg_to_unicode, normalize_unicode, __version__


def run_sample(s):
    print("input:", repr(s))
    try:
        enc = detect_encoding(s)
    except Exception as e:
        enc = f"error: {e}"
    print(" detect_encoding:", enc)
    try:
        zg = is_zawgyi(s)
    except Exception as e:
        zg = f"error: {e}"
    print(" is_zawgyi:", zg)
    try:
        conv = zg_to_unicode(s)
    except Exception as e:
        conv = f"error: {e}"
    print(" zg_to_unicode:", conv)
    try:
        norm = normalize_unicode(s)
    except Exception as e:
        norm = f"error: {e}"
    print(" normalize_unicode:", norm)
    print("-")


def main():
    print("para version:", __version__)
    samples = [
        "မင်္ဂလာပါ",  # common Myanmar greeting (Unicode)
        "",  # empty string
    ]
    for s in samples:
        run_sample(s)


if __name__ == "__main__":
    main()
