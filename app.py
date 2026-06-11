from __future__ import annotations

import streamlit as st

from modules.database import (
    get_contributions,
    get_products,
    initialize_database,
    review_contribution,
    save_contribution,
)
from modules.i18n import (
    BUDGETS_INTERNAL,
    CARE_AREAS_INTERNAL,
    CONCERNS_INTERNAL,
    SKIN_TYPES_INTERNAL,
    init_language,
    render_language_selector,
    t,
    tl,
)
from modules.recommendations import filter_products, routine_summary

st.set_page_config(
    page_title="GlowGuide",
    page_icon="G",
    layout="wide",
    initial_sidebar_state="expanded",
)


CUSTOM_CSS = """
<style>
    .main .block-container {
        padding-top: 2rem;
        max-width: 1180px;
    }
    h1, h2, h3 {
        color: #1f2933;
    }
    .gg-card {
        background: #ffffff;
        border: 1px solid #d8e3df;
        border-radius: 10px;
        padding: 1rem;
        min-height: 150px;
    }
    .gg-muted {
        color: #52635f;
        font-size: 0.95rem;
    }
    .gg-pill {
        display: inline-block;
        padding: 0.2rem 0.55rem;
        margin: 0.15rem;
        border-radius: 999px;
        background: #e2f0ee;
        color: #245b5c;
        font-size: 0.85rem;
    }
</style>
"""


def _care_category_display(en_cat: str) -> str:
    """Return the translated display name for an English care-category string."""
    return t(f"care_categories.{en_cat.lower()}")


def _index_of(options: list[str], value: str) -> int:
    """Return the index of *value* in *options*, defaulting to 0."""
    return options.index(value) if value in options else 0


def render_product_card(product: dict) -> None:
    st.markdown(
        f"""
        <div class="gg-card">
            <h3>{product["name"]}</h3>
            <p class="gg-muted">{product["description"]}</p>
            <p><strong>{t("library.card.step")}:</strong> {product["routine_step"]}</p>
            <p><strong>{t("library.card.when")}:</strong> {product["when_to_use"]}</p>
            <p><strong>{t("library.card.look_for")}:</strong> {product["ingredients"]}</p>
            <p><strong>{t("library.card.note")}:</strong> {product["caution_note"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def home_page() -> None:
    st.title(t("home.title"))
    st.subheader(t("home.subheader"))
    st.write(t("home.description"))

    cols = st.columns(4)
    cards = [
        (t("home.cards.skincare_title"), t("home.cards.skincare_text")),
        (t("home.cards.bodycare_title"), t("home.cards.bodycare_text")),
        (t("home.cards.hygiene_title"), t("home.cards.hygiene_text")),
        (t("home.cards.contribute_title"), t("home.cards.contribute_text")),
    ]
    # strict=False: cols and cards are always the same length by construction
    for col, (title, text) in zip(cols, cards, strict=False):
        with col:
            st.markdown(
                f"<div class='gg-card'><h3>{title}</h3><p>{text}</p></div>",
                unsafe_allow_html=True,
            )


def library_page(products: list[dict]) -> None:
    st.header(t("library.header"))
    st.write(t("library.description"))

    # DB returns English category names; translate for display only.
    en_categories = sorted({product["care_category"] for product in products})
    display_categories = [t("library.all_option")] + [
        _care_category_display(c) for c in en_categories
    ]
    selected_display = st.selectbox(t("library.care_category_label"), display_categories)
    query = st.text_input(t("library.search_label"))

    # Map displayed value back to English for DB filtering.
    if selected_display == t("library.all_option"):
        selected_en = "All"
    else:
        selected_en = next(
            (en for en in en_categories if _care_category_display(en) == selected_display),
            selected_display,
        )

    filtered = products
    if selected_en != "All":
        filtered = [p for p in filtered if p["care_category"] == selected_en]
    if query:
        query_lower = query.lower()
        filtered = [
            p
            for p in filtered
            if query_lower in p["name"].lower() or query_lower in p["description"].lower()
        ]

    if not filtered:
        st.info(t("library.no_results"))
        return

    for chunk_start in range(0, len(filtered), 2):
        cols = st.columns(2)
        # strict=False: last chunk may have fewer items than cols
        for col, product in zip(cols, filtered[chunk_start : chunk_start + 2], strict=False):
            with col:
                render_product_card(product)


def routine_page(products: list[dict]) -> None:
    st.header(t("routine.header"))
    st.write(t("routine.description"))

    # Translated display options
    care_areas_disp = tl("routine.care_areas")
    skin_types_disp = tl("routine.skin_types")
    concerns_disp = tl("routine.concerns")
    budgets_disp = tl("routine.budgets")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        care_area_disp = st.selectbox(t("routine.care_area_label"), care_areas_disp)
        care_category = CARE_AREAS_INTERNAL[_index_of(care_areas_disp, care_area_disp)]
    with col2:
        skin_type_disp = st.selectbox(t("routine.skin_type_label"), skin_types_disp)
        skin_type = SKIN_TYPES_INTERNAL[_index_of(skin_types_disp, skin_type_disp)]
    with col3:
        concern_disp = st.selectbox(t("routine.concern_label"), concerns_disp)
        concern = CONCERNS_INTERNAL[_index_of(concerns_disp, concern_disp)]
    with col4:
        budget_disp = st.selectbox(t("routine.budget_label"), budgets_disp)
        budget = BUDGETS_INTERNAL[_index_of(budgets_disp, budget_disp)]

    matches = filter_products(products, care_category, skin_type, concern, budget)
    steps = routine_summary(care_category, matches)

    st.subheader(t("routine.suggested_routine"))
    for step in steps:
        st.markdown(f"- {step}")

    st.subheader(t("routine.recommended_products"))
    if not matches:
        st.info(t("routine.no_match"))
    else:
        st.table(
            [
                {
                    t("routine.table.product"): product["name"],
                    t("routine.table.step"): product["routine_step"],
                    t("routine.table.when"): product["when_to_use"],
                    t("routine.table.look_for"): product["ingredients"],
                    t("routine.table.note"): product["caution_note"],
                }
                for product in matches
            ]
        )

    st.warning(t("routine.disclaimer"))


def contribute_page() -> None:
    st.header(t("contribute.header"))
    st.write(t("contribute.description"))

    care_areas_disp = tl("routine.care_areas")

    with st.form("contribution_form", clear_on_submit=True):
        title = st.text_input(t("contribute.title_label"))
        contributor_name = st.text_input(
            t("contribute.name_label"), value=t("contribute.name_default")
        )
        contribution_type = st.selectbox(t("contribute.type_label"), tl("contribute.types"))
        care_category_disp = st.selectbox(t("contribute.category_label"), care_areas_disp)
        proposed_content = st.text_area(t("contribute.content_label"), height=150)
        source_url = st.text_input(t("contribute.url_label"))
        submitted = st.form_submit_button(t("contribute.submit_btn"))

    if submitted:
        if not title.strip() or not proposed_content.strip():
            st.error(t("contribute.error_empty"))
        else:
            # Always store the English care-category string in the DB.
            care_category_en = CARE_AREAS_INTERNAL[_index_of(care_areas_disp, care_category_disp)]
            save_contribution(
                {
                    "title": title.strip(),
                    "contributor_name": (contributor_name.strip() or t("contribute.name_default")),
                    "contribution_type": contribution_type,
                    "care_category": care_category_en,
                    "proposed_content": proposed_content.strip(),
                    "source_url": source_url.strip(),
                }
            )
            st.success(t("contribute.success"))


def review_page() -> None:
    st.header(t("review.header"))
    st.write(t("review.description"))
    passcode = st.text_input(t("review.passcode_label"), type="password")
    if passcode != "glowguide-admin":
        st.info(t("review.passcode_hint"))
        return

    pending = get_contributions("pending")
    if not pending:
        st.success(t("review.no_pending"))
        return

    for row in pending:
        with st.expander(f"#{row['id']} - {row['title']}"):
            st.write(row["proposed_content"])
            st.caption(
                f"{row['contribution_type']} | {row['care_category']}"
                f" | by {row['contributor_name']}"
            )
            note = st.text_area(t("review.reviewer_note_label"), key=f"note_{row['id']}")
            # Decision values are kept in English — they are stored in the DB.
            decision = st.selectbox(
                t("review.decision_label"),
                ["approved", "rejected", "needs-changes"],
                key=f"decision_{row['id']}",
            )
            if st.button(t("review.save_btn"), key=f"save_{row['id']}"):
                review_contribution(int(row["id"]), decision, note)
                st.success(t("review.save_success"))


def main() -> None:
    # Language must be initialised before any t() call.
    init_language()
    initialize_database()
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    products = get_products()
    st.sidebar.title(t("app_title"))

    # Language selector appears directly below the app title.
    render_language_selector()

    nav_options = [
        t("nav.home"),
        t("nav.library"),
        t("nav.routine"),
        t("nav.contribute"),
        t("nav.review"),
    ]
    page = st.sidebar.radio(t("nav.navigate"), nav_options)

    if page == t("nav.home"):
        home_page()
    elif page == t("nav.library"):
        library_page(products)
    elif page == t("nav.routine"):
        routine_page(products)
    elif page == t("nav.contribute"):
        contribute_page()
    else:
        review_page()


if __name__ == "__main__":
    main()
