"""Build the data and font blocks of `round-3.html` (design 2, "early Islam") from the verified source files.

Same checks as round 2 (`build_round2.py`): checksums, the layout read as plain text, every word and every King Fahd
glyph cross-checked against the Tanzil text. Round 3 uses only the default Quran font chosen by the author on
2026-11-17 — the King Fahd Complex page fonts (Madinah mushaf, 1405H). The basmala line is drawn, as in round 2, with
the KFGQPC Hafs font (it has no U+06DF, which the basmala does not use).

Usage: python -I build_round3.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_round2 as R2  # noqa: E402  (our own script beside this one)

PAGE = os.path.join(HERE, "..", "round-3.html")
PAGES = [1, 2, 5, 545, 546]
SOURCES = ["tanzil/quran-uthmani.txt", "tanzil/quran-data.xml", "digitalkhatt/quran_text_old_madinah.ts",
           "kfgqpc/UthmanicHafs1 Ver09.otf", "kfgqpc/mushaf.txt"] + ["kfgqpc/QCF_P%03d.TTF" % p for p in PAGES]
FONTS = {"KFGQPC Hafs": ("kfgqpc/UthmanicHafs1 Ver09.otf", "opentype")}
for _p in PAGES:
    FONTS["QCF P%03d" % _p] = ("kfgqpc/QCF_P%03d.TTF" % _p, "truetype")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    R2.check_sources({rel: R2.SHA256[rel] for rel in SOURCES})
    data = R2.build_data(PAGES)
    R2.embed(PAGE, "ROUND3", data, FONTS)


if __name__ == "__main__":
    main()
