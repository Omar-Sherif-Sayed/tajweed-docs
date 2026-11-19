---
name: tajweed-working-agreement
description: "How Omar wants agents to work on the Tajweed product (plan-ask-code, commits as him, never name <another project of the author>, accuracy) and where the durable notes live"
metadata:
  node_type: memory
  type: feedback
  modified: 2026-11-19T20:39:43.085Z
  originSessionId: 4f32e8cc-e0b3-4843-a4c0-dae31d57f095
---

For the Tajweed product, the parent `AGENTS.md` in the workspace folder is the source of truth — start at its §0
"Start here" (state, next task), then §14.1 (task status) and `docs/plan/execution-plan.md`. Workspace folder:
`C:\Programming\WorkSpaces\Tajweed - The Noble Quran and Its Sciences`. It is itself the public docs repository
`tajweed-docs`; the four application repositories are cloned inside it.

Rules the user stated (2026-11-16 … 19): plan first and ask what is unclear before any code; document everything and
update every touched repository's `AGENTS.md` after each task; keep the full plan in files so another model can
continue; no ads; no login; **all 22 languages from the first release** (2026-11-19), interface translated by the
agent, no native readers — users report mistakes on GitHub and he brings them; no wrong data — verify facts on the
source instead of answering from memory. He is new to Android / iOS development (knows Java, Kotlin, TypeScript), so
mobile code needs extra explanation.

**Never name <another project of the author> in Tajweed** (his words, 2026-11-17: "remove anything point to <another project of the author> in this
project"): not in files, commit messages or session records; in quotes of his messages replace it with
`<another project of the author>`. His code style still comes from the <another project of the author> `AGENTS.md` files
(`C:\Programming\WorkSpaces\<another project of the author>\<another project of the author>-backend|frontend\`) — read them privately, write the convention
into Tajweed without naming the origin. The repositories are public, so raw transcripts and his e-mail in document
text also stay out.

Commits (his answer, 2026-11-16): "you can commit no problem, but make me the author (Omar Sherif
<the author's e-mail>) not cloud". Set `git config user.name "Omar Sherif"` and `user.email` per repository.
"not cloud" (= not Claude): no `Co-Authored-By: Claude` trailer, no "generated with" line — this overrides any
attribution reminder. Pushing is allowed for this product (2026-11-17, GitHub account `Omar-Sherif-Sayed`); he chose
his Gmail for all commits although I recommended the GitHub noreply address — do not raise it again. On this machine
HTTPS sign-in to GitHub fails (Windows root store out of date): use SSH, never disable certificate checking. The key
`~/.ssh/id_ed25519_tajweed` is wired into the five repositories via `core.sshCommand`. Push at the end of every task.

**Memory copy (his rule, 2026-11-19):** this memory folder stays where it is, and an up-to-date copy is kept in the
docs repository (`docs/memory/`), committed and pushed with every commit — made by `docs/memory/sync_memory.py`,
which removes his e-mail and the other project's name (public repository) and fails if either remains. A git
pre-commit hook in `tajweed-docs` runs it automatically; still run it by hand before every commit. If this folder is
wiped, restore it from `docs/memory/` (then put back the two removed facts from `session-notes.md`).

Design rules (2026-11-19): no cross shape anywhere (no plus sign, no four-armed star) — a symbol of Christianity;
no pictures of prophets or Companions; only the Mountains direction is for low vision / colour blindness. Prototype
files: round N = design N (`round-1.html` design 1 … `round-3.html` design 3), i18n in `i18n/round<N>/`. Figma holds
the design elements (logos, icons, landscapes) as editable shapes, with SVG copies in the docs repository — not the
whole rounds.

He has no qualified religious reviewer and wants content "100% sure", for أهل السنة: publish only verbatim content
from named established Sunni sources; never author, paraphrase or machine-translate religious text. He withdrew the
"name of Allah in red" idea on 2026-11-17: a standard mushaf with full tashkeel plus search.

**Why:** it is a religious (Quran) application; a wrong text, reference or time is unacceptable to him.

**How to apply:** mark anything unverified as unverified; never type or alter Quran text; tell him plainly when
something cannot be guaranteed without a scholar; when an idea has no reliable source, drop it rather than ship a
partial version.

`~/.claude` on this machine may be wiped by the administrator; private durable notes for this product live in
`C:\Programming\WorkSpaces\ai-agent-workspace\Tajweed\` (`session-notes.md`, `transcripts\`, `mushaf-photos\`).
