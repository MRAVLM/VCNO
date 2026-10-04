---
name: check
description: VCNO Stage 2 (/check) — اعتبارسنجی ایده، نیازمندی‌ها، MVP، امکان‌سنجی، ریسک‌ها و تناقض‌ها قبل از /PRD؛ خروجی: NOT READY | READY WITH WARNINGS | READY FOR PRD. کد نمی‌نویسد.
---

# اسکیل `/check` — نسخه‌ی ورودی Claude Code

> این فایل یک **shim** است تا Claude Code اسکیل را در مسیر بومی خودش (`.claude/skills/`) پیدا کند.
> منبع واحد حقیقت: [`skills/check/SKILL.md`](../../../skills/check/SKILL.md)

**آن فایل را بخوان و دقیقاً طبق همان مراحل اجرا کن.** خلاصه‌ی سریع:

- مأموریت: «آیا آن‌قدر می‌فهمیم که بتوانیم یک PRD قابل‌اعتماد بسازیم؟» — نه برنامه‌ریزی، نه کدنویسی.
- ورودی: خروجی `/init` (`docs/project.md`، `docs/logs/init.md`)؛ سؤال‌های پاسخ‌داده‌شده را دوباره نپرس.
- خروجی: گزارش `# VCNO Check` + دقیقاً یک حالت: `NOT READY` | `READY WITH WARNINGS` | `READY FOR PRD`.
- معماری/schema کامل طراحی نکن (کار `/PRD`)؛ پیاده‌سازی/نصب/refactor ممنوع؛ secret در داکس ممنوع.
- مرحله‌ی بعدی: `/PRD`.
