import argparse
import os

from dotenv import load_dotenv

load_dotenv()

from .ai_suggester import AiSuggester
from .checks.function_length import FunctionLengthCheck
from .checks.magic_numbers import MagicNumberCheck
from .checks.naming import NamingCheck
from .checks.nesting_depth import NestingDepthCheck
from .pipeline import CheckPipeline
from .reporters.console import ConsoleReporter

SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def main():
    parser = argparse.ArgumentParser(description="AI Maintainability Linter")
    parser.add_argument("file", help="Path to the Python file to lint")
    parser.add_argument(
        "--no-ai",
        action="store_true",
        help="Skip the AI suggestion even if an API key is configured",
    )
    args = parser.parse_args()

    with open(args.file, "r") as f:
        source = f.read()

    pipeline = CheckPipeline([
        FunctionLengthCheck(),
        MagicNumberCheck(),
        NamingCheck(),
        NestingDepthCheck(),
    ])
    issues = pipeline.run(source)

    ConsoleReporter().report(issues)

    if issues and not args.no_ai and os.environ.get("GEMINI_API_KEY"):
        worst = sorted(issues, key=lambda i: SEVERITY_ORDER.get(i.severity, 3))[0]
        lines = source.splitlines()
        snippet = "\n".join(lines[max(0, worst.line - 2): worst.line + 2])

        print("\n--- AI suggestion for the top issue ---")
        print(AiSuggester().suggest(worst, snippet))


if __name__ == "__main__":
    main()