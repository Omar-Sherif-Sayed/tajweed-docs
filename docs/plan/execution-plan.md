# Execution plan — detailed tasks

The detail behind `AGENTS.md` §14. **The status of every task is kept in one place only: `AGENTS.md` §14.1.**
This file says, for each task: what to do, where, what must exist at the end, and what it waits for.

Legend: **✔ verified** · **☐ to verify before it is relied on** · **⚠ limitation or risk** · **(author)** = needs the
author: a decision, an account, money, a device, or sending a message.

---

## 1. How to work with this plan (every agent, every model)

1. Read `AGENTS.md` (parent) → §0 "Start here" tells you the current state and the next task.
2. Open the task here. Read the sections of `AGENTS.md` it names.
3. **Plan, ask, then code** (`AGENTS.md` §1): restate the task as ordered steps, list what is unclear, list the exact
   tables / columns for a database change, and wait for the author's answer.
4. Do the task. Verify every external fact on its official page on that day (versions, licences, URLs); write the
   date beside it. Never write religious content yourself (`AGENTS.md` §6).
5. Finish the task:
   - tests / build / lint green — paste the real output in the session record, never "should pass";
   - update the repository's `AGENTS.md` and `README.md`;
   - update the parent `AGENTS.md`: §0 (state, next task), §14.1 (status), §19 (change log);
   - add or extend the session record in `docs/sessions/`;
   - commit as the author (`AGENTS.md` §1). Push only when the author has said so.

### Definition of done for a feature slice

A slice goes **verified data → backend API → web → Android → iPhone** and is done only when:

- [ ] the data source is in `docs/data-sources/README.md` with URL, licence, date and checksum;
- [ ] no religious text was written, changed or translated by us or by an AI model (§6.1, §6.5, §6.10);
- [ ] unit tests pass; the checksum / count tests pass;
- [ ] Arabic and English are complete, and the screen is correct in RTL and LTR;
- [ ] light and dark theme checked; text size can grow without breaking the layout;
- [ ] no ad, no tracker, no login, no third-party script;
- [ ] the repository's `AGENTS.md` and `README.md` are updated;
- [ ] the author has seen it and accepted it.

### Task ids

`P<phase>-<area><n>` — areas: **D** data · **B** backend · **W** web · **A** Android · **I** iPhone · **Q** quality /
acceptance. Phase 0 tasks are `P0-01` … Release-track tasks are `RT-01` …

---

## 2. Machine state (checked 2026-11-17)

| Tool | State |
| --- | --- |
| JDK 25.0.5, Node 22.23.5, npm 10.9.9, Git 2.56.1, Python 3.13 | ✔ installed |
| Docker 29.9.3 | ✔ installed — PostgreSQL for development runs in Docker; integration tests use Testcontainers |
| Angular CLI | ✔ present (☐ version — use `npx @angular/cli@22` on scaffold day) |
| PostgreSQL client (`psql`) | not installed — not needed (Docker) |
| **Android Studio / Android SDK** | ✔ installed 2026-11-17: Android Studio Rabbit 2 Patch 1, SDK platform `android-37.0`, build-tools `36.0.0`, platform-tools, an emulator image and one virtual phone |
| GitHub CLI (`gh`) | not installed — repositories were created through the author's Chrome session; pushing is done with Git over SSH (project key, `AGENTS.md` §0) |
| **Certificates** | ⚠ the Windows store does not trust GitHub's certificate chain and the automatic root update is disabled by policy: Git Credential Manager cannot sign in over HTTPS. Git works with `-c http.sslBackend=openssl`; SSH to GitHub works. Use SSH for GitHub; never disable certificate checking (`AGENTS.md` §1) |
| Mac / Xcode / iPhone | ⚠ none — `AGENTS.md` §11–12 |

---

## 3. Phase 0 — Foundations

Goal: five repositories, four empty applications that build in CI, an approved design, a signed-off source list.
Nothing religious is published in this phase.

### P0-01 Documentation repository ✔ (2026-11-17, local only)

The workspace folder itself is the documentation repository (`AGENTS.md` §3). Done: `git init`, `.gitignore` that
ignores the four application folders, `README.md`, `docs/` with its index, this plan, the first session record, first
commit as the author. Not done: the GitHub repository and the push (`P0-03`).

### P0-02 Author's confirmations (author)

`AGENTS.md` §18.2, R1–R9. The defaults written there are in effect; three points need an explicit answer because
they cannot be undone or are public:

- **R1** — create the public repositories and push (public from the first second);
- **R3** — the application id `io.github.omarsherifsayed.tajweed` (permanent after the first store release; the same
  value for the Java package, Android and iPhone);
- **R10** — the e-mail carried by the commits: the personal address, or the account's GitHub "noreply" address
  (recommended, because the account hides its address). Decided before the first push; if it changes, the local
  commits are rewritten first.

### P0-03 GitHub repositories ✔ (2026-11-17)

- Account: `Omar-Sherif-Sayed` (read from the author's Chrome session on 2026-11-17; no `tajweed-*` repository
  existed there). The repositories are created in that Chrome session (the Claude in Chrome extension must be
  connected).
- Create five **public** repositories, empty (no generated README): `tajweed-docs`, `tajweed-backend`,
  `tajweed-frontend`, `tajweed-android`, `tajweed-ios`. Description in English and Arabic; default branch `main`; no
  collaborators (only the author can write).
- In each local folder: `git remote add origin …`, set `user.name` / `user.email` (§1), push `main`.
- **Done 2026-11-17:** created, pushed over SSH and checked. How it was done, for the next machine or a new clone —
  the machine's certificates block the HTTPS sign-in (§2), so: create an SSH key used only for this product
  (`~/.ssh/`, referenced by each repository's `core.sshCommand`, so that other projects on the machine are not
  affected); register its public half in the author's GitHub account (Settings → SSH and GPG keys) through his Chrome
  session; `git remote set-url origin git@github.com:Omar-Sherif-Sayed/<name>.git` in the five folders; push; open
  each repository page and check that `README.md` shows.
- ☐ Before the first push of `tajweed-docs`: the author reads `AGENTS.md` and `docs/sessions/` once — they become
  public (they contain local folder paths and the author's own messages).
- Done when: five repositories exist, each shows its `README.md`, the parent `AGENTS.md` §3 holds the real URLs.

### P0-04 Licences

- Code: `LICENSE` = MIT in the four application repositories (default R1).
- `tajweed-docs`: our own documents and designs — **CC BY 4.0** (author, 2026-11-17); the full licence text is in
  `LICENSE`. Third-party material inside the repository (the Tanzil text file, fonts) keeps its own licence.
- Every repository's `README.md` says: **content (Quran text, audio, tafsir, hadith, books) keeps the licence of its
  source** and is listed in `docs/data-sources/README.md`; the MIT licence covers the code only.

### P0-05 Machine prerequisites (author)

- Install Android Studio (brings the Android SDK and an emulator). Without it the Android project can be written
  but not built locally.
- Confirm Docker Desktop starts (needed for PostgreSQL and Testcontainers).

### P0-06 Version check on scaffold day

For each project, open the official page, record version + date in that repository's `AGENTS.md`, and correct
`AGENTS.md` §4.1: Spring Boot · Gradle · PostgreSQL · Flyway · Angular + CLI (and its supported Node range) ·
Angular Material · Tailwind CSS · Kotlin · Android Gradle Plugin · Compose BOM · Media3 · Xcode / Swift ·
the Adhan library (Kotlin, Swift, JavaScript editions).

### P0-07 Backend scaffold — `tajweed-backend`

Follows `AGENTS.md` §9.

1. Generate with Spring Initializr: Gradle (Groovy DSL), Java 25, Spring Boot 4.1.x; dependencies: Web, Validation,
   Data JPA, Flyway, PostgreSQL driver, Actuator, Cache, Lombok. Base package: R3.
2. `general/`: `BaseResponse<T>`, `ErrorCode`, `BaseException`, `GlobalExceptionHandler`, `AbstractAuditingEntity`,
   i18n (`messages.properties` Arabic, `messages_en.properties` English, language from `Accept-Language`), CORS,
   OpenAPI (☐ library that supports Spring Boot 4.1), rate limiting (☐ library), HTTP caching helpers.
3. `business/appinfo`: `GET /v1/app-info` (application name, author, LinkedIn link, API version) — the first real
   endpoint, written exactly in the controller → service → mapper → `Dto*` style.
4. `db/migration/V1_0_0__baseline.sql`; `spring.jpa.hibernate.ddl-auto=validate`; every setting from an environment
   variable; `compose.yaml` for a local PostgreSQL.
5. Tests: unit (JUnit Jupiter, AssertJ, Mockito), integration with Testcontainers tagged `integration`.
6. CI (GitHub Actions): build, unit tests, integration tests; JaCoCo report.
7. `AGENTS.md`, `README.md`, `docs/README.md`, `LICENSE`, `.gitignore`.

Done when: `./gradlew build` is green locally and in CI; `GET /v1/app-info` answers in Arabic and in English inside
`BaseResponse`; a wrong path answers with an `ErrorCode` body in the requested language.

### P0-08 Web scaffold — `tajweed-frontend`

Follows `AGENTS.md` §10 and §4.2.

1. `ng new` with Angular 22: standalone, zoneless, SCSS, routing, **no server-side rendering** (static hosting);
   strict templates.
2. `ng add @angular/material`, then `ng add tailwindcss`; prove on one sample page that both work together in RTL
   and LTR, light and dark (the ☐ in §4.2).
3. Path aliases (`@component`, `@shared`, `@environment`, `@assets`); ESLint; unit tests with the CLI's default
   runner (☐ Vitest in Angular 22); ngx-translate with `ar.json` / `en.json`; TanStack Query.
4. Design tokens as CSS variables (from `docs/design/tokens.json`) feeding the Material theme and the Tailwind theme.
5. First wrappers in `shared/component/general/`: button, icon button, text input, select, dialog, drawer, tabs,
   tag, spinner, message (snack bar), empty state, error state.
6. Shell: main layout, navigation, language switch that also switches `dir` and `lang` on `<html>`; the first-visit
   language page (F1) saved in browser storage; an About page that calls `GET /v1/app-info`.
7. CI: `ngc --noEmit`, ESLint (0 errors), tests, production build.
8. `AGENTS.md`, `README.md`, `docs/README.md`, `LICENSE`, `.gitignore`.

Done when: the four CI steps are green; the application opens in Arabic (RTL) on first visit, switches to English
(LTR) and remembers it; the About page shows data from the local backend.

### P0-09 Android scaffold — `tajweed-android` (needs `P0-05`)

1. New project: Kotlin, Jetpack Compose, Material 3, Gradle Kotlin DSL with a version catalogue (the Android
   standard); application id: R3; minimum Android version ☐ (proposal: Android 8.0 / API 26 — check the current
   distribution numbers on that day).
2. Packages per feature with `data` → `domain` → `ui` (`AGENTS.md` §11). Proposed libraries (☐ each one's current
   stable version): Navigation Compose, Hilt, Room, DataStore, Retrofit + kotlinx.serialization, Media3, WorkManager.
3. `strings.xml` in Arabic (default) and English; per-application language; RTL support; light / dark theme from the
   design tokens.
4. First screens: language choice (F1), empty home, About (calls `GET /v1/app-info`).
5. CI: build debug, unit tests, Android lint.
6. `AGENTS.md`, `README.md` (how to open in Android Studio, run on the emulator and on a phone — step by step for a
   developer new to Android), `docs/README.md`, `LICENSE`, `.gitignore`. **Every class and function documented.**

Done when: CI is green and the application runs on the emulator in both languages.

### P0-10 iPhone scaffold — `tajweed-ios`

1. Project described by a text file (project generator, `AGENTS.md` §11–12); SwiftUI; minimum iOS version ☐
   (proposal: the current version minus two); bundle id: R3.
2. Folders `Data` → `Domain` → `UI` per feature; a String Catalog with Arabic and English; RTL.
3. First screens: language choice, empty home, About.
4. CI on a macOS runner (☐ free for public repositories — check on that day): generate the project, build, run the
   unit tests on a simulator. No signing in CI at this stage.
5. `AGENTS.md`, `README.md` (what can be done from Windows, what needs the Mac), `docs/README.md`, `LICENSE`.

Done when: the CI build and tests are green. ⚠ "Runs on a device" is **not** claimed until a session on the Mac.

### P0-11 Design ◐ (round 1 done 2026-11-17; lives in this repository)

1. `docs/design/tokens.json`: colours (light and dark), the search-result highlight,
   the six prayer backgrounds, typography, spacing, radius, elevation.
2. **Two or three colour directions** as HTML pages with real Arabic text for the author to choose from — the
   reference is the author's printed mushaf: cream page, black text, ornament frame.
3. HTML prototypes in `docs/design/prototypes/`, phone and desktop width, Arabic and English: language choice, home,
   Quran reader (+ ayah actions), player, reciter picker, prayer times (six backgrounds), Qibla, radio, adhkar
   counter, tajweed lesson, hadith, book reader, settings, About.
4. (author) review → changes → approval written in `AGENTS.md` §13.
5. After approval: the Figma file in the author's account, through his Chrome session.
6. ☐ Fonts: the licence of each font is checked and recorded before it is used (Quran font: `P0-12`).

**State 2026-11-20, fourth message — design 3 chosen** (the author: «خلينا نعتمد في الكود علي التصميم رقم 3 وسيب
التصاميم الأخري ماتمسحهاش»). All further design work is on `round-3.html`; designs 1 and 2 stay in the repository
unchanged. Remaining: the screens not yet drawn (§13 "Screens to design"), the Figma elements of design 3, `P0-17`.

**State 2026-11-20, third message:** design 3 checked against the tafsirs of every ayah (al-Sa'di, Ibn Kathir)
and the hadith numbers on sunnah.com; five landscapes corrected and five Paradise directions added (28 in all); the
Names of Allah and the names of the Prophet ﷺ screens in the three designs; the asset quality rule (`P0-17`). ☐ Figma:
the colour rows of ten directions and the new and changed landscapes wait for the Starter plan's limit to reset.

**State 2026-11-20, second message:** the author chose the **tint** look for the ayah markers (with the ayah number
inside the tint; the ribbon removed); the Hijri date and the time on the home screen too; the adhkar like the Hisn
al-Muslim application (all chapters, «فضل الذكر» first, one dhikr per page with its count, its source and a counter at
the bottom right); the duas by category (the chapters of a named book; a dua may repeat); the radio tile back in
designs 2 and 3; design 3: ten landscapes redrawn and five new directions from the Quran only (23 in all). Figma: the
landscapes updated and the earlier ones kept; ☐ the colour rows of the five new directions (the Figma Starter plan's
limit of tool calls was reached — values in `tokens-design-3.json`). Waiting for the author's choice of design.

**State 2026-11-20:** the screens of F23 – F29 (misbaha, adhkar counter, duas, ayah markers in two looks, ayah
actions, Hijri calendar) and the day / night switch in all three designs; design 3 with 18 directions and a new Two
Gardens landscape. Waiting for the author's choice of design and of the marker look.

**State 2026-11-19, evening (the author's review):** one file per design, round N = design N — design 1
`round-1.html` (the two passes merged, now in 22 languages), design 2 `round-2.html`, design 3 `round-3.html`; the
Lives screens (F20–F22) in all three; the elements of each design (logo, icons, drawings, landscapes, colours) in
Figma as editable vectors and in `docs/design/elements/` as SVG. Still waiting for the author's choice.
The two states below keep the file names of their day.

**State 2026-11-19 (round 4):** three designs to choose from — design 1 (`round-2.html`), design 2 (`round-3.html`,
kept as it is) and design 3 (`round-4.html`, "the first era": twelve directions, each in day and night with its own
landscape, the prayer times on the path of the sun, all 22 languages; the reasons in `docs/design/design-3-meanings.md`).
Waiting for the author's choice for web, Android and iPhone.

**State 2026-11-17 (round 3):** two designs to choose from — design 1 (`round-2.html`, three colour directions;
reviewed by the author, default Quran font chosen) and design 2 (`round-3.html`, "early Islam": parchment and
ink, first launch, home, mushaf page, prayer times by location, Sources, web reader). Waiting for the author's
choice. Round 2: first launch on one screen, mushaf pages as printed, six Quran fonts, Sources screen. Earlier (round 1): steps 1 (draft) and 2 are done — `docs/design/prototypes/colour-directions.html`, three
directions on four screens, with real Quran text copied by `prototypes/tools/build_quran_sample.py`; the author is
choosing. Remaining: steps 3 to 6 in the chosen direction.

Done when: the author has approved the colours and the key screens, and the tokens file is final for phase 1.

### P0-17 Asset exports at the best quality (after the design is chosen)

The author (2026-11-20): every logo, icon and picture at the best possible quality, saved in the docs repository.
1. Masters: the SVG files in `docs/design/elements/` (vectors — sharp at any size).
2. Android: vector drawables made from the masters; the adaptive launcher icon (foreground and background layers).
3. iPhone: vector assets (SVG or PDF) in the asset catalogue; the app icon at 1024 × 1024.
4. Web: SVG used directly; the favicon set.
5. Stores: Google Play icon 512 × 512, feature graphic 1024 × 500, App Store icon 1024 × 1024 — PNG exported from the
   masters at full size, never enlarged from a small image.
6. All of it saved under `docs/design/elements/<design>/exports/`, listed in `manifest.json`.

### P0-12 Data-source register and the Quran text

1. Create `docs/data-sources/README.md`: one entry per source — owner, URL, what we take, version / date, licence
   and terms (quoted), checksum, verification date, status (`VERIFIED` / `WAITING FOR PERMISSION` / `REJECTED`).
   Move the facts of `AGENTS.md` §7 into it; §7 keeps a summary.
2. **Choose the Quran text, its layout and its font once** — prepared in design round 2: displayed text Tanzil
   Uthmani (verified), page layout DigitalKhatt old Madinah 1405H (verified against Tanzil, 0 differences), fonts:
   **default: the King Fahd page fonts (author, 2026-11-17)**; the open DigitalKhatt fonts stay as an alternative.
   Quarter sign: 15:49, as the author's printed copy (quarter positions are taken from the layout). Still to
   settle: the 9 ayahs of the King Fahd glyph list, justification by letter stretching. Files and results:
   `docs/design/prototypes/assets/README.md`.
3. Download the chosen file, record its SHA-256, keep the file untouched under `content/quran/` of the backend
   repository together with its licence notice.
4. Choose the search text (§8.1): download it untouched, record its checksum, and prove that it has the same 6,236
   ayahs with the same numbering as the displayed text.
5. Page / juz / hizb / sajda metadata: choose the source and record it.

Done when: the register exists; the Quran text file, its checksum and its licence are recorded; the author has
chosen the text and the font.

### P0-13 Permission requests (author sends them)

1. Draft one letter per owner, Arabic and English, in `docs/permissions/`: what the application is (free, no ads, no
   login), exactly what we want to use, how we will credit them, and a clear question.
2. Owners: mp3quran.net (audio, timings, radio list) · EveryAyah (ayah audio) · Quran Foundation (API access) ·
   الدرر السنية (hadith API and explanations) · QuranEnc (tafsir / translations) · Tanzil (attribution wording) ·
   owners of the adhan recordings (once found).
3. (author) sends them from his own e-mail. Each answer is saved in `docs/permissions/` and the register is updated.

Done when: every letter is sent and tracked in a table (sent date, answer, decision). ⚠ A source without an answer
is used only inside what its published terms already allow.

### P0-14 Content pipeline and API contract

1. **Decision D1 (proposal — author confirms):** one import tool, kept in `tajweed-backend`, reads the untouched
   source files and produces (a) the PostgreSQL content, (b) the ready SQLite database that the two phone
   applications ship, each with a manifest of checksums. The phones never build their own copy of the Quran text.
2. **Decision D2 (proposal):** small content (surahs, ayahs, reciters, stations) enters PostgreSQL as Flyway
   migrations generated by the tool; large content (tafsir, hadith, books) is loaded by an import job from versioned
   data files with checksum verification, because such files are too large for a migration.
3. Draft `docs/api/openapi.yaml` (backend repository) for phase 1 — the endpoints in `P1-B`.

Done when: D1 and D2 are decided and written in `AGENTS.md` §5; the phase 1 contract is drafted.

### P0-15 Phase 0 review (author)

Walk through: five repositories, four green CI pipelines, approved design, register, permission table, open risks.
Then phase 1 starts.

**Suggested order:** 01 ✔ → 02 → 03, 04 → 11 (design, in parallel with the rest) → 05, 06 → 07 → 08 → 12, 13 → 14 →
09 → 10 → 15.

---

## 4. Phase 1 — Quran core (F1, F2, F16, F3, F11, F15)

**The first public release (author, 2026-11-20):** complete — every feature of `AGENTS.md` §2 that can be built
with verified, licensed content. The phases below are the order of building, not separate releases; content that
cannot be verified or licensed by then is left out (§6), and added in a later version when it can.

Goal of phase 1: the first usable build on web and Android — read the Quran with full tashkeel, search it, listen to a reciter in
three modes, playback that survives network loss, About page.

### Data

| Task | What | Check |
| --- | --- | --- |
| P1-D1 | Import the Quran text byte for byte from the file chosen in `P0-12`. | SHA-256 of the source; 114 surahs; 6,236 ayahs; the text read back from the database equals the source for every ayah. |
| P1-D2 | Surah metadata (names AR / EN, place of revelation, ayah count), page / juz / hizb / sajda positions. | Totals per surah equal the source; 30 juz; page numbers continuous. |
| P1-D3 | Search text (§8.1): the everyday-spelling text imported byte for byte beside each ayah; the list of surah names and their common spellings in Arabic and English. | SHA-256 of the source; 6,236 ayahs with the same numbering as the displayed text; a fixed list of test words with their expected number of results. |
| P1-D4 | Catalogue: reciters, recitations (style, riwayah, completeness), ordered audio sources, ayah timings — only complete Hafs mushafs of the requested reciters (§7.3) plus Sheikh Noreen as "listening only" (R5). | A script requests every surah file of every recitation and records the result and the date; a recitation with a missing file is not published. |
| P1-D6 | F19 content (§8.10): the design notes in Arabic and English from the meanings document of the chosen design (`docs/design/design-2-meanings.md` or `design-3-meanings.md`); the hadith gradings copied verbatim from Dorar; the tafsir quotes from a licensed tafsir; the reviewer's check when one exists. | The author reads both languages; every ayah reference resolves to the shipped text. |
| P1-D5 | About content: author, link, credits and licences of every source used, privacy statement (AR / EN). | The author reads and approves both languages. |

### Backend (`tajweed-backend`)

| Task | What |
| --- | --- |
| P1-B1 | Migrations — draft table list (exact columns are listed and approved before coding): `quran_surah`, `quran_ayah`, `quran_ayah_search_text`, `quran_surah_name_spelling`, `reciter`, `recitation`, `recitation_audio_source`, `recitation_surah_availability`, `recitation_ayah_timing`, `content_source`, `content_version`. |
| P1-B2 | `quran` module: `GET /v1/surahs`, `GET /v1/surahs/{number}`, `GET /v1/surahs/{number}/ayahs`, `GET /v1/quran-pages/{number}` (ayahs of a page), `GET /v1/quran-search?q=…` (a word with or without tashkeel, a surah name, an ayah reference — one endpoint, typed results, paged). |
| P1-B3 | `reciter` module: `GET /v1/reciters`, `GET /v1/reciters/{id}`, `GET /v1/recitations/{id}` (sources in order, available surahs), `GET /v1/recitations/{id}/surahs/{number}/timings`. |
| P1-B4 | `appinfo` module: `GET /v1/app-info`, `GET /v1/content-versions`, `GET /v1/content-sources` (credits). |
| P1-B5 | Public API hygiene: CORS for the web origin, rate limit, `ETag` / `Cache-Control`, OpenAPI document generated and committed, error bodies in both languages. |
| P1-B6 | Scheduler: tests the audio sources regularly and marks dead ones (with a ShedLock-style lock, so only one instance runs it). |
| P1-B7 | Tests: checksum and count tests against the database; controller, service and mapper tests; integration tests. |

### Web (`tajweed-frontend`)

| Task | What |
| --- | --- |
| P1-W1 | Home and navigation as designed; language choice (F1) complete — the searchable list of the 22 languages from the language data, Arabic and English selectable, the others marked "coming", the device's language suggested first (`AGENTS.md` §8.9). |
| P1-W2 | Quran reader: by surah and by page; the index (فهرس) of 114 surahs and 30 juz; each surah's Makki / Madani, number of ayahs and order (§8.1); go to surah / juz / page; font size; light / dark; last read position and bookmarks in browser storage. |
| P1-W3 | Search (F16): one search box for a word with or without tashkeel, a surah name, or an ayah number; results grouped by surah with the match highlighted (a display layer — the text is not changed), the number of results, and opening the ayah in the reader. |
| P1-W4 | Audio engine — one global service implementing §8.3: ordered sources, growing retry delay with a cap, switch to the next source, no retry limit, `online` event, resume at the same position, the message «جارٍ إعادة الاتصال…». |
| P1-W5 | Recitation modes (F3): one surah · ayah range · from a start ayah to the end and again from Al-Fatiha without end; the playing ayah is highlighted and scrolled into view; Media Session controls. |
| P1-W6 | Reciter and style picker; a style appears only where it exists (§7.3); the riwayah is always shown. |
| P1-W7 | About, sources and credits, privacy policy; "report a mistake" on the reader (F15, §6.9). |
| P1-W9 | F19 "Why this design" screen (§8.10 of `AGENTS.md`): from About and from the colour choice; one card per direction, icon and the logo; ayahs from the shipped Quran text, never typed. |
| P1-W10 | F25 ayah markers: colours and names chosen by the user, several at once, saved in the browser; the look: a light tint over the ayah **and its number**, the number in the marker's colour (author, 2026-11-20); the Quran text keeps one colour. |
| P1-W11 | F26 actions on an ayah or a range: from … to, marker, play in a chosen reciter with repeat, all the tafsirs of the selection (as their licences allow, `P4-D1`), virtue (`P7-D3`). |
| P1-W12 | F28 download for offline listening where the source allows it (the web keeps files in the browser's storage; the phones in the app's storage); a reciter without permission shows streaming only. |
| P1-W8 | Unit tests for the engine (retry order, source switching, endless mode crossing surah 114 → 1) and for search (handling of the typed query, the fixed list of test queries). |

### Android (`tajweed-android`)

| Task | What |
| --- | --- |
| P1-A1 | The Quran database shipped inside the application (from `P0-14` D1); a test verifies its checksum and counts. |
| P1-A2 | Reader, search on the device (works without a network), settings, last read position, bookmarks — the same behaviour as the web. |
| P1-A3 | Player: Media3 in a media-playback foreground service; notification and lock-screen controls; the §8.3 rules; network-back callback. |
| P1-A4 | Recitation modes, reciter picker, ayah highlighting. |
| P1-A5 | About, sources, privacy, report a mistake. |
| P1-A6 | Unit tests (engine rules, data checks) and a manual device checklist in `docs/quality/`. |
| P1-A7 | F19 "Why this design" screen, as `P1-W9`. |

### iPhone (`tajweed-ios`)

`P1-I1` … `P1-I6` mirror `P1-A1` … `P1-A6` with AVPlayer, background audio, Now Playing controls and the network
path monitor. Started after the Android slice is accepted. Device checks wait for a session on the Mac.

### Acceptance (P1-Q1) — tried by hand and written down with the result

1. First launch asks for the language; the choice survives a restart; everything flips between RTL and LTR.
2. Surah 1 and surah 114 and three random pages equal the printed mushaf's text, every tashkeel mark included (author compares).
3. Search: a word typed without tashkeel and the same word typed with tashkeel are both found; a word whose mushaf
   spelling differs from everyday spelling is found; a surah name in Arabic and in English opens the surah; `2:255`
   opens the ayah; web and Android give the same number of results for ten test words.
4. Play a surah; switch the network off for two minutes and on again → playback continues from the same position
   without touching the screen.
5. Block the first audio source → the player moves to the second one by itself.
6. Start "from ayah to the end" near the end of surah 114 → it continues with Al-Fatiha.
7. Android: playback continues with the screen off and from the notification.
8. No request goes to any advertising or tracking host (network log checked).

---

## 5. Phase 2 — Prayer (F8, F9, F10)

| Task | What |
| --- | --- |
| P2-D1 | Calculation methods and their parameters from the Adhan library's documentation; the default method per country — ☐ a table with a named official source per country; a country without a verified source falls back to Muslim World League and says so. **The author (2026-11-17): may be done at any time, before phase 2 — do not forget it.** Start with the countries the author named: Egypt, Saudi Arabia, Japan. Output: `docs/data-sources/prayer-methods.md` (country, method, parameters, source link, date checked). |
| P2-D2 | City search for users who do not share their location — ☐ source and licence of the city list. |
| P2-D4 | F27: the Hijri date from the platform's Umm al-Qura calendar with a −2 … +2 day setting; the time zone of the location; the screen names the calendar. Shown on its own screen **and at the top of the home screen** with the time (author, 2026-11-20). |
| P2-D3 | Muezzin recordings (⏸ until a recording with a known origin and permission exists for each one, §7.4): full version and a version under 30 seconds. |
| P2-B1 | `prayer` module: method metadata, muezzins and their audio sources. |
| P2-W/A/I-1 | Prayer times screen: today's times, the next prayer with a countdown, the Hijri date (from the platform's Umm al-Qura calendar, with a note that the local sighting can differ by a day), the six backgrounds. |
| P2-W/A/I-2 | Settings: method, Asr school, high-latitude rule, per-prayer minute adjustment, location or city. Location never leaves the device. |
| P2-W/A/I-3 | Adhan per prayer: on / off, muezzin, full or short; listen to the full adhan. Platform limits exactly as §8.6 — the screen tells the user what his platform can do. |
| P2-W/A/I-4 | Qibla: bearing from the library + compass with a calibration hint (phones); bearing in degrees and on a map (computer). |
| P2-Q1 | Compare the calculated times for at least ten cities and four dates of the year with the times published by each country's official authority; record every difference; the default method of a country is accepted only inside two minutes. |

## 6. Phase 3 — Radio (F7)

| Task | What |
| --- | --- |
| P3-D1 | Station list: for each station the broadcaster's own page that publishes the stream (§8.4), country, names AR / EN, primary and alternative stream addresses, verification date. Start: Cairo, then the other Arab countries, then non-Arab. |
| P3-B1 | `radio` module: `GET /v1/radio-stations` (filter by country), station details; health-check scheduler that hides dead streams and shows them again when they return. |
| P3-W/A/I-1 | Station list by country, search, favourites on the device; the same resilient player in "live" mode (resume at the live point). |
| P3-Q1 | Every published station is played for ten minutes on each client; a station is removed at its owner's request (procedure written in `docs/permissions/`). |

## 7. Phase 4 — Understanding (F5, F4)

| Task | What |
| --- | --- |
| P4-D1 | Tafsir list fixed from the sources whose terms allow it (§7.2); each tafsir imported verbatim with book, author, edition and checksum. English: published translations only (§6.10). |
| P4-B1 | `tafsir` module: `GET /v1/tafsirs`, `GET /v1/tafsirs/{id}/ayahs/{surah}/{ayah}`, all tafsirs of one ayah in one call. |
| P4-W/A/I-1 | Select an ayah → its tafsirs, switch between them, source shown, report a mistake. |
| P4-D2 | Muallim recitations (المنشاوي، الحصري، أيمن سويد) with ayah-level audio and timings verified surah by surah. |
| P4-W/A/I-2 | Muallim mode: per-ayah teaching playback, repeat an ayah or a range a chosen number of times, pause between ayahs for the learner. |

## 8. Phase 5 — Tajweed (F6) ⏸ publication limited by §6.10

| Task | What |
| --- | --- |
| P5-D1 | The classical texts verbatim — تحفة الأطفال and المقدمة الجزرية — from a verified edition (edition and checksum recorded). |
| P5-D2 | The curriculum structure of §8.7; every memory word checked letter by letter against the classical text and linked to its line. |
| P5-D3 | Explanations: ⏸ only from a source that permits their use, or after a qualified reviewer signs them. Until then a lesson shows the rule's name, its letters, its memory word, the line of the classical text, and the examples — no explanation written by us. |
| P5-D4 | Examples: ayah or word references for each rule, taken from the named source; audio from the chosen reciter using the ayah timings (word-level clips only if a verified word-timing source exists). |
| P5-B1 | `tajweed` module: topics, rules, memory words, examples. |
| P5-W/A/I-1 | Lessons in the teaching order, example playback in the chosen reciter's voice, progress on the device. |

## 9. Phase 6 — Adhkar (F12)

| Task | What |
| --- | --- |
| P6-D1 | حصن المسلم: right to use the text (publisher / author's foundation) — ☐; text, repeat count, reference and virtue exactly as in the book, checked item by item against the printed book by the author. English: the published translation only. |
| P6-B1 | `adhkar` module: categories, adhkar, counts, references. |
| P6-D2 | F23 duas: the Quran duas as ayah references into the shipped text; the Sunnah duas verbatim from a named collection with number and grade (rights with `P6-D1`). |
| P6-B2 | `dua` module: occasions, duas, references. |
| P6-W/A/I-2 | F24 misbaha: choose a dhikr and a count (33, 100, open), tap to count, vibration at the end of a round, rounds and the day's total on the device. |
| P6-W/A/I-3 | F23 duas by category: each category holds its Quran duas and its Sunnah duas; the categories and the place of each dua follow the chapters of a named book (author, 2026-11-20), and a dua can be in more than one category; each with its reference. |
| P6-W/A/I-1 | Like the Hisn al-Muslim application (author, 2026-11-20): all the chapters of the book, «فضل الذكر» first, numbered as in the book; one dhikr per page — its text, how many times, its source (the surah and ayah for a Quran text, the book and number for a hadith); a counter at the bottom right that counts down and opens the next dhikr; favourites. **No reminders** — the only notification of the application is the adhan (`AGENTS.md` §2). |

## 10. Phase 7 — Hadith (F13)

| Task | What |
| --- | --- |
| P7-D1 | الأربعون النووية, then صحيح البخاري and صحيح مسلم: a verified digital edition with its numbering stated; each hadith with collection, book, chapter, number, grade as stated by the source. |
| P7-D2 | The link of each hadith to its page on الدرر السنية (⏸ their permission, `P0-13`); the explanation is linked, not copied, unless they permit. |
| P7-B1 | `hadith` module: collections, books, chapters, hadiths, search. |
| P7-D3 | F29 virtues: the authentic hadiths about the virtue of prayer, of surahs, of ayahs and of other subjects, each linked to its subject, verbatim with collection, number and the source's grade; weak and fabricated narrations left out. |
| P7-W/A/I-2 | Virtues shown where their subject is: on a surah's page, an ayah's actions, the prayer screen, a dhikr. |
| P7-W/A/I-1 | Browse by collection / book / chapter, search, the hadith page with its reference, grade and link, share as text with the reference, report a mistake. |

## 11. Phase 8 — Books (F14)

| Task | What |
| --- | --- |
| P8-D1 | الأم، صحيح البخاري، صحيح مسلم: the edition, its rights (a modern verified edition can have rights) and its page numbering recorded. |
| P8-B1 | `library` module: books, volumes, chapters, pages; loading by chapter; search. |
| P8-W/A/I-1 | Reader with contents, page navigation, search, font size, last read position. |

## 11a. Phase 9 — Lives: prophets, Companions, Rightly Guided Caliphs (F20, F21, F22 — author, 2026-11-19)

Rules and sources: `AGENTS.md` §8.11. Three sections, shown together under «السِّيَر».

| Task | What |
| --- | --- |
| P9-D1 | Sources: for each candidate book (قصص الأنبياء and السيرة النبوية لابن كثير، سيرة ابن هشام، الإصابة، أسد الغابة، الاستيعاب، سير أعلام النبلاء، تاريخ الخلفاء، البداية والنهاية) choose a verified edition and record its editor, publisher, year, page numbering and rights in the register; permission letters where needed (`P0-13`); prefer an edition that grades the narrations. |
| P9-D2 | F20: the 25 prophets; the ayahs about each from a named index (copied from the shipped text); the hadiths (Sahih al-Bukhari «كتاب أحاديث الأنبياء» and others) with grade; the story chapters verbatim; the Seerah (R11). |
| P9-D3 | F21: the first groups (the ten, the Mothers of the Believers, the people of Badr — R12); each entry verbatim with book / volume / page; the hadiths of virtues with grade. |
| P9-D4 | F22: the four caliphates, events by year, verbatim with references; the chapters on the disputes kept unpublished until a reviewer signs (§8.11 rule 5). |
| P9-B1 | `prophet`, `companion`, `caliph` modules: lists, entries, chapters, search, links between them. |
| P9-W/A/I-1 … 3 | One section each: index (with search), entry page (ayahs, hadiths, chapters, references), timeline; the «السِّيَر» group on the home screen; report a mistake; sources in F17. |
| P9-Q1 | Every text compared with its edition (a sample of pages per book, recorded); no picture of a prophet or Companion; honorifics present in all languages. |

---

## 11b. Phase 10 — Study, worship tools, guides, device (F30 – F47 — author, 2026-11-20)

Part of the first release. Rules and sources: `AGENTS.md` §8.13. **No notification** in any of them — only the adhan
notifies (author, 2026-11-20).

| Task | What |
| --- | --- |
| P10-D1 | Sources and rights (also: the three books of F39 and the classical lists of F48 — al-Suyuti «الرياض الأنيقة», Ibn al-Qayyim «زاد المعاد» and others): word meanings (a named «غريب القرآن» book), asbab al-nuzul (al-Wahidi or another named book), ruqyah (a named book), the Names of Allah (a named scholar's list with the evidence of each name), the guides — wudu, prayer, Hajj and Umrah (a named book), the Zakat rules (a named fatwa body), the calendar of Islamic days (each day with its authentic hadith). Each in the register; permission letters in `P0-13`. |
| P10-W/A/I-1 | F30 Hifz: choose a range, repeat it, hide words to test yourself, a review schedule; progress on the device. |
| P10-W/A/I-2 | F31 Khatma / wird: split the Quran over a number of days, today's portion, progress — no reminder. |
| P10-W/A/I-3 | F32 personal notes on an ayah (device only, in the settings file of F47); F33 share an ayah as an image (the shipped text and font, with its reference — ⏸ the font's permission, `P0-13`). |
| P10-W/A/I-4 | F34 word meanings and asbab al-nuzul in the ayah actions, from their books (⏸ rights). |
| P10-W/A/I-5 | F35 calendar of Islamic days, F36 the last third of the night on the prayer screen, F37 a private prayer and fasting tracker. |
| P10-W/A/I-6 | F38 ruqyah; F39 the Names of Allah — each name with its evidence and three explanations, each under its book, in the author's order (Ibn Uthaymeen's list with al-Sa'di's explanation; al-Qahtani; al-Badr); F48 the names of the Prophet ﷺ — the authentic hadiths first (al-Bukhari 3532, Muslim 2354, 2355), then the classical lists of 200 names or more, each with source and meaning, a note where the evidence is weak or disputed (quoting the scholar). All verbatim. |
| P10-W/A/I-7 | F40 guides (wudu, prayer, Hajj and Umrah — text only, no pictures of people), F41 kids (short surahs with repetition in a muallim recitation, the Arabic letters). |
| P10-W/A/I-8 | F42 Zakat calculator: the nisab and the rules from a named fatwa body, the user enters the prices or a named price source is used; no inheritance calculator. |
| P10-A/I-9 | F43 home-screen widgets (prayer times, Hijri date, an ayah of the day), F44 Wear OS / Apple Watch (prayer times, misbaha), F45 Android Auto / CarPlay (recitation and radio). |
| P10-W/A/I-10 | F46 nearby mosques on an OpenStreetMap map (ODbL, credited in F17; the location stays on the device); F47 save all settings, markers, notes and progress to a file and load them on another device. |
| P10-Q1 | Every text compared with its book; the Zakat results compared with worked examples published by the chosen fatwa body. |

---

## 11c. Languages track — part of the first release (author, 2026-11-19) — `LANG-*`

| Task | What |
| --- | --- |
| LANG-01 | ✔ The list (2026-11-18): 22 languages (`AGENTS.md` §8.9). ✔ All of them in the first release (2026-11-19). |
| LANG-02 | Per language: the interface strings (`ar` / `en` keys as the reference; the agent's translations are in `docs/design/prototypes/i18n/`), corrected from users' reports on GitHub — no native readers (author, 2026-11-19); the font (licence read and recorded); a right-to-left check for Urdu, Persian and Pashto; a long-text check for German and Russian. |
| LANG-03 | Per language: the published translation of the meanings, chosen with the author, with written permission from its publisher (QuranEnc's terms page could not be opened on 2026-11-18 → letter in `P0-13`), imported untouched with its checksum like the Quran text. Without permission: the Arabic is shown with a note (§6.10). |
| LANG-04 | Store listings and the About / Sources / privacy pages in that language. |

## 12. Release track (parallel, starts in phase 1)

| Task | What | Needs |
| --- | --- | --- |
| RT-01 | Hosting decision and a written guide in `docs/deployment/`: web on a free static host; backend as a Docker image on a small server with PostgreSQL, HTTPS and a daily backup. | (author) account, a small monthly cost |
| RT-02 | Domain: web, `api.`, privacy policy. | (author) purchase |
| RT-03 | Staging deployment from CI, then production. | RT-01, RT-02 |
| RT-04 | Privacy policy and sources pages, Arabic and English, published on the domain. | RT-02 |
| RT-05 | Google Play: developer account, closed test with 12 testers for 14 days (☐ re-check the rule on that day), signed bundle, data-safety form, content rating, declarations (exact alarm, playback service, location). | (author) 25 USD, identity check, testers |
| RT-06 | Apple: developer programme, TestFlight, App Review, privacy labels, background-audio declaration, proof of content rights. | (author) 99 USD / year, the Mac, an iPhone |
| RT-07 | Store listings in both languages; the store title must fit each store's length limit (☐ check the limits; `AGENTS.md` §2). | approved design |

---

## 13. What waits for the author (summary)

| Needed | For |
| --- | --- |
| Explicit yes to create public repositories and push | P0-03 |
| Confirmation of the application id `io.github.omarsherifsayed.tajweed` | P0-07, P0-09, P0-10 |
| Choice of the commit e-mail (R10) | P0-03 |
| Android Studio installed | P0-09 |
| ✔ Design 3 chosen (2026-11-20) | P0-11 |
| Which permission letters to draft first, and sending them (`docs/permissions/README.md`) | P0-13 |
| Figma (agent): the colour rows of ten directions and the new and changed landscapes of design 3, after the Starter plan's limit resets | P0-11 |
| Reading the meanings of design 2 | P0-16, F19 |
| Choice of Quran text and font | P0-12 |
| Sending the permission letters | P0-13 |
| A qualified reviewer | P5-D3, hadith explanations |
| Hosting, domain, store accounts, testers, the Mac | Release track |
