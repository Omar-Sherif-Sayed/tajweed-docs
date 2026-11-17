# تجويد - القرآن الكريم وعلومه · Tajweed - The Noble Quran and Its Sciences

**Tajweed** is a free Islamic application for the Quran, its recitation and its sciences — on the web, Android and
iPhone, in Arabic and English. No advertisements, no registration, no login, no tracking.

> **State (2026-11-17): planning.** There is no application yet. This repository holds the plan.

Author: **Omar Sherif — عمر شريف** · <https://www.linkedin.com/in/omarsherif21/>

## What this repository is

The documentation repository of the product (`tajweed-docs`): the plan, the rules, the register of content sources,
the permission letters, the designs and the session records. It holds no application code.

| Repository | Content |
| --- | --- |
| `tajweed-docs` (this one) | Plan, rules, sources, designs, records |
| `tajweed-backend` | Spring Boot REST API (Java, Gradle, PostgreSQL) |
| `tajweed-frontend` | Web application (Angular, Angular Material, Tailwind CSS) |
| `tajweed-android` | Android application (Kotlin, Jetpack Compose) |
| `tajweed-ios` | iPhone application (Swift, SwiftUI) |

All five repositories are at <https://github.com/Omar-Sherif-Sayed>. The four application repositories hold no code
yet.

## Where to read

| File | For |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | The whole product in one file: scope, rules, decisions, structure, sources, the task list with its status. **Start at §0.** |
| [`docs/plan/execution-plan.md`](docs/plan/execution-plan.md) | Every task in detail |
| [`docs/README.md`](docs/README.md) | Index of all documents |
| [`docs/sessions/`](docs/sessions/) | What happened in each working session |

## Planned features

Quran reader with full tashkeel, and search by word, surah name or ayah number · recitation by a chosen reciter (a surah, an ayah range, or without end)
· teaching (muallim) recitation · tafsir of an ayah · the rules of tajweed with the scholars' memory words · Quran
radio stations · prayer times, adhan and Qibla · adhkar with counters · hadith with references · religious books.

## Correct data

The Quran text is imported byte for byte from a verified source and checked by checksum; nothing religious is
written, changed or translated by the developers or by an AI model; every item shows its source. The rules are in
`AGENTS.md` §6.

## Working folder layout

The application repositories are cloned **inside** this folder; this repository ignores them (`.gitignore`):

```
Tajweed - The Noble Quran and Its Sciences/     this repository (tajweed-docs)
  AGENTS.md  README.md  docs/
  tajweed-backend/       its own repository
  tajweed-frontend/      its own repository
  tajweed-android/       its own repository
  tajweed-ios/           its own repository
```

## Licence

The content the application will show (Quran text, audio, tafsir, hadith, books) belongs to its sources and keeps
their licences. The licence of the documents in this repository is not chosen yet (task P0-04).
