"""Build `round-3.html` (design 3, "the first era") and its generated companions from the verified source files.

Design 3 (first built as "round 4", renamed round 3 on 2026-11-19) was asked by the author on 2026-11-19: a new design from the time of the Prophet ﷺ, the Companions and the
Rightly Guided Caliphs, with many colour directions drawn from reflection on the Quran. It reuses every check of
rounds 1 and 2: checksums, the layout read as plain text, every word and King Fahd glyph cross-checked against Tanzil,
every cited ayah copied whole from Tanzil and checked to contain its word, every Quran excerpt in the meanings document
checked word for word, the colour checks (design3_palettes.py) and the interface texts of the 20 other languages.

Usage: python -I build_round3.py
"""
import io
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_round1 as R1  # noqa: E402  (our own scripts beside this one)
import build_round2 as B2  # noqa: E402
import design2_palettes as P2  # noqa: E402
import design3_palettes as P3  # noqa: E402

PAGE = os.path.join(HERE, "..", "round-3.html")
DESIGN = os.path.join(HERE, "..", "..")
DOC = os.path.join(DESIGN, "design-3-meanings.md")
PAGES = B2.PAGES

# Ayahs cited for design 3: reference -> the word (letters as compared by the skeleton) the citation is about.
VERSES = {
    "96:1": "اقرا", "96:2": "علق", "96:3": "الاكرم",                     # Hira: the first revelation
    "96:4": "بالقلم",                                                     # the first sheets: writing
    "9:40": "الغار",                                                      # the Cave: the Hijrah
    "50:10": "النخل",                                                     # Taybah: the palms
    "88:17": "الابل", "88:18": "السما", "88:19": "الجبال", "88:20": "الارض",  # look at the camels
    "89:1": "الفجر", "81:18": "الصبح",                                    # dawn
    "93:1": "الضحي", "93:2": "سجي",                                       # forenoon and the still night (ى is compared as ي)
    "22:63": "مخضرة",                                                     # rain
    "55:64": "مدهامتان", "55:66": "نضاختان", "55:68": "رمان",              # the two gardens (55:66 since 2026-11-20)
    "95:1": "التين",                                                      # the fig and the olive (2026-11-20)
    "108:1": "الكوثر",                                                    # al-Kawthar
    "91:1": "الشمس", "91:2": "القمر",                                     # the sun and the moon
    "51:1": "الذريت",                                                     # the scattering winds (dagger alefs are marks)
    "48:29": "كزرع",                                                      # the crop
    "87:4": "المرعي", "87:5": "احوي",                                     # the pasture (ى is compared as ي)
    "14:24": "كشجرة", "14:25": "اكلها", "67:19": "الطير", "25:45": "الظل",   # five directions from the Quran only
    "55:24": "الجوار", "103:1": "والعصر",                               # (the author, second message of 2026-11-20)
    "56:28": "سدر", "56:29": "وطلح", "56:30": "وظل", "47:15": "انهر",   # Paradise, from the Quran (2026-11-20)
    "39:20": "غرف", "69:23": "قطوفها", "76:14": "قطوفها", "55:72": "الخيام",
    "55:62": "جنتان",
    "24:35": "زجاجة",                                                     # light
    "35:27": "غرابيب",                                                    # mountains (high contrast)
    "30:22": "السنتكم",                                                   # the language choice
}


def check_doc_excerpts(verses):
    text = io.open(DOC, encoding="utf-8").read()
    text = text.split("<!--AYAHS-BEGIN-->")[0] + text.split("<!--AYAHS-END-->")[1]
    excerpts = [e for e in re.findall("«([^»]+)»", text) if B2.TASHKEEL.search(e)]
    for e in excerpts:
        if not any(e in v for v in verses.values()):
            R1.fail("excerpt in design-3-meanings.md is not part of a cited ayah: %s" % e)
    print("excerpts: %d in design-3-meanings.md, each found word for word in a cited ayah" % len(excerpts))


def write_doc_block(verses, names):
    text = io.open(DOC, encoding="utf-8").read()
    rows = ["| Reference | Ayah — copied whole from the Tanzil file by `tools/build_round3.py` |", "| --- | --- |"]
    for ref in sorted(verses, key=lambda r: tuple(int(x) for x in r.split(":"))):
        s = int(ref.split(":")[0])
        rows.append("| %s %s (%s) | %s |" % (names[s]["en"], ref, names[s]["ar"], verses[ref]))
    text = R1.replace_block(text, "<!--AYAHS-BEGIN-->", "<!--AYAHS-END-->", "\n".join(rows) + "\n")
    io.open(DOC, "w", encoding="utf-8", newline="\n").write(text)
    print("written design-3-meanings.md (ayah table)")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    lowest, failures = P3.check()
    if failures:
        R1.fail("colours: " + "; ".join(failures))
    print("colours: %d palettes pass" % len(lowest))
    R1.check_sources({rel: R1.SHA256[rel] for rel in B2.SOURCES})
    data = R1.build_data(PAGES)
    root = ET.parse(os.path.join(R1.ASSETS, "tanzil/quran-data.xml")).getroot()
    names = {int(s.get("index")): {"ar": s.get("name"), "en": s.get("tname")} for s in root.iter("sura")}
    B2.VERSES = VERSES
    verses = B2.build_verses()
    check_doc_excerpts(verses)
    data["verses"] = verses
    for ref in verses:
        data["names"][ref.split(":")[0]] = names[int(ref.split(":")[0])]
    page_starts = [(int(x.get("index")), (int(x.get("sura")), int(x.get("aya")))) for x in root.iter("page")]

    def page_of(key):
        return max(n for n, start in page_starts if start <= key)

    data["surahs"] = [{"n": int(s.get("index")), "ar": s.get("name"), "en": s.get("tname"),
                       "type": {"Meccan": "makki", "Medinan": "madani"}[s.get("type")],
                       "ayas": int(s.get("ayas")), "page": page_of((int(s.get("index")), 1))} for s in root.iter("sura")]
    data["juzs"] = [{"n": int(j.get("index")), "s": int(j.get("sura")), "a": int(j.get("aya")),
                     "page": page_of((int(j.get("sura")), int(j.get("aya"))))} for j in root.find("juzs")]
    if len(data["surahs"]) != 114 or sum(s["ayas"] for s in data["surahs"]) != 6236 or len(data["juzs"]) != 30:
        R1.fail("metadata counts")
    data["directions"] = {k: {"name": d["name"], "min": d["min"], "light": d["light"], "dark": d["dark"],
                              "swatch": {t: [d[t]["primary"], d[t]["dot"], d[t]["second"], d[t]["bg"]]
                                         for t in ("light", "dark")}}
                          for k, d in P3.DIRECTIONS.items()}
    R1.embed(PAGE, "ROUND3", data, B2.FONTS)
    html = open(PAGE, encoding="utf-8", newline="").read()
    html = R1.replace_block(html, "/*ROUND3-THEMES-BEGIN*/", "/*ROUND3-THEMES-END*/", P3.css())
    html = R1.replace_block(html, "<!--ROUND3-CVD-BEGIN-->", "<!--ROUND3-CVD-END-->", P2.svg_filters())
    i18n, extra = B2.build_i18n("round2"), B2.build_i18n("round3")   # design 2's texts, then design 3's own
    if set(i18n["en2id"].values()) & set(extra["en2id"].values()):
        R1.fail("i18n: an id of i18n/round3 is already in i18n/round2")
    i18n["en2id"].update(extra["en2id"])
    for code in i18n["tr"]:
        i18n["tr"][code].update(extra["tr"][code])
    html = R1.replace_block(html, "/*ROUND3-I18N-BEGIN*/", "/*ROUND3-I18N-END*/",
                            "window.ROUND3_I18N = " + json.dumps(i18n, ensure_ascii=False) + ";\n")
    open(PAGE, "w", encoding="utf-8", newline="\n").write(html)
    tokens = {"design": "3 — the first era (round 3)", "generated_by": "docs/design/prototypes/tools/build_round3.py",
              "meanings": "docs/design/design-3-meanings.md",
              "directions": {k: {"name": d["name"], "minimum_contrast": d["min"], "light": d["light"],
                                 "dark": d["dark"]} for k, d in P3.DIRECTIONS.items()}}
    with io.open(os.path.join(DESIGN, "tokens-design-3.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(tokens, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("written tokens-design-3.json")
    write_doc_block(verses, names)


if __name__ == "__main__":
    main()
