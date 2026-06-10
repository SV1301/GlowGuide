# GlowGuide User Manual

## Overview

GlowGuide helps users explore personal care basics across skincare, bodycare, hygiene, and haircare. It includes product education, routine suggestions, and a contribution system for community-submitted improvements.

## Running the App

From the project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL shown by Streamlit, usually:

```text
http://localhost:8501
```

## Pages

### Home

Introduces GlowGuide and its main sections.

### Product Library

Browse and search generic personal care product categories. Each item explains what the product does, when to use it, suitable concerns, and caution notes.

### Routine Builder

Choose a care area, skin type, concern, and budget. GlowGuide returns a simple educational routine based on database records.

### Contribute

Submit product terms, routine improvements, ingredient notes, caution notes, or corrections. Submissions are saved with pending status.

### Review Contributions

Maintainers can review pending submissions. The demo passcode is:

```text
glowguide-admin
```

This passcode is for MVP demonstration only and should be replaced with real authentication in production.

## Safety Note

GlowGuide is educational. It does not diagnose, treat, or replace advice from a qualified healthcare professional.
