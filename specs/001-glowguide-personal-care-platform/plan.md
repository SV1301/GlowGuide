# Implementation Plan: GlowGuide Personal Care Platform

## Technical Summary

GlowGuide will be built as a Streamlit web application. Streamlit will provide the user interface, page navigation, forms, recommendation flow, contribution submission flow, and maintainer review screens. Python modules will handle database access and recommendation logic. SQLite will be used for the MVP database because it is simple to run locally on Windows, while Supabase PostgreSQL remains the preferred future cloud database option if persistent hosted contributions are required.

## Architecture

```text
Streamlit App
  |
  | uses Python service modules
  v
Recommendation + Contribution Logic
  |
  | reads/writes structured records
  v
SQLite MVP Database
```

## Application Stack

- Streamlit for the web app interface.
- Python for application logic.
- pandas for filtering, tabular views, and dataset handling.
- SQLite for the local MVP database.
- Optional Supabase PostgreSQL for future hosted persistence.
- Streamlit theme configuration and custom CSS for styling.
- GitLab for version control and open-source contribution visibility.

## Database

SQLite will store structured records for:

- product categories
- care categories
- skin types
- concerns
- routine templates
- recommendation rules
- contributor submissions
- moderation status records

SQLite is suitable for the first Streamlit version because it works locally without server setup. If the app is deployed and needs persistent public contributions, the same data model can later move to Supabase PostgreSQL.

## Key Pages

- Home
- Skincare
- Bodycare
- Hygiene
- Haircare
- Product Library
- Routine Builder
- Recommendation Results
- Contribute
- Maintainer Review Dashboard

## Streamlit Actions

```text
load_categories()
load_skin_types()
load_concerns()
load_products(filters)
generate_recommendation(care_category, skin_type, concern, budget)
submit_contribution(data)
load_contributions(status="pending")
review_contribution(contribution_id, decision, reviewer_note)
```

## Recommendation Logic

The user selects:

- care category
- skin type
- concern
- budget level

The Python recommendation service matches these inputs against database fields:

- `bestForSkinTypes`
- `relatedConcerns`
- `routineStep`
- `budgetLevel`
- `avoidForSkinTypes`

The app displays:

- routine title
- morning steps
- evening steps
- weekly steps
- product category suggestions
- ingredient suggestions
- caution notes

## Contribution Logic

Public contributors can submit suggested content through a contribution form. Each submission is saved with:

- contributor name or alias
- contribution type
- affected care category
- proposed content
- optional source link
- status set to `pending`

Maintainers review pending submissions. Approved contributions can be converted into product category records, routine notes, ingredient notes, or caution notes. Rejected contributions remain stored with a review reason.

## Minimum Viable Product

The hackathon MVP should include:

- Responsive homepage.
- Category pages for skincare, bodycare, and hygiene.
- Product library with database-backed entries.
- Routine builder form.
- Contribution form for public suggestions.
- Review status field for submitted contributions.
- SQLite database connected through Python helper functions.
- Seed data for products, skin types, concerns, and routines.
- README and Spec Kit documentation.

## Deferred Features

These should be saved for future scope:

- Login and saved routines.
- Full admin dashboard with role-based login.
- Supabase PostgreSQL migration for persistent hosted contributions.
- Real e-commerce product links.
- AI chatbot.
- Image upload skin analysis.
- Medical-condition recommendation system.

## Security and Privacy

- Do not collect sensitive personal data in MVP.
- Store only general preference inputs if needed.
- Allow anonymous or alias-based contributions.
- Keep database credentials in environment variables if using Supabase later.
- Do not commit `.env` files to GitLab.

## Deployment Plan

- App: Streamlit Community Cloud.
- MVP Database: SQLite file seeded with starter content.
- Future Database: Supabase PostgreSQL.
- Environment variables for future Supabase setup:
  - `SUPABASE_URL`
  - `SUPABASE_KEY`

## Project Structure

```text
glowguide/
  app.py
  requirements.txt
  .streamlit/
    config.toml
  data/
    seed_products.csv
    seed_skin_types.csv
    seed_concerns.csv
  db/
    glowguide.db
  modules/
    database.py
    recommendations.py
    contributions.py
    content.py
  pages/
    1_Skincare.py
    2_Bodycare.py
    3_Hygiene.py
    4_Product_Library.py
    5_Routine_Builder.py
    6_Contribute.py
    7_Review_Contributions.py
  .specify/
    memory/
      constitution.md
  specs/
    001-glowguide-personal-care-platform/
      spec.md
      plan.md
      tasks.md
      research.md
      data-model.md
  README.md
```

## Build Strategy

1. Complete Spec Kit docs.
2. Create Streamlit app structure.
3. Add unisex theme and navigation.
4. Create SQLite tables and seed starter data.
5. Build category pages.
6. Build product library and filters.
7. Build routine recommendation flow.
8. Add contribution submission and review status flow.
9. Polish styling and responsive behavior.
10. Deploy to Streamlit Community Cloud.
