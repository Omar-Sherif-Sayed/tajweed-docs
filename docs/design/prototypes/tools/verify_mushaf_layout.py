"""Verify the DigitalKhatt old-Madinah page layout against the verified Tanzil sources.

Nothing is changed or written back: the script reads the files and reports.

Checks
  1. Words: every ayah of the layout has the same words, in the same order, as the Tanzil Uthmani text.
     The comparison uses a *skeleton* of each word (letters only, all marks removed, hamza and alef forms unified),
     because the two files use different but valid Unicode encodings for the same script.
     This is a comparison key only - no displayed text is ever built from it.
  2. Pages: every one of the 604 pages starts at the ayah that Tanzil's metadata gives for the Madinah mushaf.
  3. Quarter marks: the layout's rub-el-hizb signs (U+06DE) stand at the 240 hizb quarters of Tanzil's metadata.
  4. Glyph fonts (optional): for the King Fahd page fonts, every ayah has one glyph per word plus its end sign.

Usage:
  python -I verify_mushaf_layout.py <quran_text_old_madinah.ts> <quran-uthmani.txt> <quran-data.xml> [<mushaf.txt>]
"""
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

AYAH_END = "۝"     # ۝ end of ayah
RUB = "۞"          # ۞ rub el hizb
SAJDA = "۩"        # ۩ place of sajdah
ARABIC_DIGITS = "٠١٢٣٤٥٦٧٨٩"
BASMALA_SKELETON = None  # set from Tanzil 1:1


def skeleton(word):
    """Letters only: decompose, drop marks and format characters, unify alef and hamza seats."""
    out = []
    for ch in unicodedata.normalize("NFD", word):
        cat = unicodedata.category(ch)
        if cat.startswith("M") or cat in ("Cf", "Lm") or ch in (RUB, SAJDA, "۝"):
            continue
        if ch.isdigit():
            continue
        out.append(ch)
    s = "".join(out)
    s = s.replace("ٱ", "ا")           # alef wasla -> alef
    s = s.replace("ء", "")                 # standalone hamza (written above the line in some encodings)
    s = s.replace("ی", "ي")           # farsi yeh -> yeh (encoding variant)
    s = s.replace("ى", "ي")           # alef maksura -> yeh (dotless / dotted written the same in rasm)
    return s


def parse_layout(path):
    """Return a list of 604 pages, each a list of line strings (read as text, never executed)."""
    text = open(path, encoding="utf-8").read()
    pages = []
    for block in re.split(r"\n  \],?\n?", text):
        lines = re.findall(r"^\s{4}'([^'\n]*)',?$", block, flags=re.M)
        if lines:
            pages.append([l.replace("͏", "") for l in lines])
    return pages


def parse_tanzil(path):
    ayahs = {}
    for line in open(path, encoding="utf-8"):
        parts = line.rstrip("\r\n").split("|", 2)
        if len(parts) == 3 and parts[0].isdigit():
            ayahs[(int(parts[0]), int(parts[1]))] = parts[2]
    return ayahs


def parse_meta(path):
    root = ET.parse(path).getroot()
    pages = [(int(p.get("sura")), int(p.get("aya"))) for p in root.iter("page")]
    quarters = [(int(q.get("sura")), int(q.get("aya"))) for q in root.iter("quarter")]
    juzs = [(int(j.get("sura")), int(j.get("aya"))) for j in root.iter("juz")]
    counts = {int(s.get("index")): int(s.get("ayas")) for s in root.iter("sura")}
    return pages, quarters, juzs, counts


def walk_layout(pages, counts):
    """Yield (page, line, kind, data). kinds: 'header', 'basmala', 'word', 'end' (ayah number), 'rub'."""
    surah = 0
    for pno, lines in enumerate(pages, start=1):
        for lno, line in enumerate(lines, start=1):
            if line.startswith("سُورَةُ") and AYAH_END not in line:
                surah += 1
                yield pno, lno, "header", surah
                continue
            if surah > 1 and AYAH_END not in line and skeleton(line.replace(" ", "")) == BASMALA_SKELETON:
                yield pno, lno, "basmala", surah
                continue
            for token in line.split(" "):
                if not token:
                    continue
                if token.startswith(SAJDA):          # "۩۝٢٤": the sajdah sign written before the ayah number
                    token = token[1:]
                    if not token:
                        continue
                # a token can be: word, word+pause mark, ۝N, ۝N۞, ۞, ۩
                m = re.fullmatch(AYAH_END + "([" + ARABIC_DIGITS + "]+)(" + RUB + ")?", token)
                if m:
                    yield pno, lno, "end", int("".join(str(ARABIC_DIGITS.index(d)) for d in m.group(1)))
                    if m.group(2):
                        yield pno, lno, "rub", None
                    continue
                if token == RUB:
                    yield pno, lno, "rub", None
                    continue
                if token == SAJDA:
                    continue
                if token.startswith(RUB):
                    yield pno, lno, "rub", None
                    token = token[1:]
                yield pno, lno, "word", token


def main():
    global BASMALA_SKELETON
    sys.stdout.reconfigure(encoding="utf-8")
    layout_path, tanzil_path, meta_path = sys.argv[1:4]
    glyph_path = sys.argv[4] if len(sys.argv) > 4 else None

    tanzil = parse_tanzil(tanzil_path)
    BASMALA_SKELETON = skeleton(tanzil[(1, 1)].replace(" ", ""))
    meta_pages, meta_quarters, meta_juzs, counts = parse_meta(meta_path)
    pages = parse_layout(layout_path)
    print("layout pages:", len(pages), "| lines per page (min/max over pages 3-604):",
          min(len(p) for p in pages[2:]), "/", max(len(p) for p in pages[2:]))

    # Rebuild ayahs from the layout, remembering where each ayah starts and where the quarter signs stand.
    layout_ayahs = {}        # (surah, ayah) -> list of words
    ayah_start_page = {}     # (surah, ayah) -> page of its first word
    rub_before = set()       # (surah, ayah) whose first word is preceded by ۞
    ayah_lines = {}          # (surah, ayah) -> list of (page, line) of its words
    surah, current, pending_rub = 0, [], False
    next_ayah = {}
    for pno, lno, kind, data in walk_layout(pages, counts):
        if kind == "header":
            surah = data
            next_ayah[surah] = 1
            continue
        if kind == "basmala":
            continue
        if kind == "rub":
            pending_rub = True
            continue
        if kind == "word":
            key = (surah, next_ayah[surah])
            if not current:
                ayah_start_page[key] = pno
                if pending_rub:
                    rub_before.add(key)
                    pending_rub = False
            current.append(data)
            ayah_lines.setdefault(key, []).append((pno, lno))
            continue
        if kind == "end":
            if data != next_ayah[surah]:
                print("NUMBERING ERROR at page %d line %d: expected %d:%d, found %d" % (pno, lno, surah, next_ayah[surah], data))
            layout_ayahs[(surah, data)] = current
            current = []
            next_ayah[surah] = data + 1

    print("ayahs rebuilt from the layout:", len(layout_ayahs), "| surahs:", surah)

    # 1. Words
    word_diffs = []
    for key in sorted(tanzil):
        t_words = [w for w in tanzil[key].split(" ") if w and w not in (SAJDA, RUB)]
        if key[1] == 1 and key[0] not in (1, 9):
            # Tanzil writes the basmala in front of ayah 1; the printed mushaf has it on its own line.
            t_words = t_words[4:]
        l_words = layout_ayahs.get(key)
        if l_words is None:
            word_diffs.append((key, "missing in layout", "", ""))
            continue
        # Tanzil writes pause marks as separate tokens; they have no letters and are left out of the word list.
        a = [s for s in (skeleton(w) for w in t_words) if s]
        b = [s for s in (skeleton(w) for w in l_words) if s]
        if a != b:
            word_diffs.append((key, "%d vs %d words" % (len(a), len(b)), " ".join(a), " ".join(b)))
    print("\n1. WORDS: ayahs whose words differ:", len(word_diffs), "of", len(tanzil))
    for d in word_diffs[:25]:
        print("   %s:%s  %s\n      tanzil : %s\n      layout : %s" % (d[0][0], d[0][1], d[1], d[2], d[3]))

    # 2. Page starts
    page_diffs = []
    starts = {}
    for key, p in ayah_start_page.items():
        starts.setdefault(p, []).append(key)
    for i, key in enumerate(meta_pages, start=1):
        first = min(starts.get(i, [(999, 999)]))
        if first != key:
            page_diffs.append((i, key, first))
    print("\n2. PAGES: page starts that differ from Tanzil's Madinah metadata:", len(page_diffs), "of", len(meta_pages))
    for d in page_diffs[:25]:
        print("   page %d: tanzil %s, layout %s" % d)

    # 3. Quarter signs (the first quarter of each hizb starts a juz or a hizb and may carry no sign in print)
    q_set = set(meta_quarters)
    missing = sorted(q_set - rub_before)
    extra = sorted(rub_before - q_set)
    print("\n3. QUARTERS: Tanzil quarters %d | layout signs %d | quarters without a sign %d | signs not at a quarter %d"
          % (len(q_set), len(rub_before), len(missing), len(extra)))
    print("   quarters without a sign, other than the first ayah of a surah:", [k for k in missing if k[1] != 1])
    print("   signs not at a Tanzil quarter:", extra[:12])

    # 4. Glyph fonts: mushaf.txt has one line per ayah: "<page>,<glyphs>"; one glyph per word, a separate glyph
    #    for each pause mark, and one glyph for the ayah's end sign.
    if glyph_path:
        pause = re.compile("[ۖ-ۛ]")  # pause marks; U+06DC (small seen) belongs to its word
        glyph_diffs, page_diffs4 = [], []
        glyph_lines = [l.rstrip("\r\n") for l in open(glyph_path, encoding="utf-8") if l.strip()]
        keys = sorted(tanzil)
        for key, line in zip(keys, glyph_lines):
            page_text, glyphs = line.split(",", 1)
            if int(page_text) != ayah_start_page.get(key):
                page_diffs4.append((key, int(page_text), ayah_start_page.get(key)))
            words = layout_ayahs.get(key, [])
            expected = sum(1 + len(pause.findall(w)) for w in words) + 1
            expected += 1 if key in rub_before else 0          # the quarter sign has its own glyph
            expected += 1 if SAJDA in tanzil[key] else 0       # so has the sajdah sign
            if len(glyphs) != expected:
                glyph_diffs.append((key, "%d glyphs, %d expected" % (len(glyphs), expected)))
        print("\n4. GLYPHS: mushaf.txt lines %d | ayahs whose page differs from the layout: %d | ayahs whose glyph count "
              "differs (word + pause marks + end sign): %d" % (len(glyph_lines), len(page_diffs4), len(glyph_diffs)))
        for d in page_diffs4[:10]:
            print("   page: %s:%s glyph page %d, layout page %s" % (d[0][0], d[0][1], d[1], d[2]))
        for d in glyph_diffs[:15]:
            print("   count: %s:%s %s" % (d[0][0], d[0][1], d[1]))

    # Facts asked by the author
    print("\nPAGE 5:")
    for lno, line in enumerate(pages[4], start=1):
        print("   %2d  %s" % (lno, line))
    print("   ayah 2:25 occupies lines:", sorted(set(l for p, l in ayah_lines[(2, 25)] if p == 5)))


if __name__ == "__main__":
    main()
