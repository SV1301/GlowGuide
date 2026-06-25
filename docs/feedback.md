# User Feedback Loop — GlowGuide

## Overview

GlowGuide collects user feedback directly through the **Contribute** section of the live web application. This is the primary channel for the public to submit knowledge improvements, report inaccuracies, and suggest new content.

---

## How Feedback Is Collected

### In-App Contribution Form

The **Contribute** page (accessible from the sidebar) allows any visitor to submit structured feedback without creating an account:

| Field | Description |
|---|---|
| **Contribution title** | Short summary of the suggestion |
| **Name or alias** | Contributor identity (anonymous alias is accepted) |
| **Contribution type** | `product-term`, `routine-step`, `ingredient-note`, `caution-note`, `correction`, `other` |
| **Care category** | Skincare, Bodycare, Haircare, or Hygiene |
| **Proposed content** | Full text of the suggestion |
| **Optional source URL** | Reference link to support the submission |

All submissions are stored in the SQLite database (`contributions` table) with `status = 'pending'`.

### GitHub / GitLab Issues

Contributors and users may also open issues on the repository:

- **Bug reports**: UI issues, incorrect product information, broken filters
- **Feature requests**: New care categories, language support, new concern types
- **Content corrections**: Inaccurate descriptions, outdated ingredient guidance

---

## Review Process

1. **Submission** — A visitor completes the in-app form. The contribution is saved as `pending`.
2. **Notification** — Maintainers periodically check the **Review Contributions** page (passcode-protected) to see pending submissions.
3. **Review** — Each submission is evaluated against the content guidelines in `CONTRIBUTING.md`:
   - Is it beginner-friendly?
   - Does it avoid medical claims?
   - Is there a source reference if needed?
4. **Decision** — The maintainer marks the submission as one of:
   - `approved` — Content is correct and safe; added to the product library or routine data.
   - `rejected` — Content is inaccurate, unsafe, or outside scope; a reviewer note explains why.
   - `needs-changes` — Submission is promising but requires edits; reviewer note guides the contributor.
5. **Integration** — Approved suggestions are manually integrated into `modules/database.py` seed data or product records, then committed to the repository.

---

## Prioritisation

Feedback is prioritised in this order:

1. **Safety corrections** — Inaccurate caution notes, unsafe ingredient advice (fix immediately).
2. **Content gaps** — Missing product categories or under-represented concerns (next release).
3. **Language / translation issues** — Missing or incorrect Hindi/Telugu strings (next release).
4. **Feature suggestions** — New sections, filters, UI improvements (backlog / roadmap).
5. **Growth suggestions** — New care categories (e.g., mental wellness) — evaluated quarterly.

---

## Feedback-to-Product Cycle

```
User submits via in-app form or GitHub issue
        │
        ▼
Stored as "pending" in SQLite DB
        │
        ▼
Maintainer reviews on Review Contributions page
        │
        ▼
Decision: approved / rejected / needs-changes
        │
        ▼
Approved content → committed to modules/database.py
        │
        ▼
Released in next version (tracked in CHANGELOG.md)
```

---

## Future Improvements

- Email or webhook notification when new contributions arrive.
- GitHub Issue auto-creation from in-app submissions.
- Public-facing moderation dashboard with approved content preview.
- Structured rating / upvoting for community prioritisation.
