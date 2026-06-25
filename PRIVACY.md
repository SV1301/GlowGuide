# Privacy Policy — GlowGuide

**Effective date:** June 2026  
**Project:** GlowGuide Personal Care Education Platform  
**Contact:** Open a GitHub issue at https://github.com/SV1301/GlowGuide/issues

---

## 1. Overview

GlowGuide is an open-source, educational personal care platform. We are committed to being transparent about how we handle any data that passes through the application. This policy applies to the live deployment at [glowguide-personalcare.streamlit.app](https://glowguide-personalcare.streamlit.app/) and any self-hosted instances.

---

## 2. What Data We Collect

### 2.1 Data You Provide (Community Contributions)

When you use the **Contribute** page, you may optionally provide:

| Data | Required? | Purpose |
|---|---|---|
| Contribution title | Yes | Identifies your submission for review |
| Name or alias | No (defaults to "Community Contributor") | Attribution; you may use a pseudonym |
| Proposed content | Yes | The knowledge you are sharing |
| Source URL | No | Supports your suggestion with a reference |
| Care category + contribution type | Yes | Classifies the submission |

> **No email address, phone number, government ID, or payment information is ever collected.**

### 2.2 Data We Do NOT Collect

- We do **not** require account registration or login.
- We do **not** track individual user sessions or browsing behaviour beyond what Streamlit Community Cloud provides at the infrastructure level.
- We do **not** use cookies for tracking.
- We do **not** embed third-party analytics scripts.
- We do **not** collect or store IP addresses in the application database.

---

## 3. How Data Is Stored

- Contributions are stored in a **SQLite database** (`db/glowguide.db`) on the Streamlit Community Cloud infrastructure.
- The database is not publicly accessible.
- All contributions remain in a `pending` state until reviewed by a maintainer.
- No contribution data is shared with third parties.

---

## 4. Data Retention

| Data type | Retention |
|---|---|
| Approved contributions | Kept indefinitely as part of the product knowledge base |
| Rejected contributions | Kept for moderation audit trail; not shown publicly |
| Pending contributions | Kept until reviewed |
| Reviewer notes | Kept alongside the contribution record |

We do not have an automated deletion schedule for the MVP. If you wish to have a contribution removed, open a GitHub issue and a maintainer will process the request within 14 days.

---

## 5. Your Rights

You have the right to:

- **Access** — Request a copy of any contribution you submitted (identify it by title and approximate date).
- **Correction** — Request correction of inaccurate content you submitted.
- **Deletion** — Request removal of a contribution you submitted.
- **Pseudonymity** — Contribute under an alias; your real name is never required.

To exercise any of these rights, open a GitHub issue at https://github.com/SV1301/GlowGuide/issues with the subject line `[Privacy Request]`.

---

## 6. Third-Party Services

The live deployment uses the following third-party services:

| Service | Purpose | Privacy Policy |
|---|---|---|
| Streamlit Community Cloud | App hosting | https://streamlit.io/privacy-policy |
| Google Fonts (CDN) | Typography (Inter, Playfair Display) | https://policies.google.com/privacy |
| GitHub | Source code hosting, issue tracking | https://docs.github.com/en/site-policy/privacy-policies |
| GitLab | Secondary repository mirror, CI/CD | https://about.gitlab.com/privacy/ |

GlowGuide does not control these services. Refer to their respective privacy policies for details.

---

## 7. Children's Privacy

GlowGuide is not directed at children under the age of 13. We do not knowingly collect personal information from children. If you believe a child has submitted a contribution with personally identifiable information, please contact us immediately via a GitHub issue.

---

## 8. Security

- The application does not store passwords or authentication tokens for regular users.
- The maintainer review passcode used in the MVP is for demonstration only and is not a secure credential system. See `SECURITY.md` for our full security policy.
- Secrets and API keys are stored in environment variables and never committed to the repository (see `.env.example`).

---

## 9. Changes to This Policy

We may update this privacy policy as the application evolves. Material changes will be noted in `CHANGELOG.md`. Continued use of GlowGuide after changes constitutes acceptance of the updated policy.

---

## 10. Contact

If you have questions about this privacy policy:

- Open a GitHub issue: https://github.com/SV1301/GlowGuide/issues
- Tag the issue with the `privacy` label.

This project is open source. The full source code, including how data is handled, is available at https://github.com/SV1301/GlowGuide.
