# Sources for the waiting features — research of 2026-11-27

The author asked (2026-11-27): «حاجات مستنية مصدر أو مراجع — تقدر تبحث عن مصادر معتمدة للحاجات دي؟». This is what was
found, what is verified, and what each needs next. Nothing here is used before the author chooses it and its rights are
confirmed (`AGENTS.md` §6.8, §6.10). ✔ = read on the official page or checked through our own API access on this date;
☐ = still to verify.

## 1. Strong candidates — usable soon

| Need | Source | Verified | Next step |
| --- | --- | --- | --- |
| **Tajweed (F6)** — the rules and their explanation | **«التجويد الميسر»**, King Fahd Complex, prepared by a committee of the Complex under the supervision of Sheikh Dr. Ali al-Hudhaifi (Hafs from Asim, by way of al-Shatibiyyah); revised edition 1442H / 2020 | ✔ The Complex announced an electronic edition on its digital portal (`qurancomplex.gov.sa`, news page «أطلق المجمع نسخة إلكترونية من كتاب "التجويد الميسر"»; hosted on `epub.qurancomplex.gov.sa`). ✔ The Complex's written answer of 2026-11-26 (`docs/permissions/answers/01b-…`) permits **its electronic publications published on its official site** — unchanged, its rights kept, credited to the Complex, never commercial | ☐ open the e-book on the Complex's portal and record its exact page and edition; the author approves it as the tajweed source; then the lessons are copied verbatim, lesson by lesson. ☐ The Complex's usage policy (asked in letter 01c). This meets rule §6.10: one authoritative source that covers the content and permits its use |
| Tajweed — audio | The Complex's **audio books** (`qurancomplex.gov.sa/books-audios/`) | ✔ The page says digital copies of the listed audio books are offered for general use free of charge, under a ministerial approval | ☐ check whether «التجويد الميسر» is among them; credit the Complex |
| **Translations of the meanings** (§8.9, the 21 languages other than Arabic) | **The Quran Foundation's translations**, under the terms we already follow (Content Sync, credit, never in a repository) | ✔ Read through our own account on 2026-11-27 (scope `content.translations.read` granted): every one of our 21 languages has at least one, including the translators of §8.9 — e.g. Saheeh International (en 20), Bubenheim & Elyas (de 27), Isa García (es 83), Rashid Maash (fr 779), Abu Adel (ru 79), Junagarhi (ur 54), Azizul Haque al-Umari (hi 122), Hamed Choi (ko 219), King Fahd Complex (id 134), Saeed Sato (ja 218), Makin (zh 109), Diyanet (tr 77), Abu Bakr Zakaria (bn 213), Hussein Taji Kal Dari (fa 29), Basmeih (ms 39), Al-Barwani (sw 793), Gumi (ha 115), Helmi Nasr (pt 103), Rowwad (ps 919), Muhammad Sodik (uz 55) | The author chooses one translator per language (only established Sunni translators — §6.10; some on the list are not, e.g. Sayyid Qutb, Maududi, Islahi, Wahiduddin Khan, Israr Ahmad: left out). Then the backend syncs them like the tafsirs. This no longer waits for QuranEnc (letter 02) |
| **Surah names in every language** (`P1-D3`) | The Quran Foundation's chapters: `name_simple` (e.g. «Al-Fatihah»), `name_arabic`, and `translated_name` — the **meaning** of the name | ✔ 2026-11-27: there is no scope `content.chapters.read` in the console; chapters come with **`content.quran.read`, already granted** in production («Read chapters, structure, pages, verses and scripts»), checked with our token: 114 chapters. `translated_name` in its own language for 12 of ours (ar, en, ru, es, it, fr, ur, id, zh, tr, bn, ms); English for the other 10 | Nothing to ask. ☐ The author decides: the transliteration (`name_simple`) for the Latin-script languages, with the meaning beside it where QF has one in that language |
| More Arabic tafsirs | The Quran Foundation also offers **al-Jalalayn** (926) and **Ibn Ashur, al-Tahrir wa al-Tanwir** (925) | ✔ listed through our account | The author decides whether to add them to `content/reviewed/tafsirs.csv` |
| **Hadiths of blessed days (F35), virtues (F29) and of adhkar** | **HadeethEnc** — written permission held (`docs/permissions/answers/09-…`) | ✔ permission; ☐ which of these hadiths HadeethEnc has (its categories) | Read HadeethEnc's categories for fasting, the days, adhkar and virtues; what it has can be built now, with its grade and credit |
| **Zakat (F42)** — the nisab and the rules | **Both, each under its name — the author's decision (2026-11-27)**: **Egypt — Dar al-Ifta al-Misriyyah**: the nisab of money is the value of **85 g of 21-carat gold**, 2.5 % after a full year — fatwa 6203 (4 Dec 1991, Dr. Muhammad Sayyid Tantawi, `dar-alifta.org/ar/fatwa/details/16827`) and fatwa 8426 (11 Aug 2024, Dr. Shawki Allam, `…/21692`, which explains the choice of 21 carat; it goes back to fatwa 12 of 1984). **Saudi Arabia — the Permanent Committee and the Council of Senior Scholars**: the nisab of paper money is **the lower of the two nisabs**, gold or silver («فتاوى اللجنة الدائمة»، المجموعة الأولى 13/444, as quoted by Dorar's Fiqh Encyclopedia `dorar.net/feqhia/2162`); in grams **85 g of pure gold, 595 g of pure silver** (Ibn Uthaymeen and the seminars on contemporary zakat issues, `dorar.net/feqhia/2153`); Shaykh Ibn Baz gives the gold nisab as **92 g** (`binbaz.org.sa/fatwas/18047`) | ✔ every page read in full on 2026-11-27. ✘ The earlier line here («85 g of pure gold = 97.14 g of 21 carat» as Dar al-Ifta's rule) was wrong: that is the Shafi'i / Hanbali view the fatwa reports, not the view it adopts. All three sites reserve their rights — the app **links** the fatwas and uses only the measures (85 g / 21 carat; the lower of 85 g gold and 595 g silver; 2.5 %), never their text | ✔ **Built on the web (2026-11-27)**: `/zakat` — money and savings only, the visitor types the prices, both bodies side by side, the app does not choose. Gold owned, jewellery, trade goods, debts: in the fatwas (they differ, e.g. on jewellery) |

## 2. Waiting — no free source found; a letter is the way

| Need | What was found | Next step |
| --- | --- | --- |
| **Adhkar, duas, misbaha, ruqyah** (F12, F23, F24, F38) — «حصن المسلم» | Letter 07 sent 2026-11-20, no answer. A lead: a printed edition (42nd printing, 1436H / 2015) is reported to carry a notice allowing anyone to print it and distribute it **free of charge without deleting anything** — read only in a poor scan (archive.org), not confirmed. Arabic Wikisource hosts the title with no permission stated (category «نصوص مجهولة المصدر») — not usable | **The author can photograph the notice in his own printed copy** (the page with «حقوق الطبع»): if it grants free reproduction without change, the agent records it in `docs/permissions/answers/` and the author decides whether it is enough for an app — 2026-11-27, the two sites the author sent: **`risala.prh.gov.sa/ar/content/51`** (رسالة الحرمين, the Presidency of Religious Affairs at the Two Holy Mosques — an official Saudi government body): the whole book, fully voweled, with its references, a PDF, and **31 translations** (en, ur, fa, sw, fr, es, tr, ru, id, bn, zh, hi among them) — but its terms of use (`prh.gov.sa/ar/terms-of-use`) reserve every text («جميع المحتويات… ملك لنا») and allow links only ⇒ the best candidate, **with a letter**. `hisnmuslim.com`: no owner, no terms, the text without full tashkeel — not usable |
| **Adhan recordings** (F9) | mp3quran's API has no adhan. No licensed recording of the requested muezzins (al-Minshawi, Abdul Basit, al-Husary, Muhammad Rifaat, Ali Ahmad Mulla, Hamad al-Daghriri) was found. Cambridge's World Oral Literature Project has Cairo mosques' adhans under CC BY-NC-ND 3.0 — other muezzins, and "no derivatives" forbids a short version | Letters: Ali Ahmad Mulla's adhan → the General Authority for the Affairs of the Two Holy Mosques; the Egyptian reciters' adhans → the Egyptian Radio (Maspero) archive. ☐ The author approves the letters |
| **Guides** (F40) — wudu, prayer, Hajj, Umrah | The Ibn Baz Foundation (`binbaz.org.sa`, the official site of his works, e.g. «التحقيق والإيضاح لكثير من مسائل الحج والعمرة», «كيفية صلاة النبي ﷺ»): no reuse terms published (privacy page only) | A letter to the foundation (its e-mail is on its privacy page). ☐ The author approves |
| **Full hadith collections** (Sahih al-Bukhari, Sahih Muslim) | sunnah.com: issue 4480 open; its About page has a section on reproduction (☐ read); Dorar: key pending | Wait for both; HadeethEnc covers a selection meanwhile |
| **IslamHouse** (many free books, guides, translations) | No terms of reuse found on the site; an official API hub on GitHub (`IslamHouse-API`, Riyadh, affiliated with rabwah.sa) states no licence | A letter if one of its books is chosen |
| The Arabic letters' sounds (F41) | None found with a named source | Later |
| Word meanings and asbab al-nuzul (F34) | Not among the Quran Foundation's resources open to us | Later — a named book and its rights |

## 3. F46 — nearby mosques: the three ways compared (the author's question)

The author picked "a wide area from our server" and asked whether it is the best, and whether the direct way would break
anyone's terms. Read on 2026-11-27 on the official pages:

| | Direct from OpenStreetMap (tiles + Overpass) | A wide area from our server |
| --- | --- | --- |
| Tiles (`tile.openstreetmap.org`) | Allowed with conditions: an identifying User-Agent, the credit «© OpenStreetMap contributors» on the map, caching ≥ 7 days; **no offline use, no bulk download**; "best-effort, no SLA", "access may be blocked without prior notice"; and OSM says "we cannot provide a free-of-charge map API or map tiles for third-parties" | No tiles from OSM: the mosques are shown as a list with distance and direction (or on a map we draw), so nothing depends on their tile servers |
| Mosque search (Overpass, `overpass-api.de`) | "No more than 10,000 queries per day … in sum" **for all the app's users together**; "commercial use should use self-hosted or paid servers"; the server "is overloaded" — a growing app would exceed it and be blocked | The data comes once from a regional extract (Geofabrik, ODbL, free, updated daily) and is refreshed by our server; no per-user request goes to OSM |
| Privacy (our rule: the location stays on the device) | The OSM servers see the area each visitor looks at | Our server sees only a ~100 km square, never the exact place |
| Licence | ODbL — credit «© OpenStreetMap contributors» with a link to openstreetmap.org/copyright | The same credit, **and share-alike**: the mosque table we derive is a Derivative Database, so it must be offered under the ODbL (we publish it — easy, it is public data) |

**Answer:** the direct way is not forbidden at a small scale, but it would break the Overpass limit as soon as the app has
users, it may be blocked without notice, and it shows each visitor's area to a third party — against our privacy rule.
**A wide area from our server is the better choice** — ✔ the author chose it (2026-11-27: «خلينا من سيرفرنا لأنه بيحترم
كل الشروط»).

### 3.1 How — revised 2026-11-27 (☐ the tables wait for the author's approval)

The planet's extracts from Geofabrik are tens of gigabytes and need a PBF tool; instead **our server asks Overpass
once per square and keeps the answer**:

- The world is cut into **half-degree squares** (≈ 55 km). The client asks for the 2 × 2 squares around the visitor —
  our server sees a ≈ 110 km area, never the place; the distances are computed on the device.
- The first request for a square: the server sends **one** Overpass query for it (`amenity=place_of_worship` +
  `religion=muslim`, nodes, ways and relations with their centre), with an identifying User-Agent, one query at a
  time, a daily cap far under 10,000 (proposed 2,000), and keeps the answer; refreshed after 30 days; on a failure the
  old answer is served. Overpass then sees only our server and a square.
- `GET /v1/mosques?cell=60:62` (the square's south-west corner × 2) answers with the mosques of the square and the
  credit «© OpenStreetMap contributors», `openstreetmap.org/copyright`; the same data is offered under the ODbL (the
  share-alike of a derived database) — said on the screen, in Sources and in the API's documentation.
- The web shows the list by distance and direction, with no map tiles from OSM.

**Tables (approved before code, AGENTS.md §1):**

| Table | Columns | Constraints |
| --- | --- | --- |
| `osm_mosque_cell` — new (a square asked once; it records an empty square too, so a desert or a sea is not asked again) | `pk_id` serial · `cell` varchar(16) (e.g. `60:62`) · `mosque_count` integer · `fetched_at` timestamptz · `created_at`, `updated_at` | `uk_osm_mosque_cell_cell` unique (`cell`) |
| `osm_mosque` — as proposed, with `cell` now a key to the square | `pk_id` serial · `cell_id` integer → `osm_mosque_cell` · `osm_type` varchar(8) (`node` / `way` / `relation`) · `osm_id` bigint · `name` varchar(300) null · `name_ar` varchar(300) null · `latitude` numeric(9,6) · `longitude` numeric(9,6) · `osm_timestamp` timestamptz null · `imported_at` timestamptz · `created_at`, `updated_at` | `uk_osm_mosque` unique (`osm_type`, `osm_id`); `fk_osm_mosque_cell` (`cell_id`) on delete cascade; `ix_osm_mosque_cell` (`cell_id`) |

Not kept: OSM editors' user names and ids (Overpass returns them with `meta`; only the timestamp is kept).

## Sources read

- King Fahd Complex: `qurancomplex.gov.sa` — the e-book news of «التجويد الميسر», `books-audios/`, `emarket.qurancomplex.gov.sa`.
- Quran Foundation: our own account (resources: tafsirs, translations; scopes granted and refused), `api-docs.quran.foundation` (list chapters).
- Dar al-Ifta: `dar-alifta.org/ar/fatwa/details/16827`, `…/21692` (read in full 2026-11-27), `…/17117`. Dorar's Fiqh Encyclopedia `dorar.net/feqhia/2162`, `/2153`. `binbaz.org.sa/fatwas/18047`.
- Hisn al-Muslim: `risala.prh.gov.sa/ar/content/51`, `prh.gov.sa/ar/terms-of-use`, `hisnmuslim.com`.
- The Quran Foundation's console (the app's permissions, production) and `/content/api/v4/chapters` in 22 languages.
- OpenStreetMap: `operations.osmfoundation.org/policies/tiles/`, `…/policies/nominatim/`, `wiki.openstreetmap.org/wiki/Overpass_API`, `osmfoundation.org/wiki/Licence/Attribution_Guidelines`, `openstreetmap.org/copyright`, `download.geofabrik.de`.
- Hisn al-Muslim: archive.org scan (7sn-muslem), `ar.wikisource.org/wiki/حصن_المسلم`.
- IslamHouse: `islamhouse.com/ar/`, `github.com/IslamHouse-API`. Ibn Baz Foundation: `binbaz.org.sa/privacy-policy`, `/about`. sunnah.com: `/about`, `/llms.txt`. mp3quran: `/api`.
