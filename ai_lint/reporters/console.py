from .base import Reporter


class ConsoleReporter(Reporter):
    def report(self, issues) -> None:
        if not issues:
            print("No issues found.")
            return
        for issue in sorted(issues, key=lambda i: i.line):
            print(f"[{issue.severity.upper()}] line {issue.line}: {issue.message}")
        print(f"\n{len(issues)} issue(s) found.")