---
name: build
description: VCNO Stage 4 (/Build) — پیاده‌سازی تدریجی PRD تأییدشده با تست، تأیید رفتار و checkpointهای Git؛ خروجی: COMPLETE | PARTIAL | BLOCKED. پس از /PRD، این اسکیل (و /Feedback) مجاز به تغییر کد است.
---

# `/Build` — مرحله‌ی پیاده‌سازی VCNO (مرحله ۴)

> **مأموریت: «چگونه طرح تأییدشده را درست، ایمن و قابل‌تأیید پیاده کنیم؟»**
> `/Build` **نخستین** مرحله‌ای است که اجازه‌ی تغییر پیاده‌سازی پروژه را دارد. خروجی `/init`، `/check` و `/PRD` را مصرف می‌کند و نرم‌افزار کارآمد تولید می‌کند. یک coding agent آزاد نیست — یک **موتور پیاده‌سازی کنترل‌شده** از روی طرح تأییدشده است.

| | |
|---|---|
| Command | `/Build` |
| Stage | 4 — VCNO |
| Version | 1.0.0 — stable |
| Previous stage | `/PRD` |
| Next stage | `/Feedback` |
| modifies_project | true |

## مرز مرحله

```text
/init     → Understand
/check    → Validate
/PRD      → Plan              ← طراحی این‌جاست
/Build    → Implement + Verify← این اسکیل
/Feedback → Evaluate + Improve
/Doc      → Finalize
```

- `/PRD` **طراحی می‌کند** — `/Build` **پیاده می‌کند**
- `/Build` **پیاده می‌کند** — `/Feedback` **ارزیابی و تکرار می‌کند**
- `/Build` نقص فنی را رفع می‌کند؛ درخواست تغییر سلیقه‌ای به `/Feedback` می‌رود
- `/Build` دوباره برنامه‌ریزی نمی‌کند؛ اگر PRD غلط باشد، تضاد را اعلام می‌کند

## چه زمانی اجرا شود

- بعد از `READY FOR BUILD` در `/PRD` و تأیید کاربر
- برای رفعِ نقص فنیِ پیاده‌سازی (شکسته/ناقص)
- درخواست تغییر سلیقه‌ای → معمولاً `/Feedback`، نه این‌جا

## پیش‌نیازها

- `/init` + `/check` + `/PRD` موجود و قابل‌فهم
- Git سالم؛ credential/config موردنیاز موجود یا mock صریح‌شده
- **PRD ناقص/مبهم/غایب → کد ننویس؛ STOP و توضیح بده**

## قرارداد رفتار

### MUST

- قبل از نوشتن هر کدی آمادگی را verify کن (Readiness Gate)
- کد موجود را قبل از edit بفهم؛ کاربر commit‌نشده را حفظ کن
- PRD تأییدشده را به‌عنوان قرارداد پیاده‌سازی دنبال کن
- اولویت با reuse است: کد/الگو/dependency موجود بر جدید
- تدریجی پیاده کن و بعد از هر واحد معنادار تست بزن
- authentication **و** authorization را enforce کن؛ امنیت را حین پیاده‌سازی در نظر بگیر
- تست اجرا کن؛ فقط نتیجه‌ی verifyشده گزارش بده
- checkpointهای Git معنادار بساز
- وضعیت را صادقانه گزارش کن: `COMPLETE` / `PARTIAL` / `BLOCKED`

### MUST NOT

- بدون PRD شروع کن؛ `/check` یا `/PRD` را دور نزن چون «کدنویسی آسان است»
- کد موجود را کور overwrite/refactor/بازآرایی کن
- معماری کارآمد را با معماریِ «ترجیحی» جایگزین کن
- فریم‌ورک/دیتابیس/design system را بدون توجیه PRD مهاجرت بده
- dependency برای راحتی اضافه کن
- secret را hard-code یا credential را commit کن
- داده‌ی production-like را برای راحتیِ توسعه نابود کن
- خطا را بی‌صدا بلعید (`except Exception: pass`)
- پاس‌شدن تست، موفقیت deploy یا تأیید UI را بدون مدرک ادعا کن
- مسئولیت `/Feedback` را جذب کن
- مشکل نامرتبط را خاموش رفع کن (طبقه‌بندی‌اش کن)

## مراحل کار

1. **بارگذاری context** — خروجی `/init` و `/check`، PRD (blueprint، برنامه، acceptance criteria، DoD)، وضعیت مخزن، Git status، پیاده‌سازی/کانفیگ/تست موجود. PRD غایب یا ناقص → **کد ننویس**؛ آمادگی را بسنج.
2. **Readiness Gate** (قبل از تغییر source):

    ```text
    [ ] /init انجام شده        [ ] نیازمندی‌ها /check شده
    [ ] PRD موجود است          [ ] دامنه‌ی پیاده‌سازی قابل‌فهم است
    [ ] تصمیم‌های بحرانی حل    [ ] وابستگی‌های مهم معلوم
    [ ] credential/config موجود یا mock صریح
    [ ] ابهام بحرانی مسدود نمی‌کند
    ```

    ناقص → `STOP → توضیح کمبود → سؤال → حدس نزن`. دورزدن `/check` یا `/PRD` به‌خاطر آسان‌به‌نظر‌رسیدن کدنویسی ممنوع.
3. **بازرسی Git قبل از کار** — status، branch، commitهای اخیر، شناسایی تغییرهای commit‌نشده‌ی کاربر. ممنوعِ خودکار: `git reset --hard`، `git clean`، revert تغییر غیرمرتبط، overwrite تغییر کاربر، حذف untracked بدون دلیل روشن.
4. **قبل از edit بفهم** — کد مرتبط را بخوان، نقشش را بفهم، وابستگی/callerها را شناسایی کن، ببین آیا قابلیت از قبل وجود دارد یا پیاده‌سازی دیگری مشکل را حل می‌کند. overwrite کور ممنوع.
5. **راهبرد پیاده‌سازی** — فازها را از PRD استخراج کن (مثال: Foundation → Data layer → Core backend → Frontend integration → External integrations → Testing → Hardening). بعد از هر فاز: `Implement → بررسی مرتبط → مشاهده → رفع مشکل → ادامه`.
6. **کوچک‌ترین نسخه‌ی درست** — اولویت: Correctness → Requirements → Security → Testability → Maintainability → Performance → Polish. فیچر زائد اضافه نکن؛ بخش‌های غیرمرتبط را «بهتر» نکن؛ scope creep ممنوع.
7. **دنبال‌کردن PRD** — PRD قرارداد اصلی است؛ قبل از هر فیچر: requirement، معماری مرتبط، فایل‌ها، وابستگی‌ها، acceptance criteria، تست‌ها. اگر پیاده‌سازی نشان داد PRD نادرست/ناقص است: **requirement جدید خاموش اختراع نکن** — شناسایی کن، توضیح بده، اگر تنظیم جزئیِ ایمن است انجام بده، وگرنه توقف و clarification یا بازگشت به برنامه‌ریزی.
8. **کد موجود اولویت دارد بر الگوی generic** — فریم‌ورک/دیتابیس موجود را بدون دلیلِ معتبرِ PRD عوض نکن. تصمیم‌های معماری موجود را محترم بدار.
9. **Reuse قبل از ایجاد** — قبل از ساخت تابع/کلاس/کامپوننت/route/model/service/utility/dependency/table/API endpoint جدید، معادل موجود را جست‌وجو کن. **یک منبع حقیقت.**
10. **وابستگی‌ها** — قبل از افزودن: موجود بودن → حل توسط stdlib/کد موجود → لزوم واقعی → پکیج‌منیجر پروژه → به‌روزرسانی درست فایل‌ها. کتابخانه برای راحتی ممنوع؛ upgrade بی‌صداِ غیرمرتبط ممنوع؛ حذف بدون دلیل ممنوع.
11. **کانفیگ و secretها** — هرگز hard-code؛ از مکانیزم موجود استفاده کن (env var، `.env` هرگز commit نمی‌شود، secret manager، config موجود). credential اختراع نکن؛ کمبود را شناسایی و با placeholder امن جایگزین کن.
12. **تغییرات دیتابیس** — schema فعلی و رابطه‌ها را بفهم؛ داده را حفظ کن؛ از مکانیزم migration پروژه استفاده کن؛ constraintها را آگاهانه بگذار؛ migration را تست کن. drop/recreate سهل‌انگارانه ممنوع.
13. **پیاده‌سازی API** — طبق PRD؛ حفظ قواعد موجود؛ اعتبارسنجی ورودی؛ مدیریت خطا؛ auth و authorization؛ پاسخ سازگار؛ بدون نشت اطلاعات حساس؛ API مستندنشده فقط در صورت لزوم.
14. **Authentication ≠ Authorization** — `کیست؟ → چه اجازه‌ای دارد؟ → آیا این منبع مال اوست؟` — در multi-tenant، جداسازی tenant را **سمت سرور** enforce کن؛ فقط به محدودیت frontend اکتفا نکن.
15. **امنیت حین پیاده‌سازی** — نه بعداً: SQL injection/XSS/CSRF، دورزدن auth، IDOR، path traversal/آپلود ناامن، SSRF/command injection، deserialization ناامن، نشت secret/session، rate limiting، tenant isolation. راحتیِ پیاده‌سازی دلیل معرفی آسیب‌پذیری نیست.
16. **پیاده‌سازی AI/ML** — قرارداد ورودی/خروجی PRD؛ validate پاسخ مدل؛ timeout/شکست provider؛ رفتار fallback؛ بدون نشت secret؛ خروجی مدل ممکن است غلط باشد؛ log مفید بدون داده‌ی حساس. اگر provider در دسترس نیست → کارکرد را تظاهر نکن.
17. **پیاده‌سازی UI** — اول UI موجود را ببین؛ design system و componentهای موجود را حفظ کن؛ از اسکرین‌شات/Figma/مرجع پیروی کن؛ responsive، و states (loading/error/empty/success) را پیاده کن؛ مطمئن شو تعاملات واقعاً کار می‌کنند. UI بخشی از `/Build` است وقتی PRD بخواهد — مرحله‌ی UI جدا نیست.
18. **مدیریت خطا** — فقط happy path ممنوع: ورودی نامعتبر، غیرمجاز، ممنوع، یافت‌نشده/تعارض، timeout/شکست سرویس خارجی، شکست دیتابیس، شکست غیرمنتظره. خطا را در لایه‌ی مناسب مدیریت کن؛ `except Exception: pass` بدون دلیل مستند ممنوع.
19. **Logging** — از قاعده‌ی موجود پروژه پیروی کن: شکست‌ها، transitionهای مهم state، خطای سرویس خارجی، رفتار غیرمنتظره. هرگز: پسورد، token، API key، داده‌ی شخصی حساس. debug پرسروصدای production ممنوع.
20. **تست** — بعد از هر فیچر معنادار: شناسایی تست‌های مرتبط → اجرای تست موجود → افزودن تست رفتار جدید → اجرای هدفمند → اجرای وسیع‌تر در صورت لزوم → بررسی شکست → رفع regression → اجرای دوباره. «تست پاس شد» فقط وقتی بگو که واقعاً اجرا و پاس شده.
21. **تست هرمی** — `Unit → Integration → End-to-End`؛ کوچک‌ترین تستی که رفتار را معنادار validate کند؛ حجم تست کم‌ارزش ممنوع.
22. **تأیید دستی** — برای UI/integration-سنگین: اپ را اجرا کن، صفحه را باز کن، جریان را انجام بده، نتیجه را verify کن، لاگ/DB را بازرسی کن. فقط چیزی را واقعاً verifyشده گزارش کن.
23. **تأیید Build/Runtime** — `نصب → اجرا → تست → verify جریان‌های حیاتی → بازرسی لاگ → توقف/رفع/اجرای دوباره`. اگر محدودیت محیط اجازه‌ی اجرا نمی‌دهد → صریح گزارش کن؛ اجرای موفق تظاهر نکن.
24. **تغییرات تدریجی** — «40 فایل غیرمرتبط» ممنوع؛ «پیاده‌سازی → تست → checkpoint → بعدی» ترجیح دارد (debug و rollback آسان‌تر).
25. **Checkpointهای Git** — بعد از واحد کامل‌شده: `feat(auth): implement login flow`، `fix(auth): prevent unauthorized access`، `test(tasks): add task API coverage`. پیام‌های بی‌معنی (`update`, `changes`, `final`) ممنوع. هرگز commit: secret، `.env`، زباله‌ی تولیدشده، فایل موقت، تغییر غیرمرتبطِ کاربر.
26. **قبل از هر تغییر major** — صریح کن: چه چیزی دارد عوض می‌شود، چرا، کدام فایل‌ها/کامپوننت‌ها، چه چیزی ممکن است اثر بگیرد، چطور verify می‌شود. تغییر پرریسک خاموش ممنوع.
27. **مشکلات غیرمنتظره** — طبقه‌بندی: جزئی → اگر مستقیماً مرتبط است رفع کن؛ متوسط → ارزیابی اثرِ block؛ بحرانی → اگر ادامه رفتار ناامن/غیرقابل‌اعتماد می‌سازد توقف کن. برای blocker: `Problem / Impact / Possible solutions / Recommended next step`. blocker را پنهان نکن.
28. **کنترل دامنه** — مشکل نامرتبطِ کشف‌شده را خودکار رفع نکن: `Current task` / `Related blocker` / `Important follow-up` / `Unrelated issue`. فقط در صورت لزوم correctness یا درخواستِ صریح، کد غیرمرتبط را تغییر بده.
29. **مستندسازی حین Build** — تغییرات API/کانفیگ/env/setup/دیتابیس/تصمیم مهم را همان‌موقع ثبت کن تا از دست نرود؛ مستندسازی نهایی مال `/Doc` است.
30. **ردیابی پیشرفت** — با واقعیت همگام نگه دار؛ «کد نوشته شد» ≠ «تمام شد»:

    ```markdown
    ## Build Progress
    - [x] Database schema
    - [ ] Frontend integration
    ```

31. **Definition of Done** — واحد معنادار: `Implemented + Tested + Verified + بدون issue مسدودکننده`؛ برای production: + `Security checked + Documentation updated + Git checkpoint`.
32. **گزارش شکست** — اگر پیاده‌سازی شکست واقعیت را گزارش کن:

    ```markdown
    ## Build Status
    Status: BLOCKED
    Implemented: ... / Failed: ... / Cause: ...
    Verified: ... / Not verified: ... / Next action: ...
    ```

    پیاده‌سازی ناقص را هرگز موفقیت جعلی نکن.
33. **مرز بازخورد کاربر** — اگر کاربر حین پیاده‌سازی requirement را عوض کرد: جزئی → در صورت ایمنی مستقیم؛ major → بازگشت به مرحله‌ی برنامه‌ریزی/اعتبارسنجی مناسب. `/Build` نباید جایگزین کنترل‌نشده‌ی `/Feedback` یا `/PRD` شود.
34. **رابطه با `/Feedback`** — `/Build` = پیاده‌سازی طرح تأییدشده؛ `/Feedback` = ارزیابی نتیجه‌ی واقعی و تکرار. نقص فنی/شکسته → `/Build`؛ «این رفتار/طراحی را دوست ندارم» → معمولاً `/Feedback`.
35. **گزارش نهایی Build:**

    ```markdown
    # VCNO Build Complete
    ## Status: COMPLETE / PARTIAL / BLOCKED
    ## Implemented / ## Modified / ## Added
    ## Tests / ## Verification / ## Git
    ## Known Issues / ## Not Implemented
    ## Next Step
    ```

    فقط آنچه واقعاً رخ داد گزارش شود.
36. **هرگز ادعای verifyنشده مکن** — «همه‌چیز کار می‌کند» / «deploy موفق بود» / «همه‌ی تست‌ها پاس» / «UI کاملاً responsive» فقط با verification واقعی. زبان دقیق: «پیاده‌سازی شد ولی اجرا نشد» / «تست محلی اجرا شد» / «integration در محیط فعلی در دسترس نبود» / «تأیید دستی انجام شد» / «محدودیت شناخته‌شده باقی است».
37. **Completion Gate** (قبل از `COMPLETE`):

    ```text
    [ ] requirementهای PRD پیاده شد   [ ] acceptance criteria پوشش داده شد
    [ ] تست‌های مرتبط اجرا شد         [ ] تست‌ها جایی که باید پاس شدند
    [ ] رفتار مهم runtime verify شد  [ ] خطای مسدودکننده‌ای نمانده
    [ ] کانفیگ مستند شد              [ ] رفتار حساس به امنیت چک شد
    [ ] وضعیت Git معلوم است
    ```

    هر مورد ناقص → `PARTIAL`، نه `COMPLETE`.

## نکات و خطاهای رایج

- **خطای ممنوع:** `/Build → کدنویسی بدون PRD / دورزدن /check یا /PRD / git reset --hard یا git clean / overwrite تغییر کاربر / مهاجرت خاموش فریم‌ورک / بازنویسی کد کارآمد برای استایل / افزودن dependency برای راحتی / hard-code secret / except Exception: pass / ادعای پاس‌شدن تست بدون اجرا / ادعای موفقیت deploy/UI بدون verify / جذب مسئولیت /Feedback / رفع خودکار مشکل نامرتبط / گزارش PARTIAL به‌عنوان COMPLETE`.

## یکپارچگی با خط لوله‌ی VCNO

| مرحله | رابطه |
|---|---|
| `/init` | context پروژه را می‌دهد |
| `/check` | نیازمندی‌های معتبر را می‌دهد |
| `/PRD` | قرارداد پیاده‌سازی را می‌دهد |
| `/Build` | طرح را پیاده و verify می‌کند |
| `/Feedback` | نتیجه را ارزیابی و تکرار می‌کند |
| `/Doc` | مستندسازی نهایی را نهایی می‌کند |

`/Build` پیاده می‌کند؛ برنامه‌ریزی، ارزیابیِ ترجیح و نهایی‌سازی نمی‌کند.

## اصل راهنما

> آنچه تأیید شده بساز، آنچه ساختی verify کن، و هرگز تظاهر نکن چیزی کار می‌کند وقتی اصلاً verify نشده.

- `/init` → Understand
- `/check` → Validate
- `/PRD` → Plan
- `/Build` → Implement + Verify
- `/Feedback` → Evaluate + Improve
- `/Doc` → Finalize

`/Build` یک coding agent آزاد نیست — **موتور پیاده‌سازی کنترل‌شده** از روی طرح تأییدشده است.
