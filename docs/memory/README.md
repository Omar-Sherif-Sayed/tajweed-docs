# The agent's memory — a copy

The author's rule (2026-11-19): the agent's memory files stay in their own place, and an up-to-date copy lives here,
committed and pushed **with every commit**.

| | |
| --- | --- |
| The memory itself | the agent's folder for this workspace: `~/.claude/projects/C--Programming-WorkSpaces-Tajweed---The-Noble-Quran-and-Its-Sciences/memory/` |
| The copy | [`copy/`](copy/) — `MEMORY.md` (the index) and one file per memory |
| Made by | [`sync_memory.py`](sync_memory.py) — `python -I docs/memory/sync_memory.py` |
| When | before every commit of this repository: the pre-commit hook runs it and adds the copy to the commit; the agent also runs it by hand |

This repository is public, so the script removes two private facts on the way — the author's e-mail address and the
name of his other project — and stops if either would still be written. Everything else is copied as it is.

**If the memory folder is wiped** (it can be, on this machine): copy `copy/*.md` back into the memory folder, then put
back the two removed facts from the private notes in `C:\Programming\WorkSpaces\ai-agent-workspace\Tajweed\`.

**The pre-commit hook** lives in `.git/hooks/pre-commit` (git does not version hooks). On a new clone, create it with:

```sh
#!/bin/sh
python -I docs/memory/sync_memory.py && git add docs/memory/copy
```

The parent `AGENTS.md` §0 and §1 hold the same rule.
