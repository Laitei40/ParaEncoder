"""Command line entrypoint for Para."""

from __future__ import annotations

import argparse
import sys
from typing import Optional

from para.convert import zg_to_unicode
from para.detect import detect_encoding, is_zawgyi
from para.io import convert_file, read_text, write_text
from para.normalize import normalize_unicode


def _read_input(input_path: Optional[str]) -> str:
    if input_path:
        return read_text(input_path)
    return sys.stdin.read()


def _write_output(data: str, output_path: Optional[str]) -> None:
    if output_path:
        write_text(output_path, data)
    else:
        sys.stdout.write(data)


def _cmd_detect(args: argparse.Namespace) -> int:
    data = _read_input(args.input)
    encoding = detect_encoding(data)
    sys.stdout.write(f"{encoding}\n")
    return 0


def _cmd_convert(args: argparse.Namespace) -> int:
    if args.input:
        converted = convert_file(
            input_path=args.input,
            output_path=args.output,
            assume_zawgyi=args.force,
            normalize=not args.no_normalize,
        )
        if not args.output:
            sys.stdout.write(converted)
    else:
        data = sys.stdin.read()
        converted = zg_to_unicode(
            data,
            normalize=not args.no_normalize,
            force=args.force,
        )
        _write_output(converted, args.output)
    return 0


def _cmd_normalize(args: argparse.Namespace) -> int:
    data = _read_input(args.input)
    normalized = normalize_unicode(data)
    _write_output(normalized, args.output)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Para: Zawgyi ↔ Unicode tooling")
    sub = parser.add_subparsers(dest="command", required=True)

    detect_parser = sub.add_parser("detect", help="Detect encoding of input text")
    detect_parser.add_argument("--input", help="Input file path; defaults to stdin")
    detect_parser.set_defaults(func=_cmd_detect)

    convert_parser = sub.add_parser("convert", help="Convert Zawgyi text to Unicode")
    convert_parser.add_argument("--input", help="Input file path; defaults to stdin")
    convert_parser.add_argument("--output", help="Output file path; defaults to stdout")
    convert_parser.add_argument(
        "--force",
        action="store_true",
        help="Force conversion even if detection is uncertain",
    )
    convert_parser.add_argument(
        "--no-normalize",
        action="store_true",
        help="Skip Unicode normalization step",
    )
    convert_parser.set_defaults(func=_cmd_convert)

    normalize_parser = sub.add_parser("normalize", help="Normalize Unicode Burmese text")
    normalize_parser.add_argument("--input", help="Input file path; defaults to stdin")
    normalize_parser.add_argument("--output", help="Output file path; defaults to stdout")
    normalize_parser.set_defaults(func=_cmd_normalize)

    return parser


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
