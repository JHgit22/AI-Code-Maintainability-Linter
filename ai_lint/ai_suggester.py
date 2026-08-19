import os

from anthropic import Anthropic

from .checks.base import Issue


class AiSuggester:
    def __init__(self, api_key: str | None = None, model: str = "claude-haiku-4-5-20251001"):
        self.client = Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))
        self.model = model

    def suggest(self, issue: Issue, code_snippet: str) -> str:
        prompt = (
            f"Here's a Python code smell: {issue.message}.\n\n"
            f"Relevant code:\n```python\n{code_snippet}\n```\n\n"
            "In 2-3 sentences, explain why this hurts maintainability, "
            "then suggest a concrete rewrite."
        )

        response = self.client.messages.create(
            model=self.model,
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}],
        )

        return response.content[0].text