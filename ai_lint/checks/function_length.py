import ast

from .base import CodeCheck, Issue


class FunctionLengthCheck(CodeCheck):
    def __init__(self, max_lines: int = 30):
        self.max_lines = max_lines

    def run(self, source: str) -> list[Issue]:
        tree = ast.parse(source)
        issues = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                length = node.end_lineno - node.lineno + 1
                if length > self.max_lines:
                    issues.append(
                        Issue(
                            line=node.lineno,
                            message=(
                                f"Function '{node.name}' is {length} lines long "
                                f"(max {self.max_lines})"
                            ),
                            severity="medium",
                        )
                    )

        return issues