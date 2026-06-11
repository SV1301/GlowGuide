"""Internationalisation (i18n) helpers for GlowGuide.

Usage
-----
from modules.i18n import init_language, render_language_selector, t, tl

# Translate a single string:
label = t("library.header")

# Translate a list (e.g. selectbox options):
options = tl("routine.care_areas")

Adding a new language
---------------------
1. Create ``locales/<code>.json`` mirroring the structure of ``locales/en.json``.
2. Add an entry to ``SUPPORTED_LANGUAGES`` below.
"""

from __future__ import annotations

import json
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------------------
# Public configuration
# ---------------------------------------------------------------------------

SUPPORTED_LANGUAGES: dict[str, str] = {
    "English": "en",
    "हिन्दी": "hi",
    "తెలుగు": "te",
}

# English values used internally for database queries.
# Must stay in sync with the order of translated lists in every locale file.
CARE_AREAS_INTERNAL: list[str] = ["Skincare", "Bodycare", "Haircare", "Hygiene"]
SKIN_TYPES_INTERNAL: list[str] = ["all", "oily", "dry", "combination", "normal", "sensitive"]
SCALP_TYPES_INTERNAL: list[str] = [
    "all",
    "oily",
    "dry",
    "normal",
    "combination",
    "flaky",
    "sensitive",
    "itchy",
]
CONCERNS_INTERNAL: list[str] = [
    "general",
    "dryness",
    "oiliness",
    "acne",
    "sensitivity",
    "texture",
    "odor",
    "pigmentation",
]
HAIRCARE_CONCERNS_INTERNAL: list[str] = [
    "general",
    "dandruff",
    "hair fall",
    "hair thinning",
    "dry hair",
    "frizzy hair",
    "split ends",
    "oily scalp",
    "itchy scalp",
    "product build-up",
    "damaged hair",
    "lack of volume",
    "curly hair",
    "color treated",
    "heat damaged",
]
BUDGETS_INTERNAL: list[str] = ["flexible", "low", "medium"]

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

_LOCALES_DIR = Path(__file__).resolve().parents[1] / "locales"
_cache: dict[str, dict] = {}


def _load(lang_code: str) -> dict:
    """Load and cache a locale JSON file."""
    if lang_code in _cache:
        return _cache[lang_code]
    path = _LOCALES_DIR / f"{lang_code}.json"
    if not path.exists():
        path = _LOCALES_DIR / "en.json"
    with path.open(encoding="utf-8") as fh:
        data: dict = json.load(fh)
    _cache[lang_code] = data
    return data


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def t(key: str) -> str:
    """Return the translated string for *key* (dot-notation).

    Falls back to the key itself when the translation is missing.
    """
    lang_code: str = st.session_state.get("lang", "en")
    node: object = _load(lang_code)
    for part in key.split("."):
        if isinstance(node, dict):
            node = node.get(part, key)
        else:
            return key
    if isinstance(node, str):
        return node
    return key


def tl(key: str) -> list[str]:
    """Return the translated string list for *key* (dot-notation).

    Falls back to an empty list when the translation is missing.
    """
    lang_code: str = st.session_state.get("lang", "en")
    node: object = _load(lang_code)
    for part in key.split("."):
        if isinstance(node, dict):
            node = node.get(part)
        else:
            return []
    if isinstance(node, list):
        return [str(item) for item in node]
    return []


def init_language() -> None:
    """Initialise language from URL query params or session state.

    Query-param persistence means the selected language survives page
    refreshes and can be shared via URL (e.g. ``?lang=hi``).
    """
    params = st.query_params
    if "lang" in params:
        candidate = params["lang"]
        if candidate in SUPPORTED_LANGUAGES.values():
            st.session_state["lang"] = candidate
    if "lang" not in st.session_state:
        st.session_state["lang"] = "en"


def render_language_selector() -> None:
    """Render the sidebar language selector widget.

    Triggers a full rerun on language change so every translated string
    is refreshed immediately.
    """
    lang_names = list(SUPPORTED_LANGUAGES.keys())
    lang_codes = list(SUPPORTED_LANGUAGES.values())
    current_code: str = st.session_state.get("lang", "en")
    current_index = lang_codes.index(current_code) if current_code in lang_codes else 0

    selected_name: str = st.sidebar.selectbox(
        t("language_selector"),
        lang_names,
        index=current_index,
        key="lang_selector",
    )
    selected_code = SUPPORTED_LANGUAGES[selected_name]
    if selected_code != current_code:
        st.session_state["lang"] = selected_code
        st.query_params["lang"] = selected_code
        st.rerun()
