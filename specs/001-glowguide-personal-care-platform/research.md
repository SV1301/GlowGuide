# Research: GlowGuide Personal Care Platform

## Decision: Use Streamlit for the MVP

Streamlit is selected because it is beginner-friendly, fast to build with, and suitable for creating forms, filters, dashboards, recommendation results, and contribution review screens in Python. It allows GlowGuide to be built as one app instead of separate frontend and backend projects.

Alternatives considered:

- React with Vite: flexible and visually strong, but requires more frontend setup.
- Next.js: powerful, but unnecessary for the MVP.
- Plain HTML, CSS, and JavaScript: simple initially, but weaker for database-backed interactive flows.

## Decision: Use Streamlit Theme and Custom CSS

Streamlit theme configuration and light custom CSS are selected because they keep styling simple while allowing GlowGuide to feel polished and unisex.

Alternatives considered:

- Tailwind CSS: strong for React projects, but not needed for Streamlit.
- Heavy custom CSS: flexible but slower for a first build.

## Decision: Use Python Modules Instead of a Separate Backend

Because Streamlit runs Python directly, the MVP does not need a separate Express backend. Recommendation logic, contribution handling, and database access can live in organized Python modules.

Alternatives considered:

- Node.js and Express: useful for a React app, but extra complexity here.
- Django: powerful but too large for the first version.
- FastAPI: good future option if GlowGuide later needs a public API.

## Decision: Use SQLite for MVP Database

SQLite is selected because it works locally on Windows without database server setup and is enough for storing product categories, concerns, recommendation rules, and contribution submissions during the MVP.

Alternatives considered:

- Supabase PostgreSQL: better for deployed public contributions, but requires cloud setup.
- MongoDB Atlas: flexible, but less directly aligned with a simple Streamlit/Python MVP.
- Local CSV or JSON only: simpler, but weaker as a database-backed project.

## Decision: Make GlowGuide Unisex

GlowGuide should support anyone learning personal care routines. The content can stay focused on skincare, bodycare, hygiene, and haircare, but the language and UI should avoid gender-exclusive wording. The visual system should use neutral, calm colors instead of a strongly feminine palette.

## Recommendation Strategy

The first version should use rule-based recommendations instead of AI. A rule-based approach is easier to explain, test, and complete during a hackathon.

Example matching fields:

- selected skin type
- selected care concern
- budget level
- product suitability
- caution rules

## Content Safety

GlowGuide should avoid medical claims. It should use phrases like "may help", "commonly used for", and "consider consulting a dermatologist" instead of promising outcomes.

## MVP Scope

The MVP should prioritize:

- educational content
- product library
- routine builder
- database-backed recommendation results
- public contribution submissions with moderation status

Features like user accounts, saved routines, admin dashboards, and AI chatbots should be future scope.

## Decision: Add Open-Source Contribution Workflow

GlowGuide should allow the public to contribute personal care information because the project is intended to grow as a community knowledge base. However, submissions should not be published automatically because personal care content can affect user safety.

The first version should support:

- public contribution form
- pending review status
- maintainer approval or rejection
- optional source link
- reviewer notes

Alternatives considered:

- GitLab merge requests only: good for developers, but not beginner-friendly for non-technical contributors.
- Open public editing: fast, but risky for misinformation and spam.
- Full user account system: useful later, but too large for the hackathon MVP.
