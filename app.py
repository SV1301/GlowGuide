from __future__ import annotations

import streamlit as st

from modules.database import (
    get_contributions,
    get_products,
    initialize_database,
    review_contribution,
    save_contribution,
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


def render_product_card(product: dict) -> None:
    st.markdown(
        f"""
        <div class="gg-card">
            <h3>{product["name"]}</h3>
            <p class="gg-muted">{product["description"]}</p>
            <p><strong>Step:</strong> {product["routine_step"]}</p>
            <p><strong>When:</strong> {product["when_to_use"]}</p>
            <p><strong>Look for:</strong> {product["ingredients"]}</p>
            <p><strong>Note:</strong> {product["caution_note"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def home_page() -> None:
    st.title("GlowGuide")
    st.subheader("A unisex personal care guide for skincare, bodycare, hygiene, and haircare.")
    st.write(
        "Explore product terms, build simple routines, and contribute safer beginner-friendly "
        "personal care knowledge through a moderated open-source workflow."
    )

    cols = st.columns(4)
    cards = [
        ("Skincare", "Cleanse, moisturize, protect, and understand skin type basics."),
        ("Bodycare", "Build body routines for dryness, odor, texture, and body acne support."),
        ("Hygiene", "Learn practical daily hygiene categories and product terms."),
        ("Contribute", "Suggest improvements that maintainers can review before publishing."),
    ]
    for col, (title, text) in zip(cols, cards):
        with col:
            st.markdown(f"<div class='gg-card'><h3>{title}</h3><p>{text}</p></div>", unsafe_allow_html=True)


def library_page(products) -> None:
    st.header("Product Library")
    st.write("Search generic product categories and learn what each one does.")

    categories = ["All"] + sorted({product["care_category"] for product in products})
    selected_category = st.selectbox("Care category", categories)
    query = st.text_input("Search product terms")

    filtered = products
    if selected_category != "All":
        filtered = [product for product in filtered if product["care_category"] == selected_category]
    if query:
        query_lower = query.lower()
        filtered = [
            product
            for product in filtered
            if query_lower in product["name"].lower()
            or query_lower in product["description"].lower()
        ]

    if not filtered:
        st.info("No matching product terms found yet.")
        return

    for chunk_start in range(0, len(filtered), 2):
        cols = st.columns(2)
        for col, product in zip(cols, filtered[chunk_start : chunk_start + 2]):
            with col:
                render_product_card(product)


def routine_page(products) -> None:
    st.header("Routine Builder")
    st.write("Choose your care area, skin type, concern, and budget to get a simple starter routine.")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        care_category = st.selectbox("Care area", ["Skincare", "Bodycare", "Hygiene", "Haircare"])
    with col2:
        skin_type = st.selectbox("Skin type", ["all", "oily", "dry", "combination", "normal", "sensitive"])
    with col3:
        concern = st.selectbox(
            "Concern",
            ["general", "dryness", "oiliness", "acne", "sensitivity", "texture", "odor", "pigmentation"],
        )
    with col4:
        budget = st.selectbox("Budget", ["flexible", "low", "medium"])

    matches = filter_products(products, care_category, skin_type, concern, budget)
    steps = routine_summary(care_category, matches)

    st.subheader("Suggested Routine")
    for step in steps:
        st.markdown(f"- {step}")

    st.subheader("Recommended Product Categories")
    if not matches:
        st.info("No exact database match yet. Try a broader concern or flexible budget.")
    else:
        st.table(
            [
                {
                    "Product": product["name"],
                    "Step": product["routine_step"],
                    "When": product["when_to_use"],
                    "Look for": product["ingredients"],
                    "Note": product["caution_note"],
                }
                for product in matches
            ]
        )

    st.warning(
        "GlowGuide is educational and does not diagnose or treat medical conditions. "
        "For persistent irritation, infection, severe acne, or allergic reactions, consult a qualified professional."
    )


def contribute_page() -> None:
    st.header("Contribute to GlowGuide")
    st.write("Submit beginner-friendly content suggestions. Contributions stay pending until reviewed.")

    with st.form("contribution_form", clear_on_submit=True):
        title = st.text_input("Contribution title")
        contributor_name = st.text_input("Name or alias", value="Community Contributor")
        contribution_type = st.selectbox(
            "Contribution type",
            ["product-term", "routine-step", "ingredient-note", "caution-note", "correction", "other"],
        )
        care_category = st.selectbox("Care category", ["Skincare", "Bodycare", "Hygiene", "Haircare"])
        proposed_content = st.text_area("Proposed content", height=150)
        source_url = st.text_input("Optional source URL")
        submitted = st.form_submit_button("Submit contribution")

    if submitted:
        if not title.strip() or not proposed_content.strip():
            st.error("Please add a title and proposed content.")
        else:
            save_contribution(
                {
                    "title": title.strip(),
                    "contributor_name": contributor_name.strip() or "Community Contributor",
                    "contribution_type": contribution_type,
                    "care_category": care_category,
                    "proposed_content": proposed_content.strip(),
                    "source_url": source_url.strip(),
                }
            )
            st.success("Contribution submitted for review.")


def review_page() -> None:
    st.header("Review Contributions")
    st.write("For the MVP, this review screen is protected by a simple demo passcode.")
    passcode = st.text_input("Maintainer passcode", type="password")
    if passcode != "glowguide-admin":
        st.info("Enter the demo passcode to review pending submissions.")
        return

    pending = get_contributions("pending")
    if not pending:
        st.success("No pending contributions.")
        return

    for row in pending:
        with st.expander(f"#{row['id']} - {row['title']}"):
            st.write(row["proposed_content"])
            st.caption(f"{row['contribution_type']} | {row['care_category']} | by {row['contributor_name']}")
            note = st.text_area("Reviewer note", key=f"note_{row['id']}")
            decision = st.selectbox("Decision", ["approved", "rejected", "needs-changes"], key=f"decision_{row['id']}")
            if st.button("Save review", key=f"save_{row['id']}"):
                review_contribution(int(row["id"]), decision, note)
                st.success("Review saved. Refresh the page to update the list.")


def main() -> None:
    initialize_database()
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    products = get_products()
    st.sidebar.title("GlowGuide")
    page = st.sidebar.radio(
        "Navigate",
        ["Home", "Product Library", "Routine Builder", "Contribute", "Review Contributions"],
    )

    if page == "Home":
        home_page()
    elif page == "Product Library":
        library_page(products)
    elif page == "Routine Builder":
        routine_page(products)
    elif page == "Contribute":
        contribute_page()
    else:
        review_page()


if __name__ == "__main__":
    main()
