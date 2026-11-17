# Design

The design of the three applications (web, Android, iPhone) is made once, here. Rules and background: parent
[`AGENTS.md`](../../AGENTS.md) §13; task `P0-11` in [`../plan/execution-plan.md`](../plan/execution-plan.md).

| File | What it is | State |
| --- | --- | --- |
| [`prototypes/colour-directions.html`](prototypes/colour-directions.html) | **Round 1.** Three colour directions on four screens (language choice, home, Quran reader, player), Arabic and English, light and dark, three Quran fonts to compare. One file — open it in any browser. | waiting for the author's choice |
| [`tokens.json`](tokens.json) | The colours of the three directions as data. After the choice it keeps one direction and gains typography, spacing, radius and the prayer backgrounds. | draft |
| [`prototypes/assets/tanzil/`](prototypes/assets/tanzil/) | The untouched Quran text file used by the prototypes, with its source, options and checksum. | see its README |
| [`prototypes/tools/build_quran_sample.py`](prototypes/tools/build_quran_sample.py) | Copies a few ayahs from that file into the prototype pages. Nobody types Quran text. | — |

## How to look at round 1

Open `prototypes/colour-directions.html`. Use the four switches at the top: **Direction** (A, B, C), **Theme**,
**Language**, **Quran font**. Below the phones, the page lists the colours of the selected direction and checks the
contrast of every text / background pair (4.5 : 1 or more is required for text).

A start state can be written in the address, for example `colour-directions.html#c-dark-en-amiri`.

| Direction | Idea |
| --- | --- |
| **A · Emerald and gold on parchment** | The classic look of printed mushafs and mosques: deep green, gold lines, warm paper. |
| **B · Deep teal and sand** | Calmer and more modern: blue-green, white cards, sand accents. |
| **C · Mushaf** | After the author's printed mushaf: cream page, black text, dark red and black frame. |

## What is real and what is a sample

- **Real:** the Quran text (surah 1, and surah 2 ayahs 1–5), copied by the script from the Tanzil file, with full
  tashkeel; the ayah counts shown in the surah headers (counted from the same file).
- **Sample:** the prayer name and time, "continue reading", the reciter, the playing position. They only show the
  layout.
- **Display layers added by the page, not part of the text:** the ayah-number signs between ayahs, the highlight of
  the playing ayah, the basmala of surah 2 on its own line.

## Checked on 2026-11-17

- All three directions, light and dark, Arabic (right to left) and English (left to right), were opened and looked at.
- Every text / background pair listed on the page passes 4.5 : 1 in all six combinations.
- The three Quran fonts load and draw the text. ⚠ **Not checked yet:** each tashkeel and pause mark against a printed
  mushaf, font by font — that is part of choosing the text and the font (task `P0-12`).

## Limits of these prototypes

- Fonts come from Google Fonts **for the prototype only** (Amiri Quran, Scheherazade New, Noto Naskh Arabic, IBM
  Plex Sans Arabic, Inter — ☐ the licence of each is recorded before it is used in an application). The applications
  will ship their fonts inside them: no third-party request at run time.
- The font of the Madinah mushaf (King Fahd Complex) is not among the three, because it is not on Google Fonts; it
  is compared in task `P0-12`.
- The reader shows a scrolling page, not yet the 604-page layout.
- Media buttons (previous / play / next) keep the same order in both languages, as in most players.

## Next rounds

1. The author chooses a direction (or asks for changes) and a first opinion on the Quran font.
2. `tokens.json` becomes final for phase 1; the remaining screens are drawn in the chosen direction: reciter picker,
   search, prayer times (six backgrounds), Qibla, radio, adhkar counter, tajweed lesson, hadith, book reader,
   settings, About — phone and desktop width.
3. After approval, the Figma file is made in the author's account.
