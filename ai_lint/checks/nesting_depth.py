import ast

from .base import CodeCheck, Issue

NESTING_NODE_TYPES = (ast.If, ast.For, ast.While, ast.Try)


class NestingDepthCheck(CodeCheck):
    def __init__(self, max_depth: int = 3):
        self.max_depth = max_depth

    def run(self, source: str) -> list[Issue]:
        tree = ast.parse(source)
        issues: list[Issue] = []
        self._walk(tree, depth=0, issues=issues)
        return issues

    def _walk(self, node, depth, issues):
        is_nesting_node = isinstance(node, NESTING_NODE_TYPES)
        next_depth = depth + 1 if is_nesting_node else depth

        if is_nesting_node and next_depth > self.max_depth:
            issues.append(
                Issue(
                    line=node.lineno,
                    message=f"Nesting depth {next_depth} exceeds max of {self.max_depth}",
                    severity="medium",
                )
            )

        for child in ast.iter_child_nodes(node):
            self._walk(child, next_depth, issues)