# Design elements

The logo, the icons and the drawings of the three designs as standalone SVG files, kept here and in Figma (the
author, 2026-11-19: "the logo and any design used in the design rounds made in Figma and saved with the docs, to be
used at any time").

| Folder | Holds |
| --- | --- |
| `design-1/` | `logo.svg` (the eight-pointed star — two squares, never a cross shape) and `icons/` (34 icons) |
| `design-2/` | `logo.svg` (the coin medallion), `prayer-dial.svg`, `colonnade.svg` (palm trunks under a roof of palm fronds) and `icons/` (30) |
| `design-3/` | `logo.svg` (an arc of light over the horizon), `landscapes/` (46: each of the 23 directions, day and night), `landscapes-earlier/` (the 20 drawings replaced on 2026-11-20, kept at the author's request) and `icons/` (30) |
| `manifest.json` | Every file with its size |

- **Made by** [`../prototypes/tools/export_elements.py`](../prototypes/tools/export_elements.py) from the pages
  themselves: the icons are the pages' own symbols, the logos and the colonnade follow the pages' drawing code, and
  the landscapes are drawn by the page's own `scene()` function (run with Node). Nothing is redrawn by hand, so a
  file here and the prototype cannot disagree — run the script again after a design changes.
- **Colours:** each file uses its design's first direction, day (the icons in its primary colour). The colours of
  every direction, day and night, are in the tokens files and on the Figma pages.
- **In Figma:** the file «Tajweed — designs» (<https://www.figma.com/design/K5RXq2tO1sVE7RwlJ9dD1L>), one page per
  design, frame "Design N — elements": the same elements as editable vectors, and the colour swatches.
  [`../prototypes/tools/figma_import_code.py`](../prototypes/tools/figma_import_code.py) writes the code that
  imports them. These SVG files are the source.
- **Rules kept in every element** (`AGENTS.md` §8.10, §8.11): no cross shape (no plus sign, no four-armed star); no
  picture of any prophet or Companion; no word of the Quran inside a logo.
- Licence: CC BY 4.0, as the rest of this repository (`LICENSE`).
