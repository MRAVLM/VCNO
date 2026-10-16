# SEO Knowledge Module for VCNO

> **Who/when:** An AI coding agent working on any VCNO-managed project (`/init → /check → /PRD → /Build → /Feedback ↺ → /Doc`) where search visibility is a possible project goal. Read the **Decision Gate** first; skip the rest when SEO is not applicable.
> **What this is:** A persistent knowledge file consumed alongside the project's security knowledge. It is **not** a Skill, command, plugin, or workflow change.
> **Version:** 1.0.0 · **Last reviewed:** 2026-10-16 · **Review policy:** see §16

---

## 0. How to use this file

1. **Run the Decision Gate (§1) at `/init` or `/check`.** If the outcome is `NOT APPLICABLE`, record one line of justification and stop. Do not run SEO checks on private dashboards, internal tools, CLI apps, or non-web projects.
2. **If applicable**, carry the selected checks into `/PRD` as requirements with verifiable acceptance criteria — never as a parallel workflow.
3. **In `/Build`**, implement only the smallest compatible change; in `/Feedback`, report findings with evidence labels; in `/Doc`, document what was configured, verified, and left unverified.
4. **Grading every recommendation you make:**

| Class | Meaning |
|---|---|
| **Required** | Needed for correctness, safety, or an explicit project requirement |
| **Recommended** | A meaningful improvement for *this* project |
| **Optional** | Useful only in certain contexts (state the context) |
| **Not applicable** | Irrelevant to this project (state why) |

5. **Label every claim you make about a live site:**

| Evidence label | Meaning |
|---|---|
| **Observed** | Directly measured in this session (tool output, fetched HTML, executed check) — quote the command/output |
| **Inferred** | Reasoned from code/config in the repo, not verified on a live host — say so |
| **Hypothesis** | Plausible but untested — must not be reported as a finding |
| **Unavailable** | Cannot be checked with current access — list as an open item |

6. **Severity for findings:** `Critical` (blocks indexing of intended-public pages, or exposes private data) · `High` (major visibility or user harm, evidence-backed) · `Medium` (clear defect, bounded impact) · `Low` (polish) · `Informational` (context, no action required). Severity follows **actual impact + evidence**, never alarmism. Never inflate severity to make work look important.

**Never fabricate:** rankings, traffic, search volume, scores, rich-result eligibility results, "verified" claims, statistics, reviews, or test outcomes. If a tool was not run, say the check was not run.

---

## 1. Decision gate: does this project need SEO?

Answer in `/init`/`/check` and record the answer in the project context:

1. **Is there a web surface intended to be found by search engines?** (marketing site, landing page, blog, docs site, content platform, SaaS marketing pages, marketplace listings, portfolio, local business site.)
2. **Who is the audience, in which language(s) and geography?** (e.g., Persian speakers in Iran; bilingual FA/EN; global EN.)
3. **What is the content model?** (static pages, articles, products, user-generated content, programmatic pages.)
4. **Which routes are *public and indexable* vs *private*?** Enumerate: public content pages; authenticated dashboards; app-only routes (`/app/*`, `/admin/*`, `/dashboard/*`); internal tools; preview/staging URLs; API endpoints; utility routes (login, cart, checkout, search results).

Outcomes:

- **`APPLICABLE`** — public pages exist and discoverability serves a project goal → proceed with applicable sections.
- **`APPLICABLE — LIMITED`** — only a few public pages (e.g., SaaS with 3 marketing pages) → apply §3 core, §4 titles/meta, and only minimal structured data (§5); skip §9 unless applicable.
- **`NOT APPLICABLE`** — no indexable public surface (internal tool, private dashboard, CLI, backend service) → stop. Adding SEO here is scope creep. The one exception: ensure private routes are **not** accidentally indexable (§3.1), which is a security-adjacent correctness item.

Rules:

- Consider SEO at the **earliest suitable stage** (`/check` or `/PRD`) — never as a post-launch repair pass.
- Do not add SEO complexity (sitemaps, hreflang, schema farms, prerendering) to projects that do not need it.
- The user's explicit requirements override this gate: if they ask for SEO features regardless, grade them honestly (Required by request) and note any risks.

---

## 2. Inspection before proposal (input to `/check`)

Before recommending anything, inspect and record (each as Observed/Inferred):

- **Stack & rendering:** static HTML, SSG/SSR (Next/Nuxt/Astro/…), SPA client-rendered, server-rendered app, CMS.
- **Routing:** framework router, URL scheme, trailing-slash behavior, query params, hash routing.
- **Existing metadata:** `<title>`, meta description, canonical, robots meta, `lang`/`dir`, Open Graph, JSON-LD.
- **Existing controls:** `robots.txt`, sitemap file(s), redirects/hosts (www/non-www, http/https), 404 handling.
- **Deployment:** host, CDN, environment URLs (staging vs production), what "production" means here.
- **Constraints:** what must not change (existing routes, auth flows, contracts, tests).

Propose changes only against this picture. The smallest compatible change wins.

---

## 3. Technical SEO (core checklist)

Apply only the items relevant to an `APPLICABLE` project.

### 3.1 Crawlability & indexability — Required for public pages

- Public content is reachable via **crawlable `<a href>` links** (not only via JS events, forms, or search boxes).
- Decide indexability **per route class**; default public content to indexable, private routes to `noindex` (and typically `Disallow` in `robots.txt` only for crawling economy — see the distinction below).
- **`robots.txt` controls crawling; `meta robots`/`X-Robots-Tag` controls indexing.** Blocking a URL in `robots.txt` does **not** `noindex` it, and blocked pages can still appear in results (often without content). For "keep out of search": use `noindex` (and confirm with URL Inspection). For "don't waste crawl budget": `robots.txt`.
- Never block important assets (CSS/JS/fonts/images) in `robots.txt` — that harms rendering and page experience. **Never weaken or change existing robots directives without the site owner's understanding and approval (§14).**
- Staging/preview/dev hosts (`staging.`, `preview.`, `test.`) must not be indexable copies of production — noindex them or keep them authenticated; verify (Observed or Inferred, labeled).

### 3.2 Status codes & redirects — Required

- Public pages return `200`. Deleted pages → `410` (or `404`). Moved pages → **single-hop `301`**. Temporary → `302/307`.
- No redirect chains (A→B→C) or loops; no redirect-to-homepage pretending to be a 404 (soft 404).
- Canonical host consistency: one of `www`/non-www, one of `http`/`https`, with permanent redirects between them; site served over **HTTPS** (this is both an SEO and security baseline).
- Never create fake redirects or cloaking-style user-agent-specific responses.

### 3.3 Canonical URLs — Required where duplicates can exist

- Every indexable page has a self-referencing `rel="canonical"` (or an authoritative canonical for true duplicates: URL params, printer versions, `http`/`www` variants, language variants — see §7).
- Canonical targets a **real, indexable, 200-returning URL** with the correct scheme/host/path. Fake canonicals (pointing at made-up or blocked URLs) are worse than none.
- Canonical, sitemap, internal links, and hreflang (if any) must all agree on the same canonical form.

### 3.4 URL hygiene — Recommended

- One consistent form per page: pick trailing-slash policy (or none) and stick to it; lowercase paths where the server is case-sensitive; no indexable query-parameter duplicates (`?utm=` variants, sort/filter params) — handle via canonicals, parameter rules, or `noindex` of faceted URLs (§9).
- Human-readable, descriptive paths (`/blog/persian-seo-basics`, not `/p?id=847`); avoid stop-word-heavy or keyword-stuffed slugs; URLs may be re-encoded only with a redirect in place.
- Hash-routed SPAs (`/#/page`) are effectively one URL to crawlers — prefer real paths if the project needs those pages indexed.

### 3.5 XML sitemap — Recommended for sites with >1 public page

- `sitemap.xml` lists **only indexable, canonical, 200 URLs** (no `noindex`, redirecting, or blocked URLs — a sitemap full of junk is a defect).
- Reference it from `robots.txt` (`Sitemap:`) and submit in Search Console when available.
- Keep it generated/accurate at build time; `lastmod` must be honest (real change dates).
- Never invent sitemap entries for pages that don't exist.

### 3.6 Internal linking & architecture — Recommended

- Descriptive anchor text (what the link is about — not "click here", not keyword-piled).
- Important pages within a few clicks of the homepage; no orphan pages (reachable only via sitemap); a sane hierarchy (`hub → section → detail`).
- Breadcrumbs with `BreadcrumbList` schema where hierarchy exists (§5).
- Pagination: use real paginated URLs (`/blog/page/2`) with self-canonicals per page (Google's guidance: each paginated page canonicalizes to itself); never `noindex` pagination chains blindly — verify current guidance before changing.

### 3.7 JavaScript-rendered content — Conditional (Required for SPA/public content)

- If public content requires JS to appear, prefer **SSR/SSG/prerender for indexable routes** where the stack supports it — justified by the project, not by habit.
- Verify what a crawler receives: check the raw HTML (view-source / `curl`-style fetch) — if key content/links/metadata are absent without JS, that is a **High** finding for a page meant to be indexed.
- Google can render JS, but rendering is not guaranteed, costly, and varies — do not rely on it when a simpler server-rendered path exists.
- Avoid lazy-loading content that is above the fold or needed for indexing without a fallback.

### 3.8 Mobile, security & privacy (SEO-relevant) — Required baseline

- Responsive layout; mobile is the primary indexing context — test the public pages at mobile widths.
- HTTPS everywhere; no mixed content; HSTS optional (a server config decision — do not add without owner approval).
- **Privacy exposure check before making anything indexable:** public pages must not leak emails/phones of private individuals, internal admin URLs, API keys/tokens, non-public user data, or hidden authenticated content. Indexability of a page publishes it. Cross-check with the project's security requirements — SEO must never weaken security (§14).
- Error pages: real `404`/`410` for missing content with useful navigation; never serve `200` with an error message (soft 404).

### 3.9 Images — Recommended

- Descriptive `alt` text where the image conveys information; `alt=""` for purely decorative; **no keyword stuffing in alt**.
- Modern formats (WebP/AVIF), explicit `width`/`height` (or `aspect-ratio`) to prevent CLS, `loading="lazy"` below the fold, eager-load the LCP image (§6).
- Meaningful `filename`/`srcset` where easy; image URLs that return `200`. Images in sitemap only when image discovery matters (Optional).

---

## 4. On-page & content quality

### 4.1 The page basics — Required for every public page

- **Unique, descriptive `<title>`** — front-load the primary topic; natural length (~50–60 chars is a guide, not a law); one line per site, no duplication across pages.
- **Meta description** — unique per page, truthful summary with real value proposition (~120–160 chars guide); it is a snippet input, not a ranking factor; missing is better than misleading.
- **One `H1`** matching the page's actual subject; logical `H2/H3` outline of the real content structure.
- **`<html lang="…">` + `dir`** correct for the page language (§7 for Persian).
- Descriptive internal link anchors (§3.6); meaningful URL (§3.4).

### 4.2 Content quality — Required principles

- Write for **genuine user intent**: answer the query the page targets better than anyone, with first-hand value — data, examples, opinion, expertise — not a restatement of what's already indexed.
- **People-first, not engine-first** (Google Search Essentials): helpful, reliable content; words people actually use, in the title and main heading.
- Avoid: duplicate/near-duplicate pages, empty shells, auto-generated thin pages, doorway pages, repetitive keyword strings, hidden/oversized text tricks, misleading titles, manipulative link schemes — these are spam-policy violations (ranking loss or removal), i.e., **Critical/High** risk if found in the project.
- **Never generate unsupported claims:** fabricated statistics, fake testimonials, invented awards, fake business details, fake expert credentials, made-up case studies. If the user provides real data, use it; otherwise leave it out.
- AI-assisted drafting is allowed but the output must meet the same standards: original, accurate, useful (Google's guidance on AI-generated content is quality-based, not authorship-based). Disclose nothing that isn't true; don't mass-produce near-duplicate pages (scaled content abuse policy).

### 4.3 Keyword & search intent research — Recommended process (no invented metrics)

1. Brainstorm the queries a real user would type for each page's purpose.
2. Classify intent: informational / navigational / commercial / transactional — the page format must match the intent (don't rank a product page for "what is X" intent and vice versa).
3. Group queries into **topic clusters**; assign each cluster **one primary page** (one page = one primary intent).
4. Detect **cannibalization**: two pages targeting the same intent → merge, differentiate, or canonicalize.
5. Prioritize by relevance × usefulness × feasibility × business value.
6. **Data honesty:** real search-volume/ranking/competitor data only if a tool or the user actually supplied it (`Observed`/`user-provided`). Otherwise label estimates as `Hypothesis`. **Never invent numbers, never promise rankings.**

---

## 5. Structured data (Schema.org)

- **When useful:** when the page's content maps to a supported feature (Article, Product, Organization, Breadcrumb, Event, Recipe, LocalBusiness, FAQ where eligible, …) **and** markup can mirror visible content. Skip when it adds nothing for the user.
- **Format:** **JSON-LD** in `<script type="application/ld+json">` (Google's recommended format); Microdata/RDFa only if the project already uses them.
- **Parity rule (hard):** markup must describe content **visible on the page**. Google's guidelines explicitly say: don't add structured data about information not visible to the user, and don't create blank pages just to hold markup. No fake `aggregateRating`, fake `Review`s, invented `price`/`availability`, fake `author`/`sameAs`.
- **Type selection:** choose `@type` from actual page content; use required + realistically-populatable recommended properties — "fewer but complete and accurate" beats every-property-badly (Google structured data intro). For Google Search behavior, **Google's feature docs take precedence over schema.org docs** (stated in Google's intro page).
- **Validation:** parse the JSON (must be valid JSON-LD), then Rich Results Test during development; Search Console's rich results status report after deploy. Validate against the specific feature's required properties.
- **Claims discipline:** valid markup ≠ guaranteed rich result, ≠ ranking boost; eligibility can change (feature retirements happen — e.g., structured-data features get discontinued, and third-party repos disagree on current FAQ/HowTo eligibility dates → **verify the current feature page** before relying on any rich-result claim).
- **AI-search note:** structured data is *not required* for Google's generative AI features (§8).

Minimal trustworthy example (Article-shaped page):

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "…exact visible H1/subject…",
  "datePublished": "2026-10-16",
  "author": { "@type": "Person", "name": "…real named author on the page…" },
  "image": "https://example.com/img.jpg",
  "mainEntityOfPage": "https://example.com/article-url"
}
```

---

## 6. Performance & Core Web Vitals

**Verified thresholds (web.dev/vitals, last updated 2024-10-31; `Observed` by fetching the page on 2026-10-16):**

| Metric | Measures | Good at 75th percentile |
|---|---|---|
| **LCP** | loading | ≤ **2.5 s** from page load start |
| **INP** | interactivity | ≤ **200 ms** |
| **CLS** | visual stability | ≤ **0.1** |

- FID is retired; **INP** is the stable interaction metric (since 2024). Do not recommend FID targets.
- **Lab vs field:** Lighthouse/DevTools = lab (simulated; **cannot measure INP — use TBT as lab proxy**); CrUX/PageSpeed Insights field data & Search Console CWV report = real users. Label which one you used. Lab ≠ field; never report a lab score as "users experience X".
- Bottlenecks worth fixing when performance matters: render-blocking resources, oversized/unoptimized images and hero media, slow TTFB, layout-shifting embeds/fonts (use `font-display`, reserve space), excessive third-party tags, unnecessary JS and long tasks (code-split, defer), missing caching/compression at the host/CDN.
- Preserve accessibility, functionality, and design while optimizing — performance never justifies breaking a11y.
- **Evidence rule:** run Lighthouse/PageSpeed Insights when a browser/tool is actually available and the target is authorized to be tested; otherwise mark `Unavailable` and give the manual steps. **Never invent scores or claim a measurement that wasn't run.**

---

## 7. Persian & multilingual SEO

Applies when the project serves Persian and/or multiple languages.

### 7.1 Language & direction — Required

- `<html lang="fa" dir="rtl">` on Persian pages (`lang="en" dir="ltr"` on English). Correct `lang` per localized page — wrong `lang` misleads assistive tech and language detection.
- Persian **and** English `<title>`/meta content when the page is genuinely in that language (write each natively in its own language; don't machine-swap and forget).
- Fonts/rendering: ensure Persian glyphs render everywhere (subset webfonts carefully — missing Persian glyphs is a quality defect).

### 7.2 Persian text hygiene — Required for correctness

- **Normalize character variants consistently:** Arabic-keyboard vs Persian-keyboard forms of ی، ک، گ (ي/ى vs ی, ك vs ک) — pick Persian forms (ی ک گ) and apply everywhere; mixed forms create **invisible duplicate content** across pages and break string matching.
- **ZWNJ (U+200C):** use it correctly in compounds (می‌شود، جست‌وجو); don't double it; be consistent — normalization differences = duplicate-content risk.
- **Digits:** Persian (۱۲۳) vs ASCII (123) — be consistent within a language version; never mix in the same template. Percent/ currency formatting consistent.
- **URL encoding:** percent-encode non-ASCII consistently if any Persian text appears in URLs (prefer ASCII slugs: `/blog/seo-basics` even on the Persian site — avoids encoding/copy-paste breakage).
- Natural Persian titles/descriptions — real Persian sentences, no transliterated keyword soup, no awkward "SEO SEO بهینه‌سازی" stuffing.

### 7.3 Language URL strategy & hreflang — Conditional

- Pick one consistent strategy for genuine language variants: path (`/fa/`, `/en/`), subdomain, or separate domains — **consistent per language**, encoded in canonical, sitemap, internal links, and hreflang alike.
- `hreflang` **only** for pages that are true translations/localizations of each other (equivalent content, not language-switched thin pages):
  - reciprocal (`return` tags both ways), valid BCP 47 codes (`fa`, `fa-IR`, `en`, `en-US`), include `x-default`;
  - the localized page's own canonical/hreflang/sitemap all agree;
  - don't hreflang two URLs that canonicalize to the same page.
- **Do not assume every Persian project needs bilingual pages** — language ≠ audience. Only build language variants the project actually needs and can maintain. **No auto-translated doorway pages** with little user value (spam-adjacent + poor UX).

---

## 8. AI search & generative search visibility (evidence-conscious)

**Officially established (Google's "Optimizing for generative AI features", fetched 2026-10-16, page last updated 2026-07-10):**

- Google's generative features (AI Overviews/AI Mode) draw from the **Search index via grounding/RAG and query fan-out** — so **foundational SEO remains the foundation**: indexable, crawlable, high-quality, helpful content.
- Google's position on "AEO/GEO": those are third-party terms; from Google's perspective, optimizing for generative AI search is still SEO. Evaluate third-party AEO/GEO advice against official guidance.
- **Google explicitly says you do NOT need:** `llms.txt` or other "special" AI files/markup for Google (it ignores them — harmless if created for *other* services that use them), content "chunking" for AI, rewriting content in an AI-specific style, seeking inauthentic "mentions", or special structured data for AI features.
- Scaling near-duplicate pages to catch query variants violates the **scaled content abuse** spam policy.
- Content guidance: unique POV, non-commodity content (not generic listicles anyone could write), clear heading structure, quality images/video, accurate organization/author/contact info where applicable.
- **Measurement:** Search Console **Generative AI performance report** (when the site is verified and included); be wary of third-party tools claiming "internal" Google metrics — none have access to Google's internal systems.

**Unproven/emerging — label as `Hypothesis`, never as a requirement:** citation-optimization formulas, "AI crawler allowlists guarantee visibility", GEO hacks, per-answer-engine keyword tactics, structured data as an AI citation guarantee.

**Crawler access:** making intended-public content accessible to legitimate crawlers is part of being on the public web; do **not** add blanket AI-crawler permissions (or blocks) without the site owner's decision — some owners intentionally block AI training crawlers, and that is their call, not an SEO default. Check `robots.txt` policy for AI crawlers only to *report* what exists (`Observed`), not to change it.

---

## 9. E-commerce, marketplaces & dynamic sites (conditional)

Apply only when the project is actually one of these:

- Unique, stable URL per product; variants handled without infinite URL space (parameter/canonical strategy).
- **Category/facet/filter/search pages:** sort/filter combinations explode into low-value URLs — control via canonicals, `noindex` on pure-facet URLs, parameter rules, or crawl restrictions (with reasoning); **internal search results pages should not be indexed by default** without a deliberate reason (they're thin, personalizable, and low-value).
- **Accuracy of commerce data:** `Product` schema price/availability/currency must **mirror the visible page and real data** (mismatches = rich-result eligibility loss + consumer-harm risk). Prices are user-provided/observed data — never invented.
- Expired/sold-out/deleted listings: `410`/redirect to a sensible successor (related product/category), never a soft-404 or a fake in-stock page.
- UGC (reviews, listings): index only moderated, valuable content; guard against user-generated spam (soft-404s, injected links); private seller/buyer data stays off public pages.
- E-commerce structured data (Product/Merchant listing/shipping/returns) only when those facts are visible and true.

---

## 10. Analytics & verification

**Tools and their limits:**

| Tool | Purpose | Needs credentials? |
|---|---|---|
| **Google Search Console** | index coverage, URL Inspection, CWV report, generative-AI report, performance data | Yes (account) — for *implementation* not required; for *monitoring* strongly recommended |
| **Sitemap submission** | faster discovery, status tracking | via GSC |
| **URL Inspection** | what Google actually sees/crawled/indexed | via GSC |
| **PageSpeed Insights / Lighthouse** | CWV lab+field, page diagnostics | No (PSI API optional for automation) |
| **Rich Results Test / validator** | structured data eligibility check | No |
| **Crawl/broken-link checks** | internal link & status integrity | No (local tools) |
| **Performance report** | queries/impressions/clicks over time | via GSC |

**Rules:**

- **Never require paid services, API keys, or external accounts to complete basic SEO implementation.** If a check needs access the project doesn't have, provide the **manual verification checklist** and mark the item `Unavailable`.
- **Authorization:** do not run external scans/crawls against a domain without the owner's authorization. Local code/repo inspection and fetching pages the user asked you to inspect are fine; bulk competitive crawling or attacking third-party sites is not.
- **Manual fallback checklist (no-tool verification):** view source for title/canonical/robots/lang/JSON-LD; fetch robots.txt & sitemap.xml; spot-check 200/301/404 behavior of key routes; confirm internal links resolve; confirm HTTPS & host consistency; confirm no private data in public HTML. Anything not run → `Unavailable`, list it.
- Every verification statement in reports must name the tool + when it ran; "should pass Lighthouse" without a run is a **fabricated claim** (prohibited).

---

## 11. Mapping to the VCNO lifecycle (integration only — no workflow changes)

| Stage | SEO action |
|---|---|
| **`/init`** | Run Decision Gate (§1). Record: web surface?, languages/geography, content model, public vs private route inventory. |
| **`/check`** | Inspect stack, rendering, routes, existing metadata/controls (§2). Surface SEO risks as project risks (JS-only content, duplicate hosts, staging exposed). |
| **`/PRD`** | Add only relevant SEO requirements with verifiable acceptance criteria (e.g., "each public route has unique title+canonical", "sitemap lists only 200/canonical URLs", "Persian pages: lang=fa/dir=rtl"). No separate SEO workflow, no new commands. |
| **`/Build`** | Implement applicable items from §3–§9: metadata, canonical, robots, sitemap, structured data, internal links, rendering, performance — smallest compatible change; test as you go. |
| **`/Feedback`** | Review actual pages; report findings with evidence labels + severity + class (§0); separate confirmed findings from assumptions; prioritize. |
| **`/Doc`** | Document: SEO configuration, route indexability map, verification performed, tools/accounts still needed (e.g., GSC setup), known limitations, maintenance duties. |

---

## 12. Agent decision process (per relevant project)

1. Determine whether search visibility is a project goal (§1) — record the answer.
2. Inspect stack/architecture/existing SEO implementation (§2) — label evidence.
3. Select only the applicable checks (§3–§10) — mark the rest `Not applicable` with a reason.
4. Prioritize correctness and user value over SEO complexity.
5. Propose the **smallest compatible reversible change**; for robots/canonical/redirect/hreflang/indexing changes, explain impact and require explicit owner approval (§14).
6. Validate with available tools; run only what you actually can run.
7. Report: findings → evidence label → severity → class → next step; list unresolved risks and what remains unverified.

---

## 13. Common failure patterns (avoid these)

- Applying a universal "SEO checklist" to a project that doesn't need SEO (§1).
- Indexing private dashboards, staging hosts, internal search results, or filter explosion pages.
- robots.txt used as noindex (wrong tool for the goal), or blocking CSS/JS assets.
- Fake canonicals, phantom sitemap URLs, redirect-to-home masquerading as 404.
- Claiming scores/rankings/eligibility that were never measured.
- Schema markup for invisible content; fake ratings/reviews/prices; promising rich results.
- Fabricated statistics/testimonials/credentials in content.
- Keyword-stuffed titles, doorway pages, scaled thin pages, hidden text (spam policy violations).
- Bilingual sites with inconsistent Persian normalization → self-inflicted duplicate content.
- hreflang that isn't reciprocal/consistent, or applied to non-equivalent pages.
- Rewriting content "for AI", adding `llms.txt`/schema expecting guaranteed AI citations (Google says not needed for Google).
- Changing production robots/canonical/redirect rules without understanding impact or having authorization (§14).
- Reporting a passing test that was never run.

---

## 14. Safety & non-negotiable constraints

- **Never weaken security to improve SEO.** Do not expose dashboards, private routes, tokens, or personal data to crawlers; do not disable auth, HTTPS, or access controls for "crawlability". If SEO and security requirements conflict → stop, surface the conflict to the user, propose the safest resolution.
- Do not modify production `robots.txt`, canonicals, redirects, or indexing settings **without understanding their impact and the site owner's explicit approval** — these are high-blast-radius changes (site-wide deindexing risk).
- No production deploys, publishes, or content pushes from SEO work without explicit authorization.
- No unauthorized external scans; no destructive tests against production or third-party systems.
- No new dependencies, frameworks, paid services, credentials, or MCP/skill/command systems for SEO — knowledge-only module.
- Do not fabricate verification. Do not claim security or SEO completeness from automated checks alone.
- Conflicts with existing project/security requirements: project + security win; document the assumption and the smallest reversible approach.

---

## 15. Verification quick-checklists

**Pre-`/Doc` (project-level, only for `APPLICABLE` projects):**

- [ ] Decision Gate answer + public/private route map recorded.
- [ ] Every public route: 200 + unique title + canonical + correct `lang`/`dir` (+ robots meta intent as designed).
- [ ] Private/auth/staging routes: `noindex` verified; no private data in public HTML.
- [ ] `robots.txt`: no important assets blocked; sitemap referenced; AI-crawler policy = owner's decision, reported as-is.
- [ ] `sitemap.xml`: only 200/canonical/indexable URLs.
- [ ] Redirects single-hop 301 for moves; no loops/chains/soft-404s.
- [ ] Structured data: valid JSON-LD, mirrors visible content, validated (or marked `Unavailable`).
- [ ] Persian pages: `lang`/`dir`, normalization/ZWNJ/digits consistent (§7).
- [ ] hreflang (if any): reciprocal + `x-default` + consistent with canonical/sitemap.
- [ ] CWV: measured (which tool, when) or explicitly `Unavailable`.
- [ ] All report claims carry evidence labels; no fabricated metrics.

**Per public page (quick pass):** title unique · description unique/truthful · one H1 · canonical self · lang/dir · crawlable internal links · images have alt where needed · no private data.

---

## 16. Versioning & maintenance policy

- **Version:** semantic, knowledge-base style — **MAJOR** = guidance reversed/section removed; **MINOR** = new section/coverage; **PATCH** = corrections/freshness (aligned with conventions used by maintained SEO knowledge repos).
- **Review triggers (re-verify against official docs):** at least **every 6 months**; immediately on any Google Search Central announcement about ranking/spam/structured-data/CWV changes; before relying on any rich-result eligibility claim; when a referenced tool changes.
- **How to review a change:** re-fetch the official source listed in §17, compare claims, update the claim **and** the `Last reviewed` date + version; record what changed in `knowledge/seo/README.md` (changelog section). Third-party repo advice stays `Hypothesis` until confirmed by official docs or direct observation.
- **Conflict rule:** official Google/search-engine documentation > reputable vendor docs > third-party SEO repos/blogs. When sources disagree (e.g., FAQ/HowTo eligibility dates across repos), keep the conservative statement ("verify the current feature page") rather than picking a date.

---

## 17. Sources & verification status (accessed 2026-10-16)

**Fetched and read directly (official unless noted):**

| Source | Used for | Page states "last updated" |
|---|---|---|
| Google Search Essentials — developers.google.com/search/docs/essentials | §4 principles, no-guarantee rule, spam/technical split | 2025-12-10 |
| Google structured data intro — …/appearance/structured-data/intro-structured-data | §5 JSON-LD, visibility parity, tool validation, precedence of Google docs over schema.org | 2025-12-10 |
| Google generative AI guide — …/fundamentals/ai-optimization-guide | §8 grounding/RAG, AEO/GEO position, mythbusting (llms.txt, chunking, mentions), gen-AI report | 2026-07-10 |
| web.dev Web Vitals — web.dev/articles/vitals | §6 thresholds (LCP 2.5 s / INP 200 ms / CLS 0.1 @ p75), FID→INP, lab vs field | 2024-10-31 |
| github.com/Bhanunamikaze/Agentic-SEO-Skill (MIT, README) | evidence/confidence labeling, severity rubric patterns — *hypotheses, not authority* | n/a |
| github.com/gaguero/seo-agent-skills (MIT, README) | evidence taxonomy (measured/inferred/user-provided/unavailable), fail-closed quality gates, human approval for risky SEO changes | n/a |
| github.com/kpab/seo-mastery-agent-skills (MIT, README) | freshness-dating (`last_verified`), semver-for-knowledge-base pattern | n/a |
| github.com/JeffLi1993/seo-audit-skill (MIT, README) | deterministic script check vs LLM judgment split for verification design | n/a |

**Linked from the above but NOT fetched in this session (do not claim they were inspected):** Google Search Console product page; PageSpeed Insights app UI (tool *referenced* via web.dev/Google docs, not run); schema.org homepage (schema.org vocabulary referenced via Google's intro page); Google Search Central docs index as a standalone page; SEO Starter Guide page as a standalone fetch.

**Attribution note:** Google/web.dev content above is CC BY 4.0 (code samples Apache 2.0); third-party repos are MIT. Nothing was copied wholesale — only principles and patterns were extracted, with attribution.

**Not executed in this session:** Lighthouse, PageSpeed API, Rich Results Test, Search Console checks, any live-site crawl — no target site was in scope. All such items must be run per-project or marked `Unavailable`.
