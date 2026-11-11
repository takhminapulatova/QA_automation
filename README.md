
# QA Automation Portfolio

A Python-based test automation project using Playwright and pytest.

## Technologies
- Python 3.11
- Playwright
- pytest
- Git

## Project Structure
- `tests/` — Automated tests and shared fixtures
- `pages/` — Page Object Model classes (planned)
- `utils/` — Reusable helper functions (planned)
- `pytest.ini` — Test marker configuration
- `requirements.txt` — Python dependencies

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
python -m playwright install chromium
```

## Running Tests

Run all tests:

```bash
pytest -v
```

Run smoke tests:

```bash
pytest -m smoke -v
```

Run regression tests:

```bash
pytest -m regression -v
```

## Current Progress

- Reusable Playwright page fixture
- Login page smoke test
- Smoke and regression markers
- Network mocking and authentication state practice
