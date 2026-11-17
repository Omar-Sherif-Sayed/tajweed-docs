"""Build `round-3.html` (design 2, "early Islam") and its generated companions from the verified source files.

Same checks as round 2 (`build_round2.py`): checksums, the layout read as plain text, every word and every King Fahd
glyph cross-checked against the Tanzil text. Round 3 uses only the default Quran font chosen by the author on
2026-11-17 — the King Fahd Complex page fonts (Madinah mushaf, 1405H). The basmala line is drawn, as in round 2, with
the KFGQPC Hafs font (it has no U+06DF, which the basmala does not use).

It also writes:
  - the colour directions of design 2 (design2_palettes.py) as CSS into round-3.html, after the contrast check, and
    as docs/design/tokens-design-2.json;
  - the ayahs cited in docs/design/design-2-meanings.md, copied whole from the Tanzil file (never typed), into
    round-3.html and into that document; each one is checked to contain the word it is cited for.

Usage: python -I build_round3.py
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_round2 as R2  # noqa: E402  (our own scripts beside this one)
import design2_palettes as P  # noqa: E402
import verify_mushaf_layout as V  # noqa: E402

PAGE = os.path.join(HERE, "..", "round-3.html")
DESIGN = os.path.join(HERE, "..", "..")
PAGES = [1, 2, 5, 545, 546]
SOURCES = ["tanzil/quran-uthmani.txt", "tanzil/quran-data.xml", "digitalkhatt/quran_text_old_madinah.ts",
           "kfgqpc/UthmanicHafs1 Ver09.otf", "kfgqpc/mushaf.txt"] + ["kfgqpc/QCF_P%03d.TTF" % p for p in PAGES]
FONTS = {"KFGQPC Hafs": ("kfgqpc/UthmanicHafs1 Ver09.otf", "opentype")}
for _p in PAGES:
    FONTS["QCF P%03d" % _p] = ("kfgqpc/QCF_P%03d.TTF" % _p, "truetype")

# Ayahs cited in the meanings document: reference -> the word (letters only, as compared by V.skeleton) that the
# citation is about. The build stops if the ayah does not contain it.
VERSES = {
    "35:27": "الونها", "35:28": "الونه",         # the variety of colours (the small alef is a mark, so not compared)
    "52:2": "مسطور", "52:3": "رق",               # parchment
    "50:10": "النخل",                            # Madinah: the palm trees
    "3:96": "ببكة",                              # Makkah
    "17:1": "الاقصا", "95:1": "الزيتون", "24:35": "زيتونة",   # Al-Quds: al-Aqsa, the olive
    "55:64": "مدهامتان", "55:76": "خضر", "18:31": "خضرا", "76:21": "خضر", "35:33": "لولوا",  # gardens
    "2:144": "قبلة", "7:204": "فاستمعوا", "73:4": "ترتيلا", "96:4": "بالقلم",  # icons
    "30:22": "السنتكم",                          # an idea considered and not used
}
TASHKEEL = re.compile("[ً-ْٰ]")


def check_doc_excerpts(verses):
    """Every vowelled «excerpt» in the meanings document must be an exact part of one of the cited ayahs."""
    text = io.open(os.path.join(DESIGN, "design-2-meanings.md"), encoding="utf-8").read()
    text = text.split("<!--AYAHS-BEGIN-->")[0] + text.split("<!--AYAHS-END-->")[1]
    excerpts = [e for e in re.findall("«([^»]+)»", text) if TASHKEEL.search(e)]
    for e in excerpts:
        if not any(e in v for v in verses.values()):
            R2.fail("excerpt in design-2-meanings.md is not part of a cited ayah: %s" % e)
    print("excerpts: %d in design-2-meanings.md, each found word for word in a cited ayah" % len(excerpts))


def ayah_text(tanzil, key):
    """The ayah exactly as in the Tanzil file, without the basmala Tanzil writes before ayah 1."""
    text = tanzil[key]
    if key[1] == 1 and key[0] not in (1, 9):
        text = " ".join(text.split(" ")[4:])
    return text


def build_verses():
    tanzil = V.parse_tanzil(os.path.join(R2.ASSETS, "tanzil/quran-uthmani.txt"))
    out = {}
    for ref, word in VERSES.items():
        key = tuple(int(x) for x in ref.split(":"))
        text = ayah_text(tanzil, key)
        if not any(word == V.skeleton(t) or (len(word) > 2 and word in V.skeleton(t)) for t in text.split(" ")):
            R2.fail("ayah %s does not contain %s" % (ref, word))
        out[ref] = text
    print("verses: %d copied from Tanzil and checked" % len(out))
    return out


def write_doc_block(verses, names):
    path = os.path.join(DESIGN, "design-2-meanings.md")
    text = io.open(path, encoding="utf-8").read()
    rows = ["| Reference | Ayah — copied whole from the Tanzil file by `tools/build_round3.py` |", "| --- | --- |"]
    for ref in sorted(verses, key=lambda r: tuple(int(x) for x in r.split(":"))):
        s = int(ref.split(":")[0])
        rows.append("| %s %s (%s) | %s |" % (names[s]["en"], ref, names[s]["ar"], verses[ref]))
    text = R2.replace_block(text, "<!--AYAHS-BEGIN-->", "<!--AYAHS-END-->", "\n".join(rows) + "\n")
    io.open(path, "w", encoding="utf-8", newline="\n").write(text)
    print("written design-2-meanings.md (ayah table)")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    lowest, failures = P.check()
    if failures:
        R2.fail("contrast: " + "; ".join(failures))
    print("contrast: %d palettes pass" % len(lowest))
    R2.check_sources({rel: R2.SHA256[rel] for rel in SOURCES})
    data = R2.build_data(PAGES)
    import xml.etree.ElementTree as ET
    root = ET.parse(os.path.join(R2.ASSETS, "tanzil/quran-data.xml")).getroot()
    names = {int(s.get("index")): {"ar": s.get("name"), "en": s.get("tname")} for s in root.iter("sura")}
    verses = build_verses()
    data["verses"] = verses
    for ref in verses:
        s = ref.split(":")[0]
        data["names"][s] = names[int(s)]
    data["directions"] = {k: {"name": d["name"], "min": d["min"],
                              "swatch": {t: [d[t]["primary"], d[t]["dot"], d[t]["second"], d[t]["bg"]]
                                         for t in ("light", "dark")}}
                          for k, d in P.DIRECTIONS.items()}
    R2.embed(PAGE, "ROUND3", data, FONTS)
    html = open(PAGE, encoding="utf-8", newline="").read()
    html = R2.replace_block(html, "/*ROUND3-THEMES-BEGIN*/", "/*ROUND3-THEMES-END*/", P.css())
    open(PAGE, "w", encoding="utf-8", newline="\n").write(html)
    tokens = {"design": "2 — early Islam", "generated_by": "docs/design/prototypes/tools/build_round3.py",
              "meanings": "docs/design/design-2-meanings.md", "roles": P.__doc__.split("Roles")[1].strip(),
              "directions": {k: {"name": d["name"], "minimum_contrast": d["min"], "light": d["light"],
                                 "dark": d["dark"]} for k, d in P.DIRECTIONS.items()}}
    with io.open(os.path.join(DESIGN, "tokens-design-2.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(tokens, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("written tokens-design-2.json")
    check_doc_excerpts(verses)
    write_doc_block(verses, names)


if __name__ == "__main__":
    main()
