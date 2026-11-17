"""Build the data and font blocks of `round-2.html` from the verified source files.

Nothing in the Quran text is typed or changed. The script:
  1. checks the SHA-256 of every source file against the values recorded in assets/README.md;
  2. reads the old-Madinah page layout (DigitalKhatt) as plain text - it is never executed;
  3. for the pages shown in the prototype, places on each printed line
       - the layout's own words (for the fonts made for that encoding),
       - the same words taken from the Tanzil Uthmani text (for the other fonts),
       - the King Fahd page-font glyphs (one glyph per word, pause mark and ayah sign);
     and stops if any word, glyph or ayah does not match;
  4. embeds the fonts (base64) and the data into round-2.html between marker comments.

Usage: python -I build_round2.py
`build_round3.py` uses the same functions (`check_sources`, `build_data`, `embed`) for its own pages.
"""
import base64
import hashlib
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
PAGE = os.path.join(HERE, "..", "round-2.html")
sys.path.insert(0, HERE)
import verify_mushaf_layout as V  # noqa: E402  (our own script beside this one)

PAGES = [1, 2, 5, 545, 546]
SHA256 = {
    "tanzil/quran-uthmani.txt": "6933e133dd56db778c801bf738848454e43648105a151e8d84d86a7cae39ec5f",
    "tanzil/quran-data.xml": "8867c1d88191472adec9db694b3cd9f135b1a2ef580574d32cf888dcb22c5c7a",
    "digitalkhatt/quran_text_old_madinah.ts": "08972d48c6c250fda4ce9c58a2f23be52c17b0cf097ac093a040e3c392b79f07",
    "digitalkhatt/oldmadina.woff2": "4404019cd8733ee4eff282b54368f4c7e342469bd601c4bfa004b5359c0935cf",
    "digitalkhatt/DigitalKhattV2.ttf": "ab495b5abb2ed30b2ffda022f2a1d10a25bfab7ea0a4dbb4ce05d5c171959c78",
    "kfgqpc/UthmanicHafs1 Ver09.otf": "59e20b2403687a67854fd199861abed3528068c035d2689898465d5faf39bb31",
    "kfgqpc/mushaf.txt": "307c073476a759ef182bb67229c05a843c5eecce91a81119c349951e421703f3",
    "kfgqpc/QCF_P001.TTF": "85099681c9a6e4aba8ad01885c212ba3af724c002cf5bb65d82afc5da8024623",
    "kfgqpc/QCF_P002.TTF": "6d6ce98f3ba8dd38715ee4c84fc5daf0966d472abed83822feb4a74e03b2f0a9",
    "kfgqpc/QCF_P005.TTF": "de1ba5401e8434bf5825483713f2cadc3c0ca00476c0f30ad1e62fe4598ff09e",
    "kfgqpc/QCF_P545.TTF": "9182a7fd37cd623ca97ef96cfc24b30f779765301491db740ec7001890b10219",
    "kfgqpc/QCF_P546.TTF": "362129554299de80073b59146ee9b5ad1e009db0255adc50eaf23c5f2ab288b4",
}
FONTS = {  # CSS family -> (file, format)
    "DK Old Madina": ("digitalkhatt/oldmadina.woff2", "woff2"),
    "DK New Madina": ("digitalkhatt/DigitalKhattV2.ttf", "truetype"),
    "KFGQPC Hafs": ("kfgqpc/UthmanicHafs1 Ver09.otf", "opentype"),
}
for _p in PAGES:
    FONTS["QCF P%03d" % _p] = ("kfgqpc/QCF_P%03d.TTF" % _p, "truetype")

PAUSE = re.compile("[ۖ-ۛ]")  # pause marks ۖ ۗ ۘ ۙ ۚ ۛ (U+06DC, the small seen, belongs to its word)
DIGITS = "٠١٢٣٤٥٦٧٨٩"


def ar(n):
    return "".join(DIGITS[int(d)] for d in str(n))


def fail(msg):
    raise SystemExit("STOP: " + msg)


def read(rel, mode="rb"):
    return open(os.path.join(ASSETS, rel), mode)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    check_sources(SHA256)
    data = build_data(PAGES)
    embed(PAGE, "ROUND2", data, FONTS)


def check_sources(sha256):
    for rel, digest in sha256.items():
        got = hashlib.sha256(read(rel).read()).hexdigest()
        if got != digest:
            fail("checksum of %s changed: %s" % (rel, got))
    print("checksums: %d files ok" % len(sha256))


def build_data(pages):
    """Lines of the given pages, with the layout, Tanzil and King Fahd forms of every word, all cross-checked."""

    tanzil = V.parse_tanzil(os.path.join(ASSETS, "tanzil/quran-uthmani.txt"))
    V.BASMALA_SKELETON = V.skeleton(tanzil[(1, 1)].replace(" ", ""))
    meta_pages, quarters, juzs, counts = V.parse_meta(os.path.join(ASSETS, "tanzil/quran-data.xml"))
    root = ET.parse(os.path.join(ASSETS, "tanzil/quran-data.xml")).getroot()
    names = {int(s.get("index")): {"ar": s.get("name"), "en": s.get("tname")} for s in root.iter("sura")}

    # Raw layout lines (kept exactly, including the invisible joiners the DigitalKhatt fonts need).
    raw = open(os.path.join(ASSETS, "digitalkhatt/quran_text_old_madinah.ts"), encoding="utf-8").read()
    raw_pages = [re.findall(r"^\s{4}'([^'\n]*)',?$", b, flags=re.M) for b in re.split(r"\n  \],?\n?", raw)]
    raw_pages = [p for p in raw_pages if p]
    clean_pages = V.parse_layout(os.path.join(ASSETS, "digitalkhatt/quran_text_old_madinah.ts"))
    if len(raw_pages) != 604:
        fail("layout pages: %d" % len(raw_pages))

    # Tanzil words per ayah, each followed by its separate marks (pause marks, sajdah sign).
    def tanzil_groups(key):
        toks = [t for t in tanzil[key].split(" ") if t]
        if key[1] == 1 and key[0] not in (1, 9):
            toks = toks[4:]
        groups = []
        for t in toks:
            if V.skeleton(t):
                groups.append(t)
            elif groups:
                groups[-1] += " " + t
            else:
                fail("mark before the first word in %s" % (key,))
        return groups

    glyph_lines = [l.rstrip("\r\n") for l in open(os.path.join(ASSETS, "kfgqpc/mushaf.txt"), encoding="utf-8") if l.strip()]
    keys = sorted(tanzil)
    glyphs = {k: l.split(",", 1)[1] for k, l in zip(keys, glyph_lines)}

    # Walk the whole layout once to know the surah, the ayah and the quarter signs at every token.
    pages_out = {}
    surah, next_ayah, word_idx = 0, {}, {}
    tz_cache, qcf_pos, rub_keys = {}, {}, set()
    quarter_index = {q: i for i, q in enumerate(quarters)}
    for pno in range(1, 605):
        keep = pno in pages
        lines_out = []
        first_key = None
        for lno, (rline, cline) in enumerate(zip(raw_pages[pno - 1], clean_pages[pno - 1]), start=1):
            if cline.startswith("سُورَةُ") and V.AYAH_END not in cline:
                surah += 1
                next_ayah[surah] = 1
                if keep:
                    lines_out.append({"t": "header", "s": surah, "dk": rline})
                continue
            if surah > 1 and V.AYAH_END not in cline and V.skeleton(cline.replace(" ", "")) == V.BASMALA_SKELETON:
                if keep:
                    lines_out.append({"t": "basmala", "dk": rline,
                                      "tz": " ".join(tanzil[(1, 1)].split(" ")[:4])})
                continue
            dk_tokens = [t for t in rline.split(" ") if t]
            tz_parts, qcf_parts, ayahs_on_line = [], [], []
            for tok in dk_tokens:
                ctok = tok.replace("͏", "")
                key = (surah, next_ayah[surah])
                if first_key is None:
                    first_key = key
                if key not in tz_cache:
                    tz_cache[key] = tanzil_groups(key)
                    word_idx[key] = 0
                    qcf_pos[key] = 0
                # quarter sign before the ayah's first word
                if ctok.startswith(V.RUB):
                    rub_keys.add(key)
                    if keep:
                        tz_parts.append(V.RUB)
                    ctok = ctok[1:]
                if ctok.startswith(V.SAJDA):
                    ctok = ctok[1:]
                m = re.fullmatch(V.AYAH_END + "([" + DIGITS + "]+)(" + V.RUB + ")?", ctok)
                if m:
                    number = int("".join(str(DIGITS.index(d)) for d in m.group(1)))
                    if number != key[1]:
                        fail("ayah number %d at %s" % (number, key))
                    if word_idx[key] != len(tz_cache[key]):
                        fail("words left over in %s" % (key,))
                    g = glyphs[key]
                    if keep:
                        tz_parts.append(V.AYAH_END + ar(number))
                        qcf_parts.append(g[qcf_pos[key]:])
                        if len(g) - qcf_pos[key] != 1:
                            fail("glyphs left over in %s: %d" % (key, len(g) - qcf_pos[key]))
                    ayahs_on_line.append(key)
                    next_ayah[surah] += 1
                    if m.group(2):  # "۝٢٥۞": the quarter sign of the next ayah, written after this number
                        rub_keys.add((surah, next_ayah[surah]))
                        if keep:
                            tz_parts.append(V.RUB)
                    continue
                if not ctok or ctok == V.RUB:
                    continue
                # a word
                g = glyphs[key]
                if word_idx[key] == 0 and keep:
                    # Glyphs are checked on the pages shown here; the whole-Quran report is verify_mushaf_layout.py.
                    expected = sum(1 + len(PAUSE.findall(w)) for w in tz_cache[key]) + 1
                    extra = len(g) - expected
                    if extra not in (0, 1) or (extra == 1) != (key in rub_keys):
                        fail("glyph count in %s" % (key,))
                    qcf_pos[key] = extra  # the extra first glyph is the quarter sign drawn by the page font
                    if extra:
                        qcf_parts.append(g[0])
                tz_word = tz_cache[key][word_idx[key]]
                if V.skeleton(tz_word.split(" ")[0]) != V.skeleton(ctok):
                    fail("word mismatch in %s: %s / %s" % (key, tz_word, ctok))
                take = 1 + len(PAUSE.findall(tz_word))
                if keep:
                    tz_parts.append(tz_word)
                    qcf_parts.append(g[qcf_pos[key]:qcf_pos[key] + take])
                    qcf_pos[key] += take
                word_idx[key] += 1
            if keep:
                lines_out.append({"t": "text", "dk": rline, "tz": " ".join(tz_parts), "qcf": " ".join(qcf_parts)})
        if keep:
            # Juz and hizb (quarters) of the page's first ayah, from Tanzil's metadata.
            juz = max(i for i, j in enumerate(juzs, start=1) if j <= first_key)
            q = max(i for i, x in enumerate(quarters) if x <= first_key)
            pages_out[pno] = {"lines": lines_out, "juz": juz, "hizb": q // 4 + 1, "quarter": q % 4,
                              "first": list(first_key), "center": pno in (1, 2),
                              "surahs": sorted({l["s"] for l in lines_out if l["t"] == "header"} | {first_key[0]})}
            print("page %3d: %2d lines | first ayah %s | juz %d | hizb %d" % (pno, len(lines_out), first_key, juz,
                                                                               q // 4 + 1))

    data = {"pages": pages_out, "names": {str(k): names[k] for k in sorted({s for p in pages_out.values()
                                                                             for s in p["surahs"]})},
            "checked": {"ayahs": len(tanzil), "pages": len(meta_pages)}}
    return data


def embed(page, prefix, data, fonts):
    """Writes the data (as window.<prefix>) and the fonts (base64) between the page's marker comments."""
    page_html = open(page, encoding="utf-8", newline="").read()
    data_block = "window." + prefix + " = " + json.dumps(data, ensure_ascii=False) + ";\n"
    css = []
    for family, (rel, fmt) in fonts.items():
        b64 = base64.b64encode(read(rel).read()).decode("ascii")
        mime = {"woff2": "font/woff2", "truetype": "font/ttf", "opentype": "font/otf"}[fmt]
        css.append("@font-face{font-family:'%s';src:url(data:%s;base64,%s) format('%s');font-display:block}"
                   % (family, mime, b64, fmt))
    page_html = replace_block(page_html, "/*%s-DATA-BEGIN*/" % prefix, "/*%s-DATA-END*/" % prefix, data_block)
    page_html = replace_block(page_html, "/*%s-FONTS-BEGIN*/" % prefix, "/*%s-FONTS-END*/" % prefix,
                              "\n".join(css) + "\n")
    open(page, "w", encoding="utf-8", newline="\n").write(page_html)
    print("written %s: %.2f MB" % (os.path.basename(page), len(page_html.encode("utf-8")) / 1e6))


def replace_block(text, begin, end, body):
    if text.count(begin) != 1 or text.count(end) != 1:
        fail("markers %s / %s not found exactly once" % (begin, end))
    head, rest = text.split(begin)
    return head + begin + "\n" + body + end + rest.split(end)[1]


if __name__ == "__main__":
    main()
