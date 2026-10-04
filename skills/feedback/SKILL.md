---
name: feedback
description: VCNO Stage 5 (/Feedback) — تبدیل بازخورد (متن، صدا، اسکرین‌شات، خطا، شکایت) به بهبودهای کنترل‌شده با طبقه‌بندی FB-NNN، ریشه‌یابی، تست و گزارش صادقانه؛ حلقه‌ی تکرار بین /Build و /Doc.
---

# `/Feedback` — مرحله‌ی تکرار VCNO (مرحله ۵)

> **مأموریت: «کاربر دقیقاً چه را می‌خواهد عوض شود، چرا، بر چه چیزی اثر می‌گذارد، و چطور بدون شکستن بقیه‌ی پروژه عوضش کنیم؟»**
> `/Feedback` «هرچه کاربر گفت عوض کن» نیست؛ یک **فرایند تکرار کنترل‌شده** است. بازخورد را شنوا و تحلیل می‌کند و به بهبودِ اعتبارسنجی‌شده تبدیل می‌کند — بدون از‌دست‌رفتن context، بدون شکستن رفتار موجود، بدون گسترش خاموش دامنه، بدون ادعای جعلی.

| | |
|---|---|
| Command | `/Feedback` |
| Stage | 5 — VCNO |
| Version | 1.0.0 — stable |
| Previous stage | `/Build` |
| Next stage | `/Doc` |
| loop | true |
| modifies_project | true |

## مرز مرحله

```text
/init     → Understand
/check    → Validate
/PRD      → Plan
/Build    → Implement + Verify
/Feedback → Listen + Analyze + Improve  ← این اسکیل (حلقه می‌زند)
/Doc      → Finalize
```

- `/Build` پیاده‌سازیِ طرح تأییدشده را می‌سازد؛ `/Feedback` نتیجه‌ی واقعی را ارزیابی و تکرار می‌کند
- درخواست‌های ذائقه‌ای/سلیقه‌ای (UX feel) → `/Feedback`؛ شکسته/ناقص بودنِ فنی → `/Build`
- **تغییر major محصول باید از `/check → /PRD → /Build` برگردد**
- `/Feedback` هرگز کدنویسی بی‌کنترل نمی‌شود

## چه زمانی اجرا شود

- بعد از اتمام `/Build` (گزارش `COMPLETE`/`PARTIAL`)
- هر وقت کاربر بازخورد دارد: باگ، UX، فیچر، اسکرین‌شات، صدا، شکایت
- بعد از مشاهده‌ی رفتار واقعی پروژه

## پیش‌نیازها

- context موجود: `/init`، `/check`، `/PRD`، گزارش `/Build`، بازخوردهای قبلی، Git
- دسترسی به کد و تست
- **قبل از هر تغییر: Git status را ببین؛ کار commit‌نشده‌ی کاربر حفظ شود**

## قرارداد رفتار

### MUST

- context قبلی را مصرف کن (کاربر را وادار به تکرار نکن)
- بازخورد را به هر شکلی بپذیر (متن، صدا، اسکرین‌شات، خطا، شکایت)
- **قبل از پیاده‌سازی classify کن**؛ severity و scope را قبل از تغییر کد تعیین کن
- برای مشکل رفتاری Expected vs Actual تعیین کن
- قبل از وصله، ریشه (root cause) را تحقیق کن
- تمایز small iteration / medium change / major product change
- رفتار موجود را حفظ کن؛ ریسک regression را کمینه کن
- هر تغییر مهم را تست و verify کن
- هر آیتم بازخورد را با وضعیت شفاف ردیابی کن؛ تاریخچه را حفظ کن
- صادقانه گزارش کن: `VERIFIED` / `IMPLEMENTED — NOT VERIFIED` / `BLOCKED` / `DEFERRED` / `REJECTED`

### MUST NOT

- فقط چون کاربر گفت، کور کد عوض کن
- برای یک شکایت، کل فیچر را بازنویسی کن
- وقتی ابهام مادی است، منظور کاربر را حدس بزن
- علامت (symptom) را وصله کن وقتی ریشه قابل‌شناسایی است
- دامنه را خاموش گسترش بده؛ هر ایده‌ی جدید را خودکار پیاده کن
- جای `/check` یا `/PRD` را برای تغییر major بگیرد
- بدون evidence بهینه‌سازی کن؛ وقتی مشکل AI جای دیگر است prompt را عوض نکن
- secret commit کن؛ کار غیرمرتبط کاربر را reset/clean/revert کن
- بدون verification موفقیت ادعا کن؛ بی‌پایان روی fix شکست‌خورده loop کن
- بازخورد را بی‌صدا دور بریزی

## مراحل کار

1. **بارگذاری context** — `docs/project.md`، PRD، نتایج `/check`، پیشرفت و گزارش `/Build`، پیاده‌سازی/تست، بازخوردهای قبلی، known issues، تاریخ/وضعیت Git، UI/design موجود. اطلاعات موجود را دوباره از کاربر نخواه.
2. **پذیرش بازخورد به هر شکل** — یک جمله، توضیح بلند، transcript صدا، اسکرین‌شات/ویدیو، مشاهده‌ی UI، پیام خطا، توصیف expected-vs-actual، درخواست فیچر، شکایت performance، نقد طراحی، «این اشتباه به‌نظر می‌رسد». زبان طبیعی را بدون قالبِ سخت تفسیر کن.
3. **حدس نزن** — «داشبورد بده‌ست» را فوراً بازنویسی **نکن**. ابعاد ممکنِ «بد»:

    ```text
    Visual design / Usability / Performance / Missing functionality
    / Incorrect data / Navigation / Responsiveness / Accessibility
    / Content / Business logic
    ```

    فقط اگر ابهام، پیاده‌سازی را مادی تحت‌تأثیر قرار دهد، clarification متمرکز بپرس.
4. **طبقه‌بندی هر آیتم** — `Bug` / `Feature Request` / `UX Improvement` / `UI Change` / `Performance` / `Security` / `Data Issue` / `Business Logic` / `Technical Debt` / `Documentation` / `Configuration` / `Architecture` / `Other`. طبقه‌بندی راهبرد پیاده‌سازی را هدایت می‌کند.
5. **تعیین severity** — `Critical / High / Medium / Low`:
    - **Critical** — آسیب‌پذیری امنیتی، فساد داده، غیرقابل‌استفاده‌شدن اپ
    - **High** — جریان هسته‌ای شکسته
    - **Medium** — قابلیت مهم با workaround تخریب‌شده
    - **Low** — polish، UX جزئی، تزئینات

    سوءاستفاده از `Critical` ممنوع.
6. **تعیین scope** — قبل از هر تغییر: فیچر متأثر، فایل‌ها، کامپوننت‌ها، دیتابیس/API/UI، کاربران متأثر، اثرات جانبی احتمالی، وابستگی‌ها. مشکلِ قابل‌مشاهده را محدود به فایلِ قابل‌مشاهده فرض نکن — رفتار را در سیستم ردیابی کن.
7. **Expected vs Actual** (برای باگ):

    ```text
    Expected: ...
    Actual: ...
    Difference: ...
    ```

    اگر بازتولید (reproduce) ممکن نیست → آن را صریح بگو. اگر باگ هرگز reproduce یا verify نشد، «رفع شد» ادعا نکن.
8. **Reproduce قبل از fix (در صورت امکان)** — بازرسی پیاده‌سازی → بازتولید → شناسایی علت → نواحی متأثر → کوچک‌ترین fix ایمن → تست → verify حل‌شدن مشکل اصلی. اگر reproduce نشد: بازرسی evidence، بیان محدودیت، کوچک‌ترین تغییر موجه، تست دفاعی در صورت مناسب، گزارش صادقِ «چه verify شد / نشد».
9. **ریشه، نه علامت** — «دکمه کار نمی‌کند» → فقط handler دیگر اضافه **نکن**: `event binding → DOM state → API request → validation → backend response → frontend error handling`. هدف fix درست است، نه وصله‌ی سطحی.
10. **درخواست فیچر** — تعیین کن: چه مشکلی را حل می‌کند، چه کسی لازمش دارد، رفتار دقیق موردنظر، تعلق به محصول فعلی، تعارض با PRD، اثر بر معماری/DB/API/UI، V1 یا آینده. **هر ایده‌ی جدید را خودکار پیاده نکن.**
11. **بازخورد vs تغییر requirement** — مقیاس را تمایز بده:
    - **Small iteration** («این دکمه را بالاتر ببر») → معمولاً مستقیم
    - **Medium change** («فلتر به دشبورد اضافه کن») → ممکن است planning، API جدید، UI، تست بخواهد
    - **Major product change** («تبدیلش کن به marketplace») → **نه** وصله‌ی عادی → بازگشت:

    ```text
    /check → /PRD → /Build
    ```

    `/Feedback` نباید خاموش جای برنامه‌ریزی محصول را بگیرد.
12. **بازخورد UI/UX** — UI در VCNO مرحله‌ی جدا نیست. پیاده‌سازی موجود، اسکرین‌شات، Figma، رجعان design، رفتار responsive، ساختار کامپوننت را بازرسی کن؛ بازخورد ذائقه‌ای را به تغییر مشخص ترجمه کن («شلوغ به‌نظر می‌رسد» → spacing، typography، سلسله‌مراتب، تراکم، layout responsive، information architecture). بازطراحی کل رابط کور ممنوع.
13. **اسکرین‌شات و بازخورد بصری** — آن را به‌عنوان evidence بگیر: ناحیه‌ی متأثر، مشکل قابل‌مشاهده، بهبود موردنظر، محل احتمالی پیاده‌سازی. مشکل بصریِ بدون پشتوانه‌ی اسکرین‌شات/context اختراع نکن؛ اگر اسکرین‌شات کافی نیست → سؤال متمرکز بپرس.
14. **ورودی صدا** — ممکن است تکرار، جمله‌ی ناقص، لحن غیررسمی، آمیخته‌ی فنی/غیرفنی داشته باشد. **intent را تفسیر کن، نه transcription را تحت‌اللفظی.** intent روشن → ادامه؛ نه → clarify.
15. **آیتم‌های چندگانه** — به آیتم‌های جدا استخراج کن و هیچ درخواستی را گم نکن:

    ```markdown
    ## Feedback Items
    ### FB-001 — Fix login redirect.  Type: Bug      Priority: High
    ### FB-002 — Add search.          Type: Feature Priority: Medium
    ### FB-003 — Increase spacing.    Type: UI      Priority: Low
    ```

    به ترتیب منطقی پردازش کن.
16. **اولویت‌بندی** — `1. Security → 2. Data integrity → 3. Blocking bugs → 4. Core functionality → 5. High-impact UX → 6. Performance → 7. Features → 8. Cosmetic polish`. تزئینات هرگز بر جریان شکسته‌ی هسته‌ای مقدم نشود.
17. **ترتیب وابستگی** — `Fix API → Fix frontend integration → Update UI` را به ترتیب وابستگی پیاده کن؛ قبل از رفع dependency پایین‌دستی، علامتِ پایین‌دستی را وصله نکن.
18. **حفظ رفتار موجود** — «رفتار درخواستی را بهبود بده بی‌آنکه بی‌جهت رفتار غیرمرتبط را بشکنی» — بازنویسی broad وقتی تغییر هدفمند کافی است ممنوع.
19. **محافظت regression** — بعد از تغییر: اجرای تست‌های موجود مرتبط، افزودن تست regression در صورت مناسب، تست جریان‌های مرتبط، verify کردن عملکرد غیرمتأثر در ریسک بالا. fix باگ در ایده‌آل باید تستی داشته باشد که آن باگ را می‌گرفت.
20. **تست** — هر جا عملی، اجباری: `Change → Relevant Test → Execute → Result` — unit/integration/API، دیتابیس/frontend/e2e، تأیید دستی. «تست پاس شد» فقط با اجرای واقعی.
21. **تأیید** — سؤال: «آیا تغییر درخواستی واقعاً مشکل کاربر را حل کرد؟» — برای هر آیتم: `Implemented? / Tested? / Verified? / Regression checked?`. «کد عوض شد» ≠ «مشکل حل شد».
22. **تغییرِ شکست‌خورده** — شکست را پنهان نکن: `Attempt 1 → Test → Failed → Investigate → Attempt 2 → Test → Verify`. حل نشد → `BLOCKED` گزارش کن، نه موفقیت جعلی.
23. **پرهیز از loop بی‌پایان** — تکرار شکست: 1. توقف 2. خلاصه‌ی آنچه امتحان شد 3. شناسایی blocker 4. درخواست اطلاعات اضافه یا escalation به برنامه‌ریزی. تغییر تصادفیِ مکرر ممنوع.
24. **مستندسازی** — بازخورد مهم و تصمیم‌های ناشی را ثبت کن، طبق قاعده‌ی موجود: `docs/feedback/`، `docs/changes/`، `docs/project.md`. برای هر تغییر مهم: بازخورد، طبقه‌بندی، تصمیم، پیاده‌سازی، verification، باقی‌مانده. برای تغییر تزئینی جزئی داکسِ زائد نساز.
25. **ایمنی Git** — قبل از تغییر: status را ببین، تغییرات کاربر را حفظ، branch را بفهم. ممنوع: reset/clean/revert کار غیرمرتبط، overwrite commit‌نشده، commit secret. بعد از iteration موفق checkpoint معنادار:

    ```text
    fix(feedback): correct dashboard filtering
    fix(ui): improve mobile navigation spacing
    ```

    طبق قاعده‌ی موجود پروژه.
26. **تاریخچه‌ی بازخورد** — بازخورد قبلی را گم نکن: `FB-001 Status: Resolved / FB-002 Status: In Progress / FB-003 Status: Blocked`. جلوی حلِ چندباره‌ی یک مشکل را بگیر.
27. **مدل وضعیت** — فقط وضعیت‌های مفید برای پروژه را استفاده کن (بوروکراسی زائد ممنوع):

    ```text
    NEW / ANALYZING / NEEDS CLARIFICATION / PLANNED / IN PROGRESS
    / TESTING / VERIFIED / BLOCKED / DEFERRED / REJECTED
    ```

28. **آیتم‌های Deferred** — وقتی: خارج از دامنه، در تعارض با جهت فعلی، نیازمند برنامه‌ریزی major، وابسته به فیچر دیگر، اولویت پایین. ثبت کن: `Reason / Impact / Recommended future stage`. **هرگز خاموش دور نریز.**
29. **آیتم‌های Rejected** — با دلیل: ناقض امنیت، متعارض با requirement معتبر، غیرعملی فنی، تکرار غیرضروری، ریسک غیرقابل‌قبول، متعلق به محصول دیگر. فقط چون پیاده‌سازی‌اش سخت است ردش نکن.
30. **تغییر معماری major** — فوراً پروژه را بازنویسی **نکن**: شناسایی اثر معماری → توضیح چرایی → بازگشت به `/check` یا `/PRD` → به‌روزرسانی طرح → بازگشت به `/Build`. این VCNO را حفظ می‌کند.
31. **تغییرات دیتابیس از بازخورد** — بازرسی schema → ارزیابی اثر migration → حفظ داده → مکانیزم migration موجود → تست migration → تست عملکرد متأثر. حذف سهل‌انگارانه‌ی داده‌ی production-like ممنوع.
32. **بازخورد امنیتی** — اولویت بالا: دورزدن auth، ایراد authorization، secret نمایان، مشکل isolation tenant، آپلود ناامن، injection. مهندسی‌اش کن، نه تزئینی؛ fix را verify و در صورت مناسب regression پوشش بده؛ جزئیات آسیب‌پذیری حساس را در داکس عمومی افشا نکن.
33. **بازخورد performance** — کور بهینه نکن: چه چیزی کند است، کجا bottleneck است، چطور اندازه می‌گیرد، frontend/backend/DB/network/external. با evidence، نه premature optimization.
34. **بازخورد AI/ML** — تمایز: `Prompt` / `Model` / `Data` / `Evaluation` / `Post-processing` / `UI presentation` / `Infrastructure`. وقتی مشکل جای دیگر است prompt را عوض نکن؛ تغییرات AI را با حالت‌های نماینده verify کن.
35. **گزارش نهایی بازخورد** — هر اجرا با این تمام می‌شود:

    ```markdown
    # VCNO Feedback Report
    ## Summary
    ## Feedback Processed
    ### FB-001  Status: VERIFIED | Type: Bug | Change: ... | Verification: ...
    ### FB-002  Status: DEFERRED | Reason: ...
    ### FB-003  Status: BLOCKED  | Reason: ...
    ## Files Changed / ## Tests / ## Verification / ## Git
    ## Remaining Issues
    ## Next Step
    ```

    فقط ادعاهای پشتوانه‌ی کار واقعی.
36. **قانون تکمیل** — `VERIFIED` فقط وقتی: تغییر پیاده شد + تست‌های مرتبط در صورت کاربرد اجرا شد + نتیجه verify شد + هیچ regression مسدودکننده‌ی شناخته‌شده باقی نیست. کد عوض شد ولی verify ممکن نبود:

    ```text
    IMPLEMENTED — NOT VERIFIED      (نه: VERIFIED)
    ```

37. **حلقه‌ی نهایی** — همه‌ی بازخوردهای فعلی حل شدند:

    ```text
    Feedback → Implemented → Tested → Verified
      → No blocking feedback → Ready for next feedback ↺
    ```

    پروژه می‌تواند بازخورد جدید بگیرد؛ حلقه تکرارپذیر می‌ماند.

## نکات و خطاهای رایج

- **خطای ممنوع:** `/Feedback → تغییر کور کد از هر بیانی از کاربر / بازنویسی کل فیچر برای یک شکایت / وصله‌ی علامت به‌جای ریشه / حدس intent با ابهام مادی / خودکارپیاده‌سازی هر ایده / جایگزینی /check یا /PRD برای تغییر major / بهینه‌سازی بدون اندازه‌گیری / عوض‌کردن prompt وقتی مشکل جای دیگر است / commit secret / reset/clean/revert کار کاربر / ادعای VERIFIED بدون verification / loop بی‌پایان روی fix شکسته / دورریختن خاموش بازخورد`.

## یکپارچگی با خط لوله‌ی VCNO

| مرحله | رابطه |
|---|---|
| `/init` | context پروژه را می‌دهد |
| `/check` | هدف تغییر major محصول/دامنه |
| `/PRD` | هدف تغییر major محصول |
| `/Build` | پیاده‌سازیِ شکسته/ناقصِ فنی را رفع می‌کند |
| `/Feedback` | روی نتیجه‌ی واقعی تکرار می‌زند؛ به `/Build` یا برنامه‌ریزی برمی‌گرداند |
| `/Doc` | وضعیت نهاییِ verifyشده‌ی بازخورد را جذب می‌کند |

`/Feedback` بهبود می‌دهد؛ برنامه‌ریزی نمی‌کند و دامنه را خاموش گسترش نمی‌دهد.

## اصل راهنما

> بازخورد دستورِ کورِ تغییر کد نیست؛ evidence درباره‌ی آن است که پیاده‌سازی فعلی چطور باید بهتر شود.

- `/init` → Understand
- `/check` → Validate
- `/PRD` → Plan
- `/Build` → Implement + Verify
- `/Feedback` → Listen + Analyze + Improve (loops)
- `/Doc` → Finalize

`/Feedback` حلقه را کنترل‌شده نگه می‌دارد: پروژه را بهتر می‌کند **بدون از‌دست‌رفتن context، شکستن رفتار موجود، گسترش خاموش دامنه، یا وانمودِ تکمیلِ تغییرِ verifyنشده.**
