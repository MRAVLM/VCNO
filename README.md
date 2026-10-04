# VCNO

**VCNO (Vibe Coding NO)** is a structured, staged workflow for AI-assisted software development. It turns a chat with a coding agent into a controlled engineering process — inspect first, validate, plan, build, iterate, and document — so that AI-assisted development is understandable, reproducible, and safe to maintain.

**Version:** v1.0
**Repository:** https://github.com/MRAVLM/VCNO
**فارسی:** [README.fa.md](README.fa.md)

---

## What is VCNO?

VCNO is a **collection of prompt-based skills** that define *how* an AI coding agent should behave at each stage of a project. Instead of asking an AI to "build this project" in one shot, VCNO breaks the work into six explicit stages:

```text
/init → /check → /PRD → /Build → /Feedback ↺ → /Doc
```

Each stage has one responsibility and hard boundaries about what it may and may not do. The result is a workflow where the developer stays in control, context is preserved, and work is verified instead of assumed.

## Why VCNO?

Most AI-assisted development today is unstructured: the developer pastes a big prompt, the agent writes a lot of code, and nobody is sure what actually works or why decisions were made. VCNO addresses this by enforcing:

- **Understand before changing.**
- **Inspect the existing project before modifying it.**
- **Preserve existing context, files, and work.**
- **Do not duplicate files, features, dependencies, or architecture.**
- **Do not guess unknown requirements — ask.**
- **Separate understanding, validation, planning, implementation, iteration, and documentation.**
- **Verify actual results instead of assuming success.**
- **Keep documentation aligned with the real state of the project.**
- **Use Git responsibly with meaningful checkpoints.**
- **Prevent uncontrolled scope expansion.**
- **Keep humans involved in important decisions.**
- **Treat AI as an engineering assistant — not an uncontrolled code generator.**

## Workflow

```text
/init       → Understand the project and its context
   ↓
/check      → Validate requirements, detect ambiguity and risks
   ↓
/PRD        → Turn validated understanding into an implementation-ready plan
   ↓
/Build      → Implement the approved plan and verify the result
   ↓
/Feedback   → Handle controlled iteration, bugs, and user feedback   ↺
   ↓
/Doc        → Document the real, final state of the project
```

## How It Works

VCNO is not an executable package. It is used **inside a compatible AI coding agent** as a set of skills that the agent invokes on demand. You point your agent at a project, invoke `/init`, and continue through the stages as the project progresses. Each stage reads the output of the previous one, so context is not lost between conversations.

> This repository is agent-agnostic: every tool reads the same source of truth through its native entry file (see [AI tool entry points](#ai-tool-entry-points)).

## Skills

All skills live in [`skills/`](skills/README.md), one folder + one `SKILL.md` each.

| Skill | Stage | What it does | Must not |
|---|---|---|---|
| [`/init`](skills/init/SKILL.md) | Understand | Inspects the repository, detects stack, assets, docs, Git state; writes the central project context | Write code, install, refactor, delete |
| [`/check`](skills/check/SKILL.md) | Validate | Validates idea, requirements, MVP scope, feasibility, risks, contradictions, unknowns | Implement, refactor, design full architecture |
| [`/PRD`](skills/prd/SKILL.md) | Plan | Produces the product/technical blueprint: requirements, flows, architecture, data, API, auth, testing, plan | Implement, install, over-engineer |
| [`/Build`](skills/build/SKILL.md) | Implement + Verify | Implements the approved PRD incrementally, tests, verifies, checkpoints in Git | Invent requirements, rewrite working code, claim unverified success |
| [`/Feedback`](skills/feedback/SKILL.md) | Iterate ↺ | Turns feedback (bugs, UX, features, screenshots, voice) into validated improvements with regression protection | Expand scope silently, replace planning, loop indefinitely |
| [`/Doc`](skills/doc/SKILL.md) | Finalize | Reconciles documentation with the real implementation; evaluates handoff/release readiness | Implement missing features, hide gaps, claim unverified status |

**Why each exists (one line):** `/init` so the agent understands before changing · `/check` so nothing is planned it does not understand · `/PRD` so `/Build` starts with clarity instead of guesswork · `/Build` to convert an approved plan into working software safely · `/Feedback` to keep improvement controlled instead of chaotic · `/Doc` so another developer can understand, run, and maintain the project.

## Who Is It For?

- AI-assisted developers and Vibe Coders
- Backend, frontend, and full-stack developers
- AI / ML engineers
- Students learning structured software development
- Startup builders, indie hackers, and technical founders
- Teams using coding agents on long-running repositories

**Probably not needed if** you are writing small, self-contained scripts where a single prompt is enough.

## Use Cases

- Starting a new application from an idea
- Working on an existing or legacy codebase
- Adding features or fixing bugs with AI assistance
- Iterating based on real user feedback
- Building an MVP under time pressure
- Keeping long-running repositories understandable with coding agents

## What VCNO Is Not

- Not a programming language
- Not a framework (not Django, FastAPI, Rails, etc.)
- Not an AI model
- Not a replacement for the developer
- Not a guarantee of bug-free software
- Not a way to skip testing or verification
- Not a way to automatically discover unknown requirements

## Philosophy

> Understand before changing. Validate before planning. Plan before building. Verify before claiming. Document reality, not intention.

VCNO exists because unstructured AI-assisted development tends to lose context, duplicate work, expand scope, and produce code nobody can maintain. VCNO treats the AI as an engineering assistant inside a controlled process.

---

## Start Here (this repository)

| I want to… | Go to |
|---|---|
| Understand the whole repository structure | [`AGENTS.md`](AGENTS.md) |
| Give the agent a repeatable job | [`skills/`](skills/README.md) |
| Run the first stage | `skills/init/SKILL.md` — say **`/init`** to your agent |
| Read the full project documentation | [`docs/`](docs/README.md) |
| See what VCNO is officially | [`docs/ABOUT.md`](docs/ABOUT.md) |
| Write code | [`docs/conventions.md`](docs/conventions.md) |

### AI tool entry points

Every major AI coding tool reads this repo through its native file — all point to the same source of truth (`AGENTS.md` + `skills/`):

| Tool | Reads | Points to |
|---|---|---|
| Codex, Cursor, Zed, Amp, … | `AGENTS.md` | ← the source |
| Claude Code | `CLAUDE.md` + `.claude/skills/*/SKILL.md` | `AGENTS.md` + `skills/` |
| GitHub Copilot | `.github/copilot-instructions.md` | `AGENTS.md` |
| Gemini CLI | `GEMINI.md` | `AGENTS.md` |
| Windsurf | `.windsurfrules` | `AGENTS.md` |

### Repository layout

```text
.
├── AGENTS.md      ← agent entry point (single source for tool shims)
├── CLAUDE.md      ← Claude Code shim
├── README.md      ← this file (English)
├── README.fa.md   ← Persian
├── .claude/skills/   ← Claude Code skill shims
├── .github/copilot-instructions.md
├── GEMINI.md / .windsurfrules
├── skills/        ← the six VCNO skills (source of truth) + _template/
├── backend/       ← server & API
├── frontend/      ← user interface
└── docs/          ← project documentation
```

## Learning

> ⏳ **The tutorial section is not written yet** — it will land here once the docs and skills are finalized.

Planned contents:

1. What vibe coding is and how to get results without deep coding knowledge
2. How to start from `AGENTS.md`
3. How to create and run a skill (step by step, with a real example)
4. How to read and maintain the project docs
5. A small practical project: from zero to done using the skills

---

## Version

This documentation describes **VCNO v1.0**. Future releases may introduce new skills, workflow improvements, or documentation changes. Follow the repository for the latest version.

## Repository

**https://github.com/MRAVLM/VCNO**

## Contributing

Contributions, issues, and suggestions are welcome through the repository. Please open an issue before proposing large changes to the workflow.

## License

**MIT** — see the [`LICENSE`](LICENSE) file for details.

## Author

- **Created by:** MRAVLM — GitHub owner `MRAVLM` verified; full name *Amirali Marjani* `NEEDS CONFIRMATION`.
- **Built with:** AI coding agent assistance. `NEEDS CONFIRMATION` — the specific agent(s) are not stated in the skill files.
