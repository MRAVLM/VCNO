# UIUX_KNOWLEDGE.md — UI/UX Knowledge Module for VCNO

**Version:** 1.0.0 · **Date:** 2026-10-16 · **Status:** knowledge reference (consumable; not a Skill, not a workflow change)

> **What this is:** persistent UI/UX decision knowledge for the same AI agent that runs the VCNO lifecycle (`/init → /check → /PRD → /Build → /Feedback ↺ → /Doc`). It teaches sound interface decisions during planning, implementation, and review — visual quality, usability, accessibility, responsive layout, interactions, consistency, Persian/RTL, perceived performance, and context-specific design.
> **Sibling modules:** `knowledge/security/SECURITY_KNOWLEDGE.md` (security) · `knowledge/seo/SEO_KNOWLEDGE.md` (SEO). Never merge modules; never weaken one for another.

---

## §0 How to use this file

**Evidence labels** (same discipline as the SEO module):

| Label | Meaning |
|---|---|
| `Confirmed` | Traceable to a fetched authoritative source (§18). Date of verification noted. |
| `Inferred` | Widely accepted engineering/design practice, not fetched from a single normative source this session. |
| `Trend` | Subjective style or vendor preference — must never be imposed as a requirement. |
| `Unknown` | Cannot be verified from the agent's position; requires human/real-user input. |

**Severity for UX findings** (used in `/Feedback` and reviews): **S1 Blocker** (user cannot complete the task, or accessibility/legal-risk failure on a core flow) · **S2 Major** (significant friction, workaround required, or AA criterion failure on a secondary flow) · **S3 Minor** (polish, inconsistency, small cognitive-load cost) · **S4 Note** (taste/trend; record, do not force).

**Core honesty rule:** the agent may *evaluate against* documented criteria and *report* findings with evidence; it may **never claim** “WCAG compliant”, “accessible”, “usable”, or “tested with users” without real audit/test evidence. Unverified success claims are forbidden (VCNO ethos).

---

## §1 Decision gate — does this project need UI/UX work?

Answer at `/init` or `/check` from what the repository and concept actually show:

| Signal | Tier | What applies |
|---|---|---|
| CLI, scripts, libraries, no human-facing surface | **U0 — None** | Record one line; stop. Only keep code-quality hygiene (clear output, sensible defaults). |
| Internal/admin tool, few users, basic forms | **U1 — Essentials** | §4 accessibility floor + §7 states + §8 forms basics + §5 responsive floor. No design system. |
| Product web app, mobile web, public-facing | **U2 — Full** | All sections §3–§12. Accessibility target WCAG 2.2 **AA** (§4). |
| Regulated, large user base, brand-critical launch | **U3 — U2 + human process** | All sections **plus** mandatory human usability testing and professional accessibility audit before release — the agent states this requirement and stops; it cannot substitute for real users (`Unknown` by definition). |

**Non-goal (binding):** do **not** force a design system, component library, or specific framework on any project (constraint of this module). U1 projects stay CSS-minimal; U2/U3 adopt tokens (§10) only when the project already benefits from repeated values or theming.

---

## §2 Inspection before proposal (input to `/check`)

Read-only questions the agent answers from the repo/concept before proposing anything:

1. **Surface:** web app / mobile web / admin / marketing site / CLI-only? Existing UI framework (React/Vue/Svelte/plain) already in `package.json`?
2. **Existing design language:** any CSS framework, tokens, component folder, Figma exports, brand colors in repo? Reuse it; never restyle wholesale without a stated reason.
3. **Direction:** Persian, English, or bilingual? (Trigger: Persian strings, `lang=`/`dir=` attributes, fa content files.) If bilingual → §9 is mandatory reading.
4. **Users & devices:** target device mix known? Touch-only? Kiosk? (If unknown → `Unknown`, design for both pointer types.)
5. **Data density:** dashboards/tables/charts vs marketing/content pages → §12 patterns.
6. **Constraints already present:** auth flows, third-party widgets (payment, map), existing error pages.
7. **Perf budget:** any stated performance goals? (Cross-ref: `knowledge/seo/SEO_KNOWLEDGE.md` §6 Core Web Vitals for loading metrics; this module covers *perceived* performance §11.)

Record findings in the check log; skip any question the repo cannot answer (mark `Unknown`).

---

## §3 Core usability principles (`Confirmed` — NN/g heuristics)

Source: Jakob Nielsen's 10 Usability Heuristics (1994; derived from factor analysis of 249 usability problems [Nielsen 1994a/1994b]; NN/g states the ten themselves have remained unchanged; page last reviewed 2024-01-30 — fetched 2026-10-16, §18). They are **heuristics (rules of thumb)**, not testable standards — apply as review lenses, not pass/fail checkboxes.

| # | Heuristic | Agent application in `/Build` & review |
|---|---|---|
| 1 | Visibility of system status | Every action with consequence gets feedback (loading, success, failure) within ~100ms of user input (spinner/progress/disabled state). Never a dead click. |
| 2 | Match system ↔ real world | Use user vocabulary (domain terms), not internal model/field names. Natural order of steps. |
| 3 | User control and freedom | Undo/Cancel/Esc-able dialogs; destructive actions confirmed or undoable; no forced dead-ends. |
| 4 | Consistency and standards | Same thing = same label/component everywhere; follow platform conventions (Jakob's Law: users spend time in *other* products; expectations transfer). |
| 5 | Error prevention | Constraints, sensible defaults, confirmations for irreversible/high-cost actions (confirm with the *specific consequence*, not “Are you sure?”). |
| 6 | Recognition over recall | Show options, labels, help in context; don't force memory across screens. |
| 7 | Flexibility and efficiency | Shortcuts/accelerators for repeat actions (progressive disclosure); sensible defaults for novices. |
| 8 | Aesthetic and minimalist design | Remove content that doesn't serve the primary task; every element competes for attention. |
| 9 | Recognize/diagnose/recover from errors | Plain-language error messages: what happened + why + what to do next (§8.4). Never raw stack traces. |
| 10 | Help and documentation | Searchable, task-focused, in-context help — last resort after making the UI self-explanatory. |

**Conflict rule:** heuristics guide design; when they conflict with a **normative** requirement (WCAG §4, security §security module), the normative requirement wins and the trade-off is documented.

---

## §4 Accessibility baseline — WCAG 2.2 (`Confirmed` normative)

**Source:** W3C *Web Content Accessibility Guidelines (WCAG) 2.2*, W3C Recommendation **12 December 2024** (fetched 2026-10-16; §18). Four principles: **Perceivable, Operable, Understandable, Robust (POUR)**; testable Success Criteria at levels A / AA / AAA. Conforming to 2.2 implies 2.1/2.0 conformance. **4.1.1 Parsing was removed in 2.2.**

**Target for VCNO projects with a UI (U2+): WCAG 2.2 Level AA** (the common regulatory/procurement bar). U1: the A-level subset below on core flows.

### 4.1 Everyday AA set (check during `/Build` and `/Feedback`)

| SC | Level | Rule the agent implements/verifies in code |
|---|---|---|
| 1.1.1 | A | Every non-text content (images, icons, SVG) has a text alternative serving its purpose; decorative → empty alt / aria-hidden. |
| 1.3.1 | A | Structure by semantics (headings h1–h6 order, lists, tables with th, landmarks) — not by visual styling alone. |
| 1.3.2 | A | Reading/DOM order matches visual meaning order. |
| 1.4.1 | A | Color is never the *only* way to convey info (add icon/text/pattern). |
| 1.4.3 | AA | Text contrast ≥ **4.5:1** (large text ≥ 3:1). Verify computed colors, not designer intent. |
| 1.4.10 | AA | Reflow: usable at **320 CSS px** width (≈400% zoom) with no 2-D scrolling of content. |
| 1.4.11 | AA | UI components & meaningful graphics contrast ≥ **3:1** (borders, focus rings, icons-as-controls). |
| 1.4.13 | AA | Hover/focus-triggered popups dismissible, hoverable, persistent. |
| 2.1.1 | A | Full keyboard operability; no keyboard traps. |
| 2.4.3 | A | Logical focus order. |
| 2.4.7 | AA | Visible focus indicator on every interactive element (never `outline: none` without a replacement). |
| 2.4.11 | AA *(new in 2.2)* | Focused element not hidden behind sticky bars/overlays (minimum). |
| 2.5.7 | AA *(new in 2.2)* | Dragging movements have a non-drag alternative (buttons/steps). |
| 2.5.8 | AA *(new in 2.2)* | Pointer target minimum **24×24 CSS px** (with spacing exceptions); design for ≥44px on touch-primary UIs (AAA 2.5.5 direction). |
| 3.1.1 | A | `lang` on `<html>` correct for the page language. |
| 3.2.1 / 3.2.2 | A | No unexpected context change on focus/input (no auto-submit on every keystroke, no surprise popups). |
| 3.2.3 / 3.2.4 | A/AA | Consistent navigation & identification across pages. |
| 3.3.1 | A | Errors identified in text, associated to the field. |
| 3.3.2 | A | Labels/instructions for inputs (visible labels — placeholder is not a label). |
| 3.3.3 | AA | Error messages suggest a correction when known. |
| 3.3.4 | AA | For legal/financial/data submissions: reversible, checked, or confirmed before finalizing. |
| 3.3.7 | A *(new in 2.2)* | Redundant entry avoided in multi-step flows (pre-fill/offer prior answers unless essential). |
| 3.3.8 | AA *(new in 2.2)* | Accessible authentication: no cognitive function test (puzzle CAPTCHA, transcription) to log in unless essential — support password managers (`autocomplete` tokens, paste allowed). |
| 4.1.2 | A | Name, role, value exposed for custom widgets (use native elements first; ARIA only as specified). |
| 4.1.3 | AA | Status messages via `role="status"` / `aria-live` (not just visual change). |

**AAA not required** but note when cheap: 2.4.13 focus appearance, 1.4.6 enhanced contrast (7:1), 2.5.5 44px targets.

### 4.2 Accessibility method for the agent

- **Prefer native HTML** (button, a, input, label, table) over div-soup + ARIA. `Confirmed` principle across WAI authoring guidance.
- **Automated check** when tooling exists in the project (axe-class linter): catches ~30–40% of issues; findings are evidence, but “0 automated issues” ≠ accessible (cite layer honesty like security §9 spirit).
- **Keyboard pass** (agent can reason through tab order in code review) + **contrast computation** from actual color values.
- **What the agent cannot do:** claim formal conformance, run screen-reader usability with real AT users, or certify legal compliance → label `Unknown` / requires human audit (U3 gate).

---

## §5 Layout & responsive design (`Confirmed` practice — web.dev Learn Responsive Design course; §18)

1. **Mobile-first:** base styles for small screens; `min-width` media/feature queries add complexity upward. (Course: media queries article.)
2. **Reflow floor:** content must survive **320px** (WCAG 1.4.10) — design the narrow layout first.
3. **Breakpoints from content, not devices:** add a breakpoint where *the content breaks* (text lines too long, grid collapses badly) — no “iPhone X width” cargo-culting.
4. **Fluid where cheap:** `clamp()` for type/spacing, percentage/flex/grid layouts, `minmax()`; avoid fixed pixel widths on containers.
5. **Layout tools:** CSS Grid for page macro-layout; Flexbox for component micro-layout; both follow logical properties (§9) so RTL mirroring is automatic.
6. **Images:** responsive sizing (`width`/`height` or `aspect-ratio` to prevent layout shift — cross-ref SEO CWV CLS), `srcset`/`sizes`, modern formats when available; decorative images lazy (`loading="lazy"`), above-fold hero not lazy.
7. **Icons:** inline SVG (scalable, styleable, themeable); every icon-only control needs an accessible name (§4).
8. **Tables:** horizontally scrollable wrapper with visible affordance on small screens; never squash data tables into unreadable fragments.
9. **Navigation:** small screens → simple collapse pattern (disclosure button with `aria-expanded`); primary tasks must be ≤1 tap deep on mobile.
10. **Media features beyond width:** `prefers-color-scheme` (§6 dark mode), `prefers-reduced-motion` (§11), `hover`/`pointer` (enhance for fine pointers, don't *require* hover).
11. **Container queries** (`@container`): `Inferred` modern option when components live in varying-width parents; support is broad in evergreen browsers (2026) — safe for new U2 projects; fall back to media queries if project browser matrix is conservative/`Unknown`.

---

## §6 Visual foundations (token-scale guidance; `Inferred` practice + `Confirmed` where cited)

**Typography**

- One display + one text family max for U1; Persian pair per §9. Type scale ~1.2–1.25 modular (e.g., 12/14/16/20/24/32).
- Body ≥ **16px** (avoids mobile zoom-on-focus issues; `Inferred` widely-shared guidance), line-height 1.5–1.7 for Latin; **1.8–2.0 for Persian body** (`Inferred` — Persian diacritic-free text needs more leading).
- Measure (line length) ~45–75 characters for reading text.
- No justification-with-hyphenation traps for mixed EN/FA; avoid `text-align: justify` on short lines.

**Color**

- Define a small palette + **semantic tokens**: `bg`, `surface`, `text`, `text-muted`, `border`, `primary`, `danger`, `warning`, `success`, `focus-ring`. Components consume semantics, never raw hex.
- Check every text/bg pair against 1.4.3 and every control/border pair against 1.4.11 (compute, don't guess).
- **Dark mode:** `Inferred`-supported via `prefers-color-scheme: dark` + token swap; never a hard requirement. If implemented: verify contrast again in both modes; respect user preference; no flash of wrong theme (inline critical token swap or CSS `color-scheme`).
- Never encode state in color alone (1.4.1).

**Spacing & density**

- 4px/8px spacing scale; consistent gaps beat ad-hoc pixels.
- Touch-primary targets ≥44px comfortable (beyond the 24px AA floor).
- Density modes are a `Trend`/product choice — default readable, not cramped.

---

## §7 Components & interaction states

**Every interactive element implements the full state matrix** (checklist for `/Build`):

| State | Requirement |
|---|---|
| Default | Visible, labeled, contrast pass. |
| Hover | Optional enhancement only; nothing hover-only is *required* to complete a task (touch users). |
| **Focus** | Visible ring ≥ 3:1 contrast against adjacent colors, not clipped (2.4.7/2.4.11/1.4.11). |
| Active/pressed | Affordance feedback (≤100ms). |
| Disabled | Visually distinct + `disabled`/`aria-disabled`; explain *why* when non-obvious (tooltip/help). Never use disabled for “not yet validated” alone — prefer validation messaging (§8). |
| Loading | Buttons that trigger network/work show pending state and prevent double-submit; ≥500ms operations get visible progress (§1 visibility). |
| Error | Field- and form-level messaging (§8.4). |

**Patterns**

- Buttons vs links: navigation = `<a href>`; action = `<button>`. Never `<div onClick>`.
- Dialogs: focus moves in, trapped while open, `Esc` closes, focus returns to trigger; `aria-modal`/labelled.
- Toasts/snackbars for non-blocking confirmations only; critical errors stay inline until resolved.
- Destructive actions: explicit verb labels (“Delete project”), confirm with consequence; prefer undo window over confirm-fatigue (heuristic 3/5).
- Empty states: explain what goes here + primary next action (first-run UX is part of the product).
- Icons: decorative → `aria-hidden="true"`; meaningful → text alternative.

---

## §8 Forms & validation UX

1. **Labels:** visible `<label for>` on every input; placeholder ≠ label (disappears, fails contrast often).
2. **Required:** mark visually *and* programmatically (`required`/`aria-required`); don't rely on asterisk alone — explain in instructions.
3. **Help:** short hint under label (`aria-describedby`); format examples (“YYYY-MM-DD”, phone mask).
4. **Input types & tokens:** `type=email|tel|url|number|date`, `autocomplete` tokens (name, email, tel, one-time-code, cc-*) — helps browsers/password managers and feeds WCAG 1.3.5/3.3.8.
5. **Validation timing:** validate on blur/submit for most fields; avoid aggressive per-keystroke errors on incomplete fields (heuristic 5 + 3.2.2). Show errors **next to the field** + summary at top with links for long forms (3.3.1).
6. **Error message quality:** plain language, field-specific, constructive (3.3.3): “Enter a phone number like 0912…” not “Invalid input” or “Error 422”.
7. **Server vs client:** client validation = UX only; **security validation is server-side** (never weaken the security module for form convenience — server remains authority).
8. **Preserve work:** never wipe a form on one error; network failure must not lose input (autosave/draft `Inferred` for long forms).
9. **Multi-step:** show progress; allow back without data loss; 3.3.7 redundant-entry rule (§4).
10. **Submission:** disable-once/`aria-busy`, idempotent behavior server-side (security §6.C), success feedback inline + status message (4.1.3).

---

## §9 Persian & RTL interfaces (mandatory when §2 detects Persian/RTL)

**Normative base (`Confirmed` — W3C i18n, fetched 2026-10-16; §18):**

1. **`dir="rtl"` on `<html>`** for RTL documents — set the base direction in **markup, never in CSS** (direction is semantics; must work without CSS). Pair with correct `lang="fa"` (lang ≠ dir — declare both).
2. **Logical properties/values in CSS:** use `start`/`end`, not `left`/`right`: `margin-inline-*`, `padding-inline-*`, `border-inline-*`, `inline-size`, `text-align: start|end`, `float: inline-start|inline-end`, flex/grid `*-start/-end`. Then layout mirrors automatically when direction flips. (`Confirmed` list from W3C i18n article.)
3. **`dir="auto"`** on user-generated/inserted content and form fields whose direction is unknown at authoring time (chat messages, comments, search inputs) — browser detects from first strong character. `dirname` attribute submits the computed direction to the server for later display.
4. **Mixed content:** wrap unknown-direction inline runs in `<bdi>`; punctuation/number edge cases (§ article “inline bidi markup”). Latin fragments inside Persian text (product names, code) keep their internal LTR via the bidi algorithm — don't fight it with manual overrides unless necessary.
5. **Tables:** `dir="rtl"` document flips column order automatically; use `dir="ltr"` on genuinely-LTR data tables (code, numbers) inside RTL pages.
6. **Icons that imply direction must mirror:** back/forward arrows, progress chevrons, sidebar toggles — flip in RTL (use logical positioning or dual assets). Do **not** mirror universally: checkmarks, media play buttons, logos stay.
7. **Persian typography specifics** (`Inferred` practice):
   - **ZWNJ (U+200C)** in Persian compound words (می‌شود، بررسی) — ensure fonts render it; avoid CSS (`white-space`, `word-break`) that breaks ZWNJ words; normalize (NFC) user input storage.
   - Persian digits (۰–۹) vs Latin: pick one display convention per surface and stay consistent (heuristic 4); numeric inputs often stay Latin for machine parsing — localize display, not storage.
   - Times/dates: Jalali calendar display is a product decision (`Unknown` until user research) — never silently convert stored Gregorian data.
   - Letter-spacing: never track Persian text (breaks joining); no all-caps transforms (Persian has none; Latin caps inside FA sentences OK sparingly).
8. **Bilingual UI (FA+EN):** per-page `lang`/`dir`; language switcher preserving route/state; don't concatenate translated + untranslated strings in one sentence without markup; dates/numbers localized per active locale; **labels defined once in i18n dictionaries**, not scattered hardcoded — enables 3.2.4 consistency.
9. **Font stacks:** Persian: a readable Persian face first (e.g., project-chosen Persian font), then system fallbacks (Segoe UI, Tahoma, sans-serif). Latin UI: project font + system fallback. Self-hosting fonts when offline/perf matters (`Inferred`; vcnobook did exactly this). Verify glyph coverage for Persian letters ک/گ/ی/چ/ژ/پ and ZWNJ before shipping (agent can inspect font `cmap` if given the file — as done for `vcnobook/fonts`).
10. **Testing floor the agent can do:** render `dir=rtl` layout logic in code review (logical props used?), check mirrored icons, verify `lang`/`dir` pairs, contrast in both directions; real bilingual usability testing = human gate (`Unknown`).

---

## §10 Design systems & tokens (optional, proportionate)

- **Do not force a system.** U1 stays hand-rolled CSS with semantic variables. U2+ introduces tokens when ≥3 components repeat the same raw values or theming exists.
- **Tokens = single source of truth for colors, type, spacing, radii, shadows, motion.** Semantic layer (`text-muted`, `danger`) above raw palette.
- **Standard (`Confirmed` existence, not endorsement):** W3C Design Tokens Community Group published the first stable *Design Tokens Format/Color/Resolver* modules **2025-10-28** (CG Final Reports — **not** a W3C Recommendation; industry tooling adoption announced). Use the format when tooling needs interchange; plain CSS custom properties are enough for most VCNO projects.
- **Component reuse:** prefer project-existing libraries (if `package.json` shows one) — accessibility of established libraries usually beats bespoke reimplementation; still verify states (§7) and labels (§4).
- **Documentation minimum for U2 tokens:** one table in the project docs: token name → value → usage rule; dark-mode mapping if any. Registered in `docs/README.md` per repo convention.
- **Forbidden:** imposing a named external design language (Material, iOS, …) as a requirement; copying marketing screenshots as spec.

---

## §11 Motion & perceived performance

1. **`prefers-reduced-motion: reduce`:** honor it — cut non-essential animation/parallax/auto-scroll (`Confirmed` CSS media feature; WCAG 2.3.3 addresses animation triggered from interactions at AAA; reduce-motion is the practical mechanism). Essential motion (progress, state change) may remain subtle.
2. **Durations:** micro-interactions 100–200ms; anything >300ms needs a reason. No infinite decorative animation in product UIs (battery, distraction).
3. **Perceived performance toolkit** (`Inferred` widely-adopted):
   - Skeleton/placeholder for content >300ms — but keep layout stable (no CLS — cross-ref SEO §6).
   - Optimistic UI only for low-risk reversible actions; always reconcile with server truth; never optimistic for money/destructive/security-critical ops.
   - Instant feedback on every click (§3 heuristic 1) even when the real work is slow.
4. **Never fake progress** that lies about completion of security/money operations (honesty + security module).
5. Load-order discipline: render text/UI shell before heavy JS/fonts when possible (font-display strategy, defer non-critical JS) — ties to real CWV in SEO module.

---

## §12 Context-specific design (conditional patterns)

| Context | Emphasis |
|---|---|
| **Marketing/landing** | One primary CTA above fold; scannable hierarchy (headline → value → proof → CTA); fast LCP (SEO §6); honest claims (no fake urgency — also trust/ethics). |
| **Dashboard/app shell** | Persistent nav + landmarks; data density with readability (§6 spacing); every chart has text/table alternative (1.1.1/1.3.1); loading & empty & error states for every data view; filter state visible (URL sync `Inferred`). |
| **Admin CRUD** | Table + filter + pagination (bounded, server-side — security §6.C.6); bulk actions need confirm + undo; permissions reflected in UI **and** enforced server-side (UI hiding ≠ authorization — security P2). |
| **E-commerce/checkout** | Progress indicator; guest checkout option (`Inferred`); price always visible before commit (3.3.4); error recovery without re-entry (§8.8); trust signals without dark patterns (no pre-checked extras — honesty + consumer-protection direction). |
| **Auth surfaces** | 3.3.8 accessible auth; password paste allowed; show-password toggle; rate-limit messaging humanized; reset flow without account enumeration (security §6.A.5 shapes the UX copy). |
| **Mobile web** | Thumb-zone primary actions; safe-area insets; no hover-dependent flows; input zoom prevention (≥16px); bottom sheets/dialogs dismissible. |

---

## §13 Mapping to the VCNO lifecycle (integration only — no workflow changes)

| Stage | UI/UX activity (additive mindset) | Output |
|---|---|---|
| `/init` | Answer §2 inspection; note UI tier U0–U3; record RTL/bilingual need | project.md notes / init log line |
| `/check` | Flag UX risks (no empty/error states anywhere, hardcoded strings for bilingual scope, zero a11y affordances in existing UI) | Risks section |
| `/PRD` | UI tier decision; accessibility target (AA); flows + acceptance criteria phrased observably (“keyboard user can complete X”; “error message names field and fix”); list of pages/components in scope; i18n requirement | PRD sections + acceptance criteria |
| `/Build` | Implement §4–§9 as code rules; states matrix; logical CSS for RTL; semantic HTML; server-side stays authority for validation/authorization | Code + self-review notes |
| `/Feedback` | UX findings as UX-NNN (or FB items) with severity S1–S4 + evidence (screenshot paths, computed contrast, SC reference); S1/S2 block “polish complete” claims | findings entries |
| `/Doc` | Document tokens (U2), i18n structure, known UX limitations honestly; never claim compliance without audit evidence | docs entries |

---

## §14 Common failure patterns (avoid these)

1. `outline: none` without visible focus replacement (kills keyboard UX).
2. Placeholder-as-label (fails 3.3.2; erases on input).
3. Color-only state (error=red border only).
4. `left/right` CSS in a product that will ever be RTL — retrofit is expensive; use logical properties from day one (§9.2).
5. Icon-only controls without accessible names.
6. div/button soup (`<div onClick>`) — no keyboard, no role.
7. Hover-only actions on touch-primary flows.
8. Disabling the submit button forever with no error shown (mystery meat).
9. Raw error strings/stack traces/`Error 500` shown to users.
10. Animations ignoring `prefers-reduced-motion`.
11. Fixed pixel widths breaking 320px reflow.
12. Claiming “accessible”/“WCAG AA compliant” from a code read-through without audit evidence.
13. Design-system imposition on a tiny project (over-engineering; VCNO anti-over-engineering ethos).
14. UI-only authorization (hiding buttons instead of server checks) — security violation dressed as UX.
15. Dark patterns: fake scarcity, confirm-shaming, hidden costs — rejected on honesty grounds even if “converts”.

---

## §15 Safety & non-negotiable constraints

1. **Never weaken security for UX** (server-side validation/authz/CSRF stay; UX-layer validation is additive).
2. **Never fabricate accessibility/usability claims or test results** (no invented audit dates, no “screen-reader tested” without evidence).
3. **No dark patterns**; no deceptive counts/reviews/urgency.
4. **Privacy-respecting personalization:** behavior tracking/analytics require project decision + consent where legally required — agent does not add stealth telemetry (`Unknown` → ask).
5. **Don't break existing brand/assets** without reason; changes are minimal and justified.
6. **No unnecessary dependencies** for design (no UI framework additions without PRD justification — same as security supply-chain discipline).
7. **Respect user agents:** never block basic functionality on JS failure where avoidable (progressive enhancement `Inferred` for U1 content surfaces; U2 apps may require JS but should fail visibly, not blank).
8. **Accessibility is not “fixed at the end”** — cheapest at `/PRD`+`/Build`; end-stage a11y refactors routinely miss S1 issues.

---

## §16 Verification checklists (agent-runnable vs human-gated)

### 16.1 Agent static review (every U1+ change with UI)

- [ ] Semantic HTML for controls/structure (§7, §4.1)
- [ ] Focus visible + order sane (2.4.7/2.4.3)
- [ ] Labels & error association present (§8)
- [ ] Contrast pairs computed if colors touched (1.4.3/1.4.11)
- [ ] RTL: logical properties used if project is/will be bilingual (§9)
- [ ] States matrix present for changed components (§7)
- [ ] Reduced-motion honored if animations added (§11)
- [ ] No raw errors to users; loading/empty states exist for new async views
- [ ] i18n strings not hardcoded in bilingual projects

### 16.2 Needs real environment/tools (run if project provides them; else mark `Not run`)

- [ ] Automated a11y scan (axe-class) on affected pages
- [ ] Lighthouse/Performance on landing-critical pages (cross-ref SEO module)
- [ ] Keyboard walkthrough of changed flows in a browser
- [ ] RTL visual render check (browser emulation)

### 16.3 Human-gated (agent states requirement; never fakes)

- [ ] Screen-reader usability session
- [ ] Real-user usability testing
- [ ] Formal WCAG conformance audit / legal review (U3)
- [ ] Brand/design sign-off

---

## §17 Versioning & maintenance

- **Semver for this file:** MAJOR = guidance reversed; MINOR = new coverage; PATCH = corrections/freshness.
- **Review cadence:** every 12 months, or immediately when: WCAG publishes a new Recommendation/major update; a cited source changes materially (NN/g heuristics page, W3C i18n, web.dev course, DTCG spec status); VCNO gains new frontend conventions.
- **Procedure:** re-fetch §18 sources → update claims/labels/`Last reviewed` → changelog line → run `python scripts/validate.py`.
- **Changelog:**
  - **1.0.0 (2026-10-16)** — initial module. Fetched: WCAG 2.2 (W3C Rec 2024-12-12), NN/g 10 heuristics, W3C i18n structural RTL markup, web.dev Learn Responsive Design (course index), W3C Design Tokens CG (2025-10 stable modules).

---

## §18 Sources & verification status (accessed 2026-10-16)

| # | Source | Status | Used for |
|---|---|---|---|
| 1 | W3C WCAG 2.2 — https://www.w3.org/TR/WCAG22/ (Rec 2024-12-12; this-version URL https://www.w3.org/TR/2024/REC-WCAG22-20241212/) | **Fetched** | §4 entire; SC numbers/levels incl. new-in-2.2 set; removal of 4.1.1; POUR structure |
| 2 | NN/g — 10 Usability Heuristics — https://www.nngroup.com/articles/ten-usability-heuristics/ (1994; reviewed 2024-01-30) | **Fetched** | §3; factor-analysis provenance; “unchanged since 1994” honesty note |
| 3 | W3C i18n — Structural markup and RTL text in HTML — https://www.w3.org/International/questions/qa-html-dir | **Fetched** | §9.1–9.5, dir/lang rules, logical-properties list, dir=auto/dirname/bdi, table direction |
| 4 | web.dev — Learn Responsive Design — https://web.dev/learn/design/ | **Fetched** (course index) | §5 topic map (media queries, i18n, layouts, typography, images, icons, theming, accessibility, interaction, UI patterns, media features) |
| 5 | W3C Design Tokens CG — https://www.w3.org/community/design-tokens/ (2025.10 final modules announcement 2025-10-28) | **Fetched** | §10 standard existence/status (CG Final ≠ W3C Rec — stated) |
| 6 | WCAG 2.2 Understanding / Quick Ref — https://www.w3.org/WAI/WCAG22/Understanding/ · https://www.w3.org/WAI/WCAG22/quickref/ | Linked only | Precise SC text thresholds (24×24 target, 320px reflow, 4.5:1) are normative SC values recalled and consistent with fetched TOC; re-verify before quoting in project docs |
| 7 | WAI-ARIA Authoring Practices — https://www.w3.org/WAI/ARIA/apg/ | Linked only | Widget pattern grounding (dialogs etc.) — pattern details `Inferred` from common practice until fetched |
| 8 | NN/g Error Message Guidelines — https://www.nngroup.com/articles/error-message-guidelines/ | Linked only | §8.6 direction consistent with fetched heuristic #9 summary |
| 9 | Live UX testing, screen-reader sessions, Lighthouse runs, formal audits | **Not run** | No target project in scope; per-project evidence required (`Unknown`) |

**Disclaimer (carry into derived project docs):** no checklist or AI review guarantees usability or accessibility conformance; this module structures decisions and verification; real users and audits remain the authority.

---

*End of UIUX_KNOWLEDGE.md v1.0.0.*
