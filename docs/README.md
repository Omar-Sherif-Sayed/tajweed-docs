# Documents — index

Everything here belongs to the whole product. Documents about one codebase live in that repository's own `docs/`.
Rule: no loose files — every document is in `docs/<kind>/` and listed here.

| Folder | What it holds | State |
| --- | --- | --- |
| [`plan/`](plan/) | [`execution-plan.md`](plan/execution-plan.md) — every task of every phase in detail. Task status is in the parent [`AGENTS.md`](../AGENTS.md) §14.1. [`backend-plan.md`](plan/backend-plan.md) — the detailed plan of the backend scaffold (2026-11-21). | written 2026-11-17 |
| [`sessions/`](sessions/) | The session memory: one record per working session (the author's messages, what was done, decisions, sources) and a conversation copy beside it. | [2026-11-16 planning — record](sessions/2026-11-16-planning.md) · [conversation copy](sessions/2026-11-16-planning-conversation.md) · [2026-11-20 design 3 and sources — record](sessions/2026-11-20-design-3-and-sources.md) |
| `data-sources/` | The register of every content source: owner, URL, licence, checksum, verification date. | task P0-12 |
| [`permissions/`](permissions/README.md) | How every pending source is cleared (read the licence / ask in writing / check the content), the status table, and later the letters and answers. | task P0-13 — started 2026-11-20 |
| [`design/`](design/) | [`README.md`](design/README.md), `tokens.json`, HTML prototypes (`prototypes/`), later screenshots and the link to the Figma file. | three designs — [design 1](design/prototypes/round-1.html), [design 2](design/prototypes/round-2.html), [design 3](design/prototypes/round-3.html); elements in [`design/elements/`](design/elements/); waiting for the author's choice |
| [`memory/`](memory/) | A copy of the agent's memory (the author's rule, 2026-11-20): refreshed by `sync_memory.py` and committed with every commit; private facts removed. | [README](memory/README.md) |
| `deployment/` | Step-by-step guides: hosting, domain, Google Play, App Store. | release track |
| `quality/` | Checklists used across the applications (acceptance runs, iPhone test sessions on the Mac). | from phase 1 |

## Session records — how to write one

File name `YYYY-MM-DD-<topic>.md`. Content: date, who, result, the author's messages quoted exactly, what was done,
decisions, findings, sources, real command output for anything claimed as "passing". No raw transcript, no e-mail
address, no secret, no text copied from another project.

## Conversation copies — how they are made

File name `YYYY-MM-DD-<topic>-conversation.md`, beside the record. A script reads the session log and keeps only
what the author typed and what the agent answered in text; tool calls, tool output, file contents and system
messages are left out, and e-mail addresses and the names of other projects are replaced. The script and the raw log
are in the author's private notes folder (`ai-agent-workspace\Tajweed\`, see the parent `AGENTS.md` §3) — the raw log
is never committed. A copy is made at the end of a session; the answer being written at that moment is added by the
next run. **A conversation copy is history: the current decisions are always in the parent `AGENTS.md`.**
