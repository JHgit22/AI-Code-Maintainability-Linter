import os

from google import genai

from .checks.base import Issue


class AiSuggester:
    def __init__(self, api_key: str | None = None, model: str = "gemini-3.5-flash"):
        self.client = genai.Client(api_key=api_key or os.environ.get("GEMINI_API_KEY"))
        self.model = model

    def suggest(self, issue: Issue, code_snippet: str) -> str:
        prompt = (
            f"Here's a Python code smell: {issue.message}.\n\n"
            f"Relevant code:\n```python\n{code_snippet}\n```\n\n"
            "In 2-3 sentences, explain why this hurts maintainability, "
            "then suggest a concrete rewrite."
        )

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text