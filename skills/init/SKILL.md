---
name: init
description: VCNO Stage 1 (/init) — بازرسانی مخزن و ساخت context مستند (docs/project.md + docs/logs/init.md) بدون دست‌زدن به کد؛ برای شروع پروژه‌ی جدید، ورود کدِ موجود به VCNO، و آماده‌سازی context قبل از /check.
---

# `/init` — نقطه‌ی ورود گردش‌کار VCNO (مرحله ۱)

> **مأموریت: Understand before changing.**
> این اسکیل فقط context جمع می‌کند؛ هرگز پیاده‌سازی نمی‌کند. خروجی آن «مبنای حقیقت» (Source of Truth) برای `/check`، `/PRD`، `/Build`، `/Feedback` و `/Doc` است.

| | |
|---|---|
| Command | `/init` |
| Stage | 1 — VCNO |
| Version | 1.0.0 — stable |
| Next stage | `/check` |

## چه زمانی اجرا شود

- شروع پروژه‌ی جدید از روی ایده
- ورود یک کدِ موجود به VCNO (onboarding)
- باز-مقداری‌ابی بعد از تغییرات بزرگ پروژه
- آماده‌سازی context قبل از اجرای `/check`

## پیش‌نیازها

- دسترسی خواندنی به مخزن (Git اختیاری است؛ نبودش خطا نیست)
- ورودی زبان طبیعی کاربر (توضیح مختصر پروژه) — اگر نبود، سؤال‌های «مرحله ۷» را بپرس
- **هیچ ابزار یا dependency‌ای نباید نصب شود**

## قرارداد رفتار

### MUST

- قبل از نوشتن هر چیزی، ابتدا مخزن را بازرسی کن
- فقط بر اساس شاهدِ مشاهده‌پذیر stack، دارایی‌ها، داکس و ساختار را تشخیص بده
- وضعیت هر یافته را صریحاً یکی از این ۴ تا انتخاب کن: `Confirmed` / `Inferred` / `Unknown` / `Needs clarification`
- اگر ساختار داکس مناسب موجود است، همان را گسترش بده (نسخه‌ی تکراری نساز)
- یک لاگ راه‌اندازی (init log) ثبت کن
- همه‌ی کارهای موجود، وضعیت Git و secretها را دست‌نخورده نگه دار
- در پایان، وضعیت VCNO را شفاف گزارش کن

### MUST NOT

- فایل کاربر را حذف یا overwrite نکن
- Git را reset نکن / کار commit‌نشده را دور نریز
- وابستگی (dependency) نصب نکن
- کد، ساختار یا پروژه را تغییر/بازآرایی نکن
- تکنولوژی، فیچر یا requirement اختراع نکن
- secret را در هیچ سندی کپی نکن
- تغییرات نامرتبط را auto-commit نکن
- شروع به ساخت پروژه نکن

## مراحل کار

1. **بازرسی مخزن** — root (عمق ۲–۳)، `README*`/`LICENSE`/`CHANGELOG*`، پوشه‌های داکس (`docs/`, `doc/`)، manifestها (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, ...)، کانفیگ (`*.config.*`, `.env.example`, Docker, Makefile)، بالای درخت source (`src/`, `app/`, `lib/`)، تست‌ها، assetها، مایگریشن‌های دیتابیس، CI. در مخزن بزرگ **همه‌ی فایل‌ها را نخوان** — یک مدل ذهنی بساز، dump نکن.
2. **کشف داکس** — جست‌وجوی `README*`, `docs/`, `doc/`, `documentation/`, `*.md(x)`. مناسب موجود → ادغام؛ ناقص → تکمیل (نه جایگزینی)؛ هیچ → ساختار حداقلی (مرحله ۸). داکِ نوشته‌شده توسط کاربر را هرگز overwrite نکن.
3. **بازرسی Git** — branch، وضعیت working tree (clean/dirty)، `git log --oneline -10`، remotes (فقط نام‌ها، نه credential). هرگز reset/stash/discard نکن.
4. **تشخیص stack** — فقط مشاهده‌پذیرها را گزارش کن و برای هر مورد **فایل شاهد** را بنویس؛ ناشناخته‌ها را `Unknown` و حدس‌های پرریسک را `Needs clarification` علامت بزن. هرگز تکنولوژی اختراع نکن:

   ```yaml
   Language:   Python 3.11 (pyproject.toml)
   Backend:    FastAPI
   Frontend:   React 18 + Vite
   Database:   PostgreSQL (docker-compose.yml)
   Testing:    Pytest
   CI:         Unknown
   Deploy:     Needs clarification
   ```

5. **تشخیص دارایی‌ها** — entry pointهای کد، لوگو/عکس/اسکرین‌شات، لینک‌های Figma در داکس یا کامنت، پیاده‌سازی‌های UI، PDF و spec sheet، مستندات API (OpenAPI, Postman, `.http`)، schema دیتابیس، PRD/спec/briefهای قبلی، کانفیگ‌های معنادار. **فقط ثبت — نه تغییر.**
6. **ورودی زبان طبیعی** — توضیح ساده‌ی کاربر را به context ساختارمند تبدیل کن (ورودی voice هم مثل متن عادی):

   ```text
   Problem:     Shop owners cannot interpret customer intent from messages
   Users:       Small/medium shop owners
   Solution:    Message analysis to surface purchase friction
   Status:      Concept
   ```

7. **سؤال‌ها (فقط در صورت لزوم)** — حداقل سؤال‌هایی که درک را جدی تحت‌تأثیر قرار می‌دهند؛ پیش‌فرض:

   1. دقیقاً چه می‌سازی؟ (یکی دو جمله)
   2. کاربر اصلی کیست؟
   3. چه مشکلی را حل می‌کند؟

   اگر مخزن + ورودی کاربر پاسخ را دارند، مزاحم نشو — پرسشنامه ننویس.

8. **ساخت `docs/project.md`** — فقط اگر ساختار مناسبی نیست، حداقلی بساز (پوشه‌ی خالی و placeholder نساز؛ `research/`, `roadmap/` را دلبخواهی نساز؛ اگر ساختار موجود هست، در جای خودش گسترش بده):

   ```text
   docs/
   ├── project.md
   ├── context/      # فقط در صورت نیاز
   ├── decisions/    # فقط در صورت نیاز
   ├── logs/
   └── feedback/     # فقط در صورت نیاز
   ```

   بخش‌های الزامی `docs/project.md`:

   ```markdown
   # Project
   ## Identity          (Name / Type / Purpose)
   ## Problem & Solution (Problem / Proposed solution / Target users)
   ## Status            (Current status / Existing features / Planned features)
   ## Technology        (Stack with evidence / Architecture high level)
   ## Assets            (Existing inputs and where they live)
   ## Constraints       (Known limitations)
   ## Decisions         (Important prior decisions)
   ## Uncertainty       (Confirmed / Inferred / Unknown / Needs clarification)
   ## VCNO              (Workflow status)
   ```

   بخش خالی با `Unknown` قابل قبول است؛ **چیزی اختراع نکن.**

9. **ساخت `docs/logs/init.md`** — زمان، وضعیت initialization، مسیرهای بازرسی‌شده، stack تشخیص‌داده‌شده، داکس/دارایی‌های موجود، فایل‌های ساخته/به‌روزرسانی‌شده، مشاهدات، سؤال‌های باز، `Next stage: /check`. واقعی و بدون filler.
10. **Git checkpoint (اختیاری)** — فقط اگر Git موجود **و** working tree از قبل clean بود: commit فقط-داکس با پیام `docs(vcno): initialize project context`. اگر dirty بود: داکس‌ها را commit نکن و این را صریح گزارش کن. هرگز secret یا فایل موقت را commit نکن.
11. **گزارش وضعیت** — دقیقاً یکی از سه حالت نهایی:
    - `INIT_STATUS = INIT_COMPLETED` → آماده‌ی `/check`
    - `INIT_STATUS = PARTIAL` → بخشی از context ناقص است ولی `/check` می‌تواند با caveat ادامه دهد
    - `INIT_STATUS = NEEDS_INPUT` → کاربر باید اطلاعات غایب را بدهد

    هرگز موفقیت دروغین گزارش نکن.

## خروجی مورد انتظار

- **فایل‌هایی که باید ساخته/به‌روز شوند:** فقط `docs/project.md` و `docs/logs/init.md` (+ گسترش ساختار داکس موجود در صورت نیاز). هیچ فایل کدی.
- **پیام نهایی به کاربر:**

  ```md
  ## Project
  <what was detected>

  ## Detected
  <stack, structure, assets>

  ## Existing Work
  <docs, code, assets already present>

  ## Documentation
  <files created or updated>

  ## Unknown / Needs Clarification
  <list>

  ## Git
  <branch, tree state, checkpoint info>

  ## Next Step
  Initialization completed. Next step: /check
  ```

  و اگر ناقص بود:

  ```md
  ## Next Step
  Initialization needs input. Before /check, please provide:
  - <question 1>
  - <question 2>
  ```

## سیاست secretها

هرگز در هیچ سندی ثبت نکن: API key، password، token، private key، credential دیتابیس، session secret. برای env var فقط این الگو:

```yaml
DATABASE_URL:
  Purpose: database connection
  Source:  environment variable
  Value:   not documented
```

## نکات و خطاهای رایج

- **خطای ممنوع (anti-pattern):** `/init → تولید کد / نصب dependency / بازآرایی پروژه / فرض کردن requirements / شروع ساخت`.
- خواندن کل فایل‌های مخزن بزرگ — به ترتیب اولویتِ مرحله ۱ برو، نه همه‌جا.
- جایگزین‌کردن داکِ موجود — ادغام یا تکمیل کن، overwrite نکن.
- اگر working tree dirty بود، هرگز commit نزن.
- اگر جواب سؤال‌های بحرانی را نداری، `INIT_COMPLETED` گزارش نکن — `NEEDS_INPUT` بده.

## یکپارچگی با خط لوله‌ی VCNO

| مرحله | از `/init` مصرف می‌کند |
|---|---|
| `/check` | `docs/project.md`، unknownها، assumptions |
| `/PRD` | context تأییدشده، کاربران هدف، مسئله |
| `/Build` | stack، محدودیت‌ها، دارایی‌های موجود |
| `/Feedback` | تصمیم‌های مهم، سؤال‌های باز |
| `/Doc` | ساختار داکس موجود |

`/init` با هیچ مرحله‌ی بعدی تضاد ندارد — فقط context آماده می‌کند.
