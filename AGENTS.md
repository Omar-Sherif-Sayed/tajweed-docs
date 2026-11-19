# AGENTS.md — Tajweed workspace (parent)

Orientation for AI agents and for the author. This is the **parent** file of the whole product **تجويد — Tajweed**: it
holds the product scope, the rules, the decisions, the structure of the repositories, the verified data sources and
the plan with the status of every task. Each application repository has its own `AGENTS.md` (conventions of that
codebase) and `README.md` (for human readers).

Legend used in this file: **✔ verified** = checked on the official page on the date shown · **☐ to verify** = believed
true, must be checked before it is relied on · **⚠** = a limitation or risk the author must know about.

| § | Content | § | Content |
| --- | --- | --- | --- |
| 0 | **Start here** — state, next task, handoff | 10 | Web structure and conventions |
| 1 | Working agreement (the author's rules) | 11–12 | Android and iPhone |
| 2 | The product and its features F1–F18 | 13 | Design system and Figma |
| 3 | Repositories and folder layout | 14 | **Plan and task status** |
| 4 | Technology and versions | 15 | Hosting and stores |
| 5 | Architecture | 16 | Risks and limitations |
| 6 | **Data integrity rules (binding)** | 17 | Recommendations |
| 7 | Data sources and reciters | 18 | Decisions and open points |
| 8 | Feature notes and platform limits | 19 | Change log |
| 9 | Backend structure and conventions | | |

---

## 0. Start here — handoff for any agent or model

Everything needed to continue is in files of this repository. Do not rely on a chat history or on the agent's
private memory (`~/.claude` is wiped on this machine).

**Reading order:** (1) this section → (2) §1 and §6, the rules that are never broken → (3) §14.1, the task list →
(4) the task's detail in [`docs/plan/execution-plan.md`](docs/plan/execution-plan.md) → (5) the `AGENTS.md` of the
repository the task touches → (6) the last record in [`docs/sessions/`](docs/sessions/).

| | Current state — **update this table at the end of every session** |
| --- | --- |
| Date | 2026-11-19 |
| Phase | **0 — Foundations** (§14) |
| Exists | **Five public repositories on GitHub** (`main` branch), the same five folders on this machine. `tajweed-docs` (this one): parent `AGENTS.md`, `README.md`, `LICENSE` (CC BY 4.0), the detailed plan, the session record with a conversation copy, and the design in `docs/design/`: round 1 (colour directions), round 2 (first-launch screen, mushaf pages as printed, six Quran fonts, Sources screen) round 3 (design 2, "early Islam") and **round 4** (design 3, "the first era") with the verified source files and the scripts that check them. The four application repositories: `README.md`, `AGENTS.md`, `LICENSE` (MIT), `.gitignore` — no application code. |
| Does not exist | Any application code, the register of content sources, the remaining screens. |
| Last task done | Round 4 (2026-11-19): **design 3, "the first era"** — `docs/design/prototypes/round-4.html`, twelve colour directions (eleven for ordinary sight, the last, Mountains, for low vision and colour blindness), each in day and night with its own landscape; the prayer times on the path of the sun; a new logo; all 22 languages; the reason for every colour and scene with its ayah or hadith in `docs/design/design-3-meanings.md` (§13). Also fixed: rounds 3 and 4 stopped drawing in the 21 languages other than Arabic (a surah name missing from the data). Then (same day, the author's review): the round-4 texts translated into the 20 languages; every cross shape removed from all designs (§8.10); no native readers — mistakes come from users' GitHub reports (§1). |
| GitHub access from this machine | **Over SSH only** (the Windows certificate store blocks the HTTPS sign-in, §1). Key `~/.ssh/id_ed25519_tajweed` (no passphrase, fingerprint `SHA256:EPCRVeCpF+Jvsj40LKpu4Cta+mKF3ivLO8szlC2k/Po`), registered in the author's account as "Tajweed project - work laptop" (he confirmed it himself). Each of the five repositories uses it through its local `core.sshCommand`; remotes are `git@github.com:Omar-Sherif-Sayed/<name>.git`. A new clone on this machine needs the same two settings. Test: `ssh -i ~/.ssh/id_ed25519_tajweed -o IdentitiesOnly=yes -T git@github.com`. |
| Folder name | `C:\Programming\WorkSpaces\Tajweed - The Noble Quran and Its Sciences` — renamed by the author on 2026-11-17. |
| GitHub account | `Omar-Sherif-Sayed` — <https://github.com/Omar-Sherif-Sayed?tab=repositories>. Pushing is allowed for this product (R1); push at the end of every task. |
| Do not forget | `P2-D1` — the default prayer-time method of every country, each with a named official source (the author, 2026-11-17: it may be done at any time, before phase 2 starts) · **F19** — the in-app section «لماذا هذا التصميم؟ / Why this design?»: the reason for every colour, icon and the logo (§8.10, `docs/design/design-2-meanings.md` or `design-3-meanings.md`, for the chosen design). |
| **Next task** | `P0-11`: the author chooses one design — 1 (`round-2.html`), 2 (`round-3.html`) or 3 (`round-4.html`) — for web, Android and iPhone; then the remaining screens in the chosen design (§13), the Figma file, and the scaffolds `P0-06` … `P0-10`. |
| Waiting for the author | His choice among designs 1, 2 and 3; his reading of the meanings documents (`design-2-meanings.md`, `design-3-meanings.md`); the reports of mistakes that users write on GitHub (issues), which he brings to the agent. |

**At the end of every session:** update the table above, the statuses in §14.1, the change log §19; write or extend
the session record; commit as the author (§1). Details: `docs/plan/execution-plan.md` §1.

---

## 1. Working agreement (the author's rules — always follow)

The author's own rules — the same in all his projects:

- **Plan, ask, then code.** Restate every task as an ordered plan, list what is unclear, and wait for the author's
  answer before editing code. A database change lists the exact tables / columns first.
- **Commits (author, 2026-11-16):** the agent may commit. The commit author is always **Omar Sherif** with the author's
  own e-mail (set per repository with `git config user.name` / `user.email`); no AI co-author and no "generated with"
  line in a commit message. **Pushing and creating repositories: only after the author says so** (§18.2 R1).
  The commits carry the author's personal address — the one his GitHub account is registered with (his decision,
  2026-11-17, R10); it is visible in the public history.
- **After every task, update the `AGENTS.md` of every repository the task touched** (and its `README.md` for human
  readers), plus this parent file when scope, structure, sources or decisions change.
- **Document everything.** Documents go in `docs/<kind>/` of the owning repository with an index `docs/README.md`;
  never loose files.
- **All 22 languages from the first release** (author, 2026-11-19 — before: Arabic and English first), in every
  client; every user-facing text exists in all of them. The interface texts are translated by the agent; there
  are no native readers (author, 2026-11-19): users report mistakes on GitHub, the author brings them to the agent,
  and they are corrected. Religious content is never translated by us (§6.10). The code is built so that more languages can be added without changing screens — §8.9.
- **Correct data only** — §6 is binding. When a fact cannot be verified, it is not shipped.
- **No advertisements, ever** — no ad SDK, no sponsored content, no tracking for marketing (§2).
- **The plan lives in files.** Every decision, every task and its status is written in this repository on the day it
  happens, so that another agent or another model can continue without the conversation (§0).
- Platform is Windows 11 (PowerShell + Git Bash). Installed (checked 2026-11-17): JDK 25, Node 22, Git, Python 3.13,
  Docker, Android Studio Rabbit 2 Patch 1 with the Android SDK in `%LOCALAPPDATA%\Android\Sdk` (platform
  `android-37.0`, build-tools `36.0.0`, platform-tools, an emulator image and one virtual phone; `ANDROID_HOME` is
  not set — the project's `local.properties` points to the SDK). Not installed: the GitHub CLI (`gh`), the
  PostgreSQL client.
- ⚠ **Certificates on this machine (checked 2026-11-17).** The Windows certificate store lacks the roots of GitHub's
  certificate chain, and the automatic root update is disabled by policy. Programs that use the Windows store fail on
  `github.com` with "untrusted root" (Git's default `schannel` backend, Git Credential Manager, and probably `gh`).
  Programs with their own certificate bundle work (Chrome, Git with `-c http.sslBackend=openssl`, OpenSSH; npm and
  Maven Central were reachable). **Never disable certificate checking** to get around it; use SSH for GitHub, and
  report any other failing host to the author.

## 2. The product

A free, public Islamic application — web, Android and iPhone — for the Quran, its recitation and its sciences, for
Muslims of أهل السنة والجماعة (every content source is an established Sunni source — §6.10).

| Name (accepted by the author, 2026-11-17) | Arabic | English |
| --- | --- | --- |
| Full name — About page, website, store description | **تجويد - القرآن الكريم وعلومه** | **Tajweed - The Noble Quran and Its Sciences** (confirmed by the author, 2026-11-17; written with a plain hyphen) |
| Short name — under the icon, in code, folders and repositories | **تجويد** | **Tajweed** |

⚠ Stores: the App Store requires a name that no other application uses, and both stores limit the length of the
title (☐ check availability and the limits when the listings are written, task RT-07). If the English full name is
too long for a store title, the store shows "Tajweed" with the rest as the subtitle.

| Hard rule | Meaning |
| --- | --- |
| Free and public | No registration, no login, no accounts, no payments. Preferences live on the device only. |
| No ads | No advertising of any kind, in any client, at any time. |
| Languages | **22 languages, all available from the first release** (author, 2026-11-18 and 2026-11-19, §8.9): Arabic (default, right-to-left), English, Russian, Spanish, German, Italian, French, Urdu, Hindi, Korean, Indonesian, Japanese, Chinese, Turkish, Bengali, Persian, Malay, Swahili, Hausa, Portuguese, Pashto, Uzbek. The user chooses on first launch, from a searchable list, and can change it later. |
| Correct data | Every text, audio link, time and reference comes from a named, verified source (§6, §7). |
| Author | **Omar Sherif — عمر شريف**, shown on the About page with one link only: `https://www.linkedin.com/in/omarsherif21/` |

### Features (the author's request, numbered for reference)

| # | Feature | Summary |
| --- | --- | --- |
| F1 | Language | Chosen on first launch (mobile and web) from a searchable list of the 22 languages, each written in its own script; the device's language is suggested first. **All 22 are available from the first release** (author, 2026-11-19), each with its own font, direction and number format (§8.9). |
| F2 | Quran reader | The full Quran text with complete tashkeel, **laid out exactly like the printed Madinah mushaf**: 604 pages of 15 lines, every page starting and every line ending on the same word as the printed copy, surah headers, basmala, juz / hizb / quarter marks in their places — one text colour (§8.1). Each surah shows whether it is Makki or Madani, its number of ayahs and its order; the mushaf has an index (فهرس) of the 114 surahs and 30 juz with their pages (author, 2026-11-18). |
| F3 | Recitation | Choose a reciter and a recitation style (murattal / mujawwad / muallim). Play a surah, an ayah range, or from a start point to the end of the Quran, then restart from Al-Fatiha, forever. |
| F4 | Muallim mushaf | Teaching recitation per ayah from a reciter who has one (Al-Husary, Al-Minshawi, Ayman Suwayd). |
| F5 | Tafsir | Select an ayah and read its tafsirs and explanations. |
| F6 | Tajweed | The complete tajweed rules, explained, with the scholars' memory words (يرملون، قطب جد، …) and audio examples in a chosen reciter's voice. |
| F7 | Quran radio | Quran radio stations of Arab and non-Arab countries, when the station is free and publicly available. |
| F8 | Prayer times | Times for the user's location, with a background that fits the time of day. |
| F9 | Adhan | Per prayer: on/off, the muezzin, full or short adhan. The user can also listen to a muezzin's full adhan. |
| F10 | Qibla | Direction of the Qibla. |
| F11 | Resilient playback | Radio and recitation keep playing through network loss: automatic reconnect, automatic switch between sources, retry without limit, no user action. |
| F12 | Adhkar and duas | All supplications with their repeat counts (morning, evening, travel, entering the mosque, leaving home, …), like Hisn Al-Muslim. |
| F13 | Hadith | The noble hadiths, each with its reference (e.g. a link to الدرر السنية) and its explanation. |
| F14 | Books | Religious books (الأم للشافعي، صحيح البخاري، صحيح مسلم). |
| F15 | About | Author name and LinkedIn link; privacy statement; a link to F17. |
| F17 | Sources | A section listing **every** source the application uses — Quran text and its layout, fonts, audio and timings, tafsir, hadith, adhkar, books, prayer-time method, radio streams, icons, software libraries — each with its owner, link, licence and verification date; built from the register `docs/data-sources/README.md`, so it is never out of step (author, 2026-11-17). |
| F18 | Appearance | Three colour directions (A emerald and gold, B teal and sand, C mushaf), each with a light and a dark theme; chosen on first launch after the language, changeable in settings; the Quran font is a reader setting (author, 2026-11-17 — §13). A second design, "early Islam" (round 3), and a third, "the first era" (round 4), were made on the author's request to compare; he chooses one design for all clients. |
| F19 | Why this design | A section inside the application that explains every colour direction, icon and the logo — the ayah (copied, never typed), the hadith reference, a design note — asked by the author, 2026-11-17 (§8.10). |
| F16 | Quran search | Search for a word with or without tashkeel, by the surah's name, and by the ayah's number (§8.1) — added by the author, 2026-11-17. |

Reference applications to study during design: Hisn Al-Muslim, Nusuk, Ayah, إذاعة القرآن الكريم من القاهرة, Radio Garden.

## 3. Repositories and workspace layout

The author asked for one GitHub repository per client and one for the backend. **Public repositories — anyone can
read, only the author can write** (author, 2026-11-16). Names (final unless the author changes them, §18.2 R1):

```
C:\Programming\WorkSpaces\Tajweed - The Noble Quran and Its Sciences\
                         = the documentation repository  -> github.com/Omar-Sherif-Sayed/tajweed-docs
  AGENTS.md              this file (parent)            README.md      for human readers
  .gitignore             ignores the four application folders below
  docs\
    README.md            index of all documents
    plan\                execution-plan.md — every task in detail
    sessions\            one record per working session
    data-sources\        the register of content sources (task P0-12)
    permissions\         permission letters and answers (task P0-13)
    design\              tokens.json, HTML prototypes, Figma link (task P0-11)
    deployment\          hosting and store guides (release track)
    quality\             acceptance runs, iPhone test sessions
  tajweed-backend\       Spring Boot REST API            -> github.com/Omar-Sherif-Sayed/tajweed-backend
  tajweed-frontend\      Angular web application         -> github.com/Omar-Sherif-Sayed/tajweed-frontend
  tajweed-android\       Android application             -> github.com/Omar-Sherif-Sayed/tajweed-android
  tajweed-ios\           iPhone application              -> github.com/Omar-Sherif-Sayed/tajweed-ios
```

| Repository | Holds | Does not hold |
| --- | --- | --- |
| `tajweed-docs` (this folder) | **The main picture of the whole product:** this `AGENTS.md`, the detailed plan and task status, decisions, the register of content sources, permission letters, the design (tokens, HTML prototypes, the Figma link and exported screens), hosting and store guides, session records and conversation copies | Application code |
| `tajweed-backend` | The Spring Boot REST API, the database migrations, the content import tool and the untouched source files of the content (Quran text, search text), the OpenAPI contract | Designs, product decisions |
| `tajweed-frontend` | The Angular web application | Content files (it reads the API) |
| `tajweed-android` | The Android application (Kotlin, Compose) with the Quran database shipped inside it | — |
| `tajweed-ios` | The iPhone application (Swift, SwiftUI) with the same Quran database | — |

Each application repository also has its own `AGENTS.md`, `README.md` and `docs/` — only about that codebase; anything
that concerns more than one application is written here.

- **The workspace folder itself is the fifth repository, `tajweed-docs`** (decided 2026-11-17, the author asked for
  a repository for the plan, the designs and everything that is not part of a running application). Reason: this
  file stays at the root, where every agent that opens the workspace reads it automatically, and it is versioned —
  one copy, no duplicate to keep in step. The four application folders are separate repositories; this repository
  ignores them. The folder is named `Tajweed - The Noble Quran and Its Sciences` (the author's choice, 2026-11-17). ⚠ The
  name contains spaces: every command puts the path in quotes.
- What belongs here: the plan, product rules and decisions, the source register, permissions, designs, store and
  deployment guides, session records. What does not: application code, and documents about one codebase (they live
  in that repository's own `docs/`).
- Each application repository: `AGENTS.md`, `README.md`, `docs/` (+ `docs/README.md` index), `LICENSE`, `.gitignore`,
  CI workflow.
- **The session memory is kept in this repository** in three forms: the current state in §0, a written record per
  session in `docs/sessions/`, and beside it a **conversation copy** — every message the author typed and every text
  answer of the agent, made by a script (rules in `docs/README.md`). ⚠ **Raw transcripts are never
  committed**: a transcript contains whole files of other projects, tool output and the author's e-mail, and this
  repository is public. They are kept privately on the author's machine in
  `C:\Programming\WorkSpaces\ai-agent-workspace\Tajweed\transcripts\`, with other private
  material such as the photos of the printed mushaf, and `session-notes.md` — the agent's private notes, which a new
  agent reads once (they hold what must not be public).

## 4. Technology

### 4.1 Versions (checked 2026-11-16 — re-check the patch numbers on the day each project is scaffolded)

| Part | Choice | Status |
| --- | --- | --- |
| Java | **25 (LTS)** — JDK 25.0.5 is installed on this machine | ✔ |
| Spring Boot | **4.1.x** — 4.1.2 is the current release on spring.io; Java 25 is supported since 4.0 | ✔ |
| Build | Gradle wrapper, latest 9.x at scaffold time (Groovy DSL — the author's usual choice) | ☐ |
| Database | **PostgreSQL** + Flyway (free and open source) | decided 2026-11-16 |
| Angular | **22.x** — released 2026-06-03, *Active* until 2027-06, then LTS until 2028-06 (angular.dev) | ✔ |
| UI library | **Angular Material 22.x** — 22.2.7 on material.angular.dev, MIT-style licence, no key (decided, §4.2) | ✔ |
| CSS | **Tailwind CSS 4**, added with `ng add tailwindcss` (the official guide, angular.dev/guide/tailwind) — §4.2 | ✔ guide · ☐ exact version at scaffold |
| Node | 22.23.5 installed; confirm it is in Angular 22's supported range when running `ng new` | ☐ |
| Android | Kotlin + Jetpack Compose + Media3 (latest stable at scaffold time) | decided, §4.3 |
| iPhone | Swift + SwiftUI + AVFoundation (latest stable Xcode at scaffold time) | decided, §4.3 |

About "LTS": in Angular, the newest major (22) is the *Active* version — it gets features and fixes. "LTS" is the
security-only phase of the previous major (21, until 2027-06). The best choice for a new project is the Active version.

### 4.2 UI library — decided: Angular Material + Tailwind CSS (PrimeNG dropped)

**Decision (author, 2026-11-16): option C — Angular 22 + Angular Material 22 + Tailwind CSS.** Reason: no licence
key, and the next major versions can be adopted without a licence question.

- **Angular Material** gives the interactive components (inputs, select, dialog, menu, tabs, slider, snack bar, …).
  Pages never import it directly: they use our own wrappers in `shared/component/general/` (the author's rule).
- **Tailwind CSS** gives layout, spacing and typography utilities. For Arabic / English, **only logical-direction
  utilities are used** (`ms-*`, `me-*`, `ps-*`, `pe-*`, `start-*`, `end-*`, `text-start`, `text-end`) — never `ml-*`,
  `mr-*`, `left-*`, `right-*`, `text-left`, `text-right`.
- **One set of design tokens** (§13) as CSS variables feeds both the Material theme and the Tailwind theme, so the two
  never disagree on a colour or a font.
- ☐ At scaffold time: the load order of Tailwind's base styles and the Material theme (CSS layers) is checked on a
  sample page before any page is built.

Background — why PrimeNG was dropped:

✔ Verified on primeui.dev ("The Next Chapter of PrimeTek"): PrimeNG 22 and later are distributed under the **PrimeUI
licence**, not MIT. PrimeNG 21 and earlier stay MIT forever but receive no new versions. The paid "PrimeNG LTS" is
closed for new sales.

| Option | Cost | Notes |
| --- | --- | --- |
| A. Angular 22 + PrimeNG 22, Community licence (not chosen) | Free | For individuals, non-profits and non-commercial open source. A licence key valid 12 months, renewed free every year (30-day grace period). ⚠ With a missing or expired key the library may show a licence notice in the application. |
| B. Angular 21 + PrimeNG 21 (last MIT version) | Free | No key. But Angular 21 is already in its security-only phase (ends 2027-06) and PrimeNG 21 gets no updates. |
| **C. Angular 22 + Angular Material — chosen** | Free (MIT) | Maintained by Google, no key; different components from the ones the author knows. |

The wrapper rule stays: the UI library is used **only through our own shared wrapper components** (the author's rule), so the
library can be replaced later without touching the pages.

### 4.3 Mobile: language and structure — decided: two native applications

**Decision (author, 2026-11-16): option 2 — two native repositories**, `tajweed-android` (Kotlin, Jetpack Compose) and
`tajweed-ios` (Swift, SwiftUI); every feature is written twice. The author has **no Mac and no iPhone**; a friend's
Mac is available for testing when the iPhone application is ready. Consequences: §11–12.

Background — the options that were compared:

- **Android in Java is not the best practice any more.** Google's Android development is Kotlin-first, and Jetpack
  Compose (the current UI toolkit) is Kotlin-only. The author knows Kotlin → **Kotlin**.
- **iPhone:** native is Swift + SwiftUI. ⚠ Building, signing and uploading an iPhone application needs **a Mac with
  Xcode** (or a paid cloud macOS build service) and an iPhone for testing — it cannot be done from Windows.

| Option | What it means |
| --- | --- |
| 1. Kotlin Multiplatform (not chosen) | The logic is written once in Kotlin (Quran data, prayer-time calculation, player rules, API client, storage) and shared by Android and iPhone; optionally the screens too (Compose Multiplatform — stable on iOS since 2025). The author can read and maintain almost everything. ⚠ It fits **one mobile repository** (`tajweed-mobile` with `shared`, `androidApp`, `iosApp`), not two. |
| **2. Two native applications — chosen** | `tajweed-android` (Kotlin, Compose) and `tajweed-ios` (Swift, SwiftUI). Best platform feel; every feature and every fix is written twice, and the author does not know Swift. |

One shared implementation also serves the "correct data" rule: the Quran text handling and the prayer-time
calculation exist once, so the two phones cannot disagree.

## 5. Architecture

```
  Angular web  ─┐
  Android app  ─┼──>  Spring Boot REST API (/v1/...)  ──>  PostgreSQL (verified content, Flyway)
  iPhone app   ─┘            │
        │                    └── schedulers: radio / audio source health checks
        └── audio streams directly from the recitation and radio sources (never through our server)
```

- **The backend serves verified content and catalogues**: Quran text and metadata, reciters and their audio sources
  (several mirrors each), timings, tafsirs, tajweed lessons, radio stations, muezzins, adhkar, hadiths, books.
  It is read-only for the public: there is no user data, so there is nothing to log in to.
- **Content enters the database only through reviewed Flyway migrations / import jobs** kept in the repository —
  there is no admin screen in the first versions (no login exists to protect one).
- **Clients work offline for the essentials**: the mobile apps ship the Quran text inside the application (it must
  open without a network); prayer times and Qibla are calculated on the device; API content is cached on the device.
- **Audio is streamed from its source** (not copied to our server) unless a source gives written permission to mirror.
- **Public API hygiene**: versioned paths (`/v1/...`), CORS for the web origin, rate limiting, HTTP caching (`ETag`,
  `Cache-Control`), a content-version endpoint so clients refresh their caches, OpenAPI document as the contract for
  the three clients (`docs/api/openapi.yaml`, generated).
- **No trackers.** No analytics or crash SDK that collects personal data. Location is used on the device only and is
  never sent to the backend.

## 6. Data integrity rules (binding — "wrong data is not allowed")

1. **The Quran text is never typed, edited, "cleaned", normalised or generated** — not by a person, not by code, not
   by an AI model. It is imported byte for byte from the chosen source file. The search text (§8.1) is a
   second file from a verified source, imported the same way and never displayed.
2. **Checksums.** The source file's SHA-256 is recorded in the data-source register; a test in every repository
   re-computes it and also checks the counts (114 surahs; 6,236 ayahs in the Hafs / Kufan numbering).
3. **Highlighting is a display layer** (the playing ayah, a search result, tajweed marks): positions are kept beside
   the text; the text itself is never changed.
4. **Every item of religious content carries its source**: tafsir (book and author), hadith (collection, number, grade,
   reference link), dhikr (reference as in the source book), tajweed rule (the classical text or book it comes from).
5. **An AI model does not author religious content.** It may structure, translate drafts and build screens; the text
   itself comes from the sources, and every item has a review status — only `REVIEWED` items are published.
6. **A qualified human reviewer** (a teacher with an ijazah for tajweed; a student of knowledge for hadith and adhkar)
   signs off the content before public release — §18 Q12.
7. **Audio matches the text shown.** A recitation is linked to its riwayah; a recitation in another riwayah is never
   played over the Hafs text as if it were the same (§7.3, Sheikh Noreen).
8. **Every source is in the register** `docs/data-sources/README.md`: URL, version / date, licence and terms, checksum,
   verification date, reviewer. A source whose licence is unclear is not used until its owner answers.
9. **Users can report a mistake** from every content screen (opens an e-mail or a form); reports are tracked.
10. **No reviewer yet (author, 2026-11-16) → only verbatim content from established sources of أهل السنة والجماعة.**
    Until a qualified reviewer exists: every religious text is copied verbatim from a named, recognised source and is
    shown with that source; nothing is written, summarised, paraphrased, merged or "explained" by us or by an AI
    model; an English religious text is only a published translation by a named translator (never a machine or AI
    translation) — where none exists the item is shown in Arabic with a note; a hadith is shown only with the grading
    stated by its source; anything that cannot be traced to its source is left out.
    ⚠ This guarantees that our copy equals the source — **it does not replace a scholar.** Content that needs a
    judgement (tajweed explanations §8.7, choosing a hadith explanation, any colouring of words §8.1) stays unpublished
    until a reviewer signs it, or one authoritative source covers it and permits its use.

## 7. Data sources

### 7.1 Verified on 2026-11-16

| Source | What | Facts verified |
| --- | --- | --- |
| Tanzil — `tanzil.net` | Quran text (several script types) | ✔ Creative Commons Attribution 3.0; verbatim copies allowed, **changing the text is not allowed**; the source must be shown with a link to tanzil.net; the copyright notice stays in the files. |
| mp3quran.net API v3 — `mp3quran.net/api/v3` | Reciters, surah audio files, radios, ayah timings | ✔ `reciters` (244 reciters, each with its "moshaf" list and surah count), `radios` (177 entries), `ayat_timing/reads` (115 recitations with per-ayah timings). ☐ Written terms of use / permission. |
| EveryAyah — `everyayah.com` | One audio file per ayah | ✔ Lists the recitations in §7.3. ☐ Terms of use / permission. |
| Quran Foundation API — `api-docs.quran.foundation` | Text, tafsirs, translations, audio with timings | ✔ Needs registration: OAuth2 client credentials, secret kept on our server; has its own developer terms (the text must not be modified). ☐ Request access; read the terms. |
| الدرر السنية — `dorar.net/article/389` | Hadith search with grading | ✔ A JSON search service for site owners exists (`dorar_api.json?skey=`). ☐ No published terms found — ask Dorar for permission and for the allowed use. |
| Angular, Spring Boot, PrimeNG | Versions and licences | ✔ §4. |
| Tanzil Quran Metadata 1.0 — `tanzil.net/res/text/metadata/quran-data.xml` | Page, juz, hizb-quarter and sajdah positions of the Madinah mushaf | ✔ Downloaded 2026-11-17 (SHA-256 in `docs/design/prototypes/assets/README.md`); Tanzil terms (CC BY 3.0). 604 pages, 240 quarters. |
| DigitalKhatt — `github.com/DigitalKhatt` | The whole Quran laid out as the printed old Madinah mushaf (1405H): 604 pages × 15 lines; the fonts DigitalKhatt Old Madina and New Madina | ✔ Layout in `digitalkhatt.org` (MIT); fonts SIL OFL 1.1 (stated in the repositories and inside the font). ✔ Verified 2026-11-17 against Tanzil: 0 word differences in 6,236 ayahs, 0 page-start differences in 604 pages; page 545 equals the author's photo; page 5 equals his printed copy. ⚠ The text's own origin is not stated by DigitalKhatt — the check above is what makes it usable. |
| King Fahd Complex fonts — via the mirror `github.com/nuqayah/qpc-fonts` | QCF page fonts (1405H, one font per page, each word the printed shape) and Uthmanic Script HAFS | ⚠ The Complex's site offers no download today («قريباً»); its copyright page is gone (404). Page fonts: "All rights reserved" only — **used by the author's decision (2026-11-17)**, credited, permission requested (`P0-13`). Hafs 0.09: licence inside the font allows use, copy and distribution, forbids sale and modification; ⚠ it does not draw U+06DF, so it is not usable as is. |
| Google Fonts — `github.com/google/fonts` | Amiri Quran, Scheherazade New, IBM Plex Sans Arabic, Inter, Noto Naskh Arabic | ✔ All SIL OFL 1.1 (`ofl/` folders with `OFL.txt`, checked 2026-11-17). |
| Noto Kufi Arabic — `github.com/notofonts/arabic` | The Kufic heading font of design 2 | SIL OFL 1.1 as stated by its packagers (Fontsource, FreeBSD ports; 2026-11-17). ☐ Read `OFL.txt` in the repository before it ships. |
| Apple notifications | Adhan on iPhone | ✔ A notification sound must be under 30 seconds (Apple documentation) — §8.6. |

### 7.2 Candidates — ☐ to verify before use (licence, completeness, accuracy)

| Need | Candidates |
| --- | --- |
| Quran text + matching font | Tanzil Uthmani text, or the King Fahd Complex (مجمع الملك فهد) Hafs text with its Uthmanic font. One text is chosen once and used by all clients. |
| Search text | Tanzil "Simple (Clean)" / "Simple" text — the same ayahs in everyday spelling — kept beside the displayed text as a search index (§8.1). ✔ These text types exist on tanzil.net/download (2026-11-17); ☐ compare with the displayed text ayah by ayah before use. |
| Tafsir (Arabic) | الميسر، السعدي، ابن كثير، الطبري، القرطبي، البغوي — through Quran Foundation API or QuranEnc. |
| Tafsir / translation (English) | QuranEnc (`quranenc.com`), Saheeh International — each translation has its own licence. |
| Prayer-time calculation | The open-source **Adhan** library (Batoul Apps; Kotlin / Swift / JavaScript editions) — calculated on the device, with the official methods (Egyptian General Authority of Survey, Umm Al-Qura, Muslim World League, …). |
| Adhkar | The book حصن المسلم (سعيد بن علي بن وهف القحطاني) — text checked against the printed book, item by item. |
| Hadith collections | Verified digital editions of صحيح البخاري and صحيح مسلم (numbering stated), with Dorar links for grading and explanation. |
| Books | المكتبة الشاملة (`shamela.ws`) editions — the classical texts are old, but a modern verified edition (تحقيق) can have rights. |
| Tajweed | Classical texts: تحفة الأطفال (الجمزوري), المقدمة الجزرية (ابن الجزري); reference: Dr. Ayman Suwayd's lessons and التجويد المصور — cited, not copied (book and figures are copyrighted). |
| Radio stations | mp3quran `radios`; each national station's own published stream; Radio Browser (community list) for discovery only. |
| Adhan recordings | Source and permission for each muezzin — none verified yet (§7.4). |

### 7.3 Requested reciters — what really exists (✔ checked 2026-11-16)

"Surah files" = mp3quran.net (number of surahs out of 114). "Ayah files" = EveryAyah. "Timings" = mp3quran ayah timings.

| Reciter | Surah files | Ayah files | Timings | Notes |
| --- | --- | --- | --- | --- |
| محمد صديق المنشاوي | مرتل 114 · مجود 114 · **معلم 114** | مرتل، مجود | ✔ | Complete. |
| محمود خليل الحصري | مرتل 114 · مجود 114 | مرتل، مجود، **معلم** | ✔ | The muallim mushaf is per ayah on EveryAyah. |
| عبد الباسط عبد الصمد | مرتل 114 · مجود 114 | مرتل، مجود | ✔ | ⚠ No muallim mushaf found for him. |
| محمد محمود الطبلاوي | مرتل 114 · مجود 114 | ✔ | ✔ | Complete. |
| محمد رفعت | ⚠ **31 surahs only** | — | — | **Not included for now** (author's rule: no complete mushaf → not shown). Second search 2026-11-16: surahquran.com lists 32 surahs although the page is titled "المصحف كامل"; archive.org and alkabbah.com hold separate historical recordings only. No complete mushaf found. |
| كامل يوسف البهتيمي | ⚠ not listed | — | — | **Not included for now.** Second search 2026-11-16: archive.org and alkabbah.com hold studio, radio and concert recordings of separate surahs; one alkabbah entry is labelled "المصحف المرتل" but shows no surah list, so completeness could not be confirmed. |
| ماهر المعيقلي | مرتل 114 · مجود 114 · معلم 38 | ✔ | مجود | Muallim incomplete (38). |
| ياسر الدوسري | 114 | ✔ | ✔ | Complete. |
| عبد الرحمن السديس | 114 | ✔ | ✔ | Complete. |
| سعود الشريم | 114 | ✔ | ✔ | Complete. |
| نورين محمد صديق | 114 | — | — | ⚠ **Riwayah الدوري عن أبي عمرو, not Hafs.** The words differ from the Hafs text in places — rule §6.7. |
| فارس عباد | 114 | ✔ | ✔ | Complete. |
| سعد الغامدي | 114 | ✔ | ✔ | Complete. |
| علي بن عبد الرحمن الحذيفي | 114 (Hafs) | ✔ | ✔ | Confirmed by the author (2026-11-16): this is the intended "الحذيفي". |
| أيمن رشدي سويد (for F4 / F6) | **معلم 114** | ✔ | ☐ | Useful for the tajweed section. |

The YouTube playlist the author sent is «المصحف المعلم للأطفال — الشيخ الحصري مع ترديد الأطفال». ⚠ YouTube content cannot
be extracted or downloaded (its terms forbid it); it can only be embedded with YouTube's own player, which may show
YouTube advertisements — that conflicts with the no-ads rule. Use the Husary / Minshawi muallim audio sources above.

### 7.4 Requested muezzins — ☐ nothing verified yet

المنشاوي، عبد الباسط، الحصري، محمد رفعت، علي أحمد ملا، حمد بن أحمد الدغريري. For each: find a clean recording, its origin
and the permission to use it; a full version and a short version (under 30 seconds for iPhone notifications, §8.6).

### 7.5 ⚠ Rights

Free of charge is not the same as free to redistribute. Recitation recordings, adhan recordings, tafsir editions,
translations and book editions often belong to a publisher, a broadcaster or an heir. The application links to or
streams from the published source and shows the credit; where the terms are unclear we ask in writing and keep the
answer in `docs/permissions/`. Apple's review can ask for proof of the right to use third-party content.

## 8. Feature notes and platform limits

### 8.1 F2 / F16 — Quran reader and search

**Reader (F2) — decision (author, 2026-11-17): a standard mushaf. One text colour, complete tashkeel, no coloured
words.**

- **Text:** the fully vocalised Uthmani script of the printed mushafs (Hafs, 6,236 ayahs), imported byte for byte
  (§6.1). It is drawn with the font made for that text, so that every mark appears exactly as printed: the tashkeel,
  the small alef, the madd sign, the sukun, the pause marks.
- **Rendering check on every client:** sample pages are compared with a printed mushaf, mark by mark, on real
  devices — a wrong font or a missing mark is treated as wrong data.
- **Page layout identical to the printed mushaf (author, 2026-11-17)** — so that a person who memorises from a
  printed mushaf finds no difference: page 1 is Al-Fatihah; page 5 begins with 2:25 and its first line ends with
  «جَنَّٰتٖ»; every page has 15 lines (pages 1 and 2 are the decorated opening pages); juz, hizb and quarter marks
  (۞) stand where the printed copy has them. This is the default reading view; a continuous "by surah" view is a
  second option. Go to surah / juz / hizb / page / ayah. Light and dark theme.
- **Which printed edition — research of 2026-11-17.** Two Madinah layouts exist in open data. The author's
  photographed page 545 (58:22 – 59:3) matches, line by line, the **old Madinah layout (1405H print, written by
  Uthman Taha)** and not the newer one, which breaks the same page differently. Proposed: the old Madinah layout.
  In that layout, ayah 2:25 takes lines 1–4 of page 5 (line 1 ends with «جَنَّٰتٖ», line 4 with «خَٰلِدُونَ ٢٥») —
  ✔ confirmed by the author on his printed copy (2026-11-17).
- **Layout source — candidates (☐ decided in task P0-12):**
  - **DigitalKhatt** (github.com/DigitalKhatt, sponsored by Tarteel): the whole Quran as 604 pages × lines, old and
    new Madinah layouts, in the `digitalkhatt.org` repository (MIT licence); fonts made for those layouts —
    `oldmadinafont` and `madinafont` (SIL Open Font Licence 1.1). ✔ Checked 2026-11-17: 604 pages; page 5 and page
    545 as above; the ۞ quarter marks are in the text. ⚠ The text's own origin is not stated: before use, a script
    must prove that every one of the 6,236 ayahs has the same words as the verified text (§6.1); any difference is
    listed and not shipped.
  - **King Fahd Complex page fonts (QPC V1, 1405H)** — one font per page, used by large Quran sites. ⚠ The
    Complex's own site lists its fonts as «قريباً» (no download, 2026-11-17); copies exist only on third-party
    mirrors with no licence file — not usable until the licence is confirmed (§6.8).
  - **QUL (qul.tarteel.ai) layout databases** — ⚠ the resource page says it has no copyright information; several
    open questions ask the same. Not usable until answered.
- **Round 2 findings (2026-11-17)** — details in `docs/design/prototypes/assets/README.md`:
  - The **King Fahd page fonts** reproduce the printed page exactly (checked on pages 1, 2, 5, 545, 546). Their
    glyph list matches the layout word by word except in **9 ayahs** (2:79, 13:37, 18:1, 19:38, 36:52, 69:8, 69:28,
    75:27, 83:14 — mostly saktah signs drawn as separate glyphs) and gives page 588 instead of 589 for 83:35: these
    need an explicit, reviewed table in `P0-12` before every page is shipped.
  - **Quarter sign at 15:49** — ✔ settled 2026-11-17: the author's printed copy (photo of pages 263–264) has the
    ۞ before 15:49, as the layout and the King Fahd data; Tanzil's metadata gives 15:50. In the applications the
    quarter positions come from the layout, not from Tanzil's metadata (`P0-12`).
  - **Fonts that can ship:** King Fahd page fonts (author's decision), DigitalKhatt Old and New Madina, Amiri Quran,
    Scheherazade New. KFGQPC Uthmanic HAFS 0.09 cannot (missing mark). ✔ **Default chosen by the author
    (2026-11-17): the King Fahd page fonts — Madinah mushaf 1405H.**
  - **The author's printed copy** (title page photographed 2026-11-17): «القرآن الكريم برواية حفص عن عاصم بالرسم
    العثماني», printed by دار طيبة, Cairo. Its pages 1, 2, 5, 263, 264, 545 and 546 match the old Madinah layout
    line by line. «بالرسم العثماني» names the spelling of the words (the Uthmani rasm), which every Madinah mushaf
    and the Tanzil Uthmani text follow — it is not the name of a font.
- **Surah details and the index (author, 2026-11-18).** Beside each surah's name: Makki or Madani, its number of
  ayahs and its order in the mushaf. On the mushaf page itself the header line shows «ترتيبها» and «آياتها» as
  the author's printed copy does; Makki / Madani is shown in the reader's title bar. An index (فهرس) lists the 114
  surahs (order, name, Makki / Madani, ayahs, first page) and the 30 juz (first ayah, first page). Source: Tanzil's
  metadata (`type`, `ayas`, page starts). ☐ `P0-12`: compare Makki / Madani with the index of the printed Madinah
  mushaf, surah by surah, and record any difference — the classification of a few surahs differs between sources.
- **Justification:** printed lines are filled by stretching letters (kashida), not by wider spaces. The DigitalKhatt
  fonts can do this; other fonts can only widen spaces. ☐ Decided with the font (P0-12).
- **The coloured name of Allah is withdrawn.** History, so that it is not proposed again without new facts: requested
  on 2026-11-16; the author's printed mushaf (reviewed by the Al-Azhar committee, Hafs) prints «الله» in red; no
  digital word list of that edition exists; printed mushafs do not agree on which words are coloured; deciding what a
  pronoun refers to is tafsir; a scholarly opinion objects to the colouring itself (islamqa.info, answer 21875). The
  author's rule: *"if you do not have a good example, don't do it."* It may return only as an optional setting, and
  only with a word list from an authoritative source that a qualified reviewer has checked.

**Search (F16) — added by the author, 2026-11-17.** One search box, three kinds of search:

| Kind | What the user types (illustration) | Result |
| --- | --- | --- |
| A word or several words, **with or without tashkeel** | the word with its marks, or the same letters without any mark | The ayahs that contain it, the match highlighted, the number of results, grouped by surah |
| **Surah name** | the Arabic name with or without «سورة» / «ال», the English name in its common spellings, or the surah's number | The surah |
| **Ayah number** | `2:255` · a surah name followed by a number · a number alone inside an open surah | The ayah, opened in the reader |

Rules:

1. **The displayed text is never changed for the search** (§6.1). Search uses a separate **search text** kept beside
   each ayah and never shown.
2. ⚠ **Why removing the tashkeel from the displayed text is not enough.** The mushaf is written in الرسم العثماني, and
   many words are spelled differently from everyday writing (for example the words for "the prayer" and "the book"
   carry a small alef instead of a written one). A user types the everyday spelling and would find nothing.
   **Solution:** the search text is the same Quran in everyday spelling, taken from a verified source — candidate:
   Tanzil's "Simple" (with tashkeel) and "Simple (Clean)" (without) text types (✔ they exist on tanzil.net/download,
   2026-11-17; same licence as §7.1). It is imported byte for byte, with its checksum, and a test proves it has the
   same 6,236 ayahs in the same order as the displayed text.
3. **What the user types is tidied before matching** — this is done to the query, not to the Quran: tashkeel and
   tatweel are removed when the query has no tashkeel; the forms of alef (أ إ آ ٱ ا) are treated as one letter;
   extra spaces are ignored. The same function is applied to the search text when the index is built, by code, in
   one place, with tests. ☐ The exact list of letter equivalences is fixed in task P1-D3 and written here.
4. **With tashkeel:** when the query contains tashkeel, it is matched against the vocalised search text, so the marks
   the user typed must agree. **Without tashkeel:** all marks are ignored.
5. **The same results everywhere.** The web asks the backend (`GET /v1/quran-search`, PostgreSQL); the phones search
   on the device so that it works without a network (SQLite full-text search). All three are built from the same
   search-text file, and a fixed list of test queries with their expected number of results runs on all three.
6. **Surah names** are matched against our own list (Arabic names, English names, common spellings), tidied by the
   same function. The list is data with a source, like everything else.
7. Searching inside translations and tafsirs is not part of F16 (it depends on the licences of §7.2).

### 8.2 F3 / F4 — Recitation

- Modes: one surah · an ayah range · from a start ayah to the end of the Quran and again from Al-Fatiha, without end.
- Per-ayah playback and highlighting use either ayah files (EveryAyah) or surah files with ayah timings (mp3quran).
- A recitation style is offered only where it really exists (§7.3); an incomplete mushaf shows which surahs it has.
- Background playback with lock-screen / notification controls on both phones; Media Session on the web.

### 8.3 F11 — Resilient playback (radio and recitation)

- Every recitation and station has an **ordered list of sources**. On an error: retry the same source with a growing
  delay (capped, e.g. 30 s), then the next source, round and round, **without limit**, until the user stops it.
- The device's "network is back" signal triggers an immediate retry. A file resumes at the same position; a radio
  resumes at the live point. The screen shows «جارٍ إعادة الاتصال…» instead of an error.
- Android: Media3 ExoPlayer in a media-playback foreground service. iPhone: AVPlayer + network path monitor +
  background audio mode. Web: the audio element + `online` event (⚠ the browser tab must stay open).

### 8.4 F7 — Radio

- A station record: country, names (AR / EN), the broadcaster's site, stream addresses (primary + alternatives),
  verification date, health status. A backend scheduler tests the streams and hides dead ones.
- "Free and available" is applied as: **only a stream the broadcaster itself publishes openly**; we never re-broadcast
  it through our server. ⚠ We cannot certify each country's broadcast law; a station is removed at its owner's request.

### 8.5 F8 / F10 — Prayer times and Qibla

- Calculated on the device from its location (or a chosen city): calculation method, Asr school (Shafi'i / Hanafi),
  high-latitude rule, per-prayer minute adjustment. The default method follows the country; the user can change it.
  ⚠ Times can differ by a minute or two from a local mosque's calendar — the method and adjustments are shown.
- **By the user's own location, on the web and on the phones (author, 2026-11-17)** — Egypt, Saudi Arabia and
  Japan get different times, and a different default method where the country has an official one: Egypt → the
  Egyptian General Authority of Survey; Saudi Arabia → Umm Al-Qura (☐ each confirmed with a named source in
  `P2-D1`). A country without a verified source falls back to Muslim World League and the screen says so. Web:
  the browser asks for the location (or the user picks a city); the calculation runs in the browser and the
  location is never sent to the backend.
- **Not to be forgotten (author, 2026-11-17):** `P2-D1` — the default prayer-time method of every country, each with a named official source (the author, 2026-11-17: it may be done at any time, before phase 2 starts). Plan: `docs/plan/execution-plan.md`, `P2-D1`.
- Background by time of day (Fajr, sunrise, Dhuhr, Asr, Maghrib, Isha) — §13.
- Qibla: bearing calculated from the location to the Kaaba + the phone's compass, with a calibration hint.
  ⚠ Web on a computer has no compass: it shows the bearing on a map / as degrees.

### 8.6 F9 — Adhan (⚠ real platform limits)

| Platform | What is possible |
| --- | --- |
| Android | Full adhan at the exact time, even when the app is closed (exact alarm + playback service). Needs the notification and exact-alarm permissions; some manufacturers' battery savers must be disabled by the user. |
| iPhone | ⚠ When the app is not open, iOS only plays a **notification sound shorter than 30 seconds**. So: a short adhan in the notification; the **full adhan plays when the user opens the app** (or taps the notification). This is Apple's rule for all applications. |
| Web | ⚠ Only while the page is open. No reliable adhan from a closed browser. |

### 8.7 F6 — Tajweed curriculum (content scope)

Order follows the classical teaching order. Every lesson: the rule, its letters, the memory word, examples from the
Quran with audio (an ayah or a word clip from the chosen reciter), and the source. Memory words to include — each one
is re-checked against تحفة الأطفال / المقدمة الجزرية before publishing:

| Topic | Rules and memory words |
| --- | --- |
| النون الساكنة والتنوين | الإظهار الحلقي (ء هـ ع ح غ خ): أوائل «أخي هاك علمًا حازه غير خاسر» و«إن غاب عني حبيبي همّني خبره» · الإدغام: «يرملون» (بغنة «ينمو»، بغير غنة: ل ر) · الإقلاب: الباء · الإخفاء (15 حرفًا): أوائل «صف ذا ثنا كم جاد شخص قد سما / دم طيبًا زد في تقى ضع ظالمًا» |
| الميم الساكنة | الإخفاء الشفوي (ب) · إدغام المثلين الصغير (م) · الإظهار الشفوي (باقي الحروف) |
| النون والميم المشددتان | الغنة |
| اللام | القمرية: «ابغ حجك وخف عقيمه» · الشمسية: أوائل «طب ثم صل رحمًا تفز ضف ذا نعم / دع سوء ظن زر شريفًا للكرم» · لام لفظ الجلالة (تفخيم وترقيق) |
| المدود | حروف المد «نوحيها» · الطبيعي والبدل والعوض والصلة · المتصل والمنفصل · العارض للسكون واللين · اللازم (كلمي وحرفي) · الحروف المقطعة: «نقص عسلكم»، «حي طهر»، «صله سحيرًا من قطعك» |
| مخارج الحروف | الجوف، الحلق، اللسان، الشفتان، الخيشوم |
| صفات الحروف | الهمس «فحثه شخص سكت» · الشدة «أجد قط بكت» · التوسط «لن عمر» · الاستعلاء «خص ضغط قظ» · الإطباق (ص ض ط ظ) · الإذلاق «فر من لب» · الصفير (ص ز س) · القلقلة «قطب جد» · اللين، الانحراف، التكرير، التفشي، الاستطالة |
| التفخيم والترقيق | حروف الاستعلاء · أحكام الراء · أحكام اللام والألف |
| المتماثلان والمتجانسان والمتقاربان | الإدغام وأنواعه |
| الوقف والابتداء | أنواع الوقف، علامات الوقف في المصحف، السكت، همزة الوصل والقطع، الروم والإشمام |

### 8.8 F5, F12, F13, F14 — Text content

- **Tafsir (F5):** "all its tafsirs" = a fixed list of named tafsirs we have the right to show (§7.2), Arabic first.
- **Adhkar (F12):** categories, each dhikr with its text, repeat count, reference and virtue as in the source book; a
  tap counter; morning / evening reminders (optional).
- **Hadith (F13):** ⚠ "all hadiths" is hundreds of thousands of narrations. Proposed start: الأربعون النووية, then صحيح
  البخاري and صحيح مسلم, each hadith with number, grade and a link to its page on الدرر السنية for the takhrij and
  explanation (we link to the explanation rather than copy it, unless Dorar permits) — §18 Q11.
- **Books (F14):** a reader with volumes / chapters / pages and search; large texts are loaded by chapter.

### 8.9 More languages (author, 2026-11-17 and 2026-11-18)

Arabic and English first. The author asked on 2026-11-17 for German, Italian, Japanese and Chinese, and on 2026-11-18
for Russian, Spanish, German, Italian, French, Urdu ("Pakistani" — Urdu is Pakistan's national language), Hindi,
Korean and Indonesian, and asked which others should be there. The agent recommended Turkish, Bengali, Persian,
Malay, Swahili, Hausa, Portuguese, Pashto and Uzbek — languages of large Muslim communities, each with a published
translation of the meanings on QuranEnc. ✔ **The author accepted all nine (2026-11-18): 22 languages in all.** He
confirmed that «الباكستانية» means Urdu, and that Hindi, written twice in his message, is one language. Others on
QuranEnc, not planned, can be added later: Tamil, Bosnian, Albanian, Kurdish, Somali, Amharic, Tagalog, Thai.

**All 22 available from the first release (author, 2026-11-19: "make all languages available now").** What it
means, and the conditions that keep it correct:

- The interface works in every language: its texts, its direction (right to left for Arabic, Urdu, Persian, Pashto),
  its font, and numbers and times in its own format (the platform's locale functions; Persian, Pashto and Bengali
  use their own digits).
- **Interface texts:** the agent wrote drafts of all 20 languages for the prototype (`docs/design/prototypes/i18n/`,
  153 texts each with round 4, checked by the build: every key present, every number slot kept). **No native
  readers** (author, 2026-11-19): the screen says "Interface translation by the project. Found a mistake? Report it
  on GitHub."; the author collects the reports (GitHub issues) and the agent corrects them (`LANG-02`). The texts
  most likely to need corrections are Hausa, Pashto, Uzbek and Swahili.
- **Religious content does not change:** the Quran is always the Arabic text; a meaning in a language is shown only
  from a published translation by a named translator with permission (QuranEnc, `P0-13`); without it the Arabic is
  shown with a note (§6.10). Hadith and adhkar texts likewise.
- **Surah names:** Arabic names for Arabic-script languages, Tanzil's transliteration for the others in the
  prototype; ☐ a named source for surah names per language (`LANG-02`).
- The first release is therefore larger: 22 store listings and more fonts to ship.

**On the first screen (author, 2026-11-18: "a drop-down list or anything better"):** a language button shows the
current language in its own script and the number of languages; it opens a list over the screen with a search box
(a language can be found by its own name, its Arabic name, its English name or its code), the device's own language
first (read on the device, never sent anywhere), then all 22 languages. Each row shows the language in its own
script, its name in the interface language and "right to left" where it applies; choosing one switches the whole
interface at once. Prototype: `docs/design/prototypes/round-3.html`, phone 1.

| Code | Language | Script, direction | Interface font (☐ licence read before use) | Published translation of the meanings — QuranEnc, read 2026-11-18 |
| --- | --- | --- | --- | --- |
| ar | العربية — Arabic | Arabic, RTL | IBM Plex Sans Arabic / Noto Kufi Arabic | — (the Quran itself) |
| en | English | Latin, LTR | Inter | ☐ several on QuranEnc (e.g. Saheeh International) |
| ru | Русский — Russian | Cyrillic, LTR | Inter | ☐ Rowwad Translation Center; Abu Adel |
| es | Español — Spanish | Latin, LTR | Inter | ✔ Muhammad Isa García; Noor International Center |
| de | Deutsch — German | Latin, LTR | Inter | ✔ Frank Bubenheim and Dr. Nadeem Elyas; Rowwad; Abu Rida |
| it | Italiano — Italian | Latin, LTR | Inter | ✔ Rowwad Translation Center |
| fr | Français — French | Latin, LTR | Inter | ✔ Rashid Maash; Dr. Nabil Radwan; Muhammad Hamidullah |
| ur | اردو — Urdu (the national language of Pakistan) | Arabic script (Nastaliq), RTL | Noto Nastaliq Urdu | ☐ Muhammad Ibrahim Junagarhi; Dr. Muhammad Luqman Salafi |
| hi | हिन्दी — Hindi | Devanagari, LTR | Noto Sans Devanagari | ☐ Azizul Haq al-Umari |
| ko | 한국어 — Korean | Hangul, LTR | Noto Sans KR | ☐ Hamid Choi; Rowwad |
| id | Bahasa Indonesia — Indonesian | Latin, LTR | Inter | ☐ Indonesian Ministry of Religious Affairs; Sabiq |
| ja | 日本語 — Japanese | Japanese, LTR | Noto Sans JP | ☐ Saeed Sato |
| zh | 中文 — Chinese | Chinese (simplified), LTR | Noto Sans SC | ☐ Muhammad Makeen (attribution to be checked) |
| tr | Türkçe — Turkish | Latin, LTR | Inter | ✔ Rowwad Translation Center; ☐ others |
| bn | বাংলা — Bengali | Bengali, LTR | Noto Sans Bengali | ☐ Abu Bakr Zakaria; Rowwad |
| fa | فارسی — Persian | Arabic script, RTL | Vazirmatn or Noto Naskh Arabic | ☐ Rowwad Translation Center |
| ms | Bahasa Melayu — Malay | Latin, LTR | Inter | ☐ Abdullah Basmeih |
| sw | Kiswahili — Swahili | Latin, LTR | Inter | ✔ Ali Muhsin al-Barwani; Dr. Abdullah Muhammad Abu Bakr and Sheikh Nasser Khamis; Rowwad |
| ha | Hausa | Latin, LTR | Inter | ✔ Abubakar Mahmoud Gumi |
| pt | Português — Portuguese | Latin, LTR | Inter | ✔ Dr. Helmi Nasr |
| ps | پښتو — Pashto | Arabic script, RTL | Noto Naskh Arabic | ☐ Rowwad; others |
| uz | Oʻzbekcha — Uzbek | Latin, LTR | Inter | ☐ Muhammad Sadiq Muhammad Yusuf; Rowwad |

✔ = read word for word on quranenc.com/en/home; ☐ = read only in a summary of that page, to be checked. Al-Mukhtasar
and Tafsir al-Sa'di entries on QuranEnc are tafsirs, not translations of the meanings. ⚠ QuranEnc says its
translations "can be downloaded and re-published, subject to" its Terms and Policies, but the link to them leads
nowhere (2026-11-18) → ask in writing (`P0-13`) before any translation is shipped.

What this means from day one, in all four codebases:

- No user-facing text in code: every text has a key in a language file (`ar`, `en`; later the other 20 codes of the
  table above).
- Numbers, dates and times are formatted through the platform's locale functions, never by hand.
- Layouts work in both directions (Arabic right to left, the others left to right) and do not assume a word
  length: German is long, Japanese and Chinese are short and need their own interface fonts.
- The language list is data (code, native name, direction, font), so adding a language does not change screens.
- Four of the planned languages are written right to left (Arabic, Urdu, Persian, Pashto); Urdu needs a Nastaliq
  font. Hindi, Bengali, Korean, Japanese and Chinese need their own fonts.
- Every language's interface text is translated by the agent and corrected from users' reports on GitHub (`LANG-*`
  tasks, §14.1; author, 2026-11-19 — no native readers).
- Backend: `Accept-Language` decides the language of messages and of names that exist in that language; content
  tables keep one row per language.
- ⚠ **Religious content in a new language** (meaning of the ayahs, tafsir, hadith, adhkar) is only a **published
  translation by a named translator with permission** (§6.10) — never a machine or AI translation. Where none
  exists, the screen shows the Arabic with a note. The interface (buttons, menus) can be translated freely.

### 8.10 F19 — Why this design (author, 2026-11-17)

The author asked that every colour, icon and the logo have a reason taken from the Quran, the hadith and the first
era of Islam, and that the reasons become a section of the application. The reasons are written in
`docs/design/design-2-meanings.md` (design 2) and `docs/design/design-3-meanings.md` (design 3); the section follows
the rules there:

- a colour is "named after a word" of an ayah — never "the meaning" of an ayah (that is tafsir, §6.10);
- the ayah is shown whole, from the Quran text the application ships, with its reference; never typed;
- a hadith is shown by book, number and the grading stated by its source;
- where a word needs explaining, only the verbatim text of a named, licensed tafsir;
- every card says "This is a design choice, not an interpretation" in both languages;
- **no cross shape anywhere** — no plus sign, no four-armed star or spark, in any icon, logo or drawing (author,
  2026-11-19: it is a symbol of Christianity, and this is an Islamic application); a star is a round dot;
- 30:22 (the languages of people) is shown beside the language choice only — after reading its tafsirs, its
  colours are people's colours, so it is not used for the colour directions (author's request, 2026-11-18);
- **only Mountains** («الجبال — لضعف البصر وعمى الألوان») is made for readers with colour blindness or weak sight —
  7 : 1, also as simulated for the three kinds of colour blindness, and colour is never its only signal; the
  other directions and their night themes are not built for it (author, 2026-11-18);
- English shows an ayah's meaning only from a published translation;
- before release a qualified reviewer reads it (§6.6), or it stays inside the rules above.

Tasks: `P0-16` (the document — done in draft), `P1-D6` (content in both languages), `P1-W9`, `P1-A7`, `P1-I7`
(the screen).

## 9. Backend — `tajweed-backend` (structure and conventions)

The author's usual backend style. The conventions below are the complete list for this product; the repository's
own `AGENTS.md` (task P0-07) repeats them with examples from the code.

```
src/main/java/<base.package>/
  Application.java
  business/<module>/
    controller/      <Entity>RetrievalController ...            @RequestMapping("/v1/<plural-kebab>")
    service/         <Entity>RetrievalService (interface)       service/impl/ <Entity>RetrievalServiceImpl
    repository/      <Entity>Repository (Spring Data JPA)       specs/ <Entity>Specs
    entity/          JPA entities                               mapper/ <Entity>Mapper (final, static methods)
    schema/request/  Req<X>                                     schema/response/ Dto<X> (+ search projections)
    enums/           with nameAr / nameEn                       constant/ Constant<Entity>     scheduler/
  general/           exception (ErrorCode, BaseException, GlobalExceptionHandler), schema (BaseResponse),
                     audit (AbstractAuditingEntity), config (CORS, cache, rate limit, OpenAPI), i18n, util
src/main/resources/
  application.properties (+ application-<profile>.properties)   every value from environment variables
  db/migration/      V<MAJOR>_<MINOR>_<PATCH>__<description>.sql (PostgreSQL)
  i18n/              messages.properties (Arabic) + messages_en.properties (English)
docs/                api/ (OpenAPI), data-sources/, permissions/, deployment/, quality/ (+ README.md index)
```

| Module | Holds |
| --- | --- |
| `quran` | surahs, ayahs, pages / juz / hizb, search text, surah-name spellings |
| `reciter` | reciters, recitations (style, riwayah, completeness), audio sources and mirrors, ayah timings |
| `tafsir` | tafsir books, tafsir text per ayah |
| `tajweed` | topics, rules, memory words, examples (ayah / word + audio) |
| `radio` | stations, streams, health checks |
| `prayer` | calculation-method metadata, muezzins, adhan audio sources |
| `adhkar` | categories, adhkar, counts, references |
| `hadith` | collections, books, chapters, hadiths, grades, reference links |
| `library` | books, volumes, chapters, pages |
| `appinfo` | about / author, content versions, sources and credits |

Conventions: constructor injection with Lombok `@RequiredArgsConstructor` (no `@Autowired`
fields); `@Transactional(readOnly = true)` on read services; responses wrapped in `BaseResponse<T>`; `Req*` / `Dto*`
naming; closed interface projections for lists; one `ErrorCode` enum grouped by prefix (`NOT_FOUND_*`, `INVALID_*`,
…) with a message key in **both** i18n files; `spring.jpa.hibernate.ddl-auto=validate` (entities must match Flyway
exactly); entities extend `AbstractAuditingEntity`, primary key `pk_id`, every constraint named; never edit an applied
migration; log identifiers not payloads, never swallow an exception; ShedLock-style scheduler pattern; tests — JUnit
Jupiter + AssertJ + Mockito, WireMock for HTTP clients, Testcontainers (PostgreSQL) tagged `integration`, class
Javadoc + `@DisplayName`, given / when / then, `<Module>TestData` fixtures.

Specific to this product: no authentication, roles, permissions or payments (the API is public and read-only);
PostgreSQL; content checksums tested (§6); rate limiting and HTTP caching for a public API.

## 10. Web — `tajweed-frontend` (structure and conventions)

The author's usual web style. The conventions below are the complete list for this product; the repository's own
`AGENTS.md` (task P0-08) repeats them with examples from the code.

```
src/app/
  component/<module>/            pages per feature: quran, recitation, tafsir, tajweed, radio, prayer-times,
                                 qibla, adhkar, hadith, library, about, onboarding (language choice)
  shared/
    component/general/           our wrappers around the UI library (inputs, buttons, dialogs, drawer, tag, ...)
    component/business/          reusable domain blocks (ayah view, audio player bar, reciter picker, ...)
    layout/                      main layout, navigation, header, footer
    service/                     audio-player, settings, app-translate, error-handling
    service/integration/<m>/     HTTP services, one per backend controller area
    schema/request|response/<m>/ Req<X> / Dto<X> interfaces mirroring the backend
    enums/<m>/                   string enums mirroring backend enum names
    utils/  constants/  validator/  interceptor/  resolver/  directives/
  app.routes.ts  app.config.ts
src/assets/i18n/ar.json | en.json
```

Conventions kept: standalone components; `inject()` field injection; signal APIs only (`input`, `output`, `model`,
`viewChild`, `computed`); built-in control flow (`@if`, `@for`, `@switch`); path aliases (`@component`, `@shared`,
`@environment`, `@assets`); lazy routes with `withComponentInputBinding`; TanStack Query for loading data; ngx-translate
with keys in both files; enum labels through an explicit i18n prefix; ESLint at 0 errors; no `console.log`; strict
templates (`ngc --noEmit`). From day one: `OnPush` / zoneless and Vitest.

UI stack (§4.2): Angular Material through our wrappers + Tailwind CSS utilities (logical-direction utilities only);
component styles stay small — a Tailwind utility first, a component SCSS rule only when no utility fits.

Specific to this product: Arabic-first RTL with a first-visit language choice saved in the browser; all preferences
(reciter, last read position, bookmarks, prayer settings) in browser storage — no account; one global audio player
service that implements §8.3; no third-party scripts (no ads, no trackers).

## 11. Android (`tajweed-android`) and 12. iPhone (`tajweed-ios`) — two native applications

Decided 2026-11-16 (§4.3). Order: **Android first**; each feature is ported to iPhone after it is stable on Android,
so the Swift code follows a design that already works.

⚠ **iPhone without a Mac.** Swift code written on Windows cannot be compiled or run there, and code that was never
compiled is not trusted. Plan:

- The Xcode project is described by a text file kept in the repository (a project generator such as XcodeGen —
  ☐ tool chosen on scaffold day), so no Mac is needed to create or change the project.
- **Every push is built and unit-tested on a macOS runner in GitHub Actions** (☐ to verify on scaffold day: standard
  hosted runners are free for public repositories). This proves the code compiles and the tests pass.
- Running on a real iPhone, sound / background / notification behaviour, signing and the App Store upload need the
  friend's Mac and an iPhone (or a paid cloud Mac) — collected into test sessions, with a written checklist in
  `docs/quality/`.
- Nothing in `tajweed-ios` is called "done" before it has been built in CI and tried on a device.

Agreed for both platforms whatever the option:

- Layers: `data` (API client, local database, repositories) → `domain` (models, use cases) → `ui` (screens, state).
  Names mirror the backend (`Dto*`, `Req*`, enum names) so a concept has one name in four codebases.
- Local database for the bundled Quran text and cached content; key-value storage for preferences.
- One player component implementing §8.3; one prayer-time component using the Adhan library.
- Strings in Arabic and English resource files; RTL layouts; dynamic font size; light and dark themes.
- Minimum OS versions, exact library versions and the module tree are fixed on scaffold day and written to the
  repository's own `AGENTS.md`.
- Every public class and function is documented, because the author is new to mobile development; each repository's
  `README.md` explains how to build, run on a device, and release, step by step.

## 13. Design system and Figma

- **One design language for web, Android and iPhone**: colours, typography, spacing, icons and components defined
  once as tokens (`docs/design/tokens.json` in the docs repository) and exported to SCSS, Compose and SwiftUI.
- **Colour direction (proposal — final values after the author sees the screens):** deep emerald green as the primary
  colour, warm gold as the accent, parchment cream for the reading surface, and deep navy for the night theme.
  The Quran text has one colour (§8.1). Prayer screen backgrounds: Fajr
  indigo-to-rose dawn, Dhuhr clear sky blue, Asr warm amber, Maghrib orange-to-violet sunset, Isha deep navy with stars.
- **Typography (open licences):** a Quran font matched to the chosen Quran text (§7.2); Arabic interface font IBM Plex
  Sans Arabic; English interface font Inter.
- **Figma:** possible in two ways — through the author's Chrome session, or through the Figma connector (it mostly
  reads designs). Recommendation: first build the screens as interactive HTML prototypes (real Arabic text, real RTL,
  fast to review and change), agree on colours and layout, then produce the Figma file from the agreed design — §18 Q8.
- **Decided (2026-11-16):** HTML prototypes first; after the author approves the colours and the layout, the Figma
  file is created in the author's own Figma account through his Chrome session (the account he named for this project).
- **Round 1 (2026-11-17) — waiting for the author's choice:** `docs/design/prototypes/colour-directions.html`, one
  self-contained page with three directions — **A** emerald and gold on parchment, **B** deep teal and sand, **C**
  "mushaf" (cream page, dark red and black frame, after the author's printed mushaf) — each on four screens
  (language choice, home, Quran reader, player), Arabic and English, light and dark, with three Quran fonts to
  compare. The Quran text on the reader screen is real: a script copies it from the untouched Tanzil file
  (`docs/design/prototypes/assets/tanzil/`, checksum recorded) — nobody typed it. Every text / background pair
  passes 4.5 : 1 in all six combinations. Details and limits: `docs/design/README.md`.
- **Decided after round 1 (author, 2026-11-17): all three directions are built**, each with its light and dark
  theme. First launch asks the language, then the colour direction (with a preview); both can be changed in
  settings. The Quran font is a reader setting; the author wants more fonts close to the printed mushaf to compare
  (round 2). The design tokens therefore keep all three directions (`docs/design/tokens.json`).
- **Round 2 (2026-11-17) — reviewed by the author** ("everything is good now"; default font chosen): `docs/design/prototypes/round-2.html` — the first
  launch on **one screen** (language, colour direction and light / dark, with a live example, as the author asked),
  the home screen, mushaf pages 1, 2, 5, 545, 546 exactly as printed with six Quran fonts, a two-page view, and the
  Sources screen (F17). Details: `docs/design/README.md`.
- **Round 3 (2026-11-17) — design 2, "early Islam" (صدر الإسلام), on the author's request.** Design 1 (rounds
  1–2) is kept; the author chooses one design for web, Android and iPhone. `docs/design/prototypes/round-3.html`:
  parchment and ink; the red vowel dots and the verse-end dots of the earliest Quran manuscripts; the palm trunks
  and mud brick of the Prophet's mosque (Sahih al-Bukhari 446); the rings of early coins; Noto Kufi Arabic for
  headings. Screens: first launch, home, mushaf page in the King Fahd page fonts, prayer times by location,
  Sources, "Why these colours?" (F19 draft), and the web reader with two pages. Details: `docs/design/README.md`.
- **Round 3, second pass (2026-11-17, the author's request): six colour directions for design 2** — Parchment,
  Madinah, Makkah, Al-Quds, Gardens, and Mountains (high contrast, ≥ 7 : 1), each in day and night; every text
  pair checked by `tools/design2_palettes.py` (≥ 4.5 : 1). New section icons, each from the first era. The reason
  for every colour, icon and the logo: `docs/design/design-2-meanings.md`. Values: `docs/design/tokens-design-2.json`.
- **Round 3, third pass (2026-11-18):** nine directions (+ Two seas 55:19–22, Lamps 41:12 / 25:61, Honey
  16:68–69); **only Mountains is the direction for colour blindness and weak sight** (author, 2026-11-18) — it is
  checked as seen with protanopia, deuteranopia and tritanopia (Machado et al. 2009; ≥ 8.4 : 1), and a "Colour
  vision" switch previews it; the other directions need 4.5 : 1 for normal vision; the surah details and the index
  (§8.1).
- **Night themes, reviewed (author, 2026-11-18):** the night theme of every direction except Mountains follows six
  rules, checked by `tools/design2_palettes.py` on every build: a deep tinted background, not black (L* 7 – 11);
  cards lighter step by step; the mushaf page a little lighter than the background; soft body text (11 – 16 : 1);
  calm accents (saturation ≤ 0.65); no bright block — the prayer card mid-dark (L* 20 – 42). Mountains stays as it
  is (black and white at full strength). The first-launch screen lists the planned languages by their own names.
- **Round 4 (2026-11-19) — design 3, "the first era" (عصر النبي ﷺ والصحابة والخلفاء الراشدين), on the author's
  request:** round 3 is kept as it is; `docs/design/prototypes/round-4.html` is a new design for the same screens.
  Twelve directions, each in day and night and each with its own landscape (home screen, web reader, first-launch
  cards): the first sheets (al-Bukhari 4986), Hira (al-Bukhari 3; 96:1–4), the Cave (9:40), Taybah (50:10), Uhud
  (al-Bukhari 4084), "look at the camels" (88:17–20), dawn (89:1, 81:18), the forenoon and the still night (93:1–2),
  rain (22:63), the two gardens (55:64, 55:68), light (24:35) and, last, Mountains (35:27) — **the only one for low
  vision and colour blindness**. The prayer times stand on the path of the sun; the logo is an arc of light over the
  horizon; headings in Amiri. Checked by `tools/build_round4.py` and `tools/design3_palettes.py` (the same checks as
  round 3). Reasons: `docs/design/design-3-meanings.md`; values: `docs/design/tokens-design-3.json`.
- Screens to design: language choice, colour-direction choice, sources (F17), home, Quran reader (+ ayah actions: play, tafsir, bookmark), player, reciter
  picker, tajweed lesson, radio list and player, prayer times (six backgrounds), adhan settings, Qibla, adhkar list and
  counter, hadith, book reader, settings, about.

## 14. Execution plan

The phases are below; **every task with its status is in §14.1**; what each task means, step by step, is in
[`docs/plan/execution-plan.md`](docs/plan/execution-plan.md).

Each feature is a vertical slice in this order: **verified data → backend API → web → Android → iPhone**, and a slice
is done only when: the data is in the register with its checksum / review; unit tests pass; both languages are
complete; the repository `AGENTS.md` and `README.md` are updated; the author has reviewed it.

| Phase | Content | Output |
| --- | --- | --- |
| **0. Foundations** | Answers to §18 · create the repositories · scaffold the four projects with CI · per-repository `AGENTS.md` / `README.md` · design tokens and key screens · data-source register · permission requests (§7.5) · choose the Quran text and font | Empty applications that build, a reviewed design, a signed-off source list |
| **1. Quran core** | F1 language · F2 reader with full tashkeel · F16 search · F3 recitation (surah, range, endless) · F11 resilient playback · F15 about | First usable release on web and Android |
| **2. Prayer** | F8 prayer times and backgrounds · F9 adhan · F10 Qibla | |
| **3. Radio** | F7 stations with health checks, on the same resilient player | |
| **4. Understanding** | F5 tafsir per ayah · F4 muallim mushaf | |
| **5. Tajweed** | F6 full curriculum with memory words and audio examples, after the reviewer's sign-off | |
| **6. Adhkar** | F12 with counters and reminders | |
| **7. Hadith** | F13 in the agreed scope with references | |
| **8. Books** | F14 reader | |
| **Release track** (parallel, starts in phase 1) | Hosting, domain, privacy policy, store accounts, Google Play closed test (takes at least 14 days), TestFlight, store listings | Public availability — §15 |

### 14.1 Task list and status (the only place where status is kept)

Status: ☐ not started · ◐ in progress · ✔ done (with the date) · ⏸ waiting (for the author, a permission or a
reviewer). Task ids: `P<phase>-<area><n>`, areas **D** data · **B** backend · **W** web · **A** Android · **I** iPhone ·
**Q** acceptance.

**Phase 0 — Foundations.** Suggested order: 01 → 02 → 03, 04 → 11 (in parallel) → 05, 06 → 07 → 08 → 12, 13 → 14 → 09
→ 10 → 15.

| Task | What | Status |
| --- | --- | --- |
| P0-01 | Documentation repository: this folder, `docs/`, the detailed plan, first session record, first commit | ✔ 2026-11-17 (local; GitHub in P0-03) |
| P0-02 | The author confirms R1 (create and push), R3 (application id) and R10 (commit e-mail) — §18.2 | ✔ 2026-11-17 |
| P0-03 | Create the five public GitHub repositories through the author's Chrome session; remotes; first push | ✔ 2026-11-17 — created, pushed over SSH, pages checked |
| P0-04 | Licences: MIT for code; the licence of these documents; the content notice | ✔ 2026-11-17 — MIT in the four application repositories; CC BY 4.0 for the documents and designs here (`LICENSE`); third-party content keeps its own licence (`README.md`) |
| P0-05 | Machine: install Android Studio; confirm Docker runs | ✔ 2026-11-17 — Android Studio, SDK and an emulator installed; Docker installed (start it before P0-07) |
| P0-06 | Re-verify every version on scaffold day and write it down | ☐ |
| P0-07 | Scaffold `tajweed-backend` with CI and `GET /v1/app-info` | ☐ |
| P0-08 | Scaffold `tajweed-frontend`: Angular 22, Material, Tailwind, wrappers, language choice, CI | ☐ |
| P0-09 | Scaffold `tajweed-android`: Kotlin, Compose, both languages, CI | ☐ (needs P0-05) |
| P0-10 | Scaffold `tajweed-ios`: generated project, SwiftUI, CI on a macOS runner | ☐ |
| P0-11 | Design: tokens, 2–3 colour directions, HTML prototypes, the author's approval, then Figma | ◐ round 1 (2026-11-17): three directions, all kept; round 2: first launch on one screen, mushaf pages as printed, six fonts, Sources — reviewed; round 3 (2026-11-17/18): design 2 "early Islam" with nine directions, colour-vision check, new icons, surah details and index; round 4 (2026-11-19): design 3 "the first era" with twelve directions, each with its landscape, in all 22 languages — ⏸ the author chooses design 1, 2 or 3; then the remaining screens and Figma |
| P0-12 | Data-source register; choose the Quran text and font; checksums | ◐ text, layout and default font chosen (Tanzil Uthmani; old Madinah 1405H layout from DigitalKhatt; King Fahd page fonts — author, 2026-11-17); quarter at 15:49 settled by the printed copy. Still to do: the register, the 9-ayah glyph table, justification, Makki / Madani compared with the printed index, the move to the backend repository |
| P0-13 | Permission letters, sent by the author, tracked | ☐ — includes a letter to the King Fahd Complex for its page fonts (author's decision 2026-11-17: use them and ask) |
| P0-14 | Content pipeline decisions D1, D2; API contract for phase 1 | ☐ |
| P0-15 | Phase 0 review with the author | ☐ |
| P0-16 | The reason for every colour, icon and the logo of design 2 (`docs/design/design-2-meanings.md`) and design 3 (`design-3-meanings.md`) — basis of F19 | ◐ 2026-11-17: written; 2026-11-19: design 3 written; ayahs copied and checked by script; ⏸ the author reads it; ☐ hadith gradings and tafsir quotes copied from their sources |

**Phase 1 — Quran core (F1, F2, F16, F3, F11, F15).**

| Tasks | What | Status |
| --- | --- | --- |
| P1-D1 … D5 | Quran text import and checks · surah / page / juz metadata · search text and surah-name spellings · reciters, sources and timings · About content | ☐ |
| P1-B1 … B7 | Migrations · `quran`, `reciter`, `appinfo` endpoints · public API hygiene · source health scheduler · tests | ☐ |
| P1-W1 … W8 | Home and language · reader · search · resilient audio engine · recitation modes · reciter picker · About / sources / privacy · tests | ☐ |
| P1-A1 … A6 | Bundled Quran database · reader · Media3 playback service · modes and picker · About · tests and device checklist | ☐ |
| P1-I1 … I6 | The same on iPhone, after Android is accepted | ☐ |
| P1-D6, P1-W9, P1-A7, P1-I7 | F19 "Why this design": content in both languages (§8.10), then the screen on each client | ☐ (after the design is chosen) |
| P1-Q1 | Eight acceptance checks, tried by hand and recorded | ☐ |

**Phases 2 – 8 and the release track.**

| Tasks | What | Status |
| --- | --- | --- |
| P2-D1 … D3, P2-B1, P2-W/A/I-1 … 4, P2-Q1 | Prayer times, adhan, Qibla; times compared with the official calendars. **`P2-D1` (the default method per country, each with a named source) may be done at any time — author, 2026-11-17** | ☐ (muezzin recordings ⏸ permissions) |
| P3-D1, P3-B1, P3-W/A/I-1, P3-Q1 | Radio stations with health checks on the resilient player | ☐ |
| P4-D1, P4-B1, P4-W/A/I-1, P4-D2, P4-W/A/I-2 | Tafsir per ayah; muallim recitation | ☐ (⏸ tafsir licences) |
| P5-D1 … D4, P5-B1, P5-W/A/I-1 | Tajweed curriculum | ☐ (explanations ⏸ reviewer or permitted source, §6.10) |
| P6-D1, P6-B1, P6-W/A/I-1 | Adhkar with counters | ☐ (⏸ right to use the book's text) |
| P7-D1, P7-D2, P7-B1, P7-W/A/I-1 | Hadith with references | ☐ (⏸ الدرر السنية permission for links / explanations) |
| P8-D1, P8-B1, P8-W/A/I-1 | Books reader | ☐ (⏸ edition rights) |
| RT-01 … RT-07 | Hosting, domain, deployment, privacy pages, Google Play, App Store, store listings | ☐ (author: accounts, costs, the Mac) |
| LANG-01 … LANG-04 | The 22 languages (§8.9): ✔ the list (2026-11-18); ✔ all in the first release (2026-11-19); draft interface texts written for the prototype · per language: interface strings translated by the agent and corrected from users' GitHub reports (no native readers — author, 2026-11-19), its font, its RTL / LTR check · the published translation of the meanings with written permission (QuranEnc, `P0-13`) · store listings in that language | ◐ (part of the first release; ⏸ native readers) |

## 15. Going public — hosting and stores

| Part | How | Cost (☐ confirm current prices) |
| --- | --- | --- |
| Domain | One domain: web application, `api.` for the backend, privacy policy page | about 10–15 USD / year |
| Web (Angular) | Static build on a free static host with HTTPS (Cloudflare Pages / GitHub Pages / Firebase Hosting) | free |
| Backend | Docker image on a small virtual server (or Oracle Cloud "Always Free"), PostgreSQL beside it, HTTPS by a reverse proxy (Caddy / Nginx), daily database backup, GitHub Actions for build and deploy | 0–6 USD / month |
| Audio | Streamed from the sources — no storage or traffic cost for us | free |
| Google Play | Developer account (one-time fee, identity verification). ⚠ A new **personal** account must run a closed test with **12 testers for 14 days** before publishing. Then: signed app bundle, data-safety form, content rating, privacy-policy link, declarations for exact alarms / playback service / location. | 25 USD once |
| Apple App Store | Apple Developer Program (yearly). ⚠ Needs a Mac with Xcode (or a cloud macOS build service) and an iPhone. TestFlight beta, App Review, privacy labels, background-audio declaration, proof of content rights if asked. | 99 USD / year |

A step-by-step guide for each row is written in `docs/deployment/` when its phase starts.

## 16. Risks and honest limitations

1. **Rights to recordings, tafsirs, translations and book editions** (§7.5) — the main non-technical risk.
2. **No qualified reviewer** (author, 2026-11-16) — rule §6.10 limits what can be published; tajweed explanations,
   and hadith explanations wait for a reviewer or a permitted authoritative source.
   (The former risk here — the PrimeNG licence — is gone: Angular Material was chosen, §4.2.)
3. **iPhone**: needs a Mac; full adhan only with the app open (§8.6).
4. **Scope**: fifteen features on three clients is a large product for one person — hence the phases; phase 1 alone is
   already a useful application.
5. **Incomplete recitations**: محمد رفعت and البهتيمي are left out until a complete mushaf is found (§7.3); ماهر المعيقلي
   muallim has 38 surahs only.
6. **Riwayah mismatch**: Sheikh Noreen recites الدوري عن أبي عمرو; shown with a clear label, without Hafs word highlighting,
   or postponed until a Duri text is added.
7. **Coloured words** (the name of Allah in red) were withdrawn by the author on 2026-11-17: no verified word list
   exists (§8.1).
8. **Radio streams change or disappear** — health checks and several sources per station reduce it; they cannot remove it.
9. **Review capacity**: correct religious content needs a qualified reviewer's time (§6.6).

## 17. Recommendations (not requested, proposed)

Listed for the author to accept or reject — none is built without approval.

- Sources and credits page, and a privacy policy page (both are required by licences and by the stores).
- "Report a mistake" on every content screen (supports the correct-data rule).
- Last read position and bookmarks, saved on the device (no account needed).
- Offline: download a recitation for listening without a network.
- Go to surah / juz / page; Hijri date on the prayer screen. (Quran search became feature F16.)
- Memorisation helpers: repeat an ayah or a range a number of times; sleep timer.
- Dark theme, adjustable Quran font size, accessibility labels.
- Later: home-screen prayer widget, Android Auto / CarPlay, tablets.
- A fifth repository for shared documents and design tokens (§3).
- An open-source licence for the code (content keeps its own licences) — §18 Q2.

## 18. Decisions and open points

### 18.1 The author's answers (2026-11-16) — numbers refer to the original questions in §18.3

| # | Topic | Decision / status |
| --- | --- | --- |
| Q1 | Name | ✔ **تجويد - القرآن الكريم وعلومه**, short «تجويد» / "Tajweed" (accepted 2026-11-17; ☐ English wording and store check, §2). |
| Q2 | GitHub | ✔ Public repositories; only the author writes. ✔ Account `Omar-Sherif-Sayed` (2026-11-17). ☐ Creation, push and code licence — R1. |
| Q3 | Fifth repository `tajweed-docs` | ✔ Yes (2026-11-17): the workspace folder itself (§3). Local commit done; GitHub in P0-03. |
| Q4 | Commits and notes | ✔ The agent commits as Omar Sherif (§1). ☐ Push — R1. ✔ Session records in `docs/sessions/`; raw transcripts stay private in `ai-agent-workspace\Tajweed\` (§3). |
| Q5 | UI library | ✔ Angular 22 + Angular Material 22 + Tailwind CSS (§4.2). |
| Q6 | Mobile | ✔ Two native repositories; no Mac / iPhone, a friend's Mac for testing (§4.3, §11–12). |
| Q7 | Database, package, domain | ✔ PostgreSQL. ☐ Base package / application id and domain — R3. |
| Q8 | Figma | ✔ Account exists (Chrome session). HTML prototypes first, Figma after approval (§13). |
| Q9 | Red colouring | ✔ **Withdrawn** (author, 2026-11-17: "if there is no good example, don't do it") → a standard one-colour mushaf with full tashkeel, and Quran search (F16, §8.1). |
| Q10 | Reciters | ✔ "الحذيفي" = علي الحذيفي. ✔ محمد رفعت and البهتيمي left out until a complete mushaf is found (searched again, §7.3). ☐ Sheikh Noreen — R5. |
| Q11 | Hadith and books | ✔ Hadith: الأربعون النووية, then صحيح البخاري and صحيح مسلم. Books: الأم، صحيح البخاري، صحيح مسلم; more recommended later. ☐ The tafsir list is fixed when the licences are checked (§7.2). |
| Q12 | Reviewer | ✔ None for now → rule §6.10; the application is for أهل السنة والجماعة. |
| Q13 | Adhan limits and muezzin recordings | ☐ R6. |
| Q14 | Order of work | ☐ R7. |
| Q15 | Recommendations in §17 | ☐ R8. |

### 18.2 Remaining points (the agent's default is applied unless the author says otherwise)

The author read these on 2026-11-16 and did not object in his next message; the defaults are in effect. **R1 still needs an
explicit yes** (it is public); R3 (permanent) and R10 (public) need the author's confirmation. R2 and R4 are settled.
**Update 2026-11-17: the author answered R1 (yes), R3 (confirmed) and R10 (his personal address) — see the rows.**

| # | Point | Default |
| --- | --- | --- |
| R1 | May the agent create the five public repositories under `Omar-Sherif-Sayed` through the author's Chrome session and push? Code licence? | ✔ **Yes** (author, 2026-11-17: "Create and push: Okay"). The five repositories are created; pushing is allowed for this product from now on. Licence: MIT for the code; content keeps its own licences. |
| R2 | A fifth public repository `tajweed-docs`. | ✔ Settled 2026-11-17 — the workspace folder itself (§3). |
| R3 | Base Java package and the Android / iPhone application id. ⚠ **It can never be changed after the first store release.** | **`io.github.omarsherifsayed.tajweed`** — one identical value for the Java base package, the Android application id and the iPhone bundle id. It is the GitHub user name `Omar-Sherif-Sayed` in lower case **with the hyphens removed**: a Java / Android name cannot contain `-`, and an Apple bundle id cannot contain `_` (✔ Apple: only letters, digits, `-` and `.`, checked 2026-11-17), so plain letters are the only form valid everywhere. ✔ **Confirmed by the author, 2026-11-17 — final.** |
| R4 | Red colouring. | ✔ Closed 2026-11-17 — no coloured words (§8.1). |
| R5 | Sheikh Noreen (riwayah الدوري عن أبي عمرو). | Listening only, labelled with his riwayah, without showing or highlighting the Hafs text (§6.7). |
| R6 | Adhan: accept the iPhone and web limits (§8.6)? Sources for the six muezzins' recordings? | Limits accepted; a muezzin is added only when a clean recording with a known origin and permission is found. |
| R7 | Order: backend + web + Android first, iPhone after each feature is stable on Android? | Yes (§11–12). |
| R8 | Recommendations in §17. | All accepted except the "later" items. |
| R9 | A qualified reviewer before phases 5–7 (tajweed, adhkar, hadith) are published. | Those phases are built, but published only inside the limits of §6.10. |
| R10 | Which e-mail do the commits carry? The author asked for his personal address; his GitHub account hides his address ("Keep my email addresses private" is on), and a pushed commit would show it to everyone, for ever. | ✔ **Decided by the author, 2026-11-17: his personal address** — the one his GitHub account is registered with — in every commit of this product. (The agent had recommended the account's "noreply" address; the author chose otherwise, knowing the address is public in the history.) |

### 18.3 Original questions (2026-11-16, kept for reference)

| # | Question |
| --- | --- |
| Q1 | The application's name (Arabic and English) — "Tajweed" is only the folder name. |
| Q2 | GitHub: account or organisation name, repository names (§3), public or private, and the code licence. The GitHub CLI is not installed: install it and sign in (`gh auth login`), or create the repositories through Chrome? |
| Q3 | A fifth repository `tajweed-docs` for this file and shared documents? |
| Q4 | Does the agent commit and push, or only the author? Where do the session notes go? |
| Q5 | PrimeNG: option A, B or C (§4.2)? |
| Q6 | Mobile: Kotlin Multiplatform in one repository, or two native repositories (§4.3)? Is a Mac and an iPhone available? |
| Q7 | Database PostgreSQL? Base Java package (e.g. from a domain you own)? Is there a domain name? |
| Q8 | Figma: is there an account (which plan)? Agree to HTML prototypes first, Figma after approval (§13)? |
| Q9 | Red colouring: which printed mushaf is the model (publisher / photo)? Start with «الله» only (level 1) and add level 2 after a scholar's review? |
| Q10 | Reciters (§7.3): accept incomplete mushafs for محمد رفعت / البهتيمي? How to treat Sheikh Noreen (Duri)? Is "الحذيفي" Sheikh علي الحذيفي? Any muallim mushaf wanted beyond الحصري، المنشاوي، أيمن سويد? |
| Q11 | Hadith scope for the first release (§8.8)? Which tafsirs (§7.2)? Which books first? |
| Q12 | Is there a qualified reviewer for tajweed, hadith and adhkar content (§6.6)? |
| Q13 | Adhan: accept the iPhone and web limits (§8.6)? Any known source for the six muezzins' recordings? |
| Q14 | Order of work: the phases in §14 as written, or another priority? Web + Android first, iPhone after? |
| Q15 | Which recommendations in §17 are accepted? |

## 19. Change log

| Date | Change |
| --- | --- |
| 2026-11-16 | First version: scope, rules, structure, verified versions and sources, execution plan, open questions. The author's code conventions adopted. |
| 2026-11-16 | The author's answers recorded (§18.1): name تجويد / Tajweed; public repositories; the agent commits as the author; Angular Material + Tailwind instead of PrimeNG (§4.2); two native mobile repositories and the plan for iPhone without a Mac (§4.3, §11–12); PostgreSQL; model mushaf for the red colouring (§8.1); محمد رفعت and البهتيمي left out after a second search (§7.3); no reviewer → rule §6.10; Sunni sources only; HTML prototypes before Figma. Remaining points: §18.2. |
| 2026-11-17 | Name accepted: «تجويد - القرآن الكريم وعلومه» (§2). The workspace folder became the documentation repository `tajweed-docs` (§3) with `README.md`, `docs/README.md`, `docs/plan/execution-plan.md` and the first session record. Added §0 "Start here" (handoff for any agent or model), the contents table and §14.1 (every task with its status). Machine checked: Docker installed, Android Studio not. First commit as the author; nothing pushed. |
| 2026-11-17 | Second update of the day (author's message): the coloured name of Allah is withdrawn — a standard one-colour mushaf with full tashkeel (§8.1, R4 closed); new feature F16 Quran search (word with or without tashkeel, surah name, ayah number) with a separate search text; the name is written with a plain hyphen and the workspace folder is named `Tajweed - The Noble Quran and Its Sciences` (§3); references to the author's other projects removed; the application id formula explained (R3) — the GitHub user name is still needed; Android Studio Rabbit 2 Patch 1 confirmed as the current version. |
| 2026-11-17 | Third update of the day: the author renamed the workspace folder; GitHub account read from his Chrome session — `Omar-Sherif-Sayed` (§0, §3); application id proposed as `io.github.omarsherifsayed.tajweed`, valid on Java, Android and iPhone (R3 — corrects the earlier "hyphen becomes underscore" note, which Apple does not accept); new point R10, the e-mail carried by the commits; §3 now lists what each repository holds; a conversation copy of the session added to `docs/sessions/`. |
| 2026-11-17 | Fourth update of the day: the author said yes to creating and pushing (R1), confirmed the application id (R3) and chose his personal address for the commits (R10). The five public repositories were created on GitHub; the four application folders got their first commit (`README.md`, `AGENTS.md`, MIT `LICENSE`, `.gitignore`). **The push did not happen:** the machine's certificate store blocks the HTTPS sign-in (§0, §1); SSH is reachable and is the way forward once the author agrees to an SSH key. |
| 2026-11-17 | Fifth update of the day: the author agreed to an SSH key and confirmed it on GitHub himself; **all five repositories were pushed** and checked on GitHub (§0); Android Studio and the SDK are installed (P0-05 done). Phase 0 tasks 01, 02, 03 and 05 are done. |
| 2026-11-17 | Sixth update of the day: design round 1 (`docs/design/`, §13) — three colour directions on four screens, draft tokens; the Tanzil Uthmani text downloaded with the author's permission for the reader mock-up (SHA-256 recorded, file kept untouched); documents and designs of this repository licensed CC BY 4.0 (P0-04 done). |
| 2026-11-17 | Seventh update of the day (author's feedback on design round 1): all three colour directions are built, chosen at first launch after the language, each with light and dark (F18, §13); more languages later — German, Italian, Japanese, Chinese (§8.9); the reader reproduces the printed Madinah mushaf page by page and line by line (F2, §8.1 — research: the author's page 545 matches the old Madinah 1405H layout; DigitalKhatt data and fonts are the open candidates); a Sources section listing every source (F17); more Quran fonts to compare. |
| 2026-11-17 | Eighth update of the day: design round 2 built and checked (`docs/design/`): first-launch screen with language, colour direction and light / dark on one page; mushaf pages exactly as printed; six Quran fonts; Sources screen. The old-Madinah layout (DigitalKhatt) verified against Tanzil — 0 word differences in 6,236 ayahs, 0 page-start differences in 604 pages; page 5 confirmed by the author on his printed copy. King Fahd page fonts used by the author's decision; KFGQPC Hafs 0.09 rejected (missing mark). Open: the quarter sign at 15:49 / 15:50, 9 ayahs in the King Fahd glyph list (§8.1). |
| 2026-11-17 | Ninth update of the day (author's review of round 2): default Quran font = the King Fahd page fonts (Madinah mushaf 1405H); his printed copy (دار طيبة, Cairo) photographed — pages 1, 2, 263, 264 match the layout, and the ۞ stands before 15:49, so the quarter question is closed; prayer times follow the user's location and country on web and phones (§8.5); design round 3 — a second design, "early Islam", to compare with design 1 (§13). |
| 2026-11-17 | Tenth update of the day (author's message): design 2 gets six colour directions — Parchment, Madinah, Makkah, Al-Quds, Gardens, Mountains (high contrast) — and new section icons; every colour, icon and the logo is explained in `docs/design/design-2-meanings.md` (ayahs copied and checked by script); new feature F19, the in-app section "Why this design" (§8.10); `P2-D1` recorded as "do not forget" (§0, §8.5). |
| 2026-11-18 | Eleventh update (author's message): design 2 gets three more directions — Two seas, Lamps, Honey (nine in all); every direction is checked for colour-blind readers by simulation, and Mountains is the direction for low vision and colour blindness; 30:22 placed beside the language choice after reading its tafsirs (§8.10); each surah shows Makki / Madani, its ayahs and its order, and the mushaf has an index (F2, §8.1). |
| 2026-11-18 | Twelfth update (author's message): **only Mountains** is the direction for colour blindness, weak colour vision and weak sight — renamed «الجبال — لضعف البصر وعمى الألوان»; the colour-blind check applies to it alone; the other directions and their night themes are not built for it (§8.10, §13). |
| 2026-11-18 | Thirteenth update (author's message): more languages planned — Russian, Spanish, German, Italian, French, Urdu, Hindi, Korean, Indonesian (with Japanese and Chinese), and nine recommended (Turkish, Bengali, Persian, Malay, Swahili, Hausa, Portuguese, Pashto, Uzbek), each with its script, font and published translation (§8.9, tasks `LANG-*`); the night themes of the eight directions other than Mountains reviewed against six rules (§13). |
| 2026-11-18 | Fourteenth update (author's message): all nine recommended languages accepted — 22 languages in all (Urdu for «الباكستانية», Hindi once); the first screen gets a searchable language list with the device's language first (F1, §2, §8.9). |
| 2026-11-19 | Fifteenth update (author's message): **all 22 languages are available from the first release** (§1, §2, F1, §8.9); round 3 works in all of them with draft interface texts (checked by the build) and a font, direction and number format per script; round 4 requested — a new design from the time of the Prophet ﷺ, the Companions and the Rightly Guided Caliphs, with many directions from the Quran (§0). |
| 2026-11-19 | Sixteenth update (author's message): **round 4 — design 3, "the first era"** — twelve directions from the places and moments of the time of the Prophet ﷺ, the Companions and the Rightly Guided Caliphs and from words of the Quran, each in day and night with its own landscape; only the last, Mountains, for low vision and colour blindness; the prayer times on the path of the sun; reasons in `docs/design/design-3-meanings.md` (§13, §8.10). Rounds 3 and 4 fixed in the 21 languages other than Arabic. Next: the author chooses design 1, 2 or 3 (§0). |
| 2026-11-19 | Seventeenth update (author's message): **no native readers** — the agent translates the interface, users report mistakes on GitHub and the author brings them (§1, §8.9, `LANG-02`); the round-4 texts translated into the 20 languages; **no cross shape anywhere** (a plus sign or a four-armed star — a symbol of Christianity): the star of the Light direction and four icons changed in all designs (§8.10); Mountains keeps its night theme (confirmed). |
