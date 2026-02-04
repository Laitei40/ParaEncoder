# Para

Para is a small, boring, and transparent toolkit for working with Burmese text. It detects whether text is encoded in Zawgyi or Unicode and converts Zawgyi to Unicode using a rule-based approach. Para never invents a new encoding and keeps its APIs explicit.

## Goals
- Be Unicode-first and never invent a new encoding.
- Offer stable, explicit APIs without side effects or magic imports.
- Provide deterministic Zawgyi vs Unicode detection.
- Convert Zawgyi to Unicode with maintainable, rule-based logic (Parabaik-style), not machine learning.
- Stay batch-friendly for spreadsheets, CSVs, and plain text.
- Avoid heavy native dependencies.
- Be honest about limitations and edge cases.

## Installation
```bash
pip install para
```

## Usage
```python
from para.detect import is_zawgyi, detect_encoding
from para.convert import zg_to_unicode
from para.normalize import normalize_unicode

text = "\u1031\u1010\u1004\u103a"  # Zawgyi-encoded string
if is_zawgyi(text):
    cleaned = zg_to_unicode(text)
    cleaned = normalize_unicode(cleaned)
```

### CLI
Detect encoding:
```bash
echo "\u1031\u1010\u1004\u103a" | para detect
```

Convert Zawgyi to Unicode:
```bash
echo "\u1031\u1010\u1004\u103a" | para convert > output.txt
```

Process a file in place (write to stdout by default):
```bash
para convert --input input.txt --output output.txt
```

## API surface
- `para.detect.is_zawgyi(text: str) -> bool`
- `para.detect.detect_encoding(text: str) -> str`: returns `"zawgyi"`, `"unicode"`, or `"unknown"`.
- `para.convert.zg_to_unicode(text: str) -> str`: Zawgyi to Unicode conversion using ordered regex rules.
- `para.normalize.normalize_unicode(text: str) -> str`: NFC normalization plus simple ordering fixes.
- `para.io.read_text(path: str) -> str`
- `para.io.write_text(path: str, data: str) -> None`
- `para.io.convert_file(...)`: batch-friendly file conversion helpers.

## Detection approach
Detection is deterministic and rule-based. Para scores the input with Zawgyi-specific patterns (e.g., `U+1031` prefix order, `U+105A`, stacked medials) and Unicode-only patterns (e.g., valid ordering of medials, `U+103A` usage). The side with the higher score wins; ties produce `"unknown"`. No machine learning, no network calls.

## Conversion approach
Conversion uses an ordered list of regex replacements derived from Parabaik-style mappings. The rules are explicit, unit-tested, and live in `para.rules`. The converter does not attempt Unicode-to-Zawgyi; it only supports Zawgyi-to-Unicode because Unicode is the target canonical encoding.

## Limitations
- Ambiguous short strings (e.g., ASCII-only) return `"unknown"` and pass through unchanged.
- Extremely malformed Zawgyi text may require manual cleanup.
- The converter focuses on common Zawgyi usage; rare legacy ligatures may need additional rules.

## Contributing
Issues and pull requests are welcome. Keep changes readable and testable.

## Packaging
- Build a wheel/sdist locally: `python -m pip install build` then `python -m build`.
- Publish to PyPI (once ready): `python -m pip install twine` then `twine upload dist/*`.
- The package metadata in `pyproject.toml` is PyPI-ready (MIT license, explicit packages, CLI entrypoint).

## License
MIT
