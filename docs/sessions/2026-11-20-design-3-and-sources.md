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

## The author's second message — "Give me all email required to send it with email and subject and content"

The agent looked for each owner's contact on its own site and wrote eight letters in `docs/permissions/letters/`
(recipient, how to send, subject, Arabic and English text). Addresses found: info@qurancomplex.gov.sa,
info@quranenc.com (decoded from the site's protected link), info@binothaimeen.com, support@dorar.net (with Dorar's
access-request form). Forms only: al-Badr (al-badr.net/contact), mp3quran (contact-us; its page also says its rights
are open to all, even for commercial use), EveryAyah (Quran.com's help centre). Hisn al-Muslim: the author, Sheikh
Sa'id al-Qahtani, died in 2018; his official site binwahaf.com publishes no address; the app he certified gives
hisn-almuslim.com — the letter asks them who holds the rights now.

## The author's third message — what was sent, Hisn al-Muslim, what is left

Sent by the author on 2026-11-20: King Fahd Complex, QuranEnc, Ibn Uthaymeen Foundation (e-mail); Sheikh al-Badr (his
site's form confirmed it); EveryAyah (Quran.com help centre, request #20971, open). mp3quran's form returned an error
each time — optional, since its pages already allow use. The agent reworded question 2 of the Dorar letter (the hadith
texts come from our own edition offline; only a link to Dorar is asked for) and found the Hisn al-Muslim address:
info@hisn-almuslim.com, the support address of the app the Sheikh certified, on its Google Play listing.

## The author's fourth message — the last two letters sent; the letters not yet written

Hisn al-Muslim and Dorar sent (2026-11-20): seven letters out. On the hadith gradings the author said «will get it
from all and mention everyone say what» — recorded in F13: every scholar's ruling with its source. QuranEnc's Arabic
tafsirs checked: al-Mukhtasar, al-Muyassar, al-Sa'di, and three more; Ibn Kathir, al-Tabari, al-Baghawi and al-Qurtubi
are not there. The agent explained why the other letters wait for a chosen edition, and R11 / R12.

## The author's fifth message — Dorar's access request submitted

The author filled Dorar's form with the two texts the agent wrote, selected **all seven encyclopedias** (also akhlaq and
aadab, «so we can add them to our plan and features»), accepted the terms and submitted the request (2026-11-20).
Recorded: F49 ethics and conduct, F50 Islamic manners; the accepted terms as binding rules (`AGENTS.md` §8.14); the
`dorar` backend module and task `P7-B2`. The terms are cited by link and summarised in the rules, not copied.

## Pages read

- https://raw.githubusercontent.com/batoulapps/adhan-js/master/LICENSE (and adhan-java, adhan-swift)
- https://raw.githubusercontent.com/notofonts/devanagari/main/OFL.txt (and bengali, nastaliq, arabic, noto-cjk), https://raw.githubusercontent.com/rastikerdar/vazirmatn/master/OFL.txt
- https://mp3quran.net/ar/privacy
- https://dorar.net/article/389 · https://dorar.net/api-services · https://dorar.net/api-services/terms
- https://qurancomplex.gov.sa/
- https://play.google.com/store/apps/details?id=com.arabiait.hisnmuslim
- https://quranenc.com/api/v1/translations/list · https://quranenc.com/ar/browse/arabic_saadi (and the other Arabic keys)
- https://quranenc.com/ar/home/contact_us · https://binothaimeen.net/ · https://al-badr.net/contact · https://www.mp3quran.net/ar/contact-us · https://everyayah.com/ · https://binwahaf.com/ · https://apps.apple.com/app/id1439791907 · https://hisn-almuslim.com/
