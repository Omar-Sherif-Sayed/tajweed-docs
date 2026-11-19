# Design

The design of the three applications (web, Android, iPhone) is made once, here. Rules and background: parent
[`AGENTS.md`](../../AGENTS.md) §13 and §8.1; task `P0-11` in [`../plan/execution-plan.md`](../plan/execution-plan.md).

| File | What it is | State |
| --- | --- | --- |
| [`prototypes/round-4.html`](prototypes/round-4.html) | **Round 4 (current) — design 3, "the first era" (عصر النبي ﷺ والصحابة والخلفاء الراشدين).** A new design for the same application with **twelve colour directions**, each in day and night, each with its own landscape: the first sheets, Hira, the Cave, Taybah, Uhud, "look at the camels", dawn, the forenoon, rain, the two gardens, light — and the last, Mountains, the only one for low vision and colour blindness. The prayer times on the path of the sun; a new logo (an arc of light over the horizon); Amiri headings. The same screens as round 3, in all 22 languages. One file (1.4 MB). | waiting for the author's choice among designs 1, 2 and 3 |
| [`prototypes/round-3.html`](prototypes/round-3.html) | **Round 3 — design 2, "early Islam" (صدر الإسلام).** A second, simpler design to compare with design 1, with **nine colour directions** (Parchment, Madinah, Makkah, Al-Quds, Gardens, Two seas, Lamps, Honey, Mountains — high contrast, for low vision and colour blindness), a colour-vision preview, the mushaf index and the surah details: first launch, home, mushaf page (King Fahd page fonts), prayer times by location, Sources, "Why these colours?" (F19 draft), the web reader with two pages, the directions and the icons with their reasons. One file (1.2 MB). | kept as it is (the author, 2026-11-19); one of the three designs |
| [`prototypes/round-2.html`](prototypes/round-2.html) | **Round 2 — design 1.** First launch on one screen (language, colour direction, light / dark, live example); mushaf pages 1, 2, 5, 545, 546 exactly as printed; six Quran fonts to compare; the Sources screen; a two-page view. One self-contained file (3.1 MB, fonts inside). | reviewed (2026-11-17): first launch accepted, default font chosen — King Fahd page fonts |
| [`prototypes/colour-directions.html`](prototypes/colour-directions.html) | Round 1: the three colour directions on four screens, with the contrast table. | done — all three directions kept |
| [`design-2-meanings.md`](design-2-meanings.md) | **Why every colour, icon and the logo of design 2 was chosen** — from the Quran, the hadith and the first era; what was avoided and why; the rules of the in-app section F19. The ayah table is generated. | ⏸ the author reads it |
| [`tokens-design-2.json`](tokens-design-2.json) | The nine directions of design 2, day and night (generated from `prototypes/tools/design2_palettes.py`). | draft |
| [`design-3-meanings.md`](design-3-meanings.md) | **Why every colour, landscape and mark of design 3 was chosen** — each direction from a place or a moment of the first era or from words of the Quran, with its ayah or hadith reference; what was left out and why. The ayah table is generated. | ⏸ the author reads it |
| [`tokens-design-3.json`](tokens-design-3.json) | The twelve directions of design 3, day and night, with the landscape colours (generated from `prototypes/tools/design3_palettes.py`). | draft |
| [`prototypes/i18n/`](prototypes/i18n/) | The interface texts of rounds 3 and 4: `keys.json` (122 texts, English and Arabic) and one file per language for the other 20 — **drafts by the agent**, to be read by native speakers (`LANG-02`). Checked by `build_round3.py`. | drafts |
| [`tokens.json`](tokens.json) | The colours of the three directions, light and dark. Typography, spacing and the prayer backgrounds follow. | all three directions kept (decision 2026-11-17) |
| [`prototypes/assets/`](prototypes/assets/) | The untouched source files (Quran text, metadata, page layout, fonts) with checksums, origins and licences. | see its README |
| [`prototypes/tools/`](prototypes/tools/) | `verify_mushaf_layout.py` (checks the layout against Tanzil), `build_round2.py` (writes the data and fonts into round 2), `build_round3.py` (the same for round 3, plus the six directions, the cited ayahs and the check of every excerpt in `design-2-meanings.md`), `design2_palettes.py` (the directions and their contrast check), `build_round4.py` and `design3_palettes.py` (the same for round 4 — twelve directions, the cited ayahs, the excerpts of `design-3-meanings.md`), `build_quran_sample.py` (round 1), `read_font_licence.py` (prints the licence stored in a font). Nobody types Quran text. | — |

## Design 3 — "the first era" (round 4)

Asked by the author on 2026-11-19: round 3 stays as it is; a new design, much better, taken from the time of the
Prophet ﷺ, the Companions and the Rightly Guided Caliphs, with many directions drawn from reflection on the Quran,
each with a day and a night theme; only the last direction is for low vision and colour blindness.

- **Twelve directions**, each a place or a moment of the first era or words of the Quran, each with its own
  landscape drawn in its own colours (home screen, web reader, the cards of the first launch): the first sheets
  (al-Bukhari 4986), Hira (al-Bukhari 3, 96:1–4), the Cave (9:40), Taybah (50:10), Uhud (al-Bukhari 4084), "look at
  the camels" (88:17–20), dawn (89:1, 81:18), the forenoon — its night theme is the still night (93:1–2), rain
  (22:63), the two gardens (55:64, 55:68), light (24:35), and Mountains (35:27). The reasons: `design-3-meanings.md`.
- **Checks on every build** (`tools/build_round4.py`): the checksums, the layout and the King Fahd glyphs against
  Tanzil, the 20 cited ayahs copied whole and checked, the 13 excerpts of the meanings document word for word,
  4.5 : 1 for every text of the eleven ordinary directions and the six night rules, 7 : 1 for Mountains also as
  simulated for the three kinds of colour blindness, and the interface texts of the 20 other languages.
- **New in the screens:** the prayer times on the path of the sun (the day runs in the reading direction), the logo
  as an arc of light over the horizon, Amiri headings, grain only in the first direction.
- The new texts of round 4 (direction names, design notes) are in Arabic and English; the other 20 languages show
  them in English until they are drafted and read by native speakers (`LANG-02`).

Start state in the address: `round-4.html#taybah-dark-ar-5` (direction, theme, language, page).

Checked in a browser on 2026-11-19: 12 directions × day / night × 22 languages — every screen drawn (index, Sources,
"Why", the web side list, the landscapes, the six points of the sun path), no console error; no sideways scroll at
phone width. Fixed during the check: the surah names of the web side list stopped the page in the 21 languages other
than Arabic (rounds 3 and 4); the web landscape was cut on a wide screen and became a card in the side list.

## Design 2 — "early Islam" (round 3)

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

Start state in the address: `round-3.html#gardens-dark-en-545` (direction, theme, language, page).

Third pass checked on 2026-11-18: 9 directions × day / night × Arabic / English × 5 pages — no line wider than
its page, every cited ayah present, no console error; the index (114 surahs, 30 juz) and the surah details;
the colour-vision preview.

Checked in a browser on 2026-11-17: pages 1, 2, 5, 545, 546 in light / dark and Arabic / English — no line wider
than its page, no console error; the web reader with the two pages; the surah start pages in the web side list
read from Tanzil's metadata.

## How to look at round 2

Open `prototypes/round-2.html` in a browser (Chrome, Edge, Firefox). Everything is inside the file except four
Google fonts (Amiri Quran, Scheherazade New, IBM Plex Sans Arabic, Inter), which need a network connection.

- **Phone 1 — first launch.** Tap a language, a colour direction and light or dark: the whole screen and the example
  change at once, and so do the other phones.
- **Phone 3 — the mushaf page.** Use the arrows or the "Page" switch (1, 2, 5, 545, 546) and the font chips.
- **Section 5** shows pages 545 and 546 side by side, to hold next to the printed copy.
- **Section 6** shows the first line of page 5 in the six fonts, with each font's licence.

A start state can be given in the address: `round-2.html#c-dark-en-qcf-545` (direction, theme, language, font, page).

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

## Next

1. ✔ The author reviewed round 2 (2026-11-17): default Quran font — the King Fahd page fonts; the quarter sign is
   at 15:49 in his printed copy.
2. The author chooses design 1 (round 2), design 2 (round 3) or design 3 (round 4).
3. Then, in the chosen design: the remaining screens in all three directions (reciter picker, search, prayer times with six backgrounds,
   Qibla, radio, adhkar counter, tajweed lesson, hadith, book reader, settings, About), phone and desktop; then Figma.
