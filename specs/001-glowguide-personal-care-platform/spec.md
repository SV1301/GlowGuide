# Feature Specification: GlowGuide Personal Care Platform

## Overview

GlowGuide is an interactive website that helps girls and young women understand personal care routines across skincare, bodycare, hygiene, and haircare. The platform explains generic product terms, organizes care steps by category, and recommends suitable product categories and routine steps based on user-selected skin type, concern, and budget.

GlowGuide is also designed as an open-source knowledge platform. Public contributors can suggest improvements to product explanations, routine steps, ingredient notes, and caution notes. Contributions must be reviewed before appearing in live recommendations.

## Goals

- Help beginners understand personal care product terms and routine steps.
- Provide organized sections for skincare, bodycare, hygiene, and haircare.
- Allow users to explore routines based on skin type and concern.
- Provide product category recommendations using structured database records.
- Support community contributions through a safe submission and review workflow.
- Create a visually engaging, easy-to-navigate website suitable for a hackathon demo.

## Non-Goals

- GlowGuide will not diagnose skin or health conditions.
- GlowGuide will not provide medical treatment plans.
- GlowGuide will not process payments or sell products directly.
- GlowGuide will not require user login in the first version.
- GlowGuide will not publish unreviewed public submissions directly into recommendations.

## Target Users

- Girls and young women starting personal care routines.
- Students who want a simple guide to skincare, bodycare, and hygiene.
- Beginners confused by product names, ingredients, and routine order.
- Users looking for budget-aware recommendations by skin type or concern.
- Open-source contributors who want to improve personal care education.

## User Stories

### US-001: Browse Personal Care Categories

As a beginner, I want to browse skincare, bodycare, hygiene, and haircare sections so that I can understand each area of personal care separately.

Acceptance Criteria:

- The homepage shows clear navigation to all major categories.
- Each category page explains its purpose and basic routine steps.
- Users can move between sections without losing context.

### US-002: Learn Product Terms

As a user, I want to search and read about product terms such as cleanser, sunscreen, exfoliant, body lotion, and deodorant so that I understand what each product does.

Acceptance Criteria:

- The product library lists generic product categories.
- Each product entry includes description, use timing, suitable users, ingredients to look for, and cautions.
- Users can filter products by category, routine step, or skin type.

### US-003: Get Skincare Routine Guidance

As a user, I want to select my skin type and concern so that I can see a suitable skincare routine.

Acceptance Criteria:

- Users can choose from oily, dry, combination, normal, and sensitive skin.
- Users can choose concerns such as acne, dullness, dryness, oiliness, pigmentation, or sensitivity.
- The platform displays morning and evening routine steps.
- Each step explains why it is included.

### US-004: Get Bodycare Guidance

As a user, I want to select a bodycare concern so that I can understand helpful routine steps and product categories.

Acceptance Criteria:

- Users can choose concerns such as dryness, body acne, odor, ingrown hair, rough texture, and pigmentation.
- The platform recommends relevant bodycare steps.
- The platform explains safe frequency for steps like exfoliation.

### US-005: View Recommendations From Database

As a user, I want recommendations to come from stored product and routine data so that results are consistent and expandable.

Acceptance Criteria:

- Product categories are retrieved from the backend API.
- Routine recommendations are generated using selected skin type, concern, and budget.
- Empty or unavailable results show a helpful fallback message.

### US-006: Submit Community Contributions

As a contributor, I want to suggest new product terms, content edits, ingredient notes, or routine improvements so that GlowGuide can grow through public knowledge.

Acceptance Criteria:

- Contributors can submit a title, contribution type, category, proposed content, and optional source link.
- Submitted contributions are stored with a `pending` status.
- Pending contributions do not appear in public recommendations until approved.
- Maintainers can review, approve, reject, or request changes.

### US-007: Review Contributions

As a maintainer, I want to review community submissions before publishing them so that GlowGuide remains safe, accurate, and beginner-friendly.

Acceptance Criteria:

- Maintainers can view pending submissions.
- Maintainers can mark submissions as approved, rejected, or needs changes.
- Approved submissions can create or update product category records.
- Rejected submissions keep a review note explaining the reason.

## Functional Requirements

- FR-001: The system shall show a homepage with visual entry points for skincare, bodycare, hygiene, haircare, product library, and routine builder.
- FR-002: The system shall display educational content for skincare, bodycare, hygiene, and haircare.
- FR-003: The system shall provide a searchable and filterable product library.
- FR-004: The system shall allow users to select skin type.
- FR-005: The system shall allow users to select personal care concern.
- FR-006: The system shall allow users to select budget level: low, medium, or flexible.
- FR-007: The system shall generate a recommended routine from backend data.
- FR-008: The system shall show product category explanations and sample product suggestions.
- FR-009: The system shall include educational disclaimers where recommendations may be health-related.
- FR-010: The system shall work on mobile and desktop screens.
- FR-011: The system shall allow public users to submit content contributions.
- FR-012: The system shall store each contribution with a review status.
- FR-013: The system shall prevent unapproved contributions from appearing in recommendation results.
- FR-014: The system shall provide maintainers with a review workflow for approving or rejecting contributions.

## Data Requirements

The backend database must store:

- Product categories
- Skin types
- Care concerns
- Routine steps
- Recommendations
- Ingredient notes
- Caution notes
- Contributor submissions
- Review statuses and reviewer notes

## Success Metrics

- A first-time user can find a recommended routine in under two minutes.
- Product terms are understandable without external research.
- The demo includes at least 20 product category entries.
- The demo includes at least 5 skin types and 8 common concerns.
- The demo includes a contribution submission flow or documented API design for contributions.
- The website is visually clear and usable on mobile.

## Risks

- Personal care recommendations may be misunderstood as medical advice.
- Too much content may make the project difficult to finish during the hackathon.
- Backend setup may consume time if the scope is too large.
- Public submissions may include inaccurate, unsafe, promotional, or duplicate content.

## Mitigations

- Add clear educational disclaimers.
- Store only generic product category data at first.
- Use a simple Express API and MongoDB Atlas database.
- Add contribution review statuses and do not publish pending submissions.
- Prioritize the routine builder, product library, and category pages.
