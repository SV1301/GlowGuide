from __future__ import annotations


def filter_products(
    products: list[dict],
    care_category: str,
    skin_type: str,
    concern: str,
    budget: str,
) -> list[dict]:
    skin = skin_type.lower()
    selected_concern = concern.lower()
    selected_budget = budget.lower()
    result = []

    for product in products:
        if product["care_category"].lower() != care_category.lower():
            continue

        best_for = product["best_for_skin_types"].lower()
        if skin not in best_for and "all" not in best_for:
            continue

        result.append(product)

    if selected_concern != "general":
        concern_matches = [
            product for product in result if selected_concern in product["related_concerns"].lower()
        ]
        if concern_matches:
            result = concern_matches

    if selected_budget != "flexible":
        budget_matches = [
            product for product in result if product["budget_level"].lower() == selected_budget
        ]
        if budget_matches:
            result = budget_matches

    return result


def routine_summary(care_category: str, products: list[dict]) -> list[str]:
    if not products:
        return [
            "Start with a gentle cleanser or wash.",
            "Add a moisturizer or hydrating step if skin feels dry.",
            "Use sunscreen on exposed skin during the day.",
        ]

    ordered_steps = []
    seen_steps = set()
    for product in products:
        if product["routine_step"] in seen_steps:
            continue
        seen_steps.add(product["routine_step"])
        step_text = f"{product['routine_step']}: {product['name']} - {product['when_to_use']}"
        ordered_steps.append(step_text)

    missing_protect = not any("Protect" in step for step in ordered_steps)
    if care_category.lower() == "skincare" and missing_protect:
        ordered_steps.append("Protect: Sunscreen - every morning")

    return ordered_steps
