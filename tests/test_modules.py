"""Basic smoke tests for GlowGuide modules.

These tests verify the core data and logic contracts without requiring
a running Streamlit server or a live database file.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Database module tests
# ---------------------------------------------------------------------------

def test_seed_products_not_empty() -> None:
    """SEED_PRODUCTS must contain at least 40 entries."""
    from modules.database import SEED_PRODUCTS

    assert len(SEED_PRODUCTS) >= 40, (
        f"Expected at least 40 seed products, got {len(SEED_PRODUCTS)}"
    )


def test_seed_product_schema() -> None:
    """Every SEED_PRODUCTS entry must have exactly 10 fields."""
    from modules.database import SEED_PRODUCTS

    for idx, product in enumerate(SEED_PRODUCTS):
        assert len(product) == 10, (
            f"Product at index {idx} has {len(product)} fields, expected 10"
        )


def test_seed_product_care_categories() -> None:
    """All care categories must be one of the four valid values."""
    from modules.database import SEED_PRODUCTS

    valid = {"Skincare", "Bodycare", "Haircare", "Hygiene"}
    for idx, product in enumerate(SEED_PRODUCTS):
        assert product[1] in valid, (
            f"Product at index {idx} has invalid care_category: {product[1]!r}"
        )


def test_seed_product_budget_levels() -> None:
    """Budget levels must be 'low' or 'medium'."""
    from modules.database import SEED_PRODUCTS

    valid = {"low", "medium"}
    for idx, product in enumerate(SEED_PRODUCTS):
        assert product[9] in valid, (
            f"Product at index {idx} has invalid budget_level: {product[9]!r}"
        )


# ---------------------------------------------------------------------------
# Recommendations module tests
# ---------------------------------------------------------------------------

def test_filter_products_returns_list() -> None:
    """filter_products must return a list."""
    from modules.recommendations import filter_products

    result = filter_products([], "Skincare", "all", "general", "flexible")
    assert isinstance(result, list)


def test_filter_products_care_category() -> None:
    """filter_products must only return products matching the care category."""
    from modules.database import SEED_PRODUCTS
    from modules.recommendations import filter_products

    # Build minimal dict list from seed data
    products = [
        {
            "id": i,
            "name": p[0],
            "care_category": p[1],
            "routine_step": p[2],
            "description": p[3],
            "when_to_use": p[4],
            "best_for_skin_types": p[5],
            "related_concerns": p[6],
            "ingredients": p[7],
            "caution_note": p[8],
            "budget_level": p[9],
        }
        for i, p in enumerate(SEED_PRODUCTS)
    ]

    skincare_results = filter_products(products, "Skincare", "all", "general", "flexible")
    for item in skincare_results:
        assert item["care_category"] == "Skincare", (
            f"Expected Skincare, got {item['care_category']!r}"
        )


def test_routine_summary_returns_list() -> None:
    """routine_summary must return a non-empty list of strings."""
    from modules.recommendations import routine_summary

    result = routine_summary("Skincare", [])
    assert isinstance(result, list)
    assert len(result) > 0


# ---------------------------------------------------------------------------
# i18n module tests (file-based, no Streamlit session_state needed)
# ---------------------------------------------------------------------------

_LOCALES_DIR = Path(__file__).resolve().parents[1] / "locales"
_LOCALE_CODES = ["en", "hi", "te"]


@pytest.mark.parametrize("code", _LOCALE_CODES)
def test_locale_file_exists(code: str) -> None:
    """Each supported locale JSON file must exist."""
    path = _LOCALES_DIR / f"{code}.json"
    assert path.exists(), f"Missing locale file: {path}"


@pytest.mark.parametrize("code", _LOCALE_CODES)
def test_locale_file_valid_json(code: str) -> None:
    """Each locale file must be valid JSON."""
    path = _LOCALES_DIR / f"{code}.json"
    with path.open(encoding="utf-8") as fh:
        data = json.load(fh)
    assert isinstance(data, dict)


@pytest.mark.parametrize("code", _LOCALE_CODES)
def test_locale_has_required_keys(code: str) -> None:
    """Every locale must have the top-level required keys."""
    path = _LOCALES_DIR / f"{code}.json"
    with path.open(encoding="utf-8") as fh:
        data = json.load(fh)

    required = {"app_title", "nav", "home", "library", "routine", "contribute", "review"}
    missing = required - data.keys()
    assert not missing, f"Locale '{code}' is missing keys: {missing}"


def test_english_locale_care_areas_length() -> None:
    """English routine.care_areas must have exactly 4 entries."""
    path = _LOCALES_DIR / "en.json"
    with path.open(encoding="utf-8") as fh:
        data = json.load(fh)
    assert len(data["routine"]["care_areas"]) == 4


def test_all_locales_same_care_area_count() -> None:
    """All locales must have the same number of routine.care_areas."""
    counts = {}
    for code in _LOCALE_CODES:
        path = _LOCALES_DIR / f"{code}.json"
        with path.open(encoding="utf-8") as fh:
            data = json.load(fh)
        counts[code] = len(data["routine"]["care_areas"])

    values = list(counts.values())
    assert len(set(values)) == 1, f"care_areas count mismatch across locales: {counts}"
