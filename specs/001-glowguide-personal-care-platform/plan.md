# Implementation Plan: GlowGuide Personal Care Platform

## Technical Summary

GlowGuide will be built as a full-stack web application. The frontend will use React with Vite and Tailwind CSS to create a responsive, visual, interactive interface. The backend will use Node.js and Express to expose API endpoints for product categories, skin types, concerns, routine recommendations, and community contributions. MongoDB Atlas will store structured content so that recommendations are database-backed instead of hardcoded.

## Architecture

```text
React Frontend
  |
  | calls REST API
  v
Express Backend
  |
  | reads structured content
  v
MongoDB Atlas Database
  ^
  |
Contribution Review Flow
```

## Frontend Stack

- React with Vite for fast development.
- Tailwind CSS for styling.
- Lucide React for clean icons.
- React Router for navigation.
- Axios or Fetch API for backend calls.

## Backend Stack

- Node.js runtime.
- Express.js API server.
- Mongoose for MongoDB models.
- CORS for frontend-backend communication.
- dotenv for environment variables.

## Database

MongoDB Atlas will store flexible JSON-like documents for:

- product categories
- care categories
- skin types
- concerns
- routine templates
- recommendation rules
- contributor submissions
- moderation status records

MongoDB is suitable because the project content is structured but may evolve during the hackathon.

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

## API Endpoints

```text
GET /api/health
GET /api/categories
GET /api/skin-types
GET /api/concerns
GET /api/products
GET /api/products?category=skincare&skinType=oily
GET /api/routines
POST /api/recommendations
POST /api/contributions
GET /api/contributions?status=pending
PATCH /api/contributions/:id/review
```

## Recommendation Logic

The user selects:

- care category
- skin type
- concern
- budget level

The backend matches these inputs against database fields:

- `bestForSkinTypes`
- `relatedConcerns`
- `routineStep`
- `budgetLevel`
- `avoidForSkinTypes`

The backend returns:

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
- Backend API connected to MongoDB Atlas.
- Seed data for products, skin types, concerns, and routines.
- README and Spec Kit documentation.

## Deferred Features

These should be saved for future scope:

- Login and saved routines.
- Full admin dashboard with role-based login.
- Real e-commerce product links.
- AI chatbot.
- Image upload skin analysis.
- Medical-condition recommendation system.

## Security and Privacy

- Do not collect sensitive personal data in MVP.
- Store only general preference inputs if needed.
- Allow anonymous or alias-based contributions.
- Keep database credentials in environment variables.
- Do not commit `.env` files to GitLab.

## Deployment Plan

- Frontend: Vercel or Netlify.
- Backend: Render.
- Database: MongoDB Atlas free tier.
- Environment variables:
  - `MONGODB_URI`
  - `PORT`
  - `CLIENT_URL`

## Project Structure

```text
glowguide/
  client/
    src/
      components/
      pages/
      data/
      services/
      App.jsx
      main.jsx
  server/
    models/
    routes/
    controllers/
    seed/
    app.js
    server.js
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
2. Create frontend layout and navigation.
3. Add static UI pages.
4. Build backend models and API routes.
5. Add contribution submission and review status flow.
6. Seed MongoDB with initial content.
7. Connect frontend filters to backend API.
8. Polish styling and responsive behavior.
9. Deploy frontend and backend.
