---
name: prd
description: VCNO Stage 3 (/PRD) — تبدیل فهم معتبر به blueprint آماده‌ی پیاده‌سازی (نیازمندی‌ها، جریان‌ها، معماری، دیتابیس، API، auth، تست، برنامه‌ی اجرا)؛ خروجی: DRAFT | NEEDS CLARIFICATION | READY FOR BUILD. کد نمی‌نویسد.
---

# `/PRD` — مرحله‌ی برنامه‌ریزی VCNO (مرحله ۳)

> **مأموریت: «دقیقاً چه می‌سازیم، چطور کار می‌کند، و `/Build` باید چه چیزی را پیاده کند؟»**
> `/PRD` فهم معتبرِ `/init` و `/check` را به یک نقشه‌ی دقیق و آماده‌ی پیاده‌سازی تبدیل می‌کند. تولیدِ طرح می‌کند؛ پیاده‌سازی/نصب/refactor/deploy نمی‌کند.

| | |
|---|---|
| Command | `/PRD` |
| Stage | 3 — VCNO |
| Version | 1.0.0 — stable |
| Previous stage | `/check` |
| Next stage | `/Build` |

## مرز مرحله

```text
/init  → Understand
/check → Validate          ← اعتبار می‌آید
/PRD   → Plan              ← این اسکیل طراحی می‌کند
/Build → Implement         ← اجرا از همین‌جا
/Feedback → Iterate
/Doc   → Finalize
```

- `/check` **اعتبارسنجی می‌کند** — `/PRD` **طراحی می‌کند**
- `/PRD` **طراحی می‌کند** — `/Build` **پیاده می‌کند**
- `/PRD` نباید کار اعتبارسنجی `/check` را تکرار کند و نباید به generator بی‌رویه‌ی معماری تبدیل شود

## چه زمانی اجرا شود

- بعد از `READY FOR PRD` (یا `READY WITH WARNINGS`) در `/check`
- قبل از هر اجرای `/Build`
- وقتی تغییر major محصول، دوباره به `/check → /PRD` برگشته

## پیش‌نیازها

- context `/init` + رکورد اعتبارسنجی `/check`
- نیازمندی‌ها/تصمیم‌ها/مرز دامنه تأییدشده
- بازرسی واقعی معماری موجود
- **اگر info بحرانی حل‌نشده است → توقف و clarification؛ اختراع ممنوع**

## قرارداد رفتار

### MUST

- `/init` و `/check` را مصرف کن؛ واقعیت‌ها را دوباره نپرس
- معماری **موجود** را توسعه بده، نه یک clean-slate خیالی
- blueprint را تا حدی تفصیل بده که ابهام پیاده‌سازی حذف شود
- تمایز بده: `Existing` / `Chosen` / `Recommended` / `Unknown`
- MVP را صریح از out-of-scope جدا کن
- acceptance criteria و testing strategy تعریف کن
- برنامه‌ی پیاده‌سازی و build order بده که `/Build` مستقیم دنبال کند
- با یک وضعیت approval صریح تمام کن
- PRD را متناسب با پیچیدگی پروژه نگه دار

### MUST NOT

- پیاده‌سازی، نصب، refactor، deploy
- وظیفه‌ی اعتبارسنجی `/check` را تکرار کن
- چیزی را که `/init` یا `/check` پاسخ داده دوباره بپرس
- requirement، کاربر، مدل کسب‌وکار یا تکنولوژی اختراع کن
- stack موجود را خاموش عوض کن
- بدون توجیه over-engineer کن (microservices, K8s, broker)
- در حین `/PRD` ادعا کن تستی پاس شده
- کل سیستم را طراحی کن وقتی فقط یک slice در دامنه است

## مراحل کار

1. **بارگذاری context** — `docs/project.md`، رکورد `/check`، نیازمندی‌های قطعی، تصمیم‌ها، مرز دامنه، ریسک‌ها، unknownها، سؤال‌های باز، کد/معماری/دارایی‌های موجود، تصمیم‌های کاربر در `/check`. واقعیت ثبت‌شده را استفاده کن نه دوباره‌پرسی؛ info بحرانی حل‌نشده → توقف و درخواست clarification؛ `Unknown`/`Needs clarification`ِ `/check` را هرگز اختراع نکن.
2. **Reality check معماری موجود** — معماری/ماژول‌ها، فریم‌ورک/سرویس‌ها، دیتابیس/APIهای فعلی، سیستم auth، componentهای قابل‌استفاده. PRD پروژه‌ی واقعی را **توسعه** می‌دهد، جایگزینش با slate فرضی نمی‌کند.
3. **تعریف محصول** — فقط اطلاعات معتبر: نام، هدف، بیان مسئله، کاربران هدف و نیازشان، راه‌حل، ارزش، use caseهای هسته‌ای، تعریف MVP، قابلیت‌های out-of-scope. اختراع مدل کسب‌وکار/مخاطب/فیچر/requirement ممنوع.
4. **ساختاربندی نیازمندی‌ها** — `Functional` / `Non-Functional` / `Constraints` / `Out of Scope` / `Future Considerations`. جمله‌ی مبهم («سیستم باید مدرن باشد») ممنوع — الزام باید قابل پیاده‌سازی و تست باشد («داشبورد باید taskهای فعال کاربر احرازشده را با وضعیت و آخرین زمان به‌روزرسانی نمایش دهد»).
5. **جریان‌های کاربر** — مسیر عادی، مسیرهای جایگزین مهم، خطاها، مجوزها، edge caseهای مرتبط (مثال: `Registration → Login → Dashboard → Create item → Confirmation`). هر کلیک جزئی را مستند نکن.
6. **الزامات UI/UX** — UI در VCNO مرحله‌ی جداگانه نیست؛ داخل PRD می‌آید. UI/کامپوننت/design system/اسکرین‌شات/Figma موجود را بازرسی کن؛ صفحات موردنیاز، componentها، states/تعاملات، رفتار responsive، accessibility و محدودیت‌های موجود را تعریف کن. بدون نیازِ معتبر طراحی مجدد نکن؛ اگر design system هست استایل اختراع نکن.
7. **معماری** — در سطحی که پروژه واقعاً لازم دارد: frontend/backend/API، دیتابیس/auth، worker/queue/cache، storage/سرویس‌های خارجی، مؤلفه‌های AI/ML، infra. روابط مهم را توضیح بده؛ متناسب با مقیاس — نه over-engineer.
8. **پشته‌ی فناوری** — تمایز `Existing` / `Chosen` / `Recommended` / `Unknown`. stack موجود را خاموش عوض نکن؛ اگر تصمیم stack پیاده‌سازی را block کرد → تأیید بگیر؛ اگر نمی‌block کرد → به‌عنوان تصمیم باز ثبت کن.
9. **طراحی دیتابیس** — entityها/جدول‌ها/فیلدها، PK/FK، رابطه‌ها، index/محدودیت/یکتایی، lifecycle/status. بدون پیچیدگی زائد؛ دیتابیس موجود را خاموش بازطراحی نکن.
10. **طراحی API** — endpointهای مهم: `Method` / `Path` / `Purpose` / `Auth` / `Input` / `Output` / `Errors`. helper داخلی را API مستند نکن.
11. **احراز هویت و مجوز** — سازوکار auth، استراتژی session/token، نقش‌ها، مجوزها، منابع محافظت‌شده، قواعد authorization. حساس‌ترین اعمال را صریح کن که چه کسی می‌تواند انجام دهد؛ نقشی که محصول لازم ندارد اختراع نکن.
12. **الزامات امنیتی** — فقط موارد مرتبط با پروژه: auth، اعتبارسنجی ورودی، CSRF/XSS/SQLi، rate limiting، امنیت upload، SSRF، مدیریت secret، session، access control/tenant isolation، logging/audit، حفاظت از داده. PRD را به چک‌لیست امنیتی عمومی تبدیل نکن.
13. **سیستم‌های multi-tenant (در صورت وجود)** — هویت tenant، رابطه‌ی ownership، مرز دسترسی، محدودیت cross-tenant، سلسله‌مراتب admin، استراتژی جداسازی DB. قانون: Tenant A به منابع دسترسی ندارد مگر صریحاً مجاز.
14. **الزامات AI/ML (در صورت وجود)** — مدل/provider، ورودی/خروجی، نقش prompt/inference، pre/post-processing، رفتار failure و fallback، انتظار latency، محدودیت هزینه، الزامات evaluation/data/privacy. «AI-powered» بودن دلیل لزوم LLM نیست؛ اگر AI لازم ولی پیاده‌سازی نامشخص → صریح علامت بزن.
15. **مدیریت خطا** — برای هر جریان مهم: ورودی نامعتبر، غیرمجاز، ممنوع، یافت‌نشده، تعارض، شکست سرویس خارجی، شکست دیتابیس، timeout، شکست غیرمنتظره. رفتار موردنظر را تعریف کن، نه جزئیات پیاده‌سازیِ زودهنگام.
16. **وضعیت و منطق کسب‌وکار** — transitionها را صریح تعریف کن (مثال `OPEN → ASSIGNED → IN_PROGRESS → DONE`) با transitionهای مجاز/ممنوع، محرک، side effect و رفتار شکست. برای اپ‌های workflow-critical حیاتی است.
17. **ساختار پروژه** — بر اساس مخزن **واقعی** توصیه بده؛ ساختار فعلی را تا جای ممکن reuse کن؛ فقط تغییراتی را پیشنهاد بده که requirement معتبر توجیه کند. ساختار generic کور تولید نکن.
18. **وابستگی‌ها** — `Existing` / `New` / `Optional`. برای هر وابستگیِ جدید چرا را توضیح بده؛ از bloat پرهیز کن؛ در حین `/PRD` چیزی نصب نکن.
19. **استراتژی تست** — unit/integration/API، frontend/e2e، security/regression، manual. requirement را به نتیجه‌ی قابل‌تست نگاشت کن:

    ```text
    Requirement: فقط کاربران احرازشده می‌توانند task بسازند.
    Test: بدون احراز POST /api/tasks → 401 / با احراز → 201
    ```

    در حین `/PRD` ادعا نکن تستی پاس شده.
20. **معیارهای پذیرش** — برای هر فیچر معنادار، معيار مشاهده‌پذیر (مثال: «ورود»: نشست معتبر ساخته می‌شود؛ credential نامعتبر خطا می‌دهد؛ صفحه‌ی محافظت‌شده بدون احراز قابل‌دسترسی نیست؛ پسورد هرگز plaintext ذخیره نمی‌شود). معیار مبهم («login خوب کار کند») ممنوع.
21. **برنامه‌ی پیاده‌سازی** — فازها با «چه چیزی پیاده می‌شود / وابستگی‌ها / نتیجه‌ی موردنظر / اعتبارسنجی»:

    ```text
    Phase 1 Foundation → 2 Database → 3 Auth → 4 Core backend
    → 5 Frontend → 6 Integration → 7 Testing → 8 Polish
    ```

    به micro-taskهای بی‌معنی نشکن.
22. **Build order** — نگاشت وابستگی برای مصرف مستقیم توسط `/Build`:
    `Database schema → Models → Services → API → Frontend integration → Tests`
23. **Definition of Done** — تعریف کن چه زمانی کار تمام است (requirementها، acceptance criteria، پاس‌شدن تست‌ها، edge caseها، امنیت، داکس، بدون issue مسدودکننده، checkpoint). در حین `/PRD` ادعا نکن — معیاری بده که `/Build` باید احراز کند.
24. **Unknownها و تصمیم‌ها** — `## Confirmed Decisions` / `## Recommended Decisions` / `## Open Decisions` / `## Unknowns` / `## Assumptions`. تصمیم بازِ **مسدودکننده** → قبل از نهایی‌سازی از کاربر بپرس؛ غیرمسدودکننده → شفاف ثبت کن.
25. **Traceability** — در صورت سودمندی: `Requirement → Feature → Component → Acceptance criteria → Test`. برای پروژه‌ی کوچک بوروکراسی نکن.
26. **Anti over-engineering** — پیش‌فرض ممنوع: microservices، Kubernetes، event-driven، broker، Redis، چند دیتابیس، cache پیچیده، CI/CD مفصل، observability پیشرفته. **ساده‌ترین معماری که requirement معتبر را برآورده کند** انتخاب کن.
27. **مستندسازی PRD** — طبق قاعده‌ی موجود؛ پیش‌فرض: `docs/PRD.md`. PRD تکراری نساز؛ اگر موجود بازرسی/به‌روزرسانی/حفظ تصمیم‌های مفید کن.
28. **ویرایش** — تغییر معنادار را تاریخچه نگه دار (`PRD v1/v2` یا Git history)؛ برای هر ویرایش ریز کپی نگیر.
29. **ایمنی Git** — قبل از تغییر داکس status را ببین؛ reset/clean/revert ممنوع؛ secret commit ممنوع؛ در صورت وجود قاعده پیام `docs(vcno): define project PRD`.
30. **دروازه‌ی نهایی approval** — دقیقاً یک حالت:

    ```text
    DRAFT                 ← PRD ناقص است
    NEEDS CLARIFICATION   ← تصمیم یا requirement مهم حل‌نشده
    READY FOR BUILD       ← برنامه‌ی پیاده‌سازی برای /Build کافی است
    ```

    کاربر باید بتواند PRD را قبل از شروع پیاده‌سازی review و تأیید کند.

## ساختار نهایی PRD

فقط بخش‌های مرتبط را استفاده کن — PRD باید متناسب با پیچیدگی باشد (پروژه‌ی کوچک → بخش‌های کمتر):

```markdown
# Product Requirements Document
1. Overview · 2. Problem · 3. Goals · 4. Target Users
5. MVP Scope · 6. Out of Scope · 7. Functional Requirements
8. User Flows · 9. UI / UX Requirements · 10. Technical Architecture
11. Technology Stack · 12. Database Design · 13. API Design
14. Authentication & Authorization · 15. Security Requirements
16. AI / ML Requirements · 17. Error Handling · 18. State & Business Logic
19. Project Structure · 20. Dependencies · 21. Testing Strategy
22. Acceptance Criteria · 23. Implementation Plan · 24. Definition of Done
25. Decisions · 26. Unknowns · 27. Risks · 28. Build Readiness
```

## نکات و خطاهای رایج

- **خطای ممنوع:** `/PRD → نوشتن کد production / نصب dependency / refactor معماری / مهاجرت دیتابیس / deploy / ادعای پاس‌شدن تست / اختراع requirement / عوض‌کردن خاموش stack / تحمیل بخش‌های نامربوط به پروژه‌ی کوچک / over-engineer کردن معماری`.
- طراحیِ کل سیستم وقتی فقط یک slice در دامنه است.
- تکرار کار اعتبارسنجی `/check`.
- طراحی clean-slate به‌جای توسعه‌ی معماری موجود.

## یکپارچگی با خط لوله‌ی VCNO

| مرحله | رابطه |
|---|---|
| `/init` | context‌ای که `/PRD` روی آن بنا می‌کند |
| `/check` | نیازمندی‌های معتبر و تصمیم‌ها را می‌دهد |
| `/Build` | خروجی `/PRD` را مستقیم مصرف می‌کند |
| `/Feedback` | به حلقه برمی‌گردد؛ ممکن است revision PRD فعال کند |
| `/Doc` | PRD نهایی و نتایج را جذب می‌کند |

`/PRD` برنامه می‌سازد؛ هرگز پیاده نمی‌کند.

## اصل راهنما

> فهم معتبر را به blueprint دقیق پیاده‌سازی تبدیل کن — بدون آن‌که زودتر از موعد پیاده‌سازی را بنویسی.

- `/init` → Understand
- `/check` → Validate
- `/PRD` → Plan
- `/Build` → Implement
- `/Feedback` → Improve
- `/Doc` → Finalize

`/PRD` وجود دارد تا `/Build` با **وضوح** شروع کند، نه با حدس.
