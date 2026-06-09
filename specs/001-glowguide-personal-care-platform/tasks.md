# Tasks: GlowGuide Personal Care Platform

## Phase 1: Documentation Submission

- [x] Create project README.
- [x] Create Spec Kit constitution.
- [x] Create feature specification.
- [x] Create implementation plan.
- [x] Create implementation task list.
- [x] Create research notes.
- [x] Create data model.
- [ ] Push documentation to GitLab repository.
- [ ] Submit GitLab repository link before 6:00 PM IST.

## Phase 2: Repository Setup

- [ ] Create root project folder named `glowguide`.
- [ ] Initialize Git repository.
- [ ] Create `client` folder for React frontend.
- [ ] Create `server` folder for Express backend.
- [ ] Add `.gitignore` for `node_modules`, `.env`, and build files.
- [ ] Add README and Spec Kit folders to repository.

## Phase 3: Frontend Setup

- [ ] Create React app using Vite.
- [ ] Install Tailwind CSS.
- [ ] Install Lucide React icons.
- [ ] Add React Router.
- [ ] Create shared layout with navigation.
- [ ] Create responsive page shell.

## Phase 4: Frontend Pages

- [ ] Build Home page.
- [ ] Build Skincare page.
- [ ] Build Bodycare page.
- [ ] Build Hygiene page.
- [ ] Build Haircare page.
- [ ] Build Product Library page.
- [ ] Build Routine Builder page.
- [ ] Build Contribute page for public submissions.
- [ ] Build Recommendation Results section.

## Phase 5: Backend Setup

- [ ] Initialize Node.js server project.
- [ ] Install Express, Mongoose, CORS, and dotenv.
- [ ] Create Express app.
- [ ] Connect backend to MongoDB Atlas.
- [ ] Add health check endpoint.
- [ ] Add error handling middleware.

## Phase 6: Database Models

- [ ] Create ProductCategory model.
- [ ] Create SkinType model.
- [ ] Create Concern model.
- [ ] Create RoutineTemplate model.
- [ ] Create RecommendationRule model.
- [ ] Create Contribution model.
- [ ] Create seed script for initial data.

## Phase 7: API Routes

- [ ] Add `/api/categories` route.
- [ ] Add `/api/skin-types` route.
- [ ] Add `/api/concerns` route.
- [ ] Add `/api/products` route with filters.
- [ ] Add `/api/routines` route.
- [ ] Add `/api/recommendations` route.
- [ ] Add `/api/contributions` route for public submissions.
- [ ] Add contribution review route for maintainers.

## Phase 8: Recommendation Flow

- [ ] Let user select care category.
- [ ] Let user select skin type.
- [ ] Let user select concern.
- [ ] Let user select budget level.
- [ ] Send selected values to backend.
- [ ] Display routine steps returned by backend.
- [ ] Display matching product categories.
- [ ] Display caution notes and educational disclaimer.

## Phase 8A: Contribution System

- [ ] Create contribution form fields.
- [ ] Store submitted contributions with `pending` status.
- [ ] Prevent pending contributions from appearing in public recommendations.
- [ ] Create basic maintainer review view or API endpoint.
- [ ] Allow maintainers to approve, reject, or request changes.
- [ ] Add reviewer notes for rejected or changed submissions.
- [ ] Add contribution guidelines to README.

## Phase 9: Content Seeding

- [ ] Add at least 20 product category records.
- [ ] Add 5 skin type records.
- [ ] Add at least 8 concern records.
- [ ] Add skincare AM and PM routine templates.
- [ ] Add bodycare routine templates.
- [ ] Add hygiene education content.

## Phase 10: Final Polish

- [ ] Test mobile layout.
- [ ] Test desktop layout.
- [ ] Check all links and navigation.
- [ ] Check API responses.
- [ ] Confirm empty states work.
- [ ] Update README with setup steps.
- [ ] Deploy frontend.
- [ ] Deploy backend.
- [ ] Add deployed links to README.
