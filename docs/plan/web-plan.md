# Web plan — `tajweed-frontend` scaffold (`P0-08`), proposal of 2026-11-26

The author (2026-11-26): «تمام ممكن تبدأ ال web ال angular». The rules: `AGENTS.md` §1 (plan, ask, then code; TSDoc
everywhere; 22 languages), §4.1 – §4.2 (Angular 22, Material, Tailwind), §10 (structure and conventions), §13 (design
3). The contract the web follows: `tajweed-backend/docs/api/client-guide.md`.

## 1. Versions — read on npm, 2026-11-26

| Part | Version | Note |
| --- | --- | --- |
| Node | 22.23.5 (installed) | ✔ inside Angular 22.3's range (`^22.22.3 \|\| ^24.15.0 \|\| >=26`) |
| Angular (core, CLI, build) | 22.3.0 (published 2026-11-18) | *Active* line |
| TypeScript | 6.0.x | what Angular 22.3's compiler accepts (`>=6.0 <6.1`) — not TypeScript 7 |
| Angular Material + CDK | 22.3.0 | MIT, no key (§4.2) |
| Tailwind CSS | 4.3.5, added with `ng add tailwindcss` | logical-direction utilities only (`ms-*`, `pe-*`, `text-start` …) |
| Test runner | Vitest (Angular's default; `@angular/build` accepts Vitest 4 or 5 — 5.1.2 current) | |
| Lint | angular-eslint 22.8.0 + a TSDoc / JSDoc rule that fails on a missing comment | the backend's «Javadoc everywhere» in its TypeScript form |
| Data loading | `@tanstack/angular-query-experimental` 5.107.2 (§10) | ⚠ the package still carries «experimental» in its name |
| Translations | `@ngx-translate/core` and `http-loader` 18.1.0 (§10) | 22 files `ar.json` … `uz.json` |

## 2. What the scaffold holds

1. `ng new` (standalone, zoneless, strict, SCSS, routing, **no SSR** — see question 1), merged into the existing
   repository (its `README.md`, `AGENTS.md`, `LICENSE`, `.gitignore` kept).
2. The structure of §10: `component/<module>/`, `shared/component/general/` (our wrappers — pages never import
   Material directly), `shared/layout/`, `shared/service/` (settings, translate, error handling, the audio player later),
   `shared/service/integration/<module>/`, `shared/schema/response/<module>/` (`Dto*` mirroring the backend),
   path aliases `@component`, `@shared`, `@environment`, `@assets`.
3. **Design 3's tokens** (`docs/design/tokens-design-3.json`) turned into CSS variables, feeding both the Material theme
   and the Tailwind theme (one source, §4.2); the load order of Tailwind and Material checked on a sample page.
4. **The 22 languages from day one** (F1, §8.9): the language data (code, own name, direction, font) as data; the
   interface texts from the design's i18n files; `dir="rtl"` for Arabic, Urdu, Persian, Pashto; each script's font;
   numbers and dates through the platform's locale functions.
5. **Fonts self-hosted** — no Google Fonts or any third-party request (§2 no trackers, §10 no third-party scripts):
   IBM Plex Sans Arabic, Inter, Amiri (design 3's headings), Noto Nastaliq Urdu, the Noto fonts of Hindi, Bengali,
   Korean, Japanese, Chinese, Vazirmatn — each OFL, its `OFL.txt` read and kept beside it.
6. **The first launch** (F1, F18 — question 2), saved in the browser only.
7. The API client: base address per environment; `GET /v1/app-info` and `/v1/content-version` called on a minimal
   About page, proving the connection (`Accept-Language` from the chosen language).
8. CI on GitHub Actions: install, lint (0 errors), `ngc` strict templates, unit tests, production build.
9. `AGENTS.md` and `README.md` of the repository rewritten for the real code; `P0-06` (web versions) recorded.

## 3. Not in the scaffold

The reader, search, the player and every feature screen (`P1-W1 …`); the King Fahd page fonts (the reader's task,
`P1-W2`); hosting (`RT-01`).

## 4. The author's answers (2026-11-26)

| Question | Answer |
| --- | --- |
| Rendering | **SSR** — `@angular/ssr`: a Node server renders each page, the browser hydrates it. Consequences: the web needs a running Node server (beside the backend, in Docker — `AGENTS.md` §15 changes from a free static host); everything that exists only in the browser (storage, audio, geolocation, the compass) is used only on the browser side. |
| The first launch | **As in design 3**: the language from the searchable list of 22, the colour direction and day / night, on one screen. |
| Data loading | **TanStack Query** (the convention of §10). |
| The language with SSR | **In the URL** — `/ar/…`, `/en/…` for all 22; the server renders each language and search engines index each one (`hreflang`). The choice is remembered in **one functional cookie** (the language and the appearance — no tracking, nothing sent anywhere but our web server), so `/` leads to the user's language; the privacy policy says so. |

## 5. As built (2026-11-26) — `tajweed-frontend` 682097f

- As planned in §2, with SSR and the language in the URL (§4). `tools/sync-design.mjs` copies from this repository the
  interface texts of the design (round 1 – 3 keys, with their 20 translations), design 3's tokens (28 directions, day and
  night, as CSS variables), its icons and logo (recoloured with `currentColor` and the dot colour) and its 56
  landscapes; `tools/extra-texts.json` holds the eleven texts the design does not have, in the 22 languages.
- The first launch follows design 3's first screen: brand, the language button and the searchable sheet (the visitor's
  own language first; names in the interface language from the platform's `Intl.DisplayNames`), the draft-translation
  note for every language but Arabic, the colour directions with their landscapes, the day / night switch, Al-Fatihah
  from `/v1/surahs/1/ayahs` in Amiri Quran with its source, «Start». The design's own translations of the short name are
  kept (e.g. German «Tadschwid»), as in the approved prototype.
- The fonts of Urdu, Hindi, Bengali, Korean, Japanese, Chinese, Persian and Pashto load only with their language
  (`font-<code>.css`); the first load is 685 kB raw, 170 kB over the network.
- A finding: Angular Material's `ng add` writes Google Fonts and Material Symbols links into `index.html`; they were
  removed (no third-party request).
- Not yet: the reader and the other features (`P1-W…`); the production `apiUrl` and the SSR host's allowed hosts
  (`RT-01`).


## 6. The features whose inputs are ready (the author, 2026-11-26: «أبدأ بكل الحاجات الجاهزه اللي مش مستنية رد من أي حد»)

Everything below is built on the backend's contract (`tajweed-backend/docs/api/client-guide.md`) or calculated in the
browser, and waits for no answer, key or permission. Built in this order, one commit each:

| # | Feature | Task | Notes |
| --- | --- | --- | --- |
| 1 | Home with the sections built so far, the Hijri date and the time at the top (F27), «continue reading» | `P1-W1`, `P2-W5` | the tiles of design 3; a section appears when its screen exists |
| 2 | The index (114 surahs, 30 juz; go to surah / juz / page) and the reader **by surah** (F2): the basmala as a heading taken from the ayah's own first four words (client guide §3), page / juz / hizb marks between ayahs, font size, the last read position | `P1-W2` (by surah) | Quran font: **Amiri Quran** (OFL; draws every mark of the Tanzil text). ⚠ The page view as printed waits for the line data in the backend (`P0-12`) and the font (letter 01c) |
| 3 | Search (F16): word with or without tashkeel, surah name or number, `2:255`; results by surah, the matched words tinted (a display layer) | `P1-W3` | |
| 4 | The audio engine (F11): ordered sources, retry with a growing delay capped at 30 s, next source, without limit, the `online` event, resume at the position, «جارٍ إعادة الاتصال…»; Media Session | `P1-W4` | one global service; tests `P1-W8` |
| 5 | Recitation (F3, F4): the reciter picker (riwayah always shown, listening-only said plainly), surah / range / endless (114 → 1), repeat, the playing ayah highlighted where timings or ayah files exist | `P1-W5`, `P1-W6` | downloads (F28) off — no source allows them yet |
| 6 | Ayah actions (F26) and markers (F25): tap an ayah → markers (tint over the ayah and its number), listen from here / a range with repeat, all its tafsirs (F5) | `P1-W10`, `P1-W11`, `P4-W1` | the virtue (F29) waits for its hadith edition |
| 7 | Radio (F7) on the same engine; Hadith from HadeethEnc (F13) with its credit on every screen | `P3-W1`, `P7-W1` | |
| 8 | Sources (F17) from `/v1/content-version` plus the web's own fonts and libraries; «report a mistake» (§6.9) opening a GitHub issue | `P1-W7` | the privacy page waits for the postal address (`RT-04`) |
| 9 | Prayer times (F8) with the Adhan library (MIT) in the browser, the last third of the night (F36), the Qibla bearing (F10), the Hijri calendar (F27) | `P2-W1`, `P2-W3`, `P2-W5`, `P10-W…` | the location never leaves the browser; the default method from `docs/data-sources/prayer-methods.md` (the five countries read), otherwise MWL and the screen says so; the adhan (F9) waits for the muezzins' recordings |

Not built now — each waits for someone: F19 (the author's reading of the meanings document), adhkar, duas, misbaha
texts (the book's rights), Dorar (its key), the tajweed lessons (a reviewer), the books and the Lives (editions),
downloads (EveryAyah and mp3quran), the privacy page (the postal address).

**As built (2026-11-26, `tajweed-frontend` 00b7527):** all nine rows above, checked in the browser with the local backend
(`tajweed-frontend/AGENTS.md`, «Verified on 2026-11-26»). Findings: the player is tested by breaking its address
mid-play — it showed «جارٍ إعادة الاتصال…» and resumed on the same source at the position reached; the Adhan library's
presets differ from the measured methods by a minute (Dhuhr), so the methods are built from the shared data file;
tafsirs and hadiths show their empty states locally until the backend syncs them (the Quran Foundation's credentials,
HadeethEnc's daily run). 45 new interface texts in the 22 languages; about 90 more reused from the design.

New interface texts go into `tools/extra-texts.json` in the 22 languages (translated by the agent, corrected from
users' reports — `AGENTS.md` §1); the design's own texts are reused wherever it has them.
