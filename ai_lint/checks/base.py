from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Issue:
    line: int
    message: str
    severity: str  # "low" | "medium" | "high"


class CodeCheck(ABC):
    @abstractmethod
    def run(self, source: str) -> list[Issue]:
        """Parse `source` and return every Issue this check finds."""
        raise NotImplementedError