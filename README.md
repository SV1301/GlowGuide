# GlowGuide

GlowGuide is an interactive unisex personal care platform. It helps users understand skincare, bodycare, hygiene, and basic self-care product categories, then guides them through personalized routines based on skin type, concern, and budget.

## Problem Statement

Many beginners feel confused by personal care content because product terms, routines, skin types, and ingredient advice are scattered across social media, blogs, and shopping apps. GlowGuide organizes this information into one beginner-friendly platform where users can learn what each product does, when to use it, and how to build a safe routine.

## Proposed Solution

GlowGuide provides:

- Educational sections for skincare, bodycare, hygiene, and haircare.
- A searchable product library explaining generic product terms.
- Routine guidance for oily, dry, combination, normal, and sensitive skin.
- Bodycare guidance for concerns like dryness, body acne, pigmentation, odor, and ingrown hair.
- A recommendation flow powered by database records for product categories, routine steps, skin types, and concerns.
- An open-source contribution system where the public can suggest product terms, routine improvements, ingredient notes, and educational content.
- A moderation workflow so public contributions are reviewed before becoming visible recommendations.
- Clear disclaimers that the platform gives educational guidance and does not replace medical advice.

## Tech Stack

- App Framework: Streamlit
- Language: Python
- Data Handling: pandas
- Database: SQLite for MVP, Supabase PostgreSQL as future cloud database option
- Charts/Visuals: Streamlit native charts and optional Plotly
- Styling: Streamlit theme configuration and custom CSS
- Deployment: Streamlit Community Cloud
- Version Control: GitLab

## UI Direction

GlowGuide should use a unisex, calm, clean design instead of a heavily feminine visual style. The interface should feel inclusive, modern, and care-focused with neutral colors such as soft white, mist gray, sage, teal, muted blue, and warm accent tones. Copy should address "users" or "people" rather than only girls or women.

## Open Source Contribution Model

GlowGuide is designed as an open-source knowledge platform. Contributors can help by:

- Suggesting new generic product terms.
- Adding beginner-friendly explanations.
- Improving routine guidance.
- Adding ingredient notes and caution notes.
- Reporting outdated or unsafe content.

Public submissions should enter a `pending` review state. Maintainers review each contribution for clarity, safety, duplication, and source quality before approving it for the public product library or recommendation system.

## Spec Kit Artifacts

Spec Kit documentation is available in:

- `.specify/memory/constitution.md`
- `specs/001-glowguide-personal-care-platform/spec.md`
- `specs/001-glowguide-personal-care-platform/plan.md`
- `specs/001-glowguide-personal-care-platform/tasks.md`
- `specs/001-glowguide-personal-care-platform/research.md`
- `specs/001-glowguide-personal-care-platform/data-model.md`

## Future Scope

- Admin panel for updating product entries.
- User saved routines.
- Region-specific product recommendations.
- Ingredient checker.
- Dermatologist-reviewed content badges.
- Multilingual support.
