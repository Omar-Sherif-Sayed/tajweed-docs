# Documents — index

Everything here belongs to the whole product. Documents about one codebase live in that repository's own `docs/`.
Rule: no loose files — every document is in `docs/<kind>/` and listed here.

| Folder | What it holds | State |
| --- | --- | --- |
| [`plan/`](plan/) | [`execution-plan.md`](plan/execution-plan.md) — every task of every phase in detail. Task status is in the parent [`AGENTS.md`](../AGENTS.md) §14.1. | written 2026-11-17 |
| [`sessions/`](sessions/) | One record per working session: the author's messages, what was done, decisions, sources. | [2026-11-16 planning](sessions/2026-11-16-planning.md) |
| `data-sources/` | The register of every content source: owner, URL, licence, checksum, verification date. | task P0-12 |
| `permissions/` | Permission letters (Arabic / English), the answers, and the status table. | task P0-13 |
| `design/` | `tokens.json`, HTML prototypes (`prototypes/`), screenshots, the link to the Figma file. | task P0-11 |
| `deployment/` | Step-by-step guides: hosting, domain, Google Play, App Store. | release track |
| `quality/` | Checklists used across the applications (acceptance runs, iPhone test sessions on the Mac). | from phase 1 |

## Session records — how to write one

File name `YYYY-MM-DD-<topic>.md`. Content: date, who, result, the author's messages quoted exactly, what was done,
decisions, findings, sources, real command output for anything claimed as "passing". No raw transcript, no e-mail
address, no secret, no text copied from another project.
