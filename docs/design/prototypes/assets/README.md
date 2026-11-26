# Source files used by the design prototypes

Every file here is **untouched**, exactly as downloaded. Never edit or re-save them; the build scripts stop when a
checksum changes. `.gitattributes` keeps Git from changing their bytes.

These copies serve the **design prototypes only**. The final choice of text, layout and fonts for the applications is
task `P0-12`; then the files move to the backend repository and the register of content sources.

## Files

| File | Bytes | SHA-256 | Source (downloaded 2026-11-17, with the author's permission) | Licence |
| --- | ---: | --- | --- | --- |
| `tanzil/quran-uthmani.txt` | 1,396,087 | `6933e133dd56db778c801bf738848454e43648105a151e8d84d86a7cae39ec5f` | Tanzil — tanzil.net/download (details: `tanzil/README.md`) | CC BY 3.0, no changes allowed |
| `tanzil/quran-data.xml` | 77,234 | `8867c1d88191472adec9db694b3cd9f135b1a2ef580574d32cf888dcb22c5c7a` | Tanzil Quran Metadata 1.0 — tanzil.net/res/text/metadata/quran-data.xml | CC BY 3.0 (Tanzil terms) |
| `digitalkhatt/quran_text_old_madinah.ts` | 1,556,898 | `08972d48c6c250fda4ce9c58a2f23be52c17b0cf097ac093a040e3c392b79f07` | github.com/DigitalKhatt/digitalkhatt.org, commit `4213fab9892774f74f7164c70a70dd84a14f0215`, `ClientApp/src/app/services/` | MIT (`LICENSE-digitalkhatt.org-MIT.txt`) |
| `digitalkhatt/oldmadina.woff2` | 531,000 | `4404019cd8733ee4eff282b54368f4c7e342469bd601c4bfa004b5359c0935cf` | github.com/DigitalKhatt/oldmadinafont, commit `adc60f3865b507684bda856d59940a7f3602be32`, `fonts/` | SIL OFL 1.1 (`LICENSE-oldmadinafont-OFL.txt`) |
| `digitalkhatt/DigitalKhattV2.ttf` | 915,252 | `ab495b5abb2ed30b2ffda022f2a1d10a25bfab7ea0a4dbb4ce05d5c171959c78` | github.com/DigitalKhatt/digitalkhatt.org, same commit, `ClientApp/src/assets/fonts/coretext/` ("DigitalKhatt New Madina") | SIL OFL 1.1 — stated inside the font; `LICENSE-madinafont-OFL.txt` from github.com/DigitalKhatt/madinafont (commit `9aeb02c26d8dae4c032820733466c1ee9137e6d6`) |
| `kfgqpc/UthmanicHafs1 Ver09.otf` | 246,428 | `59e20b2403687a67854fd199861abed3528068c035d2689898465d5faf39bb31` | Mirror github.com/nuqayah/qpc-fonts, commit `8a4f39d563ea69c994416a1692827e38156c548d`, `various/` | KFGQPC licence inside the font (below) |
| `kfgqpc/mushaf.txt` | 301,462 | `307c073476a759ef182bb67229c05a843c5eecce91a81119c349951e421703f3` | Same mirror — one line per ayah: `page,glyphs` of the page fonts | none stated |
| `kfgqpc/QCF_P001.TTF` | 80,604 | `85099681c9a6e4aba8ad01885c212ba3af724c002cf5bb65d82afc5da8024623` | Same mirror, `mushaf/` — King Fahd Complex page font, page 1 | "King Fahad Complex, All rights reserved." |
| `kfgqpc/QCF_P002.TTF` | 83,428 | `6d6ce98f3ba8dd38715ee4c84fc5daf0966d472abed83822feb4a74e03b2f0a9` | idem, page 2 | idem |
| `kfgqpc/QCF_P005.TTF` | 145,864 | `de1ba5401e8434bf5825483713f2cadc3c0ca00476c0f30ad1e62fe4598ff09e` | idem, page 5 | idem |
| `kfgqpc/QCF_P545.TTF` | 145,004 | `9182a7fd37cd623ca97ef96cfc24b30f779765301491db740ec7001890b10219` | idem, page 545 | idem |
| `kfgqpc/QCF_P546.TTF` | 162,748 | `362129554299de80073b59146ee9b5ad1e009db0255adc50eaf23c5f2ab288b4` | idem, page 546 | idem |

## Licences of the King Fahd Complex files

- **KFGQPC Uthmanic Script HAFS (version 0.09, 2010)** — the licence is written inside the font (read on 2026-11-17
  with `../tools/read_font_licence.py`): free of cost, the rights to **use, copy and distribute**; the font
  may **not be sold, modified, altered, translated, reverse engineered, decompiled, disassembled or reproduced**;
  provided "as is"; KFGQPC keeps full ownership. A free application that ships the file unchanged fits these terms.
  ⚠ This version does not draw U+06DF (small high rounded zero), which both verified texts use: dotted circles
  appear. It is not usable as is.
- **KFGQPC Hafs 3.0** (the Complex's official site, 2026-11-26) — the same fault: checked 2026-11-26 in the browser (Chrome) on the Tanzil text from our backend: **U+06DF is drawn as a dotted circle beside the word, not over its letter** (e.g. «ءَامَنُوا۟» in 103:3 — after alef, waw and ya alike); the mark is in 2,240 of the 6,236 ayahs (3,722 times after alef). **Rejected by the author (2026-11-26): «مش هانستخدم أي font فيه مشكلة العلامة الخطأ … أستخدم خطوط تانية»** — no font that shows this mark wrongly is used.
- **QCF page fonts (QCF_P001 … QCF_P604, version 5.10, designed by Harf Information Technology)** — the files say only
  "King Fahad Complex, All rights reserved." The mirror links to a copyright page of the Complex that no longer exists
  (404 on 2026-11-17), and the Complex's own site lists its fonts as «قريباً» (no download). **Decision of the author
  (2026-11-17): use them, credit the Complex, and keep asking for a written licence** — a letter to the Complex is part
  of task `P0-13`. Community copies describe the same terms as the Hafs font (free use, no sale, no modification),
  but none quotes an official text.

## What was verified (`tools/verify_mushaf_layout.py`, 2026-11-17)

| Check | Result |
| --- | --- |
| Words of the DigitalKhatt old-Madinah layout against the Tanzil Uthmani text, ayah by ayah (letters compared, marks and encoding variants ignored) | **0 differences in 6,236 ayahs** |
| Page starts of the layout against Tanzil's Madinah metadata | **0 differences in 604 pages** |
| Lines per page | 15 on every page from 3 to 604 (pages 1 and 2: 8) |
| Page 5 | starts with 2:25; line 1 ends with «جَنَّٰتࣲ»; ayah 2:25 takes lines 1–4 — confirmed by the author on his printed copy |
| Page 545 | line by line the same as the author's photo |
| Pages 1, 2, 263, 264, 546 | line by line the same as the author's photos of 2026-11-17 (his copy: «بالرسم العثماني», printed by دار طيبة, Cairo) |
| Quarter signs (۞) | the layout and the King Fahd glyph data agree with each other everywhere; with Tanzil's metadata they differ at one place: **15:49** (layout, King Fahd) against **15:50** (Tanzil). ✔ The author's printed copy has it at **15:49** (photo of pages 263–264, 2026-11-17): the layout is right there |
| King Fahd glyph data (`mushaf.txt`) | one glyph per word, per pause mark, per quarter sign, per sajdah sign and per ayah end, in all but **9 ayahs** (2:79, 13:37, 18:1, 19:38, 36:52, 69:8, 69:28, 75:27, 83:14 — mostly saktah signs drawn as separate glyphs); the page of 83:35 is given as 588 instead of 589. Handled in task `P0-12`; none is on the prototype pages |
