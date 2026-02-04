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
pip install paraencoder
```

For Office document support (.docx, .xlsx, .odt):
```bash
pip install paraencoder[office]
```

## Supported File Formats

### Plain Text (built-in, no extra dependencies)
- **Text files:** `.txt`, `.text`, `.log`, `.md`, `.rst`, `.asc`
- **Web/markup:** `.html`, `.htm`, `.xhtml`, `.xml`, `.json`, `.yaml`, `.yml`, `.csv`, `.tsv`
- **Documentation:** `.tex`, `.latex`, `.adoc`, `.org`, `.wiki`, `.mediawiki`
- **Config:** `.ini`, `.cfg`, `.conf`, `.properties`, `.env`, `.toml`, `.lock`
- **Source code:** `.py`, `.js`, `.ts`, `.java`, `.c`, `.cpp`, `.h`, `.cs`, `.php`, `.rb`, `.go`, `.rs`, `.sh`, `.bat`, `.ps1`, `.sql`
- **Subtitles:** `.srt`, `.vtt`, `.sub`
- **Other:** `.po`, `.pot`, `.texi`, `.man`, `.nfo`, `.readme`, `.eml`, `.mbox`

### Office Documents (requires `paraencoder[office]`)
- **Microsoft Word:** `.docx`, `.docm`
- **Microsoft Excel:** `.xlsx`, `.xlsm`
- **OpenDocument:** `.odt`

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

Convert Office documents (requires `paraencoder[office]`):
```bash
para convert --input "Document.docx" --output "Document_Unicode.docx"
para convert --input "Spreadsheet.xlsx" --output "Spreadsheet_Unicode.xlsx"
```

#### Windows / PowerShell note
PowerShell's default encoding corrupts Myanmar text in pipes. Before piping Burmese text, set UTF-8 encoding:
```powershell
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
echo "ျမန္မာ" | para convert
```
Or use file-based input/output to avoid pipe issues:
```powershell
para convert --input input.txt --output output.txt
```

## API surface
- `para.detect.is_zawgyi(text: str) -> bool`
    - Input: `text` string.
    - Output: `True` only when the detector score prefers Zawgyi; otherwise `False`.
    - Guarantee: Never raises on empty/ASCII-only input; returns `False` for those.

- `para.detect.detect_encoding(text: str) -> Literal["zawgyi", "unicode", "unknown"]`
    - Input: `text` string.
    - Output: One of the three labels. Ties or insufficient evidence → `"unknown"` (no auto-conversion).
    - Guarantee: Deterministic, no network/ML, explicit tie handling.

- `para.convert.zg_to_unicode(text: str, *, normalize: bool = True, force: bool = False) -> str`
    - Input: `text` string.
    - Output: Converted Unicode string when detection prefers Zawgyi (or when `force=True`). Otherwise passes through (optionally normalized).
    - Guarantee: Ordered, test-backed regex rules; no Unicode→Zawgyi path; `force=False` avoids silent conversion on ambiguous text.

- `para.normalize.normalize_unicode(text: str) -> str`
    - Input: `text` string.
    - Output: NFC-normalized string with simple Myanmar ordering tweaks.
    - Guarantee: Idempotent on already-normalized Unicode Burmese.

- `para.io.read_text(path: str, *, encoding: str = "utf-8") -> str`
- `para.io.write_text(path: str, data: str, *, encoding: str = "utf-8") -> None`
- `para.io.convert_file(...) -> str`
    - Batch helpers for files; never guess encodings beyond the provided `encoding` argument.

## Detection approach
Detection is deterministic and rule-based. Para scores the input with Zawgyi-specific patterns (e.g., `U+1031` prefix order, `U+105A`, stacked medials) and Unicode-only patterns (e.g., valid ordering of medials, `U+103A` usage). The side with the higher score wins; ties produce `"unknown"`. No machine learning, no network calls.

## Conversion approach
Conversion uses an ordered list of regex replacements derived from Parabaik-style mappings. The rules are explicit, unit-tested, and live in `para.rules`. The converter does not attempt Unicode-to-Zawgyi; it only supports Zawgyi-to-Unicode because Unicode is the target canonical encoding.

## Limitations
- Ambiguous short strings (e.g., ASCII-only) return `"unknown"` and pass through unchanged.
- Extremely malformed Zawgyi text may require manual cleanup.
- The converter focuses on common Zawgyi usage; rare legacy ligatures may need additional rules.

## Non-goals
- Creating or endorsing any new Burmese encoding.
- Unicode-to-Zawgyi conversion.
- ML-based detection or probabilistic auto-conversion.
- Silent mutation of text when detection confidence is low; ties stay `"unknown"`.

## Contributing
Issues and pull requests are welcome. Keep changes readable and testable.

## Packaging
- Build a wheel/sdist locally: `python -m pip install build` then `python -m build`.
- Publish to PyPI (once ready): `python -m pip install twine` then `twine upload dist/*`.
- The package metadata in `pyproject.toml` is PyPI-ready (MIT license, explicit packages, CLI entrypoint).

## License
MIT
