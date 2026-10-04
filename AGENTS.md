# 📁 دستیار وایپ‌کدینگ — فایل اصلی پروژه

این فایل، **نقطه‌ی ورود هر ایجنت کدنویسی** است.
هر کسی که تازه می‌خواهد با این پروژه کار کند (چه انسان، چه ایجنت)، فقط همین فایل را بخواند تا بفهمد همه‌چیز کجاست — دیگر لازم نیست دنبال پرامپت یا توضیح بگردد.

---

## 🚀 سه قدم برای شروع (تازه‌کارها)

1. **بخش موردنیازت را پیدا کن:** اسکیل ← `skills/` — کد ← `backend/` و `frontend/` — داکس ← `docs/`
2. **به ایجنت بگو از کدام اسکیل استفاده کند** (فقط نام اسکیل کافی است؛ جزئیات داخل خود اسکیل است).
3. **قبل از هر تغییر بزرگ،** `docs/conventions.md` را مرور کن.

---

## ۱️⃣ بخش اسکیل‌ها → `skills/`

اسکیل = **دستور تکرارپذیر آماده برای ایجنت**. دیگر لازم نیست هر بار پرامپت بنویسی؛ اسکیل را صدا می‌زنی و ایجنت کل مسیر کار را طبق الگو اجرا می‌کند.

- 📖 راهنما و فهرست کامل: [`skills/README.md`](skills/README.md)
- 🧩 الگوی خالی برای ساخت اسکیل جدید: [`skills/_template/SKILL.md`](skills/_template/SKILL.md)
- 📂 محل قرار گرفتن هر اسکیل: `skills/<نام-اسکیل>/SKILL.md`

**اسکیل‌های موجود:**

| اسکیل | دستور | فایل | کاربرد |
|---|---|---|---|
| init | `/init` | [`skills/init/SKILL.md`](skills/init/SKILL.md) | بازرسانی مخزن + ساخت `docs/project.md` و `docs/logs/init.md` — **کد نمی‌نویسد** |
| check | `/check` | [`skills/check/SKILL.md`](skills/check/SKILL.md) | اعتبارسنجی ایده/نیازمندی/MVP/ریسک → آمادگی `/PRD` — **کد نمی‌نویسد** |
| prd | `/PRD` | [`skills/prd/SKILL.md`](skills/prd/SKILL.md) | blueprint آماده‌ی پیاده‌سازی + برنامه‌ی اجرا → آمادگی `/Build` — **کد نمی‌نویسد** |
| build | `/Build` | [`skills/build/SKILL.md`](skills/build/SKILL.md) | پیاده‌سازی تدریجی PRD با تست و checkpoint — **اولین مرحله‌ی مجازِ تغییر کد** |
| feedback | `/Feedback` | [`skills/feedback/SKILL.md`](skills/feedback/SKILL.md) | بازخورد → آیتم‌های FB-NNN با طبقه‌بندی/ریشه‌یابی/تست (حلقه ↺) |
| doc | `/Doc` | [`skills/doc/SKILL.md`](skills/doc/SKILL.md) | هم‌راستاسازی داکس با واقعیت + ارزیابی release — **فقط داکس** |

**ترتیب اجرا:** `/init → /check → /PRD → /Build → /Feedback ↺ → /Doc`

> **نکته برای ایجنت‌ها:** اگر ایجنت فقط مسیرهای خاص خودش را می‌خواند، از شیم‌های آماده استفاده کن — منبع حقیقت همیشه `skills/` است (فهرست کامل در [`skills/README.md`](skills/README.md)).

---

## ۲️⃣ بخش کدها → `backend/` و `frontend/`

پروژه به دو بخش جدا تقسیم شده؛ هرکدام README خودش را دارد:

- 🖥 **بک‌اند:** [`backend/README.md`](backend/README.md) — سرور، API، دیتابیس
- 🎨 **فرانت‌اند:** [`frontend/README.md`](frontend/README.md) — رابط کاربری

**تصمیم فنی (مشترک هر دو بخش):** زبان مشترک **TypeScript** برای سادگی تازه‌کارها — فقط یک زبان یاد بگیر، در هر دو طرف استفاده کن.

---

## ۳️⃣ بخش داکس → `docs/`

هر پروژه‌ی سالمی به این مجموعه داکس نیاز دارد (فهرست + وضعیت هرکدام):

- 📖 فهرست و راهنمای نوشتن داکس: [`docs/README.md`](docs/README.md)

| داکس | فایل | وضعیت |
|---|---|---|
| معرفی رسمی VCNO | `docs/ABOUT.md` | ✅ کامل |
| شروع سریع | `docs/getting-started.md` | ✅ کامل |
| معماری پروژه | `docs/architecture.md` | ✅ کامل |
| قواعد کدنویسی | `docs/conventions.md` | ✅ کامل |
| مرجع API | `docs/api.md` | ⚪ بدون API (تا `/Build`) |
| چگونه کمک کنم؟ | `docs/contributing.md` | ✅ کامل |

---

## 📜 قواعد کلی کار با ایجنت

1. **زبان داکس و کامیت‌ها:** فارسی (توضیح) / انگلیسی (نام فایل‌ها و توابع).
2. **هر تغییر بزرگ** اول در داکس، بعد در کد.
3. **تست قبل از اتمام** — هیچ تغییری بدون اجرای تست/تایپ‌چک تمام نمی‌شود.
4. **نام‌گذاری فایل‌ها:** kebab-case و انگلیسی.
5. **اسکیل جدید** فقط از الگوی `skills/_template/` ساخته می‌شود.

---

## 🤖 ورودی ابزارهای AI (بهینه‌سازی برای همه‌ی ایجنت‌ها)

این پروژه برای **هر ابزار AI-coding** بهینه شده؛ هر ابزار فایل بومی خودش را دارد و همه به یک منبع واحد اشاره می‌کنند:

| ابزار | فایلی که خودش را می‌خواند | به کجا اشاره می‌کند |
|---|---|---|
| استاندارد مشترک (Codex، Cursor، Zed، Amp، ...) | `AGENTS.md` | ← منبع اصلی |
| Claude Code | `CLAUDE.md` + `.claude/skills/*/SKILL.md` (هر ۶ اسکیل) | `AGENTS.md` + `skills/` |
| GitHub Copilot | `.github/copilot-instructions.md` | `AGENTS.md` |
| Gemini CLI | `GEMINI.md` | `AGENTS.md` |
| Windsurf | `.windsurfrules` | `AGENTS.md` |

**قانون:** محتوای اصلی فقط در `AGENTS.md` و `skills/` نوشته می‌شود؛ فایل‌های بالا شیم (pointer) هستند و نباید جداگانه ویرایش شوند.

---

## 🗺️ نقشه‌ی کلی پروژه

```
.
├── AGENTS.md          ← همین فایل (ورودی اصلی ایجنت‌ها)
├── CLAUDE.md          ← شیم Claude Code → AGENTS.md
├── README.md          ← معرفی + آموزش
├── .claude/skills/    ← شیم اسکیل‌ها برای Claude Code
├── .github/copilot-instructions.md  ← شیم Copilot
├── GEMINI.md          ← شیم Gemini CLI
├── .windsurfrules     ← شیم Windsurf
├── skills/            ← ۱) بخش اسکیل‌ها (منبع واحد حقیقت)
│   ├── README.md
│   ├── _template/SKILL.md
│   ├── init/SKILL.md     ← /init     (مرحله ۱ — درک)
│   ├── check/SKILL.md    ← /check    (مرحله ۲ — اعتبارسنجی)
│   ├── prd/SKILL.md      ← /PRD      (مرحله ۳ — برنامه‌ریزی)
│   ├── build/SKILL.md    ← /Build    (مرحله ۴ — پیاده‌سازی)
│   ├── feedback/SKILL.md ← /Feedback (مرحله ۵ — تکرار ↺)
│   ├── doc/SKILL.md      ← /Doc      (مرحله ۶ — نهایی‌سازی)
│   └── <اسکیل‌ها>/
├── backend/           ← ۲) بخش کدها (سرور)
├── frontend/          ← ۲) بخش کدها (رابط کاربری)
└── docs/              ← ۳) بخش داکس
    ├── README.md
    ├── ABOUT.md
    ├── getting-started.md
    ├── architecture.md
    ├── conventions.md
    ├── api.md
    └── contributing.md
```
