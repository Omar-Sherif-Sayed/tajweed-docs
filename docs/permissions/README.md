# Permissions and verifications — every source that is not yet cleared

Task `P0-13` (and the register of `P0-12`). The author asked on 2026-11-20 how each source marked "⏳ check or
permission pending" will be verified or permitted. This file is the answer and the tracker: one row per source, how
it is cleared, who does it, and its status. Rule `AGENTS.md` §6.8: **a source whose licence is unclear is not used
until its owner answers.**

## How a source is cleared — three ways

| Way | When | Who | What is kept here |
| --- | --- | --- | --- |
| **A. Read the licence** | The owner publishes a licence or terms (a `LICENSE` / `OFL.txt` file, a terms page) | The agent reads it on the owner's own site, records the link, the date and the exact clause | The link, the date, the clause in a short quote |
| **B. Ask in writing** | No licence, "all rights reserved", or terms that need a key or an agreement | The agent drafts the letter (Arabic and English) in `letters/`; **the author sends it from his own e-mail or fills the owner's form** (the agent never sends a message on his behalf); the answer is saved in `answers/` | The letter, the date sent, the answer, the decision |
| **C. Check the content itself** | Every religious text, even when its licence is clear | The agent compares it by script with its source (checksums, counts, word-for-word comparison); the author checks samples against his printed copy; a qualified reviewer when one exists (§6.6) | The script, its result, the date |

A source can be **A-cleared and still need C** (the Quran text: CC BY 3.0, and checked word for word). Free to read
on a website is not the same as free to copy into an application (§7.5).

## The status table

✔ cleared · ◐ partly · ☐ not started · ⏸ waiting for an answer.

| Source | Used for | Way | Status (2026-11-20) |
| --- | --- | --- | --- |
| Tanzil Quran text and metadata | F2, F16 | A + C | ✔ CC BY 3.0 (2026-11-16); text checked by checksum and counts |
| DigitalKhatt layout | F2 | A + C | ✔ MIT; 0 word and 0 page-start differences with Tanzil (2026-11-17) |
| Google / Noto fonts, Vazirmatn, Amiri, Inter, IBM Plex | interface | A | ✔ OFL 1.1 — the `OFL.txt` / `LICENSE` of notofonts/devanagari, bengali, nastaliq, arabic, noto-cjk and rastikerdar/vazirmatn read on 2026-11-20 |
| Adhan library (Batoul Apps) | F8 | A | ✔ MIT — `LICENSE` of adhan-js, adhan-java, adhan-swift read on 2026-11-20 |
| mp3quran.net (recitations, timings, radio) | F3, F7, F28 | A (+ B advised) | ✔ Its contact page adds: «حقوق الموقع متاحة للجميع حتى ولو كانت لإغراض تجارية». The courtesy letter could not be sent — the contact form fails (2026-11-20); other channels: x.com/mp3quran, facebook.com/MP3Quran. ✔ Its rights clause (mp3quran.net/ar/privacy, read 2026-11-20): «جميع الحقوق متاحة للجميع و يحق لأي زائر أو مطور استخدام اي مادة أو رابط من الموقع». Advised: a short letter telling them about the app and asking them to confirm downloads for offline listening (F28) — the recordings themselves belong to the reciters. |
| الدرر السنية — Dorar API | F13, F29 (grading, links) | B | ⏸ **Letter sent 2026-11-20** to support@dorar.net. Dorar replied with the link to its access-request form. **The author submitted the access request on 2026-11-20 for all seven encyclopedias** (hadith, tafsir, aqeeda, fiqh, akhlaq, aadab, history) and **accepted the API terms** (dorar.net/api-services/terms, as published on 2026-11-20) — binding rules in `AGENTS.md` §8.14. ⏸ Waiting for the key. Every one of them online only, through our server, with Dorar's name and link (their terms). **Written terms now exist** (dorar.net/api-services/terms, read 2026-11-20) with an access-request form. What they require: «الدرر السنية» named on every text with its link visible and clickable; the grade never changed, shortened or shown apart from the hadith; no bulk download or full storage, cache at most 24–48 hours; the key only on our server, never in the apps; 60 requests a minute; **a test environment for Dorar to review before publishing**. Consequence: Dorar is a live lookup through our backend (fits §5), not our hadith database and not offline — the hadith texts of F13 come from a verified edition (`P7-D1`). The author fills the access request when the backend exists (`P0-07`). |
| King Fahd Complex — page fonts (1405H) | F2 (default font) | B | ⏸ **Letter sent by the author on 2026-11-20** — waiting for the answer. ☐ Its site still says «جميع الحقوق محفوظة» and the fonts «قريباً» (2026-11-20). Letter to **info@qurancomplex.gov.sa** (phone +966 14 861 5600): permission to ship the page fonts in a free, ad-free application, with the credit they choose. Until an answer: DigitalKhatt Old Madina is the fallback (OFL, same layout). |
| QuranEnc — translations of the meanings and tafsirs | LANG-03, F5 | B | ⏸ **Letter sent by the author on 2026-11-20** — waiting for the answer. ☐ Its terms link led nowhere (2026-11-18). Letter through its contact page, one request covering every translation and tafsir we would ship. |
| Quran Foundation API | F5 (option) | B | ☐ Registration (OAuth2) and its developer terms; only if QuranEnc is not enough. |
| EveryAyah | F3, F4 (per-ayah audio) | B | ⏸ No published terms; **request sent 2026-11-20** through Quran.com's help centre (request #20971, open). |
| Hisn al-Muslim (Sa'id al-Qahtani) | F12, F23, F24 | B | ⏸ **Letter sent 2026-11-20** to info@hisn-almuslim.com (the certified app's support address).  The rights of the edition (the author's foundation or publisher); one letter covering his «شرح أسماء الله الحسنى» too (F39). |
| Tafsir texts | F5, F19, F34 | A or B | ◐ **On QuranEnc (covered by the letter sent 2026-11-20):** al-Mukhtasar (Arabic and about 30 languages), al-Muyassar, al-Sa'di, and three more Arabic works (keys `arabic_nafahat`, `arabic_seraj` — word meanings, useful for F34 — and `arabic_yaseer`), checked on quranenc.com 2026-11-20. **Not on QuranEnc:** Ibn Kathir, al-Tabari, al-Baghawi, al-Qurtubi — each needs its own digital edition and its owner's permission (Quran Foundation API, or a publisher). ☐ |
| Hadith editions (al-Bukhari, Muslim, the Forty) | F13, F29, F35 | A or B | ☐ A verified digital edition with its numbering and a licence that allows shipping (`P7-D1`). sunnah.com was used only to check numbers. |
| Books (F14) and the Lives books (F20 – F22) | F14, F20 – F22 | B | ☐ Classical texts with modern edited editions (تحقيق): the edition's rights per book (`P8-D1`, `P9-D1`). |
| The Names of Allah books | F39 | B | ⏸ **Letters sent by the author on 2026-11-20** to the Ibn Uthaymeen Foundation and Sheikh al-Badr (his site's form confirmed it) — waiting for the answer. ☐ Ibn Uthaymeen «القواعد المثلى» (his foundation), al-Sa'di's explanation (its edition), al-Qahtani, al-Badr. |
| The names of the Prophet ﷺ — classical lists | F48 | B | ☐ al-Suyuti, Ibn al-Qayyim and others: the edition's rights. |
| Muezzin recordings | F9 | B | ☐ Origin and permission for each recording (§7.4). |
| Radio streams | F7 | A per station | ☐ Only streams the broadcaster publishes openly (§8.4); the station's page recorded. |
| OpenStreetMap | F46 | A | ☐ ODbL: attribution and share-alike — read before F46 is built. |

## Folders

- [`letters/`](letters/README.md) — **eight letters ready to send (2026-11-20)**: King Fahd Complex, QuranEnc, the Ibn
  Uthaymeen Foundation, the rights holders of Hisn al-Muslim, Sheikh al-Badr, Dorar, mp3quran, EveryAyah — each with its
  verified address or form, subject and text in Arabic and English.
- `answers/` — each answer as received, with its date (the author forwards it or saves it).
