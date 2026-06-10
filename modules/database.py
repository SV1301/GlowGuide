from __future__ import annotations

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_DIR = ROOT_DIR / "db"
DB_PATH = DB_DIR / "glowguide.db"


def connect() -> sqlite3.Connection:
    DB_DIR.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database() -> None:
    with connect() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                care_category TEXT NOT NULL,
                routine_step TEXT NOT NULL,
                description TEXT NOT NULL,
                when_to_use TEXT NOT NULL,
                best_for_skin_types TEXT NOT NULL,
                related_concerns TEXT NOT NULL,
                ingredients TEXT NOT NULL,
                caution_note TEXT NOT NULL,
                budget_level TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS contributions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                contributor_name TEXT NOT NULL,
                contribution_type TEXT NOT NULL,
                care_category TEXT NOT NULL,
                proposed_content TEXT NOT NULL,
                source_url TEXT,
                status TEXT NOT NULL DEFAULT 'pending',
                reviewer_note TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            """
        )

        count = conn.execute("SELECT COUNT(*) FROM products").fetchone()[0]
        if count == 0:
            conn.executemany(
                """
                INSERT INTO products (
                    name, care_category, routine_step, description, when_to_use,
                    best_for_skin_types, related_concerns, ingredients,
                    caution_note, budget_level
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                SEED_PRODUCTS,
            )


def get_products() -> list[dict]:
    with connect() as conn:
        rows = conn.execute("SELECT * FROM products ORDER BY care_category, routine_step, name").fetchall()
        return [dict(row) for row in rows]


def save_contribution(data: dict[str, str]) -> None:
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO contributions (
                title, contributor_name, contribution_type, care_category,
                proposed_content, source_url, status
            ) VALUES (?, ?, ?, ?, ?, ?, 'pending')
            """,
            (
                data["title"],
                data["contributor_name"],
                data["contribution_type"],
                data["care_category"],
                data["proposed_content"],
                data.get("source_url", ""),
            ),
        )


def get_contributions(status: str | None = None) -> list[dict]:
    query = "SELECT * FROM contributions"
    params: tuple[str, ...] = ()
    if status:
        query += " WHERE status = ?"
        params = (status,)
    query += " ORDER BY created_at DESC"
    with connect() as conn:
        rows = conn.execute(query, params).fetchall()
        return [dict(row) for row in rows]


def review_contribution(contribution_id: int, status: str, reviewer_note: str) -> None:
    with connect() as conn:
        conn.execute(
            "UPDATE contributions SET status = ?, reviewer_note = ? WHERE id = ?",
            (status, reviewer_note, contribution_id),
        )


SEED_PRODUCTS = [
    (
        "Gentle Cleanser",
        "Skincare",
        "Cleanse",
        "Removes sweat, oil, sunscreen, and daily buildup without stripping the skin.",
        "Morning and evening",
        "dry, sensitive, normal, combination",
        "dryness, sensitivity, basic routine",
        "glycerin, ceramides, low-fragrance formulas",
        "Stop if it causes burning, tightness, or visible irritation.",
        "low",
    ),
    (
        "Gel Cleanser",
        "Skincare",
        "Cleanse",
        "A lightweight cleanser that can suit oilier skin types.",
        "Morning and evening",
        "oily, combination",
        "oiliness, acne-prone skin",
        "salicylic acid, green tea, niacinamide",
        "Avoid over-cleansing because it can worsen dryness or irritation.",
        "low",
    ),
    (
        "Moisturizer",
        "Skincare",
        "Moisturize",
        "Helps maintain the skin barrier and reduce dryness.",
        "Morning and evening",
        "all",
        "dryness, sensitivity, barrier support",
        "ceramides, glycerin, hyaluronic acid",
        "Choose lighter textures for oily skin and richer textures for dry skin.",
        "low",
    ),
    (
        "Sunscreen",
        "Skincare",
        "Protect",
        "Protects exposed skin from UV damage and supports long-term skin health.",
        "Every morning",
        "all",
        "pigmentation, dullness, sun exposure",
        "broad spectrum SPF 30 or higher",
        "Reapply when outdoors for long periods. Sunscreen is not optional in daytime routines.",
        "medium",
    ),
    (
        "Chemical Exfoliant",
        "Skincare",
        "Exfoliate",
        "Helps remove dead skin cells and can improve rough texture when used carefully.",
        "Once or twice weekly",
        "oily, combination, normal",
        "texture, clogged pores, dullness",
        "lactic acid, mandelic acid, salicylic acid",
        "Do not use too often. Avoid if skin is irritated or barrier is damaged.",
        "medium",
    ),
    (
        "Body Wash",
        "Bodycare",
        "Cleanse",
        "Cleanses the body while helping maintain comfort and freshness.",
        "Daily",
        "all",
        "odor, sweat, daily hygiene",
        "gentle surfactants, glycerin",
        "Avoid harsh scrubbing if skin feels dry or itchy.",
        "low",
    ),
    (
        "Body Lotion",
        "Bodycare",
        "Moisturize",
        "Hydrates body skin and supports smoother texture.",
        "After showering",
        "all",
        "dryness, rough texture",
        "glycerin, shea butter, ceramides",
        "Apply on slightly damp skin for better comfort.",
        "low",
    ),
    (
        "Deodorant",
        "Hygiene",
        "Freshness",
        "Helps manage body odor caused by sweat and bacteria.",
        "As needed",
        "all",
        "odor, sweat",
        "fragrance-free options, gentle formulas",
        "If irritation occurs, switch to a gentler formula.",
        "low",
    ),
    (
        "Scalp Cleanser",
        "Haircare",
        "Cleanse",
        "Cleanses scalp buildup, sweat, and oil according to hair and scalp needs.",
        "As needed",
        "all",
        "oiliness, buildup, scalp comfort",
        "mild cleansing agents, soothing ingredients",
        "Frequency depends on scalp oiliness, activity, and hair type.",
        "low",
    ),
]
