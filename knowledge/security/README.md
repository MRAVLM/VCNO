# knowledge/security — Security Knowledge Module for VCNO

> **یک خط:** این ماژول، مشخصات مهندسی امنیت VCNO (نسخه‌ی دانشی) برای همان ایجنتی است که چرخه‌ی VCNO را اجرا می‌کند — کنار ماژول‌های سئو و UI/UX؛ **نه** اسکیل جدید و **نه** مجوز اجرا.
> **One line:** The VCNO Security Engineering Specification stored as consumable knowledge for the same AI agent — sibling of SEO/UIUX knowledge; adding it changes nothing in the workflow.

## What this package contains

| File | Purpose |
|---|---|
| [`SECURITY_KNOWLEDGE.md`](SECURITY_KNOWLEDGE.md) | The full VCNO Security Engineering Specification v1.0-draft (2026-10-16): principles P1–P12, tiering (T1/2/3), STRIDE threat-model method + template, vulnerability taxonomy 6.A–6.K (auth, injection, business logic, secrets/crypto, data, uploads, misconfiguration, supply chain, logging, resource exhaustion, AI-agent risks), AI-assisted development policy (untrusted-content, agent permissions, anti-false-confidence), per-stage integration design (§8), 13-layer testing strategy, severity/remediation policy (SEC-NNN), CI/CD gates, reporting templates, phased implementation plan, acceptance criteria, test matrix, rollback rules, documentation requirements, references, implementing-agent checklist, explicit exclusions & open questions with defaults. |
| [`README.md`](README.md) | This file — status, provenance, integration, consumption, maintenance. |

## Status & provenance (honest ledger)

| Item | State |
|---|---|
| Source | User-supplied specification (chat-exported), restored into clean Markdown: heading markers, tables, and code fences repaired; chat-panel artifacts (`Sources`/`Reasoning`/timestamps) removed; body content otherwise verbatim. |
| Completeness | **§1–§20 complete** through “End of specification.” (An earlier truncated copy existed; the fixed full version is what is stored here.) |
| Authorization | **Knowledge only.** The specification itself states implementation is not authorized by its existence (§20.1 exclusions; phases gated on maintainer action). This package does **not** edit `skills/`, `AGENTS.md`, shims, scripts, or CI. |
| Implementation plan | Spec §13/§19 phases (0–6) remain **pending maintainer go-ahead** — stored as knowledge, not executed. |
| Sibling modules | `../seo/SEO_KNOWLEDGE.md` · `../uiux/UIUX_KNOWLEDGE.md` — never merge; never weaken one for another (spec P-rules + UIUX §15.1 + SEO §14 agree). |

## How the agent should consume it

- **Entry:** at `/init`/`/check`, if a project has auth, user data, uploads, payments, public API, or internet exposure → read spec §1 (summary), §4 (principles), §5 (tiering) and apply the decision gate. Tier T1 stays lightweight — proportionality is binding (P6).
- **During `/PRD`:** §5 threat-model method + §5.4 template; requirements in the SEC-REQ shape (§8.3.2); traceability (§8.3.4).
- **During `/Build`:** category playbooks 6.A–6.K before writing security-relevant code; §7 agent policy (untrusted content, no false confidence) is standing behavior on every task.
- **During `/Feedback`:** finding format §10.2 (SEC-NNN), severity §10.1 (never lower severity to pass a build).
- **During `/Doc`:** honest security documentation set (§8.6/§17); disclaimer from §4.3.
- **Implementation of the spec into VCNO itself** (editing skills/scripts/CI) happens **only** when the maintainer starts Phase 0 — until then the agent treats the file as reference knowledge.

## Scope & non-goals

- ✅ Knowledge: principles, taxonomy, methods, templates, policy, checklists.
- ❌ Not a Skill, no new slash commands, no plugin, no dependencies.
- ❌ No changes to existing architecture, workflows, scripts, or shims by virtue of this package.
- ❌ No offensive tooling; reproduction guidance is defensive/isolated only (spec §20.1).
- ❌ No guarantee of security — the spec's own standing disclaimer applies (§4.3).

## Maintenance

- **Version:** knowledge wrapper `1.0.0`; embedded spec `1.0-draft` (2026-10-16).
- **Review cadence:** before implementing any phase; and when OWASP/NIST/standards versions cited in §4.3/§18 change (re-verify URLs before citing — spec's own note).
- **Changelog:**
  - **1.0.0 (2026-10-16)** — initial storage of the complete specification (§1–§20) as `SECURITY_KNOWLEDGE.md`; formatting restoration documented above.

## Verification performed for this package (2026-10-16)

| Check | Result |
|---|---|
| Completeness | “End of specification.” present; §§1–20 headings restored and verified |
| Chat artifacts removed | `Sources`/`Reasoning`/timestamps confirmed absent |
| Code fences balanced | even count after restoration |
| Secrets scan | no credential-shaped strings (spec references patterns, not values) |
| `python scripts/validate.py` | run after creating package — see final report |
| No existing file modified | confirmed (`git status`: new files only under `knowledge/`) |
