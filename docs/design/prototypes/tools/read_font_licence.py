"""Print the copyright, licence and version strings stored inside OpenType / TrueType font files.

Reads only the 'name' table with the standard library. WOFF2 files are not supported (they are compressed).
Usage: python -I read_font_licence.py <font file> [<font file> ...]
"""
import struct
import sys

WANTED = {0: "Copyright", 1: "Family", 4: "Full name", 5: "Version", 7: "Trademark", 8: "Manufacturer",
          9: "Designer", 10: "Description", 11: "Vendor URL", 12: "Designer URL", 13: "Licence", 14: "Licence URL"}


def names(path):
    data = open(path, "rb").read()
    tag = data[:4]
    if tag == b"wOF2":
        return {"error": "WOFF2 (compressed) - not readable here"}
    num_tables = struct.unpack(">H", data[4:6])[0]
    for i in range(num_tables):
        rec = data[12 + 16 * i: 28 + 16 * i]
        t, _, off, length = struct.unpack(">4sIII", rec)
        if t == b"name":
            table = data[off: off + length]
            break
    else:
        return {"error": "no name table"}
    _, count, string_off = struct.unpack(">HHH", table[:6])
    out = {}
    for i in range(count):
        pid, eid, lid, nid, ln, so = struct.unpack(">HHHHHH", table[6 + 12 * i: 18 + 12 * i])
        if nid not in WANTED:
            continue
        raw = table[string_off + so: string_off + so + ln]
        if pid in (0, 3):
            text = raw.decode("utf-16-be", "replace")
        else:
            text = raw.decode("latin-1", "replace")
        key = "%s (platform %d, language 0x%x)" % (WANTED[nid], pid, lid)
        out.setdefault(WANTED[nid], {})[key] = text
    return out


for p in sys.argv[1:]:
    print("=" * 100)
    print(p.replace("\\", "/").split("/")[-1])
    result = names(p)
    if "error" in result:
        print("  ", result["error"])
        continue
    for field, variants in result.items():
        seen = set()
        for key, text in variants.items():
            if text in seen:
                continue
            seen.add(text)
            print("  %-48s %s" % (key, text.replace("\r", " ").replace("\n", " / ")))
