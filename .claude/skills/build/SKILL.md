---
name: build
description: VCNO Stage 4 (/Build) — پیاده‌سازی تدریجی PRD تأییدشده با تست، تأیید رفتار و checkpointهای Git؛ خروجی: COMPLETE | PARTIAL | BLOCKED. پس از /PRD، این اسکیل (و /Feedback) مجاز به تغییر کد است.
---

# اسکیل `/Build` — نسخه‌ی ورودی Claude Code

> این فایل یک **shim** است تا Claude Code اسکیل را در مسیر بومی خودش (`.claude/skills/`) پیدا کند.
> منبع واحد حقیقت: [`skills/build/SKILL.md`](../../../skills/build/SKILL.md)

**آن فایل را بخوان و دقیقاً طبق همان مراحل اجرا کن.** خلاصه‌ی سریع:

- مأموریت: «طرح تأییدشده را درست، ایمن و قابل‌تأیید پیاده کن.» — اول Readiness Gate، بعد Git، بعد فهمِ کد، بعد پیاده‌سازیِ تدریجی.
- PRD غایب/ناقص/مبهم → STOP، کد ننویس، سؤال کن.
- اولویت با reuse؛ auth **و** authorization اجباری؛ secret هرگز hard-code؛ `except Exception: pass` ممنوع.
- تست را واقعاً اجرا کن؛ «پاس شد» فقط با اجرای واقعی؛ بدون مدرک `COMPLETE` نگو — `PARTIAL` یا `BLOCKED` بده.
- خروجی: گزارش `# VCNO Build Complete` با `COMPLETE | PARTIAL | BLOCKED`. مرحله‌ی بعدی: `/Feedback`.
