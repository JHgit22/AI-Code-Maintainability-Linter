# AI Maintainability Linter

A small Python CLI tool that checks a file for common maintainability issues — long functions, magic numbers, non-snake_case naming, and deeply nested code — then uses the Gemini API to suggest a fix for the worst one it finds.

## Why this exists

Built as a hands-on way to practice object-oriented design principles (Strategy pattern, Open/Closed Principle) through a real, working tool rather than a toy example.

## Features

- **Function length check** — flags functions over a configurable line limit
- **Magic number check** — flags unnamed numeric literals outside a small allowed set
- **Naming check** — flags function and variable names that aren't snake_case
- **Nesting depth check** — flags code nested past a configurable depth
- **AI suggestion** — sends the single worst issue to Gemini for a plain-English explanation and a suggested rewrite

## Installation

\`\`\`bash
git clone https://github.com/JHgit22/ai-maintainability-linter.git
cd ai-maintainability-linter
python3 -m venv venv
venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
\`\`\`

Copy \`.env.example\` to \`.env\` and add your own Gemini API key (get one free at [aistudio.google.com](https://aistudio.google.com)):

GEMINI_API_KEY=your_key_here


## Usage

\`\`\`bash
python3 -m ai_lint.cli path/to/your_file.py
\`\`\`

Skip the AI suggestion and only run the deterministic checks:
\`\`\`bash
python3 -m ai_lint.cli path/to/your_file.py --no-ai
\`\`\`

### Example output
[MEDIUM] line 5: Function 'a_really_long_function_that_should_get_flagged' is 33 lines long (max 30)
[LOW] line 9: Magic number 3 should be a named constant
[LOW] line 10: Magic number 4 should be a named constant
[LOW] line 11: Magic number 5 should be a named constant
[LOW] line 12: Magic number 6 should be a named constant
[LOW] line 13: Magic number 7 should be a named constant
[LOW] line 14: Magic number 8 should be a named constant
[LOW] line 15: Magic number 9 should be a named constant
[LOW] line 16: Magic number 10 should be a named constant
[LOW] line 17: Magic number 11 should be a named constant
[LOW] line 18: Magic number 12 should be a named constant
[LOW] line 19: Magic number 13 should be a named constant
[LOW] line 20: Magic number 14 should be a named constant
[LOW] line 21: Magic number 15 should be a named constant
[LOW] line 22: Magic number 16 should be a named constant
[LOW] line 23: Magic number 17 should be a named constant
[LOW] line 24: Magic number 18 should be a named constant
[LOW] line 25: Magic number 19 should be a named constant
[LOW] line 26: Magic number 20 should be a named constant
[LOW] line 27: Magic number 21 should be a named constant
[LOW] line 28: Magic number 22 should be a named constant
[LOW] line 29: Magic number 23 should be a named constant
[LOW] line 30: Magic number 24 should be a named constant
[LOW] line 31: Magic number 25 should be a named constant
[LOW] line 32: Magic number 26 should be a named constant
[LOW] line 33: Magic number 27 should be a named constant
[LOW] line 34: Magic number 28 should be a named constant
[LOW] line 35: Magic number 29 should be a named constant
[LOW] line 36: Magic number 30 should be a named constant
[LOW] line 41: Magic number 47 should be a named constant
[LOW] line 45: Function name 'badlyNamedFunction' should be snake_case
[LOW] line 46: Variable name 'myBadVariable' should be snake_case
[MEDIUM] line 54: Nesting depth 4 exceeds max of 3

33 issue(s) found.

--- AI suggestion for the top issue ---
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.
Long functions hurt maintainability because they often attempt to do too much, violating the Single Responsibility Principle and making the code difficult to comprehend at a glance. This high cognitive load increases the likelihood of introducing bugs during future updates and makes the individual logical steps nearly impossible to isolate and unit test.

### Suggested Rewrite

To fix this, extract distinct logical steps into smaller, focused helper functions. This makes the main function act as a high-level, easily readable controller:

```python
# Before: A single 33-line function doing loading, transforming, and saving.

# After: Broken down into modular, single-purpose functions
def process_monthly_report():
    raw_data = fetch_report_data()
    cleaned_data = clean_report_data(raw_data)
    save_report(cleaned_data)

def fetch_report_data():
    # Focused logic for fetching data (under 10 lines)
    pass

def clean_report_data(data):
    # Focused logic for data transformation (under 15 lines)
    pass

def save_report(data):
    # Focused logic for database saving (under 10 lines)
    pass
```

## Project structure

\`\`\`
ai_lint/
├── checks/          # one file per check, all implementing the CodeCheck interface
├── reporters/        # output formatting (console, extensible to JSON etc.)
├── ai_suggester.py    # Gemini API integration
├── pipeline.py       # runs all checks, has no knowledge of what any check does
└── cli.py            # entry point
\`\`\`

Adding a new check means adding one new file to \`checks/\` and one line to the pipeline in \`cli.py\` — nothing else changes.

