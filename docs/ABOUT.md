# About VCNO

> **برای چه کسی؟** هرکسی که می‌خواهد یک خط‌بندی رسمی از VCNO ببیند — هویت، فلسفه، گردش‌کار و وضعیت واقعی پروژه.
> **منبع:** از `about.txt` (official public documentation v1.0) استخراج و با وضعیت واقعی مخزن به‌روزرسانی شده.

## Project Identity

- **Name:** VCNO (Vibe Coding NO)
- **Type:** Prompt-based skill system for AI coding agents
- **Stage count:** 6 (`/init`, `/check`, `/PRD`, `/Build`, `/Feedback`, `/Doc`)
- **Version:** v1.0
- **Repository:** https://github.com/MRAVLM/VCNO

## Purpose

VCNO gives AI-assisted software development a controlled, stage-based structure. Each stage has a single responsibility and explicit boundaries. Context is preserved between stages so the agent never plans or builds on top of misunderstanding.

## Philosophy

- Understand before changing.
- Inspect the existing project before modifying it.
- Preserve existing context, files, and work.
- Do not duplicate files, features, dependencies, or architecture.
- Do not guess unknown requirements — ask.
- Separate understanding, validation, planning, implementation, iteration, and documentation.
- Verify actual results instead of assuming success.
- Keep documentation aligned with the real state of the project.
- Use Git responsibly with meaningful checkpoints.
- Prevent uncontrolled scope expansion.
- Keep humans involved in important decisions.
- Treat AI as an engineering assistant — not an uncontrolled code generator.

## Workflow

```text
/init → /check → /PRD → /Build → /Feedback ↺ → /Doc
```

| Stage | Responsibility | Must not |
|---|---|---|
| `/init` | Understand the project | Write code, install, refactor, delete |
| `/check` | Validate requirements and risks | Implement, design full architecture |
| `/PRD` | Produce the implementation blueprint | Implement, install, over-engineer |
| `/Build` | Implement and verify the approved plan | Invent requirements, rewrite working code |
| `/Feedback` | Controlled iteration and bug fixing | Expand scope, replace planning, loop indefinitely |
| `/Doc` | Reconcile docs with reality; evaluate release | Implement, hide gaps, claim unverified status |

## Target Users

AI-assisted developers, Vibe Coders, backend / frontend / full-stack developers, AI/ML engineers, students, startup builders, indie hackers, technical founders, teams using coding agents on long-running repositories.

## Design Principles

1. **One responsibility per stage.** No stage absorbs another's job.
2. **Explicit boundaries.** Every skill states what it must *not* do.
3. **Context continuity.** Each stage consumes prior outputs.
4. **Evidence over assumption.** Verified results only.
5. **Reality-based documentation.** Docs reflect the implementation, not the plan.
6. **Human-in-the-loop.** Important decisions require user confirmation.
7. **Proportional effort.** Small projects get small docs; complex projects get more.

## Project Status

**Version 1 / Public project.** The repository (`MRAVLM/VCNO`) is public and **published** with v1.0 content (initial commit `ef79773`, 2026-10-04). Not claimed as production-ready. Not claimed as stable beyond what the repository states.

## Author / Creator

- **Created by:** MRAVLM — GitHub owner `MRAVLM` **verified**; full name *Amirali Marjani* `NEEDS CONFIRMATION`.
- **Built with:** AI coding agent assistance `NEEDS CONFIRMATION` — the specific agent(s) are not stated in the skill files.

## Repository

https://github.com/MRAVLM/VCNO

## Future Direction

Future releases may add new skills, refine existing ones, improve documentation, or adjust the workflow. No specific future features are guaranteed. Check the repository for the latest version.

---

## Validation Status

| Item | Status |
|---|---|
| Repository inspected | `VERIFIED` — https://github.com/MRAVLM/VCNO reachable, public; v1.0 pushed as `ef79773` (2026-10-04) |
| Existing README found | `VERIFIED` — none upstream at inspection time; placeholder README in this copy merged, not overwritten |
| Existing docs found | `VERIFIED` — none upstream at inspection time; `docs/` extended in place |
| Author attribution | `PARTIAL` — owner `MRAVLM` verified; full name `NEEDS CONFIRMATION` |
| License | `VERIFIED` — MIT, [`LICENSE`](../LICENSE) file present |
| Version number in repo | `PARTIAL` — README declares v1.0; no git tag yet (`NEEDS CONFIRMATION`) |
| Exact invocation mechanism | `VERIFIED` for this repo — skills invoked by name (e.g. `/init`) per [`AGENTS.md`](../AGENTS.md); agent-specific shims provided |
| Contents of the six skills | `VERIFIED` — [`skills/`](../skills/README.md) |
| Workflow order | `VERIFIED` |
| Philosophy and principles | `VERIFIED` |
| Skill boundaries | `VERIFIED` |

## Next Recommended Step

1. ~~Confirm the items marked `NEEDS CONFIRMATION` by inspecting the repository~~ — done; remaining: full author name, version tag.
2. ~~Check whether a `README.md`, `README.fa.md`, `LICENSE`, or `docs/` already exist~~ — done: upstream was empty; local files merged in place.
3. ~~Verify the exact invocation mechanism~~ — done: skill name = command (`/init`, `/check`, `/PRD`, `/Build`, `/Feedback`, `/Doc`).
4. ~~Add the `LICENSE` file~~ — done: MIT [`LICENSE`](../LICENSE) added (2026-10-04). Remaining: confirm author full name.
5. ~~Publish this copy to `MRAVLM/VCNO` as official v1.0 documentation~~ — done: pushed as `ef79773`.

## پیوند به داکس‌های مرتبط

- [`README.md`](../README.md) / [`README.fa.md`](../README.fa.md) — معرفی رسمی
- [`AGENTS.md`](../AGENTS.md) — نقطه‌ی ورود ایجنت‌ها
- [`skills/README.md`](../skills/README.md) — فهرست مهارت‌ها
- [`README.md`](README.md) — فهرست کل داکس
