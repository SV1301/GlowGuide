from __future__ import annotations

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_DIR = ROOT_DIR / "db"
DB_PATH = DB_DIR / "glowguide.db"

# Bump this number whenever new products are added to SEED_PRODUCTS.
# initialize_database() will re-seed automatically when the stored count
# falls below this threshold (handles both first-run and migrations).
_EXPECTED_MIN_COUNT = 45


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
        if count < _EXPECTED_MIN_COUNT:
            conn.execute("DELETE FROM products")
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
        query = "SELECT * FROM products ORDER BY care_category, routine_step, name"
        rows = conn.execute(query).fetchall()
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


# ---------------------------------------------------------------------------
# Seed data
# ---------------------------------------------------------------------------
# Schema: (name, care_category, routine_step, description, when_to_use,
#          best_for_skin_types, related_concerns, ingredients,
#          caution_note, budget_level)
#
# For Haircare products:
#   best_for_skin_types  → scalp type (oily, dry, normal, combination,
#                          flaky, sensitive, itchy, all)
#   related_concerns     → haircare concern keywords (see i18n.HAIRCARE_CONCERNS_INTERNAL)
# ---------------------------------------------------------------------------

SEED_PRODUCTS: list[tuple] = [
    # ── SKINCARE ─────────────────────────────────────────────────────────
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
        "A lightweight cleanser that effectively removes excess oil and impurities.",
        "Morning and evening",
        "oily, combination",
        "oiliness, acne, basic routine",
        "salicylic acid, green tea, niacinamide",
        "Avoid over-cleansing; it can worsen dryness or irritation.",
        "low",
    ),
    (
        "Micellar Water",
        "Skincare",
        "Cleanse",
        "A gentle no-rinse cleanser that lifts makeup and impurities using micellar technology.",
        "Morning or as a first-cleanse step in the evening",
        "all",
        "sensitivity, dryness, basic routine",
        "micelles, glycerin, gentle surfactants",
        "Not a full replacement for a rinse-off cleanser when wearing heavy SPF or makeup.",
        "medium",
    ),
    (
        "Face Scrub",
        "Skincare",
        "Exfoliate",
        "A physical exfoliant that manually buffs away dead skin cells for smoother texture.",
        "Once or twice weekly",
        "normal, combination, oily",
        "texture, dullness, oiliness",
        "sugar, rice powder, jojoba beads",
        "Avoid on active breakouts or sensitive skin. Use gentle circular motions.",
        "low",
    ),
    (
        "Chemical Exfoliant",
        "Skincare",
        "Exfoliate",
        "Helps remove dead skin cells and improve rough texture when used carefully.",
        "Once or twice weekly",
        "oily, combination, normal",
        "texture, oiliness, dullness, acne",
        "lactic acid, mandelic acid, salicylic acid",
        "Do not use too often. Avoid if skin is irritated or barrier is damaged.",
        "medium",
    ),
    (
        "Toner",
        "Skincare",
        "Tone",
        "Balances skin pH after cleansing and prepares skin for subsequent steps.",
        "Morning and evening after cleansing",
        "all",
        "oiliness, dryness, dullness, texture, basic routine",
        "niacinamide, hyaluronic acid, AHA, BHA, rose water",
        "Avoid alcohol-heavy toners on dry or sensitive skin.",
        "low",
    ),
    (
        "Essence",
        "Skincare",
        "Treat",
        "A lightweight hydrating layer that boosts absorption of serums and moisturizers.",
        "Morning and evening after toning",
        "dry, normal, combination",
        "dryness, dullness, pigmentation",
        "fermented ingredients, hyaluronic acid, niacinamide",
        "Layer sparingly before serum for best results.",
        "medium",
    ),
    (
        "Serum",
        "Skincare",
        "Treat",
        "A concentrated treatment targeting specific concerns with high-potency actives.",
        "Morning or evening after toning",
        "all",
        "pigmentation, dullness, acne, dryness, texture",
        "vitamin C, niacinamide, retinol, hyaluronic acid, peptides",
        "Introduce one new active at a time. Some actives increase sun sensitivity.",
        "medium",
    ),
    (
        "Spot Treatment",
        "Skincare",
        "Treat",
        "A targeted product applied to blemishes to reduce inflammation and speed healing.",
        "Evening on active blemishes only",
        "oily, combination",
        "acne, oiliness",
        "salicylic acid, benzoyl peroxide, tea tree oil, sulfur",
        "Apply only on blemishes. Overuse can cause dryness. Discontinue if irritation is severe.",
        "low",
    ),
    (
        "Sheet Mask",
        "Skincare",
        "Mask",
        "A single-use cloth mask soaked in serum for intense hydration and skin benefits.",
        "Once or twice weekly, leave on 15-20 minutes",
        "all",
        "dryness, dullness, sensitivity, basic routine",
        "hyaluronic acid, ceramides, vitamin C, collagen peptides",
        "Do not reuse. Pat remaining serum into skin rather than rinsing.",
        "low",
    ),
    (
        "Face Mask",
        "Skincare",
        "Mask",
        "A rinse-off treatment mask for specific concerns like oiliness, dryness, or dullness.",
        "Once or twice weekly",
        "all",
        "oiliness, dryness, dullness, texture, acne",
        "kaolin, bentonite, hyaluronic acid, charcoal, AHA",
        "Follow time instructions. Do not let clay masks dry completely on skin.",
        "medium",
    ),
    (
        "Moisturizer",
        "Skincare",
        "Moisturize",
        "Helps maintain the skin barrier and reduce dryness throughout the day.",
        "Morning and evening",
        "all",
        "dryness, sensitivity, basic routine",
        "ceramides, glycerin, hyaluronic acid",
        "Choose lighter textures for oily skin and richer textures for dry skin.",
        "low",
    ),
    (
        "Night Cream",
        "Skincare",
        "Moisturize",
        "A richer moisturizer designed for overnight skin barrier repair and renewal.",
        "Evening as the last skincare step",
        "dry, normal, sensitive",
        "dryness, sensitivity, pigmentation",
        "ceramides, peptides, retinol, shea butter, hyaluronic acid",
        "Night creams with retinol may cause purging. Introduce slowly.",
        "medium",
    ),
    (
        "Sunscreen",
        "Skincare",
        "Protect",
        "Protects exposed skin from UV damage and supports long-term skin health.",
        "Every morning, reapply when outdoors",
        "all",
        "pigmentation, dullness, basic routine",
        "broad spectrum SPF 30 or higher, zinc oxide, chemical filters",
        "Reapply every 2 hours when outdoors. Sunscreen is non-negotiable in daytime routines.",
        "medium",
    ),
    (
        "Eye Cream",
        "Skincare",
        "Treat",
        "A gentle formulation for the delicate eye area to address puffiness, dryness, and lines.",
        "Morning and evening after serum",
        "all",
        "dryness, sensitivity, pigmentation",
        "peptides, caffeine, hyaluronic acid, ceramides",
        "Use ring finger to apply gently. Avoid direct contact with eyes.",
        "medium",
    ),
    (
        "Lip Balm",
        "Skincare",
        "Protect",
        "Protects and moisturizes the delicate lip skin to prevent chapping and dryness.",
        "Throughout the day and before bed",
        "all",
        "dryness, sensitivity, basic routine",
        "shea butter, beeswax, vitamin E",
        "Choose fragrance-free formulas for sensitive skin.",
        "low",
    ),
    # ── BODYCARE ─────────────────────────────────────────────────────────
    (
        "Body Wash",
        "Bodycare",
        "Cleanse",
        "Cleanses the body while helping maintain skin comfort and freshness.",
        "Daily during shower",
        "all",
        "odor, general",
        "gentle surfactants, glycerin",
        "Avoid harsh scrubbing if skin feels dry or itchy.",
        "low",
    ),
    (
        "Body Scrub",
        "Bodycare",
        "Exfoliate",
        "Removes dead skin cells from the body to improve texture and prep skin for moisturizing.",
        "Once or twice weekly before body wash",
        "all",
        "rough texture, dryness, dullness",
        "sugar, salt, coffee grounds, jojoba beads, oils",
        "Avoid on irritated or sunburned skin. Moisturize well after use.",
        "low",
    ),
    (
        "Body Lotion",
        "Bodycare",
        "Moisturize",
        "Hydrates body skin and supports smoother, softer texture after bathing.",
        "After showering on slightly damp skin",
        "all",
        "dryness, rough texture",
        "glycerin, shea butter, ceramides",
        "Apply on slightly damp skin for better absorption.",
        "low",
    ),
    (
        "Body Butter",
        "Bodycare",
        "Moisturize",
        "A rich, thick moisturizer for intense hydration of very dry or rough body skin.",
        "After showering, focus on dry areas like elbows and knees",
        "dry, normal",
        "dryness, rough texture",
        "shea butter, cocoa butter, mango butter, vitamin E",
        "Can feel heavy on oily skin. Use sparingly on body acne-prone areas.",
        "medium",
    ),
    (
        "Body Oil",
        "Bodycare",
        "Moisturize",
        "A lightweight oil that seals in moisture and gives skin a healthy glow.",
        "After showering on damp skin",
        "dry, normal, combination",
        "dryness, rough texture, dullness",
        "jojoba oil, argan oil, rosehip oil, vitamin E",
        "Patch test for fragrance sensitivity. Avoid on acne-prone areas.",
        "medium",
    ),
    (
        "Hand Cream",
        "Bodycare",
        "Moisturize",
        "A targeted moisturizer that repairs hand dryness caused by frequent washing or weather.",
        "After washing hands and before bed",
        "all",
        "dryness, rough texture",
        "shea butter, glycerin, ceramides, lanolin",
        "Reapply throughout the day. Consider SPF formula for daytime outdoor exposure.",
        "low",
    ),
    (
        "Foot Cream",
        "Bodycare",
        "Moisturize",
        "A rich cream formulated for the rough skin of the feet, targeting cracked heels.",
        "Before bed after washing feet",
        "all",
        "dryness, rough texture",
        "urea, shea butter, salicylic acid, lanolin",
        "Higher urea concentrations are more effective for very rough skin.",
        "low",
    ),
    (
        "Bath Salts",
        "Bodycare",
        "Cleanse",
        "Mineral-rich salts that relax muscles and soften skin during bathing.",
        "Added to warm bath water, soak 15-20 minutes",
        "all",
        "dryness, rough texture, general",
        "Epsom salt, Himalayan salt, essential oils, magnesium",
        "Avoid on broken or irritated skin. Rinse and moisturize after soaking.",
        "low",
    ),
    # ── HAIRCARE ─────────────────────────────────────────────────────────
    (
        "Shampoo",
        "Haircare",
        "Cleanse",
        "Removes dirt, oil, and product buildup from hair and scalp.",
        "As needed based on scalp type — typically every 2-3 days",
        "all",
        "dandruff, oily scalp, product build-up, general",
        "gentle surfactants, biotin, scalp-calming agents",
        "Over-washing strips natural oils. Frequency depends on scalp oiliness and lifestyle.",
        "low",
    ),
    (
        "Conditioner",
        "Haircare",
        "Condition",
        "Replenishes moisture and smooths the hair cuticle for softer, more manageable hair.",
        "After shampooing, focus on mid-lengths to ends",
        "dry, normal, combination, sensitive",
        "dry hair, frizzy hair, damaged hair, split ends, general",
        "silicones, fatty alcohols, panthenol, natural oils",
        "Avoid applying to scalp if prone to buildup. Rinse thoroughly.",
        "low",
    ),
    (
        "Hair Mask",
        "Haircare",
        "Treat",
        "An intensive deep conditioning treatment that restores moisture and strength to hair.",
        "Once or twice weekly, leave on 10-30 minutes before rinsing",
        "dry, sensitive, combination",
        "dry hair, damaged hair, frizzy hair, split ends, hair thinning",
        "protein, keratin, argan oil, avocado, honey",
        "Protein overload can cause brittleness. Alternate with moisture-only masks.",
        "medium",
    ),
    (
        "Hair Serum",
        "Haircare",
        "Style",
        "A lightweight product that adds shine, reduces frizz, and protects hair during styling.",
        "On damp or dry hair before or after styling",
        "all",
        "frizzy hair, dry hair, heat damaged, damaged hair, general",
        "silicones, argan oil, keratin, vitamin E",
        "Use sparingly to avoid weighing hair down or causing buildup.",
        "medium",
    ),
    (
        "Hair Oil",
        "Haircare",
        "Nourish",
        "Nourishes and conditions hair from scalp to ends, promoting shine and reducing breakage.",
        "As an overnight treatment or pre-wash oil before shampooing",
        "dry, normal, combination, itchy",
        "dry hair, hair fall, itchy scalp, dandruff, damaged hair, hair thinning",
        "coconut oil, argan oil, castor oil, bhringraj, amla",
        "Heavy oils can weigh fine hair down. Avoid if scalp is acne-prone.",
        "low",
    ),
    (
        "Leave-in Conditioner",
        "Haircare",
        "Condition",
        "A no-rinse conditioner that detangles, moisturizes, and protects hair all day.",
        "After washing on damp hair; do not rinse",
        "dry, normal, combination, sensitive",
        "dry hair, frizzy hair, damaged hair, split ends, curly hair, general",
        "panthenol, fatty acids, glycerin, plant extracts",
        "Start with a small amount. Overuse causes buildup, especially on fine hair.",
        "medium",
    ),
    (
        "Heat Protectant",
        "Haircare",
        "Protect",
        "Shields hair from heat damage caused by blow dryers, straighteners, and curling tools.",
        "Before any heat styling, applied to damp or dry hair",
        "all",
        "heat damaged, damaged hair, dry hair, frizzy hair, general",
        "thermal polymers, silicones, panthenol, hydrolyzed proteins",
        "Apply before every heat styling session. Does not make heat styling completely safe.",
        "medium",
    ),
    (
        "Scalp Cleanser",
        "Haircare",
        "Cleanse",
        "Cleanses scalp buildup, sweat, and oil according to hair and scalp needs.",
        "As needed — typically 1-2 times per week",
        "all",
        "oily scalp, itchy scalp, product build-up, dandruff, general",
        "mild cleansing agents, soothing ingredients",
        "Frequency depends on scalp oiliness, activity level, and hair type.",
        "low",
    ),
    (
        "Scalp Scrub",
        "Haircare",
        "Exfoliate",
        "Removes dead skin cells, product buildup, and excess sebum from the scalp surface.",
        "Once weekly before shampooing",
        "oily, flaky, combination",
        "dandruff, oily scalp, itchy scalp, product build-up, flaky scalp",
        "sugar, sea salt, salicylic acid, tea tree oil, charcoal",
        "Use gently — no more than once weekly. Follow with a gentle shampoo.",
        "medium",
    ),
    (
        "Dry Shampoo",
        "Haircare",
        "Cleanse",
        "Absorbs excess scalp oil between washes to extend time between shampoo days.",
        "Between wash days on dry hair only",
        "oily, combination",
        "oily scalp, product build-up, general",
        "starch, silica, kaolin clay",
        "Not a substitute for regular washing. Overuse leads to buildup and scalp irritation.",
        "low",
    ),
    (
        "Curl Cream",
        "Haircare",
        "Style",
        "Defines and moisturizes curly or wavy hair, reducing frizz and enhancing curl pattern.",
        "On damp hair before air drying or diffusing",
        "dry, normal, combination",
        "curly hair, frizzy hair, dry hair, lack of volume, general",
        "glycerin, shea butter, botanical extracts",
        "Adjust the amount based on hair density. Too much weighs curls down.",
        "medium",
    ),
    (
        "Hair Mist",
        "Haircare",
        "Treat",
        "A lightweight spray that refreshes and adds moisture to hair between washes.",
        "On dry or slightly damp hair throughout the day",
        "all",
        "dry hair, frizzy hair, lack of volume, general",
        "aloe vera, rose water, panthenol, light botanical oils",
        "Spray lightly and evenly. Excess misting can weigh fine hair down.",
        "low",
    ),
    # ── HYGIENE ──────────────────────────────────────────────────────────
    (
        "Deodorant",
        "Hygiene",
        "Freshness",
        "Helps manage body odor caused by sweat and bacteria throughout the day.",
        "On clean dry underarms daily",
        "all",
        "odor, general",
        "fragrance-free options, baking soda, zinc ricinoleate",
        "If irritation occurs, switch to a gentler formula. Avoid on broken skin.",
        "low",
    ),
    (
        "Antiperspirant",
        "Hygiene",
        "Freshness",
        "Reduces sweating by temporarily blocking sweat glands, controlling odor and moisture.",
        "On clean dry underarms daily or as needed",
        "all",
        "odor, sweat, general",
        "aluminum compounds, fragrance-free options available",
        "Apply to fully healed, unbroken skin only. Avoid immediately after shaving.",
        "low",
    ),
    (
        "Intimate Wash",
        "Hygiene",
        "Cleanse",
        "A pH-balanced cleanser formulated for the sensitive intimate area.",
        "During daily bathing, externally only",
        "all",
        "odor, sensitivity, general",
        "lactic acid, gentle surfactants, prebiotics",
        "Use externally only. Avoid fragranced products on sensitive skin.",
        "low",
    ),
    (
        "Hand Wash",
        "Hygiene",
        "Cleanse",
        "A liquid or foam soap that cleanses hands while minimizing dryness.",
        "After the bathroom, before eating, and when visibly dirty",
        "all",
        "general, odor",
        "mild surfactants, glycerin, aloe vera",
        "Rinse thoroughly. Choose moisturizing formulas if hands feel dry.",
        "low",
    ),
    (
        "Hand Sanitizer",
        "Hygiene",
        "Cleanse",
        "An alcohol-based hand cleanser for use when soap and water are unavailable.",
        "When hand washing is not possible",
        "all",
        "general",
        "ethanol or isopropyl alcohol 60-70%, glycerin",
        "Not a replacement for soap when hands are visibly dirty.",
        "low",
    ),
    (
        "Mouthwash",
        "Hygiene",
        "Oral Care",
        "An antibacterial rinse that freshens breath and reduces harmful oral bacteria.",
        "After brushing; swish for 30 seconds then spit",
        "all",
        "odor, oral health, general",
        "fluoride, essential oils, alcohol-free options available",
        "Do not swallow. Alcohol-free formulas are gentler for daily use.",
        "low",
    ),
    (
        "Toothpaste",
        "Hygiene",
        "Oral Care",
        "Cleanses and protects teeth from decay while freshening breath.",
        "Twice daily during brushing, for two minutes",
        "all",
        "oral health, general",
        "fluoride, silica, sodium bicarbonate, whitening agents",
        "Use a pea-sized amount. Rinse and spit; do not swallow.",
        "low",
    ),
    (
        "Tongue Cleaner",
        "Hygiene",
        "Oral Care",
        "Removes bacteria and debris from the tongue to improve oral hygiene and freshen breath.",
        "Daily, as part of the oral hygiene routine",
        "all",
        "odor, oral health, general",
        "stainless steel or plastic scraper",
        "Scrape gently from back to front. Rinse the cleaner after each use.",
        "low",
    ),
    (
        "Dental Floss",
        "Hygiene",
        "Oral Care",
        "Removes food particles and plaque from between teeth where a toothbrush cannot reach.",
        "Daily, before or after brushing",
        "all",
        "oral health, general",
        "nylon or PTFE thread, waxed or unwaxed options",
        "Floss gently to avoid gum damage. Consider a water flosser as an alternative.",
        "low",
    ),
    (
        "Foot Powder",
        "Hygiene",
        "Freshness",
        "Absorbs excess moisture and controls odor in shoes and on feet throughout the day.",
        "Applied to clean dry feet and inside shoes daily",
        "all",
        "odor, sweat, general",
        "talc-free alternatives, baking soda, cornstarch, antifungal agents",
        "Do not use on broken or irritated skin.",
        "low",
    ),
    (
        "Feminine Hygiene Products",
        "Hygiene",
        "Care",
        "Disposable or reusable products for menstrual hygiene management.",
        "During menstruation as per individual preference and product instructions",
        "all",
        "general, sensitivity",
        "organic cotton, fragrance-free options, biodegradable materials",
        "Change regularly per product instructions. Choose unscented for sensitive skin.",
        "low",
    ),
    (
        "Shaving Cream",
        "Hygiene",
        "Grooming",
        "Creates a protective lather that softens hair and shields skin during shaving.",
        "Applied to wet skin immediately before shaving",
        "all",
        "sensitivity, general",
        "glycerin, fatty acids, soothing botanicals",
        "Choose sensitive-skin formulas to reduce irritation. Avoid on broken skin.",
        "low",
    ),
    (
        "Aftershave",
        "Hygiene",
        "Grooming",
        "Soothes, hydrates, and protects freshly shaved skin to reduce redness and irritation.",
        "Applied immediately after shaving",
        "all",
        "sensitivity, general",
        "aloe vera, witch hazel, glycerin, alcohol-free options available",
        "Avoid alcohol-heavy formulas on dry or sensitive skin.",
        "low",
    ),
    (
        "Nail Care Products",
        "Hygiene",
        "Grooming",
        "Tools and treatments for clean, healthy nails, including files and cuticle oil.",
        "Weekly or as needed for grooming and maintenance",
        "all",
        "general",
        "cuticle oil, nail strengthener, base coat, top coat",
        "Keep nails trimmed and clean. Moisturize cuticles to prevent cracking.",
        "low",
    ),
]
