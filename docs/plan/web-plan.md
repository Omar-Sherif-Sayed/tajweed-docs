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

