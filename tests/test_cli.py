import io
from typing import List

import para.cli as cli


def run_cli(args: List[str], input_text: str) -> str:
    stdin = io.StringIO(input_text)
    stdout = io.StringIO()
    original_stdin, original_stdout = cli.sys.stdin, cli.sys.stdout
    try:
        cli.sys.stdin = stdin
        cli.sys.stdout = stdout
        cli.main(args)
        return stdout.getvalue()
    finally:
        cli.sys.stdin = original_stdin
        cli.sys.stdout = original_stdout


def test_cli_detect_reports_zawgyi():
    output = run_cli(["detect"], "\u106A")
    assert "zawgyi" in output


def test_cli_convert_stdin():
    output = run_cli(["convert", "--force"], "\u106A")
    assert "\u1009" in output
