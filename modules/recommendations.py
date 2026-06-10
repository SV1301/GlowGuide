from __future__ import annotations

import pandas as pd


def filter_products(
    products: pd.DataFrame,
    care_category: str,
    skin_type: str,
    concern: str,
    budget: str,
) -> pd.DataFrame:
    result = products[products["care_category"].str.lower() == care_category.lower()].copy()

    skin = skin_type.lower()
    selected_concern = concern.lower()
    selected_budget = budget.lower()

    result = result[
        result["best_for_skin_types"].str.lower().str.contains(skin, na=False)
        | result["best_for_skin_types"].str.lower().str.contains("all", na=False)
    ]

    if selected_concern != "general":
        concern_matches = result["related_concerns"].str.lower().str.contains(selected_concern, na=False)
        if concern_matches.any():
            result = result[concern_matches]

    if selected_budget != "flexible":
        budget_matches = result["budget_level"].str.lower().eq(selected_budget)
        if budget_matches.any():
            result = result[budget_matches]

    return result


def routine_summary(care_category: str, products: pd.DataFrame) -> list[str]:
    if products.empty:
        return [
            "Start with a gentle cleanser or wash.",
            "Add a moisturizer or hydrating step if skin feels dry.",
            "Use sunscreen on exposed skin during the day.",
        ]

    ordered_steps = []
    for _, row in products.drop_duplicates("routine_step").iterrows():
        ordered_steps.append(f"{row['routine_step']}: {row['name']} - {row['when_to_use']}")

    if care_category.lower() == "skincare" and not any("Protect" in step for step in ordered_steps):
        ordered_steps.append("Protect: Sunscreen - every morning")

    return ordered_steps
