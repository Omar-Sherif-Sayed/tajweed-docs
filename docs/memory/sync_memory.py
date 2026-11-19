"""Copy the agent's memory folder into this repository (the author's rule, 2026-11-19).

The memory stays where it is (the agent's own folder for this workspace, under ~/.claude/projects/); this script keeps
an up-to-date copy in docs/memory/, so that it is committed and pushed with every commit and can be restored if that
folder is wiped. This repository is public, so two private facts are removed on the way: the author's e-mail address
and the name of his other project. The script stops if either would still be written.

Usage (from anywhere):  python -I docs/memory/sync_memory.py
Run automatically by the pre-commit hook of this repository (see docs/memory/README.md); without the memory folder
it prints a note and leaves the copy as it is.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(os.path.expanduser("~"), ".claude", "projects",
                      "C--Programming-WorkSpaces-Tajweed---The-Noble-Quran-and-Its-Sciences", "memory")
OUT = os.path.join(HERE, "copy")

# private fact -> what the public copy says instead
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@(?!anthropic\.com)[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
OTHER = re.compile(r"public[\s_-]*marts?", re.I)


def clean(text):
    text = EMAIL.sub("<the author's e-mail>", text)
    text = OTHER.sub("<another project of the author>", text)
    return text


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if not os.path.isdir(SOURCE):
        print("memory folder not found (%s): copy left as it is" % SOURCE)
        return
    os.makedirs(OUT, exist_ok=True)
    names = sorted(n for n in os.listdir(SOURCE) if n.endswith(".md"))
    for old in os.listdir(OUT):
        if old.endswith(".md") and old not in names:
            os.remove(os.path.join(OUT, old))
    for n in names:
        text = clean(io.open(os.path.join(SOURCE, n), encoding="utf-8").read())
        if EMAIL.search(text) or OTHER.search(text):
            raise SystemExit("private text left in " + n)
        with io.open(os.path.join(OUT, n), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    print("memory: %d file(s) copied to docs/memory/copy/ (e-mail and the other project's name removed)" % len(names))


if __name__ == "__main__":
    main()
