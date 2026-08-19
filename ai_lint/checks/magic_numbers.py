import ast

from .base import CodeCheck, Issue

DEFAULT_ALLOWED_NUMBERS = {0, 1, -1, 2, 100}


class MagicNumberCheck(CodeCheck):
    def __init__(self, allowed_numbers: set | None = None):
        self.allowed_numbers = (
            allowed_numbers if allowed_numbers is not None else DEFAULT_ALLOWED_NUMBERS
        )

    def run(self, source: str) -> list[Issue]:
        tree = ast.parse(source)
        issues = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Constant):
                value = node.value
                if isinstance(value, bool):
                    continue  # True/False are technically ints in Python
                if isinstance(value, (int, float)) and value not in self.allowed_numbers:
                    issues.append(
                        Issue(
                            line=node.lineno,
                            message=f"Magic number {value!r} should be a named constant",
                            severity="low",
                        )
                    )

        return issues