class CheckPipeline:
    def __init__(self, checks: list):
        self.checks = checks

    def run(self, source: str) -> list:
        issues = []
        for check in self.checks:
            issues.extend(check.run(source))
        return issues