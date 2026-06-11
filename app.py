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
    HAIRCARE_CONCERNS_INTERNAL,
    SCALP_TYPES_INTERNAL,
    SKIN_TYPES_INTERNAL,
    init_language,
    render_language_selector,
    t,
    tl,
)
from modules.recommendations import filter_products, routine_summary

st.set_page_config(
    page_title="GlowGuide",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Design system CSS
# ---------------------------------------------------------------------------
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

/* ── Root tokens ─────────────────────────────────────────── */
:root {
    --c-dark:   #050505;
    --c-burg:   #610C27;
    --c-burg2:  #4a0a1e;
    --c-taupe:  #AC9C8D;
    --c-blush:  #E3C1B4;
    --c-warm:   #DDD9CE;
    --c-off:    #EFECE9;
    --c-white:  #ffffff;
    --r-card:   12px;
    --shadow:   0 2px 16px rgba(5,5,5,.08);
    --trans:    0.25s ease;
}

/* ── Global ──────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}
.main .block-container {
    padding-top: 2rem;
    max-width: 1200px;
}
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: var(--c-dark) !important;
    letter-spacing: -0.02em;
}
h1 { font-size: 2.6rem !important; }
h2 { font-size: 1.9rem !important; }
h3 { font-size: 1.25rem !important; }
p, li, label { color: var(--c-dark); }

/* ── Sidebar ─────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: var(--c-dark) !important;
}
[data-testid="stSidebar"] * {
    color: var(--c-off) !important;
}
[data-testid="stSidebar"] .stRadio label {
    padding: .35rem 0;
    font-size: .92rem;
    transition: color var(--trans);
}
[data-testid="stSidebar"] .stRadio label:hover {
    color: var(--c-blush) !important;
}
[data-testid="stSidebar"] [data-baseweb="select"] {
    background: #1a1a1a !important;
}

/* ── Product cards ───────────────────────────────────────── */
.gg-card {
    background: var(--c-white);
    border: 1px solid var(--c-warm);
    border-top: 3px solid var(--c-burg);
    border-radius: var(--r-card);
    padding: 1.25rem 1.1rem;
    min-height: 160px;
    box-shadow: var(--shadow);
    transition: transform var(--trans), box-shadow var(--trans);
}
.gg-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 28px rgba(97,12,39,.13);
}
.gg-muted {
    color: var(--c-taupe);
    font-size: 0.9rem;
    line-height: 1.5;
}
.gg-pill {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    margin: 0.1rem;
    border-radius: 999px;
    background: #f5ece9;
    color: var(--c-burg);
    font-size: 0.8rem;
    font-weight: 500;
}

/* ── Homepage navigation cards ──────────────────────────── */
.gg-home-card {
    background: var(--c-white);
    border-radius: var(--r-card);
    padding: 1.6rem 1.2rem 1rem;
    text-align: center;
    border: 1px solid var(--c-warm);
    box-shadow: var(--shadow);
    margin-bottom: .5rem;
    transition: transform var(--trans), box-shadow var(--trans);
    cursor: pointer;
}
.gg-home-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 32px rgba(97,12,39,.15);
    border-color: var(--c-blush);
}
.gg-home-card .gg-icon {
    font-size: 2rem;
    margin-bottom: .5rem;
    display: block;
}
.gg-home-card h3 {
    margin: .3rem 0 .5rem;
    font-size: 1.15rem !important;
    color: var(--c-dark) !important;
}
.gg-home-card p {
    font-size: .86rem;
    color: var(--c-taupe);
    margin: 0 0 .8rem;
    line-height: 1.5;
}

/* ── Buttons ─────────────────────────────────────────────── */
.stButton > button {
    background: var(--c-burg) !important;
    color: var(--c-off) !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: .88rem !important;
    padding: .5rem 1.2rem !important;
    transition: background var(--trans), transform var(--trans) !important;
    letter-spacing: .02em !important;
}
.stButton > button:hover {
    background: var(--c-burg2) !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Form inputs ─────────────────────────────────────────── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
[data-baseweb="select"] {
    border-radius: 8px !important;
    border-color: var(--c-warm) !important;
    background: var(--c-white) !important;
    font-family: 'Inter', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--c-burg) !important;
    box-shadow: 0 0 0 2px rgba(97,12,39,.15) !important;
}

/* ── Tables ──────────────────────────────────────────────── */
.stTable table {
    border-radius: var(--r-card) !important;
    overflow: hidden;
    font-size: .88rem;
}
.stTable thead th {
    background: var(--c-burg) !important;
    color: var(--c-off) !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: .03em;
}
.stTable tbody tr:nth-child(even) { background: var(--c-off) !important; }
.stTable tbody tr:hover { background: #f5ece9 !important; }

/* ── Section dividers ────────────────────────────────────── */
.gg-divider {
    border: none;
    border-top: 1px solid var(--c-warm);
    margin: 1.5rem 0;
}

/* ── Hero strip ──────────────────────────────────────────── */
.gg-hero {
    background: linear-gradient(135deg, var(--c-dark) 0%, var(--c-burg) 100%);
    border-radius: var(--r-card);
    padding: 2.5rem 2rem;
    color: var(--c-off) !important;
    margin-bottom: 1.5rem;
}
.gg-hero h1, .gg-hero p { color: var(--c-off) !important; }
.gg-hero h1 { margin: 0 0 .5rem !important; }
.gg-hero p { color: var(--c-blush) !important; font-size: 1.05rem; margin: 0; }

/* ── Alerts / info boxes ─────────────────────────────────── */
[data-testid="stAlert"] {
    border-radius: 8px !important;
    font-size: .9rem !important;
}

/* ── Expanders ───────────────────────────────────────────── */
[data-testid="stExpander"] {
    border: 1px solid var(--c-warm) !important;
    border-radius: 8px !important;
    background: var(--c-white) !important;
}
</style>
"""

# ---------------------------------------------------------------------------
# Page IDs (session-state keys)
# ---------------------------------------------------------------------------
_PAGE_HOME = "home"
_PAGE_LIBRARY = "library"
_PAGE_ROUTINE = "routine"
_PAGE_CONTRIBUTE = "contribute"
_PAGE_REVIEW = "review"
_NAV_ORDER = [_PAGE_HOME, _PAGE_LIBRARY, _PAGE_ROUTINE, _PAGE_CONTRIBUTE, _PAGE_REVIEW]

_HOME_CARDS: list[tuple[str, str, str]] = [
    ("skincare", "🧴", "Skincare"),
    ("bodycare", "🛁", "Bodycare"),
    ("haircare", "💆", "Haircare"),
    ("hygiene", "🪥", "Hygiene"),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _navigate(page: str, preset_care_area: str | None = None) -> None:
    """Switch page and optionally preset the routine builder care area."""
    st.session_state["nav_page"] = page
    if preset_care_area is not None:
        st.session_state["preset_care_area"] = preset_care_area
    elif page != _PAGE_ROUTINE:
        st.session_state.pop("preset_care_area", None)
    st.rerun()


def _care_category_display(en_cat: str) -> str:
    return t(f"care_categories.{en_cat.lower()}")


def _index_of(options: list[str], value: str) -> int:
    return options.index(value) if value in options else 0


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------


def _render_sidebar() -> None:
    st.sidebar.markdown(
        f"<h2 style='color:#E3C1B4;font-family:Playfair Display,serif;"
        f"font-size:1.5rem;margin-bottom:.2rem'>{t('app_title')}</h2>",
        unsafe_allow_html=True,
    )
    st.sidebar.markdown(
        "<hr style='border-color:#333;margin:.5rem 0 1rem'>",
        unsafe_allow_html=True,
    )

    render_language_selector()
    st.sidebar.markdown("<div style='margin:.5rem 0'></div>", unsafe_allow_html=True)

    nav_labels = [t(f"nav.{p}") for p in _NAV_ORDER]
    current_idx = _NAV_ORDER.index(st.session_state.get("nav_page", _PAGE_HOME))
    selected_label: str = st.sidebar.radio(
        t("nav.navigate"),
        nav_labels,
        index=current_idx,
    )
    chosen_page = _NAV_ORDER[nav_labels.index(selected_label)]
    if chosen_page != st.session_state.get("nav_page"):
        _navigate(chosen_page)


# ---------------------------------------------------------------------------
# Shared component
# ---------------------------------------------------------------------------


def render_product_card(product: dict) -> None:
    st.markdown(
        f"""
        <div class="gg-card">
            <h3>{product["name"]}</h3>
            <p class="gg-muted">{product["description"]}</p>
            <p><strong>{t("library.card.step")}:</strong> {product["routine_step"]}</p>
            <p><strong>{t("library.card.when")}:</strong> {product["when_to_use"]}</p>
            <p><strong>{t("library.card.look_for")}:</strong>
               <span class="gg-pill">{product["ingredients"]}</span></p>
            <p><strong>{t("library.card.note")}:</strong>
               <span class="gg-muted">{product["caution_note"]}</span></p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------


def home_page() -> None:
    # Hero banner
    st.markdown(
        f"""
        <div class="gg-hero">
            <h1>{t("home.title")}</h1>
            <p>{t("home.subheader")}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(t("home.description"))
    st.markdown("<hr class='gg-divider'>", unsafe_allow_html=True)

    cols = st.columns(4)
    for col, (key, icon, en_area) in zip(cols, _HOME_CARDS, strict=False):
        with col:
            title = t(f"home.cards.{key}_title")
            text = t(f"home.cards.{key}_text")
            btn_label = t("home.explore_btn")
            st.markdown(
                f"""
                <div class="gg-home-card">
                    <span class="gg-icon">{icon}</span>
                    <h3>{title}</h3>
                    <p>{text}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(btn_label, key=f"home_btn_{key}", use_container_width=True):
                _navigate(_PAGE_ROUTINE, preset_care_area=en_area)


def library_page(products: list[dict]) -> None:
    st.header(t("library.header"))
    st.write(t("library.description"))
    st.markdown("<hr class='gg-divider'>", unsafe_allow_html=True)

    en_categories = sorted({p["care_category"] for p in products})
    display_categories = [t("library.all_option")] + [
        _care_category_display(c) for c in en_categories
    ]
    col_f, col_s = st.columns([1, 2])
    with col_f:
        selected_display = st.selectbox(t("library.care_category_label"), display_categories)
    with col_s:
        query = st.text_input(t("library.search_label"))

    if selected_display == t("library.all_option"):
        selected_en = "All"
    else:
        selected_en = next(
            (e for e in en_categories if _care_category_display(e) == selected_display),
            selected_display,
        )

    filtered = products
    if selected_en != "All":
        filtered = [p for p in filtered if p["care_category"] == selected_en]
    if query:
        q = query.lower()
        filtered = [p for p in filtered if q in p["name"].lower() or q in p["description"].lower()]

    if not filtered:
        st.info(t("library.no_results"))
        return

    st.markdown(
        f"<p class='gg-muted'>{len(filtered)} product(s) found</p>",
        unsafe_allow_html=True,
    )
    for chunk_start in range(0, len(filtered), 3):
        cols = st.columns(3)
        # strict=False — last chunk may have fewer items than columns
        for col, product in zip(cols, filtered[chunk_start : chunk_start + 3], strict=False):
            with col:
                render_product_card(product)


def routine_page(products: list[dict]) -> None:
    st.header(t("routine.header"))
    st.write(t("routine.description"))
    st.markdown("<hr class='gg-divider'>", unsafe_allow_html=True)

    care_areas_disp = tl("routine.care_areas")

    # Apply homepage preset (only once)
    preset = st.session_state.pop("preset_care_area", None)
    if preset and preset in CARE_AREAS_INTERNAL:
        preset_disp = care_areas_disp[CARE_AREAS_INTERNAL.index(preset)]
        st.session_state["routine_care_area"] = preset_disp

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        care_area_disp: str = st.selectbox(
            t("routine.care_area_label"),
            care_areas_disp,
            key="routine_care_area",
        )
        care_area_idx = _index_of(care_areas_disp, care_area_disp)
        care_category = CARE_AREAS_INTERNAL[care_area_idx]

    is_haircare = care_category == "Haircare"

    with col2:
        if is_haircare:
            scalp_types_disp = tl("routine.scalp_types")
            scalp_disp: str = st.selectbox(t("routine.scalp_type_label"), scalp_types_disp)
            skin_type = SCALP_TYPES_INTERNAL[_index_of(scalp_types_disp, scalp_disp)]
        else:
            skin_types_disp = tl("routine.skin_types")
            skin_disp: str = st.selectbox(t("routine.skin_type_label"), skin_types_disp)
            skin_type = SKIN_TYPES_INTERNAL[_index_of(skin_types_disp, skin_disp)]

    with col3:
        if is_haircare:
            concerns_disp = tl("routine.haircare_concerns")
            concern_internal = HAIRCARE_CONCERNS_INTERNAL
        else:
            concerns_disp = tl("routine.concerns")
            concern_internal = CONCERNS_INTERNAL
        concern_disp: str = st.selectbox(t("routine.concern_label"), concerns_disp)
        concern = concern_internal[_index_of(concerns_disp, concern_disp)]

    with col4:
        budgets_disp = tl("routine.budgets")
        budget_disp: str = st.selectbox(t("routine.budget_label"), budgets_disp)
        budget = BUDGETS_INTERNAL[_index_of(budgets_disp, budget_disp)]

    matches = filter_products(products, care_category, skin_type, concern, budget)
    steps = routine_summary(care_category, matches)

    st.markdown("<hr class='gg-divider'>", unsafe_allow_html=True)
    c_left, c_right = st.columns([1, 2])

    with c_left:
        st.subheader(t("routine.suggested_routine"))
        for step in steps:
            st.markdown(f"• {step}")

    with c_right:
        st.subheader(t("routine.recommended_products"))
        if not matches:
            st.info(t("routine.no_match"))
        else:
            st.table(
                [
                    {
                        t("routine.table.product"): p["name"],
                        t("routine.table.step"): p["routine_step"],
                        t("routine.table.when"): p["when_to_use"],
                        t("routine.table.look_for"): p["ingredients"],
                        t("routine.table.note"): p["caution_note"],
                    }
                    for p in matches
                ]
            )

    st.warning(t("routine.disclaimer"))


def contribute_page() -> None:
    st.header(t("contribute.header"))
    st.write(t("contribute.description"))
    st.markdown("<hr class='gg-divider'>", unsafe_allow_html=True)

    care_areas_disp = tl("routine.care_areas")

    with st.form("contribution_form", clear_on_submit=True):
        title = st.text_input(t("contribute.title_label"))
        contributor_name = st.text_input(
            t("contribute.name_label"), value=t("contribute.name_default")
        )
        contribution_type = st.selectbox(t("contribute.type_label"), tl("contribute.types"))
        care_category_disp: str = st.selectbox(t("contribute.category_label"), care_areas_disp)
        proposed_content = st.text_area(t("contribute.content_label"), height=150)
        source_url = st.text_input(t("contribute.url_label"))
        submitted = st.form_submit_button(t("contribute.submit_btn"))

    if submitted:
        if not title.strip() or not proposed_content.strip():
            st.error(t("contribute.error_empty"))
        else:
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
    st.markdown("<hr class='gg-divider'>", unsafe_allow_html=True)

    passcode = st.text_input(t("review.passcode_label"), type="password")
    if passcode != "glowguide-admin":
        st.info(t("review.passcode_hint"))
        return

    pending = get_contributions("pending")
    if not pending:
        st.success(t("review.no_pending"))
        return

    for row in pending:
        with st.expander(f"#{row['id']} — {row['title']}"):
            st.write(row["proposed_content"])
            st.caption(
                f"{row['contribution_type']} | {row['care_category']}"
                f" | by {row['contributor_name']}"
            )
            note = st.text_area(t("review.reviewer_note_label"), key=f"note_{row['id']}")
            # Decision values are stored in English in the DB.
            decision = st.selectbox(
                t("review.decision_label"),
                ["approved", "rejected", "needs-changes"],
                key=f"decision_{row['id']}",
            )
            if st.button(t("review.save_btn"), key=f"save_{row['id']}"):
                review_contribution(int(row["id"]), decision, note)
                st.success(t("review.save_success"))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    # Language must be initialised before any t() call.
    init_language()

    # Page state
    if "nav_page" not in st.session_state:
        st.session_state["nav_page"] = _PAGE_HOME

    initialize_database()
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    products = get_products()
    _render_sidebar()

    current_page: str = st.session_state["nav_page"]
    if current_page == _PAGE_HOME:
        home_page()
    elif current_page == _PAGE_LIBRARY:
        library_page(products)
    elif current_page == _PAGE_ROUTINE:
        routine_page(products)
    elif current_page == _PAGE_CONTRIBUTE:
        contribute_page()
    else:
        review_page()


if __name__ == "__main__":
    main()
