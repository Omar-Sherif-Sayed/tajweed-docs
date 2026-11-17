# Tanzil Quran text — used by the design prototypes

| | |
| --- | --- |
| File | `quran-uthmani.txt` — **untouched; never edit it, never re-save it in an editor** |
| Source | Tanzil Project — <https://tanzil.net/download/> |
| Version | Tanzil Quran Text (Uthmani, Version 1.1) |
| Downloaded | 2026-11-17, with the author's permission, accepting Tanzil's terms of use |
| Options chosen on the download page | Text type **Uthmani** · format **Text (with aya numbers)** · pause marks **on** · sajdah signs **on** · rub-el-hizb signs **off** · tatweel below superscript alefs **on** (the page's default options) |
| Download address | `https://tanzil.net/pub/download/index.php?marks=true&sajdah=true&tatweel=true&quranType=uthmani&outType=txt-2&agree=true` |
| Size | 1,396,087 bytes |
| SHA-256 | `6933e133dd56db778c801bf738848454e43648105a151e8d84d86a7cae39ec5f` |
| Checked | 6,236 ayah lines · 114 surahs · UTF-8 · the copyright block is at the end of the file |
| Licence | Creative Commons Attribution 3.0. Verbatim copies may be distributed; **changing the text is not allowed**; the source (Tanzil Project) must be shown with a link to tanzil.net; the copyright notice stays in the file. |

Line format: `surah|ayah|text`. From surah 2 on, the first ayah of a surah begins with the basmala (except
surah 9).

`.gitattributes` marks this file `-text`, so Git never changes its line endings and the checksum stays true.

## Status

This copy serves the **design prototypes only**. The final choice of the Quran text for the applications (this
text or the King Fahd Complex text), its options and its font is task `P0-12`; the file then moves to the backend
repository and gets its entry in the register of content sources (`docs/data-sources/README.md`).
