# Growth Strategy — GlowGuide User Base

## Objective

Grow GlowGuide from a hackathon MVP into a widely-used personal care education platform, expanding the product scope to include **Mental Wellness**, enhancing the **Recommended Products** experience, and onboarding users across India and globally.

---

## Phase 1 — Foundation & Feature Expansion (Weeks 1–4)

### Week 1 — Mental Wellness Section (Product Expansion)

**Goal:** Add a fifth care pillar — Mental Wellness — alongside Skincare, Bodycare, Haircare, and Hygiene.

| Task | Owner | Notes |
|---|---|---|
| Add `Mental Wellness` as a care category in `database.py` | Dev | New seed products: aromatherapy, sleep hygiene, stress-relief rituals |
| Add mental wellness concerns to the routine builder | Dev | e.g., stress, sleep issues, burnout recovery |
| Update `locales/en.json`, `hi.json`, `te.json` with new strings | Dev | Translate new UI labels |
| Update homepage hero with the new Mental Wellness card | Dev | New icon: 🧘 |
| Add disclaimer: content is not a substitute for professional mental health care | Dev | Align with current educational-only approach |

### Week 2 — Recommended Products Section

**Goal:** Surface external product recommendations (affiliate or informational) alongside the educational routine builder output.

| Task | Owner | Notes |
|---|---|---|
| Add `recommended_brands` and `price_range` fields to the products schema | Dev | Keep brand suggestions generic and beginner-friendly |
| Build a "Recommended Products" card below the routine table | Dev | Link to search queries or general marketplaces (no direct affiliate links in MVP) |
| Add budget-tier visual guide (₹ / ₹₹ / ₹₹₹) | Dev | India-first pricing |
| User research: Collect 5–10 user sessions to validate the new feature | PM | Use the in-app contribution form for early feedback |

### Week 3 — SEO, Discoverability & Social Proof

**Goal:** Make GlowGuide findable to new users organically.

| Task | Owner | Notes |
|---|---|---|
| Add meta description, og:image, and Twitter card tags to the Streamlit app | Dev | Streamlit supports custom HTML in `config.toml` |
| Write 3 beginner blog posts (skincare, haircare, hygiene) | Content | Publish on GitHub Pages / Hashnode / Dev.to — link back to GlowGuide |
| Post on Reddit: r/IndianSkincareAddicts, r/HaircareScience, r/selfcare | Outreach | Educational framing, not self-promotion |
| Post on LinkedIn about the open-source launch | Outreach | Focus on social impact and multilingual aspect |
| Create a short demo video (screen recording) | Content | Share on Twitter/X and Instagram |

### Week 4 — Community Seeding & Feedback Loop Activation

**Goal:** Get the first 50 active users and 10 community contributions.

| Task | Owner | Notes |
|---|---|---|
| Share in college WhatsApp/Telegram groups (target: personal care beginners) | Outreach | Message includes direct app link |
| Post in open-source communities: FOSS India, GirlScript, OSSI | Outreach | Focus on the Hindi/Telugu multilingual angle |
| Review and respond to all in-app contributions received so far | Maintainers | Publish first batch of approved contributions |
| Email 5 personal care educators/influencers for feedback | Outreach | Keep it informal; request honest feedback |

---

## Phase 2 — Growth & Retention (Weeks 5–8)

### Week 5 — Hindi & Telugu Content Push

| Task | Notes |
|---|---|
| Promote the Hindi and Telugu UI on regional platforms | Twitter/X in Hindi; YouTube community posts in Telugu |
| Translate the 3 blog posts into Hindi | Publish on regional platforms |
| Collaborate with 1–2 vernacular personal care influencers | Co-create beginner guides in Hindi or Telugu |

### Week 6 — Kaggle / Dataset Publication

| Task | Notes |
|---|---|
| Package the GlowGuide product library as an open dataset | Publish on Kaggle under CC-BY-4.0 |
| Document the dataset schema, collection methodology, and license | `data/README.md` |
| Promote the dataset to AI/ML communities | LinkedIn, Kaggle forums, HuggingFace datasets |

### Week 7 — Contributor Onboarding Drive

| Task | Notes |
|---|---|
| Tag 10 beginner-friendly GitHub issues as `good first issue` | Content corrections, new product entries |
| Post about GlowGuide in HacktoberFest prep channels | Drive October contributor spike |
| Publish a 5-minute contributor onboarding video | Screen record the setup + first PR |

### Week 8 — Review & Iterate

| Task | Notes |
|---|---|
| Analyse: Which care categories get the most routine builder traffic? | Check via Streamlit analytics or in-app usage data |
| Publish CHANGELOG for v0.2.0 | Summarise all Phase 1 + 2 additions |
| Plan Phase 3 based on user feedback collected | Add AI chatbot, saved routines, or PWA based on demand |

---

## Geographical Expansion

See [`docs/geographical-expansion.md`](geographical-expansion.md) for the full regional plan.

**Summary targets:**

| Region | Strategy | Language |
|---|---|---|
| South India (AP, Telangana) | Telugu UI, regional social media | Telugu (తెలుగు) |
| North India (UP, Delhi, MP) | Hindi UI, WhatsApp group outreach | Hindi (हिन्दी) |
| Pan-India English users | GitHub, LinkedIn, Reddit, Streamlit showcase | English |
| Global / Diaspora | Open-source community channels | English |

---

## Success Metrics

| Metric | Target (End of Phase 2) |
|---|---|
| Monthly active users | 500+ |
| Community contributions submitted | 50+ |
| Approved contributions | 20+ |
| GitHub stars | 50+ |
| Supported languages | 5 (add Tamil and Kannada) |
| Care categories | 5 (add Mental Wellness) |
| Recommended products shown | 3–5 per routine result |
