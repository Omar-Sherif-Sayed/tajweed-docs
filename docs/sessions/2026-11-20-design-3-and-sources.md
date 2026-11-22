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

## 2026-11-21 — the author's sixth message: scholars, sources, R11, R12, the Names on the home screen

The author asked: a fourth part of «السِّيَر» for the scholars of Islam (Ibn al-Qayyim, Ibn Kathir, al-Bukhari, Muslim
…), with all their names shown to him first, and their books in F14; the hadith and tafsir sources explained in
Arabic and researched "from the best place"; R11 — the Seerah is the last story of the prophets; R12 — all the
Companions with all their stories; where the Names of Allah and of the Prophet ﷺ are on the home screen; and «تحري
دائماً أن تأتي بأفضل المصادر … تحري الدقة في كل شيء».

The agent checked the sources: sunnah.com (complete collections; API key by a GitHub issue; offline dump not yet),
HadeethEnc.com (about 4,000 hadiths with grade, explanation, references and translations; open API; info@hadeethenc.com),
the Quran Foundation Content APIs (Ibn Kathir, al-Tabari, al-Qurtubi, al-Baghawi, al-Sa'di, al-Muyassar, al-Wasit; offline
allowed with a weekly sync; developers@quran.com). Recorded R11, R12, F51 and the accuracy rule; letters 09 – 11
drafted; the list of scholars and their books proposed in the answer, for the author's approval.

## 2026-11-21 — the author's seventh message: the scholars approved; the home order; the Sources screen

```text
1- موافق - وزد في الكتب مثل الداء والدواء لأبن القيم - ممكن ان يتم ترتيب العلماء بالعام الذي ولدوا فيه أو بالمجموعة (أول صف في ال table اللي انت كاتبة)
2- الأسماء مع كذا feature تانية خليهم فوق السير مع الراديو والباقي - يعني خلي السير أخر شيء فين design بتاع كل ال features ممكن تعمله في design 3
3- اعملي table فيه أسم كل ملف وأبعته لمين بالظبط في الحاجات اللي ناقصة - وماتنساش تعمل update لصفحة المصادر (اضف ما تم التحقق منه او ما ننتظر التحقق منه)
```

Built in design 3 only, by a new script `tools/build_design3.py` (texts in `i18n/design3/`, 22 languages): the home screen (the Names of Allah, the names of the Prophet ﷺ, memorisation, «كل الأقسام» above the Lives; the Lives last with the scholars); «كل الأقسام» — every feature F1 – F51 marked drawn / inside another screen / to come, which answers «فين design بتاع كل ال features»; the 53 scholars by group or by time; one scholar (Ibn al-Qayyim); the library of 65 books with «الداء والدواء»; the Sources screen with four states. **Ordering by birth year:** the year of birth of several scholars is not recorded (e.g. Ibn Hisham, al-Qurtubi) and differs between sources for others (e.g. Muslim), while the year of death is recorded for all — so «حسب الزمن» orders by death; every year is copied from the biographies before the order is final (`P9-D5`). The table of letters still to send was given in the answer (09 HadeethEnc, 10 sunnah.com, 11 the Quran Foundation; 07 mp3quran optional).

## 2026-11-21 — the author's eighth message: every remaining screen; letters 09 – 11

```text
* الأقتراحات يمكنك عملها الأن, اوافق عليها كلها, اعملها كلها في تصميم 3
* 09-hadeethenc.md  - أرسلت الأيميل
* 10-sunnah-com.md - قمت بإنشاء issue (https://github.com/sunnah-com/api/issues/4480) with status open
* 11-quran-foundation.md - سجلت بالأيميل الخاص بي <e-mail> حالياً مافيش option غير create app وانا لسه مافيش callback url علشان لسه ماعملتش ال application ولا ال apis (https://dev-console.quran.foundation/projects/new) - لو كريتة أنت فأنا عاوزة بالأسم الكامل (Tajweed - The Noble Quran and Its Sciences)
```

Drawn in design 3 only: 28 screens in six batches (`tools/build_design3_screens.py`, texts in `i18n/design3-screens/`, 22 languages); «كل الأقسام» now shows 48 of 51 features drawn. Letters recorded (`docs/permissions/`). **The Quran Foundation app:** its quickstart (read 2026-11-21) says a backend app uses the Client Credentials grant — a callback URL belongs to sign-in flows only, so none is needed; the client secret is shown once; new apps start in pre-live (surahs 1 – 2). The agent did not create the app: the secret must stay with the author (later the backend's environment), never in a chat or a repository — the author creates it with the full name and these settings.

## 2026-11-21 — the author's ninth message: the Quran Foundation form needs a redirect URI

The author sent a screenshot of the «Create app» form (the redirect URI is required) and the link to the Developer Terms. The agent read the terms (summary in `docs/permissions/README.md` and `AGENTS.md` §7.1, §5) and advised: redirect URI `http://localhost:8080/callback` (unused by a backend app, changeable later), «without a Client Secret» unchecked. New rule from the terms: Quran Foundation content in a public repository is redistribution — it is fetched at run time through Content Sync, never committed.

## 2026-11-21 — the author's tenth message: the Quran Foundation app created

The author created the app (screenshots of its overview: server app, active, two environments, 89 pre-live and 12 production permissions) and asked whether anything there is needed. The agent read the Developer Privacy Policy Packet and the FAQ and recorded what is used and when (`docs/permissions/README.md`): the credentials go into the backend's environment at `P0-07`; the tafsir scope checked before production; Social login, Webhooks, Connected Apps and the SDKs not used; the privacy policy needs a public e-mail and postal address — the author's decision before release.

## 2026-11-21 — the author's eleventh message: design 3 approved; the backend plan

```text
راجعت الصميم رقم 3 والدنيا تمام
حالياً لو هانبدأ في مشروع ال backend ايه ال plan وال tools وال libraries اللي شايفها هانستخدمها وال structure اللي هايقوم عليه ال spring boot project - يعني لو هانبدأ فيه دلوقتي هاتعمله ازاي تفصيلياً
```

Design 3 recorded as approved (P0-11). The agent checked today's versions on Maven Central (Spring Boot 4.2.0 of 2026-11-19 and 4.1.3; the libraries Boot manages; springdoc 3.2.1, ShedLock 7.11.0, Bucket4j 8.22.0, WireMock 3.13.2, ArchUnit 1.5.1), postgresql.org (19.0 new, 18.7) and Docker Hub, and wrote `docs/plan/backend-plan.md` with five decisions for the author (B1 – B5). No code written — the author answers first.

## 2026-11-21 — the author's twelfth message: the backend plan approved; Javadoc everywhere

```text
ok for all, don't forget to document everything, also javadoc on the code everywhere, to be readable in the feature
```

B1 – B5 approved. The agent scaffolded `tajweed-backend` (`P0-06` backend part, `P0-07`): Spring Initializr (Boot 4.2.0, Java 25), then the shared layer, `GET /v1/app-info`, 22 message files, the Flyway baseline, `compose.yaml`, `Dockerfile`, CI, and Javadoc on everything — enforced by Checkstyle (Javadoc rules only; a probe class without comments failed the build as it should) and the Javadoc tool. Problems met and fixed: Checkstyle 14 no longer has `JavadocStyle` (replaced by `SummaryJavadoc`) and `MissingJavadocMethod` takes `scope`; the `Vary` header holds several values (test corrected); Mockito's agent loaded at run time (now given up front). Result: 42 tests green (39 unit, 3 integration on PostgreSQL 18), `bootRun` answered in Urdu and French and returned `304` for a repeated request. The latest action versions were read over SSH (`git ls-remote`), because api.github.com fails on this machine's certificate store (§1).

## 2026-11-21 — the author's thirteenth message: «Start doing everything related to the backend project»

The agent read it as a go-ahead for the backend's phase 1 and built the `quran` module: the verified Tanzil files moved from the design assets into `tajweed-backend` (checksums equal), the tables written first in `docs/database/README.md` (the author may still change them — no deployed database has them), a Flyway Java import that checks the SHA-256 of every file and every count before writing, the endpoints, and 57 tests (every stored ayah compared with the file). Found while checking: Tanzil writes the basmala of 95:1 and 97:1 with a shadda («بِّسْمِ») — kept as written, recognised by its letters, noted for `P0-12`; the quarter at 15:49 applied from a reviewed correction file with its evidence. Not done, waiting: the search text needs Tanzil's «Simple» files — downloading them is the author's decision.

## 2026-11-21 — the author's fourteenth message: «Yes, download both»

```text
Yes, download both
```

The agent downloaded Tanzil «Simple» and «Simple (Clean)» (version 1.1) from tanzil.net, recorded their SHA-256, and checked them: the same 6,236 ayahs in the same order as the Uthmani text; Tanzil kept the pause marks, ۞ and ۩ although the download options asked for none — the files are kept as received and the search ignores those signs. The rules of the search were fixed and written (§8.1 rule 3) and implemented in one Java function; an independent Python implementation computed ten reference queries (for example «الصبر» 4 ayahs, «الله» 1,842, «مُحَمَّدٌ» with tashkeel 2), and the Java tests give the same. The backend got the table `ayah_search_text` (migrations 1.2.0 / 1.2.1, the same checks as the Quran import) and `GET /v1/quran-search`: words with or without tashkeel (paged, counted by surah, with the words to highlight where the two spellings have the same words), surah names in Arabic and Latin, and references such as `2:255` or «البقرة 255». 75 tests green. Still to do in `P1-D3`: the common spellings of the surah names from a named source.

## 2026-11-22 — the author's fifteenth message: «Yes, reciters next»

```text
Yes, reciters next
```

The agent read mp3quran's API (reciters, moshaf, riwayat, timing reads, one timing sample) and EveryAyah's list, wrote
the proposal (`docs/plan/backend-plan.md` §13) and asked four questions. The author's answers: download everything
from mp3quran; EveryAyah now, streaming only, «and continue the task after them answers, save that»; the other
riwayat «Include them all, وكمان مع كل رواية وضح هي ايه سواء حفص او غيرها»; both incomplete recitations.

Built: the `reciter` module (migrations 1.3.0 / 1.3.1, four endpoints, the daily health check). Found and handled:
mp3quran's timings exist for some styles only (§7.3 corrected); Ali al-Hudhaifi's timings miss the last ayah in 112
of 114 surahs and were left out whole; 7 other surahs left out with reasons. A measurement decided which EveryAyah
folders are the same recording as an mp3quran recitation — the last ayah of every surah, file length against
mp3quran's timing; same recording when 90 % agree within 5 % (controls between different reciters: 15 – 23 %):
al-Minshawi murattal 99 %, al-Husary murattal 100 / 98 %, Abdul Basit murattal 100 %, al-Tablawi murattal 100 %,
al-Shuraim 95 / 94 % — attached as fallbacks; al-Husary mujawwad 51 %, Abdul Basit mujawwad 88.5 %, al-Muaiqli 27 %
(against his mujawwad), Yasser al-Dosari 56 %, al-Sudais 39 – 43 %, Fares Abbad 27 % — their own recitations; «Ghamadi»
75 % against Saad al-Ghamdi — his own recitation; «Hudhaify» — not measurable, left out. 90 tests green.

## 2026-11-22 — the author's sixteenth message: the King Fahd Complex's answer

The author showed the Complex's reply (info@qurancomplex.gov.sa, 2026-11-22 09:45): not a decision — it asks for the
request again as a formal letter addressed to «سعادة الأمين العام لمجمع الملك فهد لطباعة المصحف الشريف وفقه الله» with
«مع التحية والتقدير». The answer was saved (`docs/permissions/answers/01-king-fahd-complex-2026-11-22.md`) and the
letter written in that form (`docs/permissions/letters/01b-king-fahd-complex-secretary-general.md`), the request
unchanged; the author fills in the Hijri date and his mobile number (kept out of this public repository) and sends it
as a reply in the same thread.

## Pages read

- https://raw.githubusercontent.com/batoulapps/adhan-js/master/LICENSE (and adhan-java, adhan-swift)
- https://raw.githubusercontent.com/notofonts/devanagari/main/OFL.txt (and bengali, nastaliq, arabic, noto-cjk), https://raw.githubusercontent.com/rastikerdar/vazirmatn/master/OFL.txt
- https://mp3quran.net/ar/privacy
- https://dorar.net/article/389 · https://dorar.net/api-services · https://dorar.net/api-services/terms
- https://qurancomplex.gov.sa/
- https://play.google.com/store/apps/details?id=com.arabiait.hisnmuslim
- https://hadeethenc.com/ar/home · https://hadeethenc.com/api/v1/hadeeths/one/?language=ar&id=2962 · https://hadeethenc.com/ar/home/contact
- https://sunnah.com/developers · https://github.com/sunnah-com/api
- https://api-docs.quran.foundation/ · https://api-docs.quran.foundation/docs/connected-apps/ · https://api.quran.com/api/v4/resources/tafsirs
- https://quranenc.com/api/v1/translations/list · https://quranenc.com/ar/browse/arabic_saadi (and the other Arabic keys)
- https://tanzil.net/download/ (the Simple and Simple Clean text types, 2026-11-21)
- https://www.mp3quran.net/api/v3/reciters (ar, eng), /moshaf, /riwayat (ar, eng), /languages, /ayat_timing/reads, /ayat_timing · https://everyayah.com/data/recitations.js · https://everyayah.com/recitations_ayat.html (2026-11-22)
- https://repo1.maven.org/maven2/ (metadata of Spring Boot and each library) · https://www.postgresql.org/versions.json · https://services.gradle.org/versions/current
- https://api-docs.quran.foundation/legal/developer-privacy/ · https://api-docs.quran.foundation/docs/tutorials/faq/ · https://api-docs.quran.foundation/legal/developer-terms/ · https://api-docs.quran.foundation/docs/quickstart/ · https://www.mp3quran.net/api/v3/radios?language=ar (and language=eng)
- https://quranenc.com/ar/home/contact_us · https://binothaimeen.net/ · https://al-badr.net/contact · https://www.mp3quran.net/ar/contact-us · https://everyayah.com/ · https://binwahaf.com/ · https://apps.apple.com/app/id1439791907 · https://hisn-almuslim.com/
