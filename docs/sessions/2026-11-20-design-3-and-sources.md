# Session record — 2026-11-20 — design 3 chosen; how the pending sources are cleared

Continues `2026-11-16-planning.md` (§1 – §23). Conversation copy: the end of `2026-11-16-planning-conversation.md` (the same conversation, continued).

## The author's message

```text
* كل شيء تمام حالياً - خلينا نعتمد في الكود علي التصميم رقم 3 وسيب التصاميم الأخري ماتمسحهاش ولكن هايكون شغلنا كله علي التصمرم رقم 3 وأي تحديث او شغل هايكون عليه إن شاء الله 
* خلينا نشوف المصادر - في حاجات كاتب عليها (⏳ بانتظار التحقق أو الإذن) دي هاتتحقق منها ازاي او هاتاخد تالأذن إزاي إننا نستخدم الأشياء دي؟
```

## What the agent did

1. **Design 3 chosen** — recorded in `AGENTS.md` (§0, §13, P0-11, §19) and the plan: all work on `round-3.html`;
   designs 1 and 2 kept unchanged.
2. **The five sources marked pending on design 3's Sources screen checked again on their owners' sites:**
   - Noto fonts (Devanagari, Bengali, Nastaliq Urdu, Kufi Arabic, CJK) and Vazirmatn — `OFL.txt` read: OFL 1.1 ✔;
   - the Adhan library — `LICENSE` of the JavaScript, Java and Swift editions: MIT ✔;
   - mp3quran.net — its rights clause on `mp3quran.net/ar/privacy`: any visitor or developer may use any material or
     link ✔ (a courtesy letter advised for offline downloads);
   - الدرر السنية — **new written API terms** (`dorar.net/api-services/terms`) with an access-request form: attribution
     and clickable link, the grade never altered or separated, no bulk storage (cache 24–48 h), the key only on the
     server, 60 requests a minute, a test environment for their review before publishing ⏸;
   - the King Fahd Complex — still «جميع الحقوق محفوظة», fonts «قريباً»; contact info@qurancomplex.gov.sa ☐ letter.
3. **`docs/permissions/README.md`** — the three ways a source is cleared (read the licence; ask in writing — the agent
   drafts, the author sends; check the content itself), and a status table of every pending source of the product.
4. Design 3's Sources screen updated: mp3quran and Adhan shown as verified, the font row cleared, Dorar pointing to its
   API page.

## Pages read

- https://raw.githubusercontent.com/batoulapps/adhan-js/master/LICENSE (and adhan-java, adhan-swift)
- https://raw.githubusercontent.com/notofonts/devanagari/main/OFL.txt (and bengali, nastaliq, arabic, noto-cjk), https://raw.githubusercontent.com/rastikerdar/vazirmatn/master/OFL.txt
- https://mp3quran.net/ar/privacy
- https://dorar.net/article/389 · https://dorar.net/api-services · https://dorar.net/api-services/terms
- https://qurancomplex.gov.sa/
