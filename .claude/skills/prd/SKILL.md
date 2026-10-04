---
name: prd
description: VCNO Stage 3 (/PRD) — تبدیل فهم معتبر به blueprint آماده‌ی پیاده‌سازی (نیازمندی‌ها، جریان‌ها، معماری، دیتابیس، API، auth، تست، برنامه‌ی اجرا)؛ خروجی: DRAFT | NEEDS CLARIFICATION | READY FOR BUILD. کد نمی‌نویسد.
---

# اسکیل `/PRD` — نسخه‌ی ورودی Claude Code

> این فایل یک **shim** است تا Claude Code اسکیل را در مسیر بومی خودش (`.claude/skills/`) پیدا کند.
> منبع واحد حقیقت: [`skills/prd/SKILL.md`](../../../skills/prd/SKILL.md)

**آن فایل را بخوان و دقیقاً طبق همان مراحل اجرا کن.** خلاصه‌ی سریع:

- مأموریت: «دقیقاً چه می‌سازیم، چطور کار می‌کند، و `/Build` باید چه چیزی را پیاده کند؟»
- ورودی: context `/init` + رکورد `READY FOR PRD` از `/check`؛ معماری **موجود** را توسعه بده، clean-slate نساز.
- خروجی: `docs/PRD.md` (یا قاعده‌ی موجود) + دقیقاً یک حالت: `DRAFT` | `NEEDS CLARIFICATION` | `READY FOR BUILD`.
- پیاده‌سازی/نصب/refactor/deploy ممنوع؛ requirement اختراع نکن؛ over-engineer نکن؛ در حین `/PRD` ادعا نکن تستی پاس شده.
- مرحله‌ی بعدی: `/Build` (بعد از تأیید کاربر).
