"""Check and load the interface texts of the 20 languages after Arabic and English (AGENTS.md §8.9).

One folder per round: i18n/round<N>/keys.json (id, English, Arabic) and i18n/round<N>/<code>.json; the Lives screens,
shared by the three designs, use i18n/lives/. Every file is checked: every key present, no unknown key, and every
{slot} the English and Arabic texts share is kept. Used by build_round1.py, build_round2.py, build_round3.py and
build_lives.py.
"""
import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))


def fail(msg):
    raise SystemExit("FAILED: " + msg)


I18N = os.path.join(HERE, "..", "i18n")
LANG_CODES = ["ru", "es", "de", "it", "fr", "ur", "hi", "ko", "id", "ja", "zh", "tr", "bn", "fa", "ms", "sw", "ha",
              "pt", "ps", "uz"]
SLOT = re.compile(r"\{(\w+)\}")


def build_i18n(folder="round2"):
    """The interface texts of the 20 languages after Arabic and English (by the agent, AGENTS.md §8.9), each file
    checked: every key present, no unknown key, and every {slot} the English and Arabic texts share is kept.
    One folder per round: i18n/<round>/keys.json (id, English, Arabic) and i18n/<round>/<code>.json."""
    keys = json.load(io.open(os.path.join(I18N, folder, "keys.json"), encoding="utf-8"))
    ids = [k["id"] for k in keys]
    out = {"en2id": {k["en"]: k["id"] for k in keys}, "tr": {}}
    for code in LANG_CODES:
        tr = json.load(io.open(os.path.join(I18N, folder, code + ".json"), encoding="utf-8"))
        tr.pop("_status", None)
        missing, extra = [i for i in ids if i not in tr], [i for i in tr if i not in ids]
        if missing or extra:
            fail("i18n/%s/%s.json: missing %s, unknown %s" % (folder, code, missing, extra))
        for k in keys:
            allowed = set(SLOT.findall(k["en"])) | set(SLOT.findall(k["ar"]))
            needed = set(SLOT.findall(k["en"])) & set(SLOT.findall(k["ar"])) if k["ar"] else set(SLOT.findall(k["en"]))
            got = set(SLOT.findall(tr[k["id"]]))
            if not got <= allowed or not needed <= got:
                fail("i18n/%s/%s.json %s: slots %s (allowed %s, needed %s)" % (folder, code, k["id"], got, allowed, needed))
        out["tr"][code] = tr
    print("i18n/%s: %d keys x %d languages checked" % (folder, len(ids), len(LANG_CODES)))
    return out


