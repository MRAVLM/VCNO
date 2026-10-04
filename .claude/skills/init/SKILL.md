---
name: init
description: VCNO Stage 1 (/init) — بازرسانی مخزن و ساخت context مستند (docs/project.md + docs/logs/init.md) بدون دست‌زدن به کد؛ برای شروع پروژه‌ی جدید، ورود کدِ موجود به VCNO، و آماده‌سازی context قبل از /check.
---

# اسکیل `/init` — نسخه‌ی ورودی Claude Code

> این فایل یک **shim** است تا Claude Code اسکیل را در مسیر بومی خودش (`.claude/skills/`) پیدا کند.
> منبع واحد حقیقت: [`skills/init/SKILL.md`](../../../skills/init/SKILL.md)

**آن فایل را بخوان و دقیقاً طبق همان مراحل اجرا کن.** خلاصه‌ی سریع:

- مأموریت: **Understand before changing** — فقط بازرسی و مستندسازی؛ هیچ کد/نصب/بازآرایی ممنوع.
- خروجی: `docs/project.md` + `docs/logs/init.md` + گزارش نهایی با یکی از `INIT_COMPLETED` / `PARTIAL` / `NEEDS_INPUT`.
- secretها هرگز در داکس ثبت نمی‌شوند؛ Git reset/stash ممنوع؛ dirty tree را commit نکن.
- مرحله‌ی بعدی: `/check`.
