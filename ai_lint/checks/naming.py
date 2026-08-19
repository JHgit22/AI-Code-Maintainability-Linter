import ast
import re

from .base import CodeCheck, Issue

SNAKE_CASE = re.compile(r"^[a-z_][a-z0-9_]*$")


class NamingCheck(CodeCheck):
    def run(self, source: str) -> list[Issue]:
        tree = ast.parse(source)
        issues = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not SNAKE_CASE.match(node.name):
                    issues.append(
                        Issue(
                            line=node.lineno,
                            message=f"Function name '{node.name}' should be snake_case",
                            severity="low",
                        )
                    )
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and not SNAKE_CASE.match(target.id):
                        issues.append(
                            Issue(
                                line=target.lineno,
                                message=f"Variable name '{target.id}' should be snake_case",
                                severity="low",
                            )
                        )

        return issues