# Research: GlowGuide Personal Care Platform

## Decision: Use React with Vite for Frontend

React with Vite is selected because it is beginner-friendly, fast to start, widely used in hackathons, and suitable for building interactive interfaces such as filters, tabs, cards, and routine builders.

Alternatives considered:

- Plain HTML, CSS, and JavaScript: easier at first, but harder to organize as the app grows.
- Next.js: powerful, but may add unnecessary complexity for a first hackathon.

## Decision: Use Tailwind CSS

Tailwind CSS is selected because it allows fast styling without writing large custom CSS files. It is suitable for creating a clean, responsive, visually polished interface within limited time.

Alternatives considered:

- Bootstrap: faster for basic components but less flexible visually.
- Custom CSS: flexible but slower for a beginner.

## Decision: Use Node.js and Express for Backend

Express is selected because it is simple, common, and easy to connect with a React frontend. It is suitable for building REST API endpoints for products, skin types, concerns, and recommendations.

Alternatives considered:

- Django: powerful but may be heavier for this project.
- Firebase-only backend: simpler, but less clear for demonstrating custom backend logic.

## Decision: Use MongoDB Atlas for Database

MongoDB Atlas is selected because GlowGuide content is document-based and may have flexible fields for ingredients, concerns, cautions, and recommendations. MongoDB documents match the JSON-like structure used by the frontend.

Alternatives considered:

- PostgreSQL: strong relational database, but schema changes may take more planning.
- Local JSON only: simpler, but does not satisfy the backend/database requirement.

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
