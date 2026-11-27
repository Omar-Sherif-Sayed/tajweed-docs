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
| **Surah names in every language** (`P1-D3`) | The Quran Foundation's chapters (`translated_name` per language, English as the fallback) | ✔ Their documentation says so; ✘ our token is refused the scope `content.chapters.read` | The author asks for the scope `content.chapters.read` in the Quran Foundation's console (the app's scopes) |
| More Arabic tafsirs | The Quran Foundation also offers **al-Jalalayn** (926) and **Ibn Ashur, al-Tahrir wa al-Tanwir** (925) | ✔ listed through our account | The author decides whether to add them to `content/reviewed/tafsirs.csv` |
| **Hadiths of blessed days (F35), virtues (F29) and of adhkar** | **HadeethEnc** — written permission held (`docs/permissions/answers/09-…`) | ✔ permission; ☐ which of these hadiths HadeethEnc has (its categories) | Read HadeethEnc's categories for fasting, the days, adhkar and virtues; what it has can be built now, with its grade and credit |
| **Zakat (F42)** — the nisab and the rules | **Dar al-Ifta al-Misriyyah** (Egypt's official fatwa body): fatwa 16827 (the nisab in Egyptian currency: 85 g of gold, 2.5 %), fatwa 21692 (why the nisab is reckoned in 21-carat gold: 97.14 g in 21 carat, 85 g of pure gold) | ✔ the fatwa pages exist on `dar-alifta.org` (search of 2026-11-27); ☐ their text read in full, and the site's terms for quoting | The author chooses the fatwa body (Dar al-Ifta of Egypt, or the Saudi Permanent Committee — they differ on the carat); the calculator then follows that body only, says so, and is checked against its worked examples |

## 2. Waiting — no free source found; a letter is the way

| Need | What was found | Next step |
| --- | --- | --- |
| **Adhkar, duas, misbaha, ruqyah** (F12, F23, F24, F38) — «حصن المسلم» | Letter 07 sent 2026-11-20, no answer. A lead: a printed edition (42nd printing, 1436H / 2015) is reported to carry a notice allowing anyone to print it and distribute it **free of charge without deleting anything** — read only in a poor scan (archive.org), not confirmed. Arabic Wikisource hosts the title with no permission stated (category «نصوص مجهولة المصدر») — not usable | **The author can photograph the notice in his own printed copy** (the page with «حقوق الطبع»): if it grants free reproduction without change, the agent records it in `docs/permissions/answers/` and the author decides whether it is enough for an app |
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
**A wide area from our server is the better choice**, and it respects every term above. It needs: (1) a new table
(proposed: `osm_mosque` — pk_id, osm_type, osm_id, name, name_ar, latitude, longitude, cell (the ~100 km square),
osm_timestamp, imported_at, audit; unique (osm_type, osm_id)) — ☐ the author approves the columns; (2) the import job
(Geofabrik extracts filtered to `amenity=place_of_worship` + `religion=muslim`); (3) the published ODbL copy of the
table and the credit in the app and in Sources.

## Sources read

- King Fahd Complex: `qurancomplex.gov.sa` — the e-book news of «التجويد الميسر», `books-audios/`, `emarket.qurancomplex.gov.sa`.
- Quran Foundation: our own account (resources: tafsirs, translations; scopes granted and refused), `api-docs.quran.foundation` (list chapters).
- Dar al-Ifta: `dar-alifta.org/ar/fatwa/details/16827`, `…/21692`, `…/17117`.
- OpenStreetMap: `operations.osmfoundation.org/policies/tiles/`, `…/policies/nominatim/`, `wiki.openstreetmap.org/wiki/Overpass_API`, `osmfoundation.org/wiki/Licence/Attribution_Guidelines`, `openstreetmap.org/copyright`, `download.geofabrik.de`.
- Hisn al-Muslim: archive.org scan (7sn-muslem), `ar.wikisource.org/wiki/حصن_المسلم`.
- IslamHouse: `islamhouse.com/ar/`, `github.com/IslamHouse-API`. Ibn Baz Foundation: `binbaz.org.sa/privacy-policy`, `/about`. sunnah.com: `/about`, `/llms.txt`. mp3quran: `/api`.
