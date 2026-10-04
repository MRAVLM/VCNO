# Copilot Instructions — نقطه‌ی ورود GitHub Copilot

این فایل فقط یک pointer است؛ **محتوای اصلی پروژه در [`AGENTS.md`](../AGENTS.md) است.**

- ابتدا [`AGENTS.md`](../AGENTS.md) را بخوان (ساختار، قواعد، اسکیل‌ها).
- قواعد کدنویسی: [`docs/conventions.md`](../docs/conventions.md) — نام فایل kebab-case انگلیسی؛ توابع camelCase؛ کامیت انگلیسی و فعل‌محور.
- معماری: بک‌اند `route → service → db`؛ فرانت‌اند `page → component → api` (fetch فقط در `frontend/src/api/`).
- قبل از پایان کار: `npm run typecheck` و `npm run test`.
- اسکیل‌ها: [`skills/`](../skills/README.md) — شش مهارت VCNO با ترتیب `/init → /check → /PRD → /Build → /Feedback ↺ → /Doc`؛ مثلاً `/init` در [`skills/init/SKILL.md`](../skills/init/SKILL.md) (فقط context جمع می‌کند، کد نمی‌نویسد).
- فارسی برای توضیح داکس/کامیت، انگلیسی برای نام فایل‌ها و کد.
