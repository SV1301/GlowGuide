# Data Model: GlowGuide Personal Care Platform

## ProductCategory

Represents a generic product term such as cleanser, moisturizer, sunscreen, body lotion, deodorant, or exfoliant.

Fields:

- `name`: Product category name.
- `slug`: URL-friendly identifier.
- `careCategory`: skincare, bodycare, hygiene, or haircare.
- `routineStep`: cleanser, treatment, moisturizer, protection, exfoliation, hygiene, or other.
- `description`: Simple explanation of the product.
- `whenToUse`: Morning, evening, weekly, or as needed.
- `bestForSkinTypes`: List of suitable skin types.
- `avoidForSkinTypes`: List of skin types that should be cautious.
- `relatedConcerns`: List of concerns this product may support.
- `lookForIngredients`: Ingredients or qualities to look for.
- `avoidIngredients`: Ingredients or qualities to avoid.
- `budgetLevel`: low, medium, or flexible.
- `cautionNote`: Safety or usage note.

## SkinType

Represents a skin type used for recommendations.

Fields:

- `name`: Oily, dry, combination, normal, or sensitive.
- `slug`: URL-friendly identifier.
- `description`: Beginner-friendly explanation.
- `commonSigns`: Signs users can identify.
- `recommendedApproach`: General routine approach.

## Concern

Represents a user concern such as acne, dryness, pigmentation, odor, or ingrown hair.

Fields:

- `name`: Concern name.
- `slug`: URL-friendly identifier.
- `careCategory`: skincare, bodycare, hygiene, or haircare.
- `description`: Explanation of the concern.
- `recommendedSteps`: Suggested care steps.
- `cautionNote`: When to seek professional advice.

## RoutineTemplate

Represents a reusable routine structure.

Fields:

- `title`: Routine name.
- `careCategory`: skincare, bodycare, hygiene, or haircare.
- `skinTypes`: Matching skin types.
- `concerns`: Matching concerns.
- `morningSteps`: Ordered list of morning steps.
- `eveningSteps`: Ordered list of evening steps.
- `weeklySteps`: Ordered list of weekly steps.
- `disclaimer`: Educational disclaimer.

## RoutineStep

Represents one step inside a routine.

Fields:

- `order`: Step order.
- `stepName`: Name of the step.
- `productCategorySlug`: Linked product category.
- `instruction`: What the user should do.
- `reason`: Why this step is included.
- `frequency`: Daily, weekly, or as needed.

## RecommendationRule

Represents matching logic for recommendation results.

Fields:

- `careCategory`: skincare, bodycare, hygiene, or haircare.
- `skinType`: Matching skin type.
- `concern`: Matching concern.
- `budgetLevel`: low, medium, or flexible.
- `recommendedProductSlugs`: Product categories to recommend.
- `routineTemplateId`: Linked routine template.
- `priority`: Rule priority if multiple rules match.
- `explanation`: Reason for the recommendation.

## Contribution

Represents a public suggestion submitted by a community contributor.

Fields:

- `title`: Short title for the contribution.
- `contributorName`: Public name or alias.
- `contributorContact`: Optional contact field if follow-up is needed.
- `type`: product-term, routine-step, ingredient-note, caution-note, correction, or other.
- `careCategory`: skincare, bodycare, hygiene, or haircare.
- `targetSlug`: Existing record slug if the contribution updates existing content.
- `proposedContent`: Main submitted content.
- `sourceUrl`: Optional supporting source link.
- `status`: pending, approved, rejected, or needs-changes.
- `reviewerNote`: Maintainer review note.
- `createdAt`: Submission timestamp.
- `reviewedAt`: Review timestamp.

## ContentReview

Represents a review action taken on a contribution.

Fields:

- `contributionId`: Linked contribution.
- `reviewerName`: Maintainer who reviewed the contribution.
- `decision`: approved, rejected, or needs-changes.
- `note`: Explanation of the decision.
- `createdAt`: Review timestamp.

## Example ProductCategory Document

```json
{
  "name": "Gel Cleanser",
  "slug": "gel-cleanser",
  "careCategory": "skincare",
  "routineStep": "cleanser",
  "description": "A lightweight cleanser that removes oil, sweat, and dirt without feeling heavy.",
  "whenToUse": "Morning and evening",
  "bestForSkinTypes": ["oily", "combination"],
  "avoidForSkinTypes": ["very-dry"],
  "relatedConcerns": ["oiliness", "acne"],
  "lookForIngredients": ["salicylic acid", "green tea", "niacinamide"],
  "avoidIngredients": ["harsh fragrance", "strong alcohol"],
  "budgetLevel": "low",
  "cautionNote": "If the cleanser causes burning or severe dryness, stop using it and choose a gentler option."
}
```

## Example Contribution Document

```json
{
  "title": "Add explanation for mineral sunscreen",
  "contributorName": "Community Contributor",
  "type": "product-term",
  "careCategory": "skincare",
  "targetSlug": "sunscreen",
  "proposedContent": "Mineral sunscreen uses ingredients such as zinc oxide or titanium dioxide and is often preferred by people with sensitive skin.",
  "sourceUrl": "https://example.com/source",
  "status": "pending",
  "reviewerNote": "",
  "createdAt": "2026-06-09T16:40:00.000Z",
  "reviewedAt": null
}
```
