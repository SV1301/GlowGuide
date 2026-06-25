# Geographical Expansion Plan — GlowGuide

## Overview

GlowGuide already supports Hindi and Telugu out of the box, making it naturally positioned for regional expansion across India. This document outlines how we will grow user and contributor bases in specific geographies.

---

## India — Regional Rollout

### South India — Andhra Pradesh & Telangana

**Language:** Telugu (తెలుగు) — already supported.

| Action | Channel |
|---|---|
| Promote Telugu UI via Twitter/X in Telugu | @GlowGuide (to be created) |
| Partner with Telugu-language personal care content creators | Instagram / YouTube |
| Share in student communities at regional universities (e.g., OU, JNTU, GITAM) | WhatsApp / Telegram |
| Submit to TSIC and AP tech community newsletters | Email outreach |

### North India — Delhi, UP, Rajasthan, MP

**Language:** Hindi (हिन्दी) — already supported.

| Action | Channel |
|---|---|
| Promote Hindi UI on Hindi Twitter/X communities | #HindiTwitter |
| Post in Hindi-language personal care groups on Facebook | Facebook Groups |
| Collaborate with Hindi YouTube personal care channels (2–3 mid-tier creators) | YouTube / Instagram Collab |
| Share in college networks in Delhi, Lucknow, Jaipur | WhatsApp university groups |

### West India — Maharashtra, Gujarat

**Language:** English + future Marathi / Gujarati support planned.

| Action | Channel |
|---|---|
| Post in Mumbai and Pune tech meetup communities | LinkedIn, Meetup.com |
| Share via GirlScript Summer of Code and similar programs | GirlScript Discord |
| Promote at college fests in Pune/Mumbai | Offline events (remote-first) |

### South India — Karnataka & Tamil Nadu

**Language:** English currently; Tamil and Kannada planned for Phase 3.

| Action | Channel |
|---|---|
| Add Tamil (`ta`) and Kannada (`kn`) locale files | `locales/ta.json`, `locales/kn.json` |
| Partner with Tamil and Kannada beauty/wellness communities | YouTube, Instagram |
| Engage with FOSS communities in Bangalore (FSMK, IFFOpenHack) | In-person and Discord |

---

## Global — Open-Source & Diaspora

### Indian Diaspora (UK, US, UAE, Singapore)

| Action | Channel |
|---|---|
| Post in Indian expat personal care communities | Reddit: r/ABCDesis, r/India |
| Share on platforms popular with global Indians | LinkedIn, Twitter/X, Facebook |
| Highlight the multilingual aspect (Hindi/Telugu) as a differentiator | Blog posts, dev.to |

### Global Open-Source Community

| Action | Channel |
|---|---|
| Submit GlowGuide to Streamlit's app showcase | https://streamlit.io/gallery |
| List on Awesome-Streamlit and similar curated lists | GitHub PR |
| Promote during Hacktoberfest (October) | GitHub good-first-issues |
| Submit to Open Source India, FOSS Asia newsletters | Email outreach |

---

## Language Expansion Roadmap

| Language | Locale Code | Status | Target Quarter |
|---|---|---|---|
| English | `en` | ✅ Live | — |
| Hindi | `hi` | ✅ Live | — |
| Telugu | `te` | ✅ Live | — |
| Tamil | `ta` | 🔲 Planned | Q3 2026 |
| Kannada | `kn` | 🔲 Planned | Q3 2026 |
| Marathi | `mr` | 🔲 Planned | Q4 2026 |
| Gujarati | `gu` | 🔲 Planned | Q4 2026 |
| Bengali | `bn` | 🔲 Planned | Q1 2027 |

Adding a new language requires only:
1. Creating `locales/<code>.json` mirroring `locales/en.json`
2. Adding one entry to `SUPPORTED_LANGUAGES` in `modules/i18n.py`

---

## Contributor Geography Goals

| Region | Goal (contributors) | Channel |
|---|---|---|
| Hyderabad / AP / Telangana | 10 | University tech fests, Telugu communities |
| Delhi NCR / North India | 10 | Hindi communities, college hackathons |
| Bangalore | 8 | FOSS communities, startup meetups |
| Maharashtra | 5 | GirlScript, college networks |
| Global / Diaspora | 7 | GitHub, Hacktoberfest, open-source forums |
