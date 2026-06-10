# Agent Handoff Guide

This file helps future coding agents continue GlowGuide without needing the full prior conversation.

## Project Summary

GlowGuide is a unisex Streamlit personal care web app for skincare, bodycare, hygiene, and haircare education. It includes a product library, routine builder, and moderated public contribution workflow.

## Current Stack

- Python
- Streamlit
- SQLite
- GitLab/GitHub
- Streamlit Community Cloud for deployment

## Important Files

- `app.py`: Main Streamlit app.
- `requirements.txt`: Python dependencies. Keep it simple; currently only `streamlit`.
- `modules/database.py`: SQLite setup, seed data, contribution storage.
- `modules/recommendations.py`: Filtering and routine recommendation logic.
- `.streamlit/config.toml`: Streamlit theme.
- `.specify/`: Spec Kit files and templates.
- `specs/001-glowguide-personal-care-platform/`: Feature specification, plan, tasks, research, and data model.

## Design Requirements

- Keep the UI unisex and inclusive.
- Use calm neutral colors.
- Avoid medical diagnosis or treatment claims.
- Keep content beginner-friendly.
- Keep public contributions pending until reviewed.

## Common Commands

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
git status
git add .
git commit -m "Update GlowGuide"
git push origin main
git push github main
```

## Future Work

- Add Kaggle datasets under `data/`.
- Expand seed product records.
- Improve recommendation quality.
- Add real authentication for maintainers.
- Deploy to Streamlit Community Cloud.
