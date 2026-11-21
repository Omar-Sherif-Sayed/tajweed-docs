# Design

The design of the three applications (web, Android, iPhone) is made once, here. Rules and background: parent
[`AGENTS.md`](../../AGENTS.md) §13 and §8.1; task `P0-11` in [`../plan/execution-plan.md`](../plan/execution-plan.md).

**Names (the author, 2026-11-19): round N = design N.** One file per design; a later change to a design stays in
the same file (its history is in git). The first names, used in the session records, were: design 1 =
`colour-directions.html` (first pass) + `round-2.html` (second pass), design 2 = `round-3.html`, design 3 = `round-4.html`.

| File | What it is | State |
| --- | --- | --- |
| [`prototypes/round-1.html`](prototypes/round-1.html) | **Design 1 (round 1)** — one up-to-date file since 2026-11-19 (the first and second passes together): the three colour directions A emerald and gold, B teal and sand, C "mushaf", light and dark, on every screen — first launch on one screen with the searchable list of the 22 languages, home, mushaf pages 1, 2, 5, 545, 546 exactly as printed in six Quran fonts, the reading view by surah with the ayah actions, the player with the "reconnecting" state, Sources, the Lives screens; the two-page view, the font comparison, the palette with its contrast table. All 22 languages. One file (3.2 MB, fonts inside). | reviewed (2026-11-17): first launch accepted, default font chosen — King Fahd page fonts; one of the three designs |
| [`prototypes/round-2.html`](prototypes/round-2.html) | **Design 2 (round 2) — "early Islam" (صدر الإسلام).** Nine colour directions (Parchment, Madinah, Makkah, Al-Quds, Gardens, Two seas, Lamps, Honey, Mountains — high contrast, for low vision and colour blindness), a colour-vision preview, the mushaf index and the surah details: first launch, home, mushaf page (King Fahd page fonts), prayer times by location, Sources, "Why these colours?" (F19 draft), index, the Lives screens, the web reader with two pages, the directions and the icons with their reasons. All 22 languages. | one of the three designs |
| [`prototypes/round-3.html`](prototypes/round-3.html) | **Design 3 (round 3) — "the first era" (عصر النبي ﷺ والصحابة والخلفاء الراشدين).** Twelve colour directions, each in day and night, each with its own landscape: the first sheets, Hira, the Cave, Taybah, Uhud, "look at the camels", dawn, the forenoon, rain, the two gardens, light — and the last, Mountains, the only one for low vision and colour blindness. The prayer times on the path of the sun; a logo of an arc of light over the horizon; Amiri headings; the Lives screens. All 22 languages. | one of the three designs |
| **The Lives screens (F20, F21, F22)** — in all three designs | A group «السِّيَر» on the home screen; a Lives screen with three tabs (prophets — index; Companions — groups; Rightly Guided Caliphs — timeline) and one sample entry (Nuh عليه السلام, with 71:1 copied from Tanzil). Only names beyond doubt are shown; every story, hadith, date and event is a dashed placeholder naming its source book (`AGENTS.md` §8.11). No picture of any prophet or Companion. Written by `tools/build_lives.py`. | design sample (2026-11-19) |
| **The new screens (F23 – F29), 2026-11-20** — in all three designs | Home tiles for the misbaha and the duas (and the radio again in designs 2 and 3); **the Hijri date and the time at the top of the home screen**; the misbaha; **the adhkar like the Hisn al-Muslim application** — all chapters («فضل الذكر» first), then one dhikr per page with its count, its source and a counter at the bottom right (Ayat al-Kursi and the last three surahs copied from Tanzil); **the duas by category** (seven Quran duas copied from Tanzil, a dua may be in more than one category, the Sunnah duas as placeholders); **the ayah markers in the tint look, covering the ayah and its number** (the author's choice; the ribbon removed); the actions on an ayah or a range (markers, reciter, range, repeat, all tafsirs, download, virtue); the Hijri calendar (Umm al-Qura, −2 … +2) with the device's time. The day / night choice is one switch beside the colour directions. Written by `tools/build_extras.py`; texts in `i18n/extras/`. Changed on the author's second message of 2026-11-20. | design sample |
| [`elements/`](elements/) | **The design elements as SVG files** (the author, 2026-11-19): the logo and every icon of each design, design 2's colonnade and prayer dial, design 3's 56 landscapes (28 directions × day / night) and, in `landscapes-earlier/`, the 32 drawings replaced on 2026-11-20; `manifest.json` lists them. Exported from the pages by `tools/export_elements.py` (nothing redrawn by hand). | 135 files |
| [Figma — «Tajweed — designs»](https://www.figma.com/design/K5RXq2tO1sVE7RwlJ9dD1L) | One page per design (Design 1, 2, 3), each with one frame "Design N — elements": the logo, the drawings / landscapes and the icons as **editable vectors** made from the SVG files above, and the colours of every direction, day and night. The SVG files here stay the source: after a change, `tools/figma_import_code.py` writes the import code again. The full screens stay in the HTML prototypes (the mushaf pages need the King Fahd page fonts, which Figma cannot use). | imported 2026-11-19 |
| [`design-2-meanings.md`](design-2-meanings.md) | **Why every colour, icon and the logo of design 2 was chosen** — from the Quran, the hadith and the first era; what was avoided and why; the rules of the in-app section F19. The ayah table is generated. | ⏸ the author reads it |
| [`tokens-design-2.json`](tokens-design-2.json) | The nine directions of design 2, day and night (generated from `prototypes/tools/design2_palettes.py`). | draft |
| [`design-3-meanings.md`](design-3-meanings.md) | **Why every colour, landscape and mark of design 3 was chosen** — each direction from a place or a moment of the first era or from words of the Quran, with its ayah or hadith reference; what was left out and why. The ayah table is generated. | ⏸ the author reads it |
| [`tokens-design-3.json`](tokens-design-3.json) | The twelve directions of design 3, day and night, with the landscape colours (generated from `prototypes/tools/design3_palettes.py`). | draft |
| [`prototypes/i18n/`](prototypes/i18n/) | The interface texts of the 20 languages after Arabic and English, **one folder per round**: `round1/` (design 1, 81 texts), `round2/` (design 2, 122 texts), `round3/` (the 53 texts design 3 adds to design 2's), `lives/` (the 28 texts of the Lives screens) and `extras/` (the 74 texts of the screens of 2026-11-20), the last two shared by the three designs. Each folder: `keys.json` (id, English, Arabic) and one file per language. **Translations by the agent**, corrected from users' reports on GitHub (no native readers, the author's decision 2026-11-19; `LANG-02`). Written by `tools/write_round1_i18n.py`, `write_round3_i18n.py`, `write_lives_i18n.py`, `write_extras_i18n.py` (design 2's keys by `extract_i18n_keys.py`), checked by `tools/i18n_check.py` in every build. | by the agent |
| [`tokens.json`](tokens.json) | The colours of design 1's three directions, light and dark. | all three directions kept (decision 2026-11-17) |
| [`prototypes/assets/`](prototypes/assets/) | The untouched source files (Quran text, metadata, page layout, fonts) with checksums, origins and licences. | see its README |
| [`prototypes/tools/`](prototypes/tools/) | `verify_mushaf_layout.py` (checks the layout against Tanzil); `build_round1.py`, `build_round2.py`, `build_round3.py` (each writes its page's data, fonts, colours and texts, after every check); `build_lives.py` (the Lives screens into the three pages); `build_extras.py` (the screens of 2026-11-20 and the day / night switch); `build_design3_screens.py` (design 3 only, 2026-11-21: the 28 remaining screens in six batches; texts by `write_design3_screens_i18n.py` in `i18n/design3-screens/`); `build_design3.py` (design 3 only, 2026-11-21: the home order, «كل الأقسام», the scholars, the library, the Sources screen; texts by `write_design3_i18n.py` in `i18n/design3/`); `build_quran_sample.py` (the ayahs of design 1's reading view); `design2_palettes.py`, `design3_palettes.py` (the directions and their checks); `i18n_check.py`; `export_elements.py`, `figma_import_code.py`; `read_font_licence.py`. Build order: `build_round1.py`, `build_round2.py`, `build_round3.py`, then `build_lives.py`, `build_extras.py`, `build_design3.py`, `build_design3_screens.py` and `export_elements.py`. Nobody types Quran text. | — |

## Design 3 — "the first era" (round 3)

Asked by the author on 2026-11-19 (as "round 4"): design 2 stays as it is; a new design, much better, taken from the time of the
Prophet ﷺ, the Companions and the Rightly Guided Caliphs, with many directions drawn from reflection on the Quran,
each with a day and a night theme; only the last direction is for low vision and colour blindness.

- **Twelve directions**, each a place or a moment of the first era or words of the Quran, each with its own
  landscape drawn in its own colours (home screen, web reader, the cards of the first launch): the first sheets
  (al-Bukhari 4986), Hira (al-Bukhari 3, 96:1–4), the Cave (9:40), Taybah (50:10), Uhud (al-Bukhari 4084), "look at
  the camels" (88:17–20), dawn (89:1, 81:18), the forenoon — its night theme is the still night (93:1–2), rain
  (22:63), the two gardens (55:64, 55:68), light (24:35), and Mountains (35:27). The reasons: `design-3-meanings.md`.
- **Checks on every build** (`tools/build_round3.py`): the checksums, the layout and the King Fahd glyphs against
  Tanzil, the 20 cited ayahs copied whole and checked, the 13 excerpts of the meanings document word for word,
  4.5 : 1 for every text of the eleven ordinary directions and the six night rules, 7 : 1 for Mountains also as
  simulated for the three kinds of colour blindness, and the interface texts of the 20 other languages.
- **New in the screens:** the prayer times on the path of the sun (the day runs in the reading direction), the logo
  as an arc of light over the horizon, Amiri headings, grain only in the first direction.
- The new texts of design 3 (direction names, design notes) are translated into all 20 other languages.
- **No cross shape anywhere** (the author, 2026-11-19): the star of the Light direction is a round dot; the knuckle
  marks of the dhikr hand, the rings across the pillars of the home icon, the equator of the language globe (all in
  designs 2 and 3) and the four-armed star and the plus of the counter (design 1) were changed.

Start state in the address: `round-3.html#taybah-dark-ar-5` (direction, theme, language, page).

Checked in a browser on 2026-11-19: 12 directions × day / night × 22 languages — every screen drawn (index, Sources,
"Why", the web side list, the landscapes, the six points of the sun path), no console error; no sideways scroll at
phone width. Fixed during the check: the surah names of the web side list stopped the page in the 21 languages other
than Arabic (designs 2 and 3); the web landscape was cut on a wide screen and became a card in the side list.

## Design 2 — "early Islam" (round 2)

Asked by the author on 2026-11-17: a simple, beautiful design that speaks of the art of the first era of Islam,
beside the existing design, so that one of the two is chosen for web, Android and iPhone.

| Element | Inspired by | Where it is used |
| --- | --- | --- |
| Parchment and brown-black ink | the earliest Quran manuscripts, written on parchment | backgrounds (with a faint grain drawn by the browser), text |
| Red dots | early copies marked the vowels with red dots (a system attributed to Abu al-Aswad al-Du'ali, d. 69 AH) | the active item, the page number, small marks — never on the Quran text |
| Verse-end dots | early manuscripts end a verse with a group of dots or strokes | the divider between sections |
| Palm trunks, palm-frond roof, mud brick | the Prophet's mosque — walls of mud brick, a roof of palm fronds, pillars of palm trunks, as Ibn Umar describes it in Sahih al-Bukhari 446 (dorar.net/h/wVDAbFDs) | the band at the top of the home screen; the brick texture of the prayer card; no arches, no domes (they came later) |
| Rings and a dotted border | early Islamic coins | the logo; the prayer dial |
| Kufic letters | the script of the early Quran manuscripts | headings, in Noto Kufi Arabic (a modern font, OFL 1.1) |

Nine colour directions, each in day and night: Parchment, Madinah, Makkah, Al-Quds, Gardens, Two seas, Lamps,
Honey, and Mountains. Every text / background pair is at least 4.5 : 1. **Mountains is the only direction made for
colour blindness and weak sight** (the author's decision, 2026-11-18): 7 : 1, also as simulated for the three kinds
of colour blindness (checked by `tools/design2_palettes.py` on every build; the "Colour vision" switch shows the
same simulation). The reason for each colour and icon: `design-2-meanings.md`. The Quran page is the same as in design 1: the King Fahd page fonts, one text colour.
**Night themes (2026-11-18):** the eight directions other than Mountains follow six rules for night reading, checked
on every build — a deep tinted background (not black), cards lighter step by step, the mushaf page a little lighter
than the background, soft body text (11 – 16 : 1), calm accents, and no bright block. Mountains stays at full
strength. The first-launch screen lists the planned languages by their own names (`AGENTS.md` §8.9).

Start state in the address: `round-2.html#gardens-dark-en-545` (direction, theme, language, page).

Third pass checked on 2026-11-18: 9 directions × day / night × Arabic / English × 5 pages — no line wider than
its page, every cited ayah present, no console error; the index (114 surahs, 30 juz) and the surah details;
the colour-vision preview.

Checked in a browser on 2026-11-17: pages 1, 2, 5, 545, 546 in light / dark and Arabic / English — no line wider
than its page, no console error; the web reader with the two pages; the surah start pages in the web side list
read from Tanzil's metadata.

## How to look at design 1 (round 1)

Open `prototypes/round-1.html` in a browser (Chrome, Edge, Firefox). Everything is inside the file except the
Google fonts (Amiri Quran, Scheherazade New, IBM Plex Sans Arabic, Inter and the interface fonts of the other
languages), which need a network connection.

- **Phone 1 — first launch.** Choose a language from the list (22, searchable), a colour direction and light or dark: the whole screen and the example
  change at once, and so do the other phones.
- **Phone 3 — the mushaf page.** Use the arrows or the "Page" switch (1, 2, 5, 545, 546) and the font chips.
- **Phones 4 and 5** are the reading view by surah (with the ayah being recited) and the player.
- **Section 9** shows pages 545 and 546 side by side, to hold next to the printed copy.
- **Section 10** shows the first line of page 5 in the six fonts, with each font's licence.

A start state can be given in the address: `round-1.html#c-dark-en-qcf-545` (direction, theme, language, font, page).

## The six Quran fonts

| Font | Looks like the printed mushaf | Licence | Can ship? |
| --- | --- | --- | --- |
| **King Fahd Complex page fonts (QCF, 1405H)** | Identical — each word is the printed mushaf's own shape | "All rights reserved"; no official licence text found; the author decided to use them and request permission | yes, by the author's decision (2026-11-17); permission letter in `P0-13` |
| **DigitalKhatt Old Madina** | Very close — a font made for the 1405H Madinah mushaf | SIL OFL 1.1 | yes |
| **DigitalKhatt New Madina** | Close — the newer Madinah style | SIL OFL 1.1 | yes |
| **Amiri Quran** | Naskh, classic book style | SIL OFL 1.1 | yes |
| **Scheherazade New** | Naskh, very readable | SIL OFL 1.1 | yes |
| KFGQPC Uthmanic Script HAFS 0.09 | Madinah style | KFGQPC licence (free use, no modification) | ⚠ no — this version does not draw one mark of the verified text (dotted circles) |

## What is real and what is a sample

- **Real:** every Quran word and line. The page layout (DigitalKhatt, old Madinah 1405H) was checked against the
  Tanzil text: 0 differences in 6,236 ayahs; page starts: 0 differences in 604 pages; page 545 matches the author's
  photo; page 5 matches his printed copy. Details: `prototypes/assets/README.md`.
- **Display layers, not part of the text:** the ayah-number signs for the Amiri and Scheherazade rows (the Tanzil text
  has none), the surah header frame, the page header (surah, juz, hizb) and the page number.
- **Sample:** prayer time, "continue reading", the reciter.

## Checked on 2026-11-17

- Pages 1, 2, 5, 545 and 546 in the King Fahd page fonts, DigitalKhatt Old Madina and Amiri Quran; direction A light
  Arabic, B light English, C dark English. Fixed during the check: page 1 was measured before its font arrived (it was
  cut off); the wordmark overlapped the tagline in English.
- No errors in the browser console.
- ⚠ Not checked: every page of every font against a printed mushaf (only the five pages above); lines are justified by
  widening spaces, while the printed mushaf stretches letters — a decision for `P0-12`.

## Checked on 2026-11-19 (one file per design, the Lives screens)

- The three pages in all 22 languages: every text present, no console error; the Lives screens (three tabs and the
  entry) in each; the home screens keep their height with the Lives group (Urdu, the tallest, too). Fixed during
  the check: the Arabic honorific touched a transliterated name; the Lives group was cut on the home screens of
  designs 2 and 3 (made one compact row).
- Figma: the three element frames checked by screenshot.

## Checked on 2026-11-20 (new screens, switch, six directions)

- The three pages in all 22 languages: no console error, no empty text, every home screen fits (the tightest:
  design 1 in Russian, 32 px left). The misbaha counts, the adhkar counter moves on, the switch changes the theme,
  the calendar draws the current Hijri month. Fixed during the check: the class names of the markers screen collided
  with design 2 and 3 styles; design 1's home grew a fourth row of tiles (tiles made a little shorter).
- Design 3: the 18 directions pass the contrast and night checks; the six new and the redrawn landscapes looked at in
  day and night; the river of al-Kawthar and the springs of the Two Gardens redrawn after the first look.
- Figma: the new icons in the three pages; design 3's landscapes and colours updated; checked by screenshot.

## Checked on 2026-11-20, second message (markers, home date, adhkar, duas, radio, landscapes, five directions)

- The three pages in all 22 languages: no console error, no empty text, the home date and time present in every
  language, every home screen fits (the tightest: design 1 in Russian, 15 px left). The dhikr counter counts down and
  turns the page; the duas categories show "also in" for a dua in two categories.
- Every Quran text on the new screens copied from Tanzil and checked to contain its word (2:255, 112 – 114, 7:23,
  71:28, 17:24, 14:40 and the earlier ones); the 29 excerpts of `design-3-meanings.md` checked word for word.
- Design 3: the 23 directions pass the contrast and night checks; every landscape looked at, day and night, on one
  sheet; fixed after the look: al-Kawthar's river (it read as a mound) and its reeds (their blades crossed — now they
  spread from one base), the dark of the cave at night, the olive branch of Light, the water of the sun and the moon.
- Figma: the 30 new and redrawn landscapes placed after a checksum check of each one, the 20 earlier ones kept in a
  section «Earlier landscapes»; ☐ the colour rows of the five new directions (the Starter plan's limit of tool calls
  was reached; values in `tokens-design-3.json`).

## Checked on 2026-11-20, third message (tafsirs, Paradise, the Names)

- Every ayah of design 3 read in al-Sa'di and Ibn Kathir (quran.ksu.edu.sa) and every hadith number checked on
  sunnah.com (al-Bukhari 61, 3251, 3532, 4698, 4878, 4879, 4881, 4964; Muslim 2354, 2355, 2838); the review table is
  `design-3-meanings.md` §3.0. Five landscapes corrected, five Paradise directions added; 28 directions pass the
  contrast and night checks; the 38 excerpts of the meanings document found word for word.
- Every new and changed landscape looked at, day and night, on one sheet; fixed after the look: al-Kawthar's river
  (read as a hill), the trunk and the talh of the extended shade, the trees of fruit hanging near, the tents (made pearl).
- The three pages in all 22 languages: no error, no empty text, every home screen fits; the Names of Allah (14 names
  from 59:22–24, al-Rahman with 1:3 and 59:22) and the names of the Prophet ﷺ (8 from the two Sahihs) in the three.
- ☐ Figma: not updated — the Starter plan's limit of tool calls.

## Checked on 2026-11-21 (design 3 only: home, all sections, scholars, library, Sources)

- The home screen: 16 tiles (the Names of Allah, the names of the Prophet ﷺ, memorisation and «كل الأقسام» added beside the radio and the rest) and the Lives last with four parts — it fits the phone in Arabic.
- «كل الأقسام»: F1 – F51 exactly once (checked by the script), the Lives the last group; a drawn section opens its screen.
- The scholars: 53, each once in the group order and once in the time order (checked by the script); the order by time follows the year of death and is a draft until every year is copied from the biographies (`P9-D5`). No date and no biography is typed: the sample entry shows placeholders naming its sources.
- The library: 65 books, every author one of the 53 (or named, for «تحفة الأطفال»); «الداء والدواء» present.
- The Sources screen: 25 sources — 11 verified, 7 letters sent, 3 letters ready, 4 to check.
- All 22 languages, day and night: no error; designs 1 and 2 unchanged by the build.

## Checked on 2026-11-21, second message (the 28 remaining screens)

- All 22 languages: no error, no empty screen or title; Arabic, English and Urdu at night looked at screen by screen; the Qibla text measured on the page (number first, then «من الشمال», right to left).
- Ayahs copied from Tanzil and checked by a word: 67:1 – 5, 1:2, 94:5 – 6; the search sample «الصبر» — whole words only — found 4 ayahs (2:45, 2:153, 90:17, 103:3).
- «كل الأقسام»: 48 of the 51 features drawn, F28 and F47 inside another screen, F11 a behaviour.
- The map's streets redrawn after the look: four-way crossings made plus shapes; now only T-junctions and a curve.

## Next

1. ✔ The author reviewed design 1 (2026-11-17): default Quran font — the King Fahd page fonts; the quarter sign is
   at 15:49 in his printed copy.
2. The author chooses design 1 (`round-1.html`), design 2 (`round-2.html`) or design 3 (`round-3.html`).
3. Then, in the chosen design: the remaining screens in all three directions (reciter picker, search, prayer times with six backgrounds,
   Qibla, radio, adhkar counter, tajweed lesson, hadith, book reader, settings, About), phone and desktop; then Figma.
