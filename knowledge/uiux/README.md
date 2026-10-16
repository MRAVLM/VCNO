# knowledge/uiux — UI/UX Knowledge Module for VCNO

> **یک خط:** این ماژول، دانش ماندگار UI/UX برای ایجنت VCNO است — کنار ماژول‌های امنیت و سئو قرار می‌گیرد، **نه** به‌عنوان اسکیل یا دستور جدید.
> **One line:** A persistent UI/UX knowledge package consumed by the same AI agent that runs the VCNO lifecycle — sibling of the security and SEO knowledge modules; never a Skill.

## What this package contains

| File | Purpose |
|---|---|
| [`UIUX_KNOWLEDGE.md`](UIUX_KNOWLEDGE.md) | The primary knowledge document: decision gate (U0–U3), inspection checklist, Nielsen heuristics, WCAG 2.2 AA everyday set, responsive layout, visual foundations, component states, forms UX, Persian/RTL, tokens (optional), motion/perceived performance, context patterns, lifecycle mapping, failure patterns, safety constraints, two-level verification checklists, versioning, dated sources. |
| [`README.md`](README.md) | This file — placement, integration, scope, assumptions, maintenance. |

## Placement & integration note

```text
knowledge/                ← persistent agent-knowledge packages
├── security/
│   ├── SECURITY_KNOWLEDGE.md
│   └── README.md
├── seo/
│   ├── SEO_KNOWLEDGE.md
│   └── README.md
└── uiux/                  ← this package
    ├── UIUX_KNOWLEDGE.md
    └── README.md
```

Sibling placement matches the documented assumption in `knowledge/seo/README.md` (security module was expected as `knowledge/security/` — now exists).

## How the agent should consume it

- **Entry:** at `/init` or `/check`, when a project has (or may have) a human-facing surface, read `UIUX_KNOWLEDGE.md` §0–§2; the decision gate picks tier U0–U3 in seconds. `U0` projects record one line and stop.
- **Flow-through:** applicable requirements become `/PRD` acceptance criteria (observable phrasing); implementation happens in normal `/Build`; findings use S1–S4 severity through `/Feedback`; honest limitations land in `/Doc`. **No new commands, skills, hooks, or workflows.**
- **Cross-module rule:** accessibility never weakens security (server-side authority stays); performance pointers to `../seo/SEO_KNOWLEDGE.md` §6 (CWV); security form/auth constraints from `../security/SECURITY_KNOWLEDGE.md` (§6.A/§6.C).

## Scope & non-goals

- ✅ Knowledge only: decision rules, checklists, evidence labels, severity taxonomy.
- ❌ Not a Skill (no `SKILL.md`), no slash command, no plugin, no dependencies.
- ❌ No forced design system, framework, or component library on any project (explicit constraint).
- ❌ No fabricated compliance claims — WCAG conformance/usability testing are human-gated (`Unknown` until real evidence).
- ❌ No modification of security or SEO modules.

## Maintenance

- **Version:** `1.0.0` (in `UIUX_KNOWLEDGE.md` header). Semver: MAJOR = reversed guidance, MINOR = new coverage, PATCH = corrections.
- **Review cadence:** every 12 months, or on WCAG Recommendation updates / material changes to cited sources.
- **Procedure:** re-fetch §18 sources → update labels + `Last reviewed` → changelog line → `python scripts/validate.py`.
- **Changelog:**
  - **1.0.0 (2026-10-16)** — initial module; fetched: WCAG 2.2, NN/g heuristics, W3C i18n RTL, web.dev responsive course (index), W3C Design Tokens CG.

## Verification performed for this package (2026-10-16)

| Check | Result |
|---|---|
| `python scripts/validate.py` | run after creating package — see final report |
| No `SKILL.md` / command added | confirmed (exactly 2 markdown files) |
| No existing repo file modified | confirmed (`git status` shows only new files under `knowledge/`) |
| Secrets scan | no credentials/keys present |
| Claims traceable | §18 lists fetched vs linked-only vs not-run |
| Live audits/Lighthouse/user tests | **not run** — no target project; per-project step |
