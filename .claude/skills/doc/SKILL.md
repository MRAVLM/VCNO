---
name: doc
description: VCNO Stage 6 (/Doc) — هم‌راستاسازی مستندات با پیاده‌سازی واقعی و ارزیابی آمادگی تحویل/انتشار؛ خروجی: DOCUMENTED | READY FOR HANDOFF | READY FOR RELEASE | PARTIALLY DOCUMENTED | BLOCKED. فقط داکس را تغییر می‌دهد.
---

# اسکیل `/Doc` — نسخه‌ی ورودی Claude Code

> این فایل یک **shim** است تا Claude Code اسکیل را در مسیر بومی خودش (`.claude/skills/`) پیدا کند.
> منبع واحد حقیقت: [`skills/doc/SKILL.md`](../../../skills/doc/SKILL.md)

**آن فایل را بخوان و دقیقاً طبق همان مراحل اجرا کن.** خلاصه‌ی سریع:

- مأموریت: «واقعیت را مستند کن، نه نیّت را.» — اول پروژه را بازرسی کن، بعد audit داکس موجود، بعد reconcile.
- **پیاده‌سازی نهایی منبع حقیقت است**؛ فیچر غایب را مستندش کن، نسازش؛ باگ خاموش رفع نکن.
- `Documented` / `Verified` / `Not Verified` / `Unknown` را همیشه تمایز بده؛ secret هرگز در داکس نرو.
- خروجی: `# VCNO Documentation Report` با دقیقاً یک حالت: `DOCUMENTED` | `READY FOR HANDOFF` | `READY FOR RELEASE` | `PARTIALLY DOCUMENTED` | `BLOCKED`.
- مرحله‌ی پایانی VCNO است؛ `READY FOR RELEASE` فقط با مدرک واقعی.
