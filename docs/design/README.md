# Design

The design of the three applications (web, Android, iPhone) is made once, here. Rules and background: parent
[`AGENTS.md`](../../AGENTS.md) §13 and §8.1; task `P0-11` in [`../plan/execution-plan.md`](../plan/execution-plan.md).

| File | What it is | State |
| --- | --- | --- |
| [`prototypes/round-2.html`](prototypes/round-2.html) | **Round 2 (current).** First launch on one screen (language, colour direction, light / dark, live example); mushaf pages 1, 2, 5, 545, 546 exactly as printed; six Quran fonts to compare; the Sources screen; a two-page view. One self-contained file (3.1 MB, fonts inside). | waiting for the author's review |
| [`prototypes/colour-directions.html`](prototypes/colour-directions.html) | Round 1: the three colour directions on four screens, with the contrast table. | done — all three directions kept |
| [`tokens.json`](tokens.json) | The colours of the three directions, light and dark. Typography, spacing and the prayer backgrounds follow. | all three directions kept (decision 2026-11-17) |
| [`prototypes/assets/`](prototypes/assets/) | The untouched source files (Quran text, metadata, page layout, fonts) with checksums, origins and licences. | see its README |
| [`prototypes/tools/`](prototypes/tools/) | `verify_mushaf_layout.py` (checks the layout against Tanzil), `build_round2.py` (writes the data and fonts into round 2), `build_quran_sample.py` (round 1), `read_font_licence.py` (prints the licence stored in a font). Nobody types Quran text. | — |

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

1. The author reviews round 2: the first-launch screen, the fonts (which one is the default), the page look, the
   Sources screen.
2. The author checks the quarter sign at 15:49 on his printed copy (`prototypes/assets/README.md`).
3. Then: the remaining screens in all three directions (reciter picker, search, prayer times with six backgrounds,
   Qibla, radio, adhkar counter, tajweed lesson, hadith, book reader, settings, About), phone and desktop; then Figma.
