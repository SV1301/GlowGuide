# Contributing to GlowGuide

Thank you for helping improve GlowGuide — a unisex, beginner-friendly personal care knowledge base covering skincare, bodycare, hygiene, and haircare.

---

## Table of Contents

1. [Ways to Contribute](#ways-to-contribute)
2. [Getting Started](#getting-started)
3. [Branch & PR Workflow](#branch--pr-workflow)
4. [Coding Standards](#coding-standards)
5. [Running Tests](#running-tests)
6. [Content Guidelines](#content-guidelines)
7. [Reporting Bugs & Requesting Features](#reporting-bugs--requesting-features)
8. [Contribution Review Process](#contribution-review-process)

---

## Ways to Contribute

**Code contributions:**
- Fix bugs (see [Issues](https://github.com/SV1301/GlowGuide/issues) labelled `bug`).
- Improve the routine recommendation logic in `modules/recommendations.py`.
- Add new Streamlit UI pages or improve existing ones.
- Add translations for a new language (see [Adding a new language](#adding-a-new-language)).
- Improve CI/CD pipelines or code quality tooling.

**Content contributions (no coding required):**
- Add beginner-friendly product explanations via the in-app **Contribute** form at [glowguide-personalcare.streamlit.app](https://glowguide-personalcare.streamlit.app/).
- Suggest routine improvements, ingredient notes, or caution notes.
- Report unclear, unsafe, outdated, or duplicated content.

**Documentation contributions:**
- Improve or expand `README.md`, `CONTRIBUTING.md`, `USER_MANUAL.md`, or files in `docs/`.
- Improve the specs in `specs/001-glowguide-personal-care-platform/`.

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git

### Local setup (Windows PowerShell)

```powershell
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/<your-username>/GlowGuide.git
cd GlowGuide

# 2. Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install all dependencies (runtime + dev tools)
pip install -r requirements.txt

# 4. Run the app locally
streamlit run app.py
```

### Local setup (Linux / macOS)

```bash
git clone https://github.com/<your-username>/GlowGuide.git
cd GlowGuide
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The app opens at **http://localhost:8501**.

---

## Branch & PR Workflow

We use a simple feature-branch workflow.

### Branch naming

| Type | Convention | Example |
|---|---|---|
| Bug fix | `fix/<short-description>` | `fix/routine-empty-results` |
| New feature | `feat/<short-description>` | `feat/mental-wellness-page` |
| Documentation | `docs/<short-description>` | `docs/update-contributing` |
| Locale / translation | `i18n/<lang-code>-<description>` | `i18n/ta-tamil-locale` |
| Chore / tooling | `chore/<short-description>` | `chore/bump-ruff` |

### PR process

1. **Create a branch** from `main` using the naming convention above.
2. **Make your changes** with small, focused commits.
3. **Run all local quality checks** (see [Coding Standards](#coding-standards)) before pushing.
4. **Open a pull request** against `main` on GitHub.
5. **Fill in the PR description** — explain what changed and why.
6. **Wait for CI** — all GitHub Actions checks must pass.
7. **Address review comments** if requested by a maintainer.

### Commit convention

This project uses [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add mental wellness care category
fix: prevent empty routine builder results when concern is "general"
docs: add Tamil locale instructions to CONTRIBUTING
chore: bump ruff to 0.5.x
i18n: add Tamil (ta) locale file
```

Changelogs are generated automatically by `git-cliff` based on commit messages.

---

## Coding Standards

Run these checks locally before opening a PR. The CI pipeline will fail if any of these do not pass.

```powershell
# Lint (fast Python linter)
ruff check .

# Format check
ruff format --check .

# Additional style checks
flake8 app.py modules/

# Static type checking
mypy app.py modules/

# Security scan
bandit -r app.py modules/ -c pyproject.toml

# Dead code detection
vulture app.py modules/ --min-confidence 80
```

Full tool configuration lives in `pyproject.toml` and `.flake8`.

**Key rules:**
- Max line length: **100 characters**.
- Python version target: **3.10+**.
- All public functions in `modules/` must have **type annotations**.
- No hardcoded credentials; use environment variables (see `.env.example`).
- No `exec()` or `eval()`.

---

## Running Tests

```powershell
# Run all tests with coverage
pytest --cov=modules --cov-report=term-missing --ignore=.venv --ignore=specs -q

# Run a specific test file
pytest tests/test_modules.py -v
```

Tests live in `tests/test_modules.py`. When adding new features, please add corresponding tests.

---

## Content Guidelines

All content additions must follow these rules:

- Use **simple, non-judgmental, inclusive language**.
- Keep content **educational** — explain what a product does, not what outcome it promises.
- **Do not make medical claims** or promise results.
- Avoid diagnosis or treatment instructions.
- Use safer wording: `"may help"`, `"commonly used for"`, `"consider consulting a qualified professional"`.
- Include a **source link** where possible.

### Adding a new language

1. Create `locales/<code>.json` mirroring the full structure of `locales/en.json`.
2. Add one entry to `SUPPORTED_LANGUAGES` in `modules/i18n.py`.
3. Open a PR with the new locale file and the `i18n.py` change.

---

## Reporting Bugs & Requesting Features

Use GitHub Issues: https://github.com/SV1301/GlowGuide/issues

| Issue type | Label | What to include |
|---|---|---|
| **Bug report** | `bug` | Steps to reproduce, expected vs. actual behaviour, screenshots if applicable |
| **Feature request** | `enhancement` | Problem it solves, proposed solution, any alternatives considered |
| **Content issue** | `content` | Incorrect or missing product info; include a source link if possible |
| **Documentation** | `documentation` | Which file and what is unclear or missing |
| **Setup / dev query** | `question` | Your OS, Python version, and exact error message |

> **Security vulnerabilities** must not be reported via public issues. See `SECURITY.md` for the responsible disclosure process.

---

## Contribution Review Process

Public content submissions made through the in-app **Contribute** form:

1. Are stored with `status = 'pending'` in the SQLite database.
2. Are reviewed by a maintainer on the **Review Contributions** page.
3. May be **approved** (integrated into the product library), **rejected** (with a reviewer note), or **needs-changes** (returned for revision).

Code contributions submitted via GitHub PR:
1. Must pass all CI checks.
2. Are reviewed by at least one maintainer.
3. May require changes before merging.

See `docs/feedback.md` for the full feedback loop and prioritisation process.

---

## Pull Request Checklist

Before submitting a PR, confirm:

- [ ] The app runs locally (`streamlit run app.py`).
- [ ] All quality checks pass (`ruff`, `flake8`, `mypy`, `bandit`, `vulture`).
- [ ] Tests pass (`pytest`).
- [ ] New content is beginner-friendly and avoids medical claims.
- [ ] Documentation is updated if behaviour changed.
- [ ] Commit messages follow the Conventional Commits format.
- [ ] The branch name follows the naming convention above.
