# knowledge/seo — SEO Knowledge Module for VCNO

> **یک خط:** این ماژول، دانش ماندگار سئو برای ایجنت VCNO است — کنار ماژول امنیت (security knowledge) قرار می‌گیرد، **نه** به‌عنوان اسکیل یا دستور جدید.
> **One line:** A persistent SEO knowledge package consumed by the same AI agent that runs the VCNO lifecycle — separate from (and never merged into) the security knowledge module.

## What this package contains

| File | Purpose |
|---|---|
| [`SEO_KNOWLEDGE.md`](SEO_KNOWLEDGE.md) | The primary knowledge document — self-contained guidance: decision gate, technical/on-page/content/structured-data/performance checks, Persian & multilingual SEO, AI-search claims discipline, e-commerce conditionals, verification rules, lifecycle mapping, severity/evidence taxonomy, safety constraints, maintenance policy, sources. |
| [`README.md`](README.md) | This file — placement, integration, scope, assumptions, maintenance. |

**Deliberately omitted:** `references/` and `tests/` directories. The main document is designed to be consumed alone (progressive disclosure was considered; a single file won because the target format is a *knowledge file beside the security module*, not a skill pack). Validation reuses the repository's existing checker instead of a new framework.

## Placement & integration note (the one integration detail to confirm)

The task specification says this module belongs **beside VCNO's existing security knowledge file**. As of this session, **that security file does not exist in the repository** (searched: working tree, git history, all branches — the promised `VCNO_SECURITY_ENGINEERING_SPEC.md` was never supplied).

Assumption (documented, smallest reversible approach):

```text
knowledge/                ← persistent agent-knowledge packages (new, created by this module)
├── seo/
│   ├── SEO_KNOWLEDGE.md
│   └── README.md
└── security/             ← when VCNO_SECURITY_ENGINEERING_SPEC.md (or its final
                             knowledge form) lands, place it here as the sibling
```

- **If the security knowledge lands elsewhere** (e.g., repo root as `VCNO_SECURITY_ENGINEERING_SPEC.md`), move this package beside it with a plain `git mv knowledge/seo <location>/seo` — no content changes needed; only this README's paths would be updated.
- Naming: `SEO_KNOWLEDGE.md` is SCREAMING_SNAKE to match the intended `VCNO_SECURITY_ENGINEERING_SPEC.md` naming, not the kebab-case used by `docs/` and `skills/` (both styles already exist in the repo; knowledge files follow the spec-style name).

## How the agent should consume it

- **Entry:** when a VCNO project reaches `/init` or `/check`, the agent reads `knowledge/seo/SEO_KNOWLEDGE.md` **if the project has (or may have) a public web surface**. §0 + §1 (Decision Gate) decide applicability in seconds; `NOT APPLICABLE` projects record one line and stop.
- **Flow-through:** applicable requirements move into `/PRD` acceptance criteria; implementation happens inside the normal `/Build` step; findings go through `/Feedback` with evidence labels + severity; configuration/limitations are recorded in `/Doc`. **No new commands, skills, hooks, or workflows are introduced or modified.**
- **Optional pointer (requires owner authorization — not done here):** the maintainer may later add a one-line pointer in `AGENTS.md` (e.g., "دانش دائمی: `knowledge/`") so agents discover the package automatically. This session intentionally did **not** edit `AGENTS.md`, `README.md`, `docs/`, `skills/`, CI, or any existing file — the deliverable is self-contained under `knowledge/seo/`.

## Scope & non-goals

- ✅ Knowledge only: instructions, checklists, decision rules, evidence/severity taxonomy.
- ❌ Not a Skill (no `SKILL.md`), no slash command, no plugin/MCP/agent framework, no dependencies, no paid services, no credentials.
- ❌ No merge with security knowledge; no duplication or weakening of security requirements (the module explicitly forbids weakening security for SEO — §14 of the knowledge file).
- ❌ No production changes, no unauthorized external scans, no robots/canonical/redirect changes without owner approval.

## Maintenance

- **Version:** `1.0.0` (in `SEO_KNOWLEDGE.md` header). Knowledge-base semver: MAJOR = guidance reversed, MINOR = new coverage, PATCH = corrections/freshness.
- **Review cadence:** every 6 months, and immediately on Google Search Central announcements (ranking/spam/structured-data/CWV changes) or before relying on any rich-result eligibility claim.
- **Review procedure:** re-fetch the official sources listed in `SEO_KNOWLEDGE.md` §17 → update claims + `Last reviewed` date + version → append a line to the changelog below → run `python scripts/validate.py`.
- **Conflict rule:** official search-engine docs > vendor docs > third-party repos; when sources disagree, keep "verify current official guidance" rather than picking a side.
- **Changelog:**
  - **1.0.0 (2026-10-16)** — initial module; official sources fetched: Search Essentials, structured data intro, generative-AI guide, web.dev Vitals; 4 third-party SEO repos reviewed (MIT) for patterns only.

## Verification performed for this package (2026-10-16)

| Check | Result |
|---|---|
| `python scripts/validate.py` (repo CI check: frontmatter + relative links) | run after creating this package — see final report for observed output |
| No `SKILL.md` / manifest / command added | confirmed (package contains exactly 2 markdown files) |
| No existing repo file modified | confirmed (`git status` shows only new `knowledge/` files) |
| Secrets scan of package content | no credentials/keys present |
| Claims traceable to fetched sources | §17 table lists fetched vs linked-only vs not-run |
| Live-site tools (Lighthouse, Rich Results Test, GSC, crawls) | **not run** — no target site in scope; per-project step |
