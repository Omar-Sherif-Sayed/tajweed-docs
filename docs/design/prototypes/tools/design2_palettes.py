"""The colour directions of design 2 ("early Islam"), with their contrast check.

One place for the values: build_round3.py writes them into round-3.html (CSS) and docs/design/tokens-design-2.json.
Why each colour was chosen: docs/design/design-2-meanings.md.

Roles (the same in every direction):
  bg, surface, surface2  page background and cards       text, muted   body text, secondary text
  border, rule           card edges, thin ink rules      ink, page     Quran text and the mushaf page
  primary, onprimary     main buttons                    dot, dotsoft  the small marks (active item, page number)
  second, secondsoft     prayer / qibla / adhkar, "verified"   card, oncard   the prayer card
Rule: every text / background pair below reaches 4.5 : 1; the high-contrast direction reaches 7 : 1.
"""

DIRECTIONS = {
    "parchment": {
        "name": {"ar": "الرَّقّ", "en": "Parchment"}, "min": 4.5,
        "light": dict(bg="#EFE5CE", surface="#F8F1E0", surface2="#E7DABD", border="#D2BF99", rule="#B9A27A",
                      text="#2A2018", muted="#665443", ink="#1F1811", page="#F6EDD8", primary="#2E231A",
                      onprimary="#F8F1E0", dot="#9E2F1D", dotsoft="#F1DACB", second="#45602F",
                      secondsoft="#DDE5CB", card="#7E4B2E", oncard="#FFF6E6"),
        "dark": dict(bg="#15110C", surface="#1F1913", surface2="#2A2219", border="#40342A", rule="#5E4D3B",
                     text="#EEE4CF", muted="#B8A98F", ink="#F0E6D0", page="#1B160F", primary="#E9DCBD",
                     onprimary="#1E1711", dot="#E58A6E", dotsoft="#3D2219", second="#A7BC86", secondsoft="#26301C",
                     card="#C98A62", oncard="#1A120C"),
    },
    "madinah": {
        "name": {"ar": "المدينة", "en": "Madinah"}, "min": 4.5,
        "light": dict(bg="#EEE2C6", surface="#F8F0DC", surface2="#E5D5B2", border="#CDB98F", rule="#B09A6E",
                      text="#2B2416", muted="#62553C", ink="#211B10", page="#F6ECD3", primary="#2F4A2A",
                      onprimary="#F8F0DC", dot="#8B3A22", dotsoft="#EFD8C6", second="#3D6633",
                      secondsoft="#DCE6C9", card="#8A5A36", oncard="#FFF6E6"),
        "dark": dict(bg="#13140D", surface="#1C1D14", surface2="#26271B", border="#3C3D2C", rule="#585A40",
                     text="#ECE6CF", muted="#B4AD90", ink="#EFE9D2", page="#191A11", primary="#B9D3A1",
                     onprimary="#16220F", dot="#E59A7C", dotsoft="#3A2418", second="#A9C98E", secondsoft="#243020",
                     card="#C79566", oncard="#1A120B"),
    },
    "makkah": {
        "name": {"ar": "مكة", "en": "Makkah"}, "min": 4.5,
        "light": dict(bg="#F6F4EF", surface="#FFFFFF", surface2="#ECE9E2", border="#D6D1C7", rule="#A9A397",
                      text="#1A1918", muted="#57534D", ink="#121110", page="#FBFAF6", primary="#161514",
                      onprimary="#FBFAF6", dot="#7B4030", dotsoft="#F0DFD7", second="#3E4E57",
                      secondsoft="#E0E5E8", card="#24211F", oncard="#FBFAF6"),
        "dark": dict(bg="#0E0E0D", surface="#181716", surface2="#22211F", border="#36342F", rule="#55524B",
                     text="#F3F1EC", muted="#B5B0A6", ink="#F6F4EF", page="#141312", primary="#F3F1EC",
                     onprimary="#141312", dot="#E0A08C", dotsoft="#3A2620", second="#A9BAC4", secondsoft="#222A2F",
                     card="#E9E5DC", oncard="#151413"),
    },
    "quds": {
        "name": {"ar": "القدس", "en": "Al-Quds"}, "min": 4.5,
        "light": dict(bg="#F0EADB", surface="#FAF6EC", surface2="#E6DEC9", border="#D1C6A9", rule="#B3A684",
                      text="#24221B", muted="#5E5946", ink="#1C1A14", page="#F7F2E4", primary="#3B4722",
                      onprimary="#FAF6EC", dot="#7C5010", dotsoft="#F0E0C2", second="#4F6230",
                      secondsoft="#E1E6CF", card="#4B5A2A", oncard="#FAF6EC"),
        "dark": dict(bg="#12130E", surface="#1B1C15", surface2="#25261D", border="#3B3C2E", rule="#5A5B45",
                     text="#EEEADB", muted="#B5B096", ink="#F1EDDE", page="#181912", primary="#C9D59F",
                     onprimary="#1A2010", dot="#E2B061", dotsoft="#3A2E17", second="#B4C68A", secondsoft="#262E1A",
                     card="#B9C78A", oncard="#151A0C"),
    },
    "gardens": {
        "name": {"ar": "الجنّات", "en": "Gardens"}, "min": 4.5,
        "light": dict(bg="#F2F0E8", surface="#FBFAF5", surface2="#E7E5DB", border="#CFCEC4", rule="#A9ABA1",
                      text="#13241B", muted="#4C5A51", ink="#0F1C15", page="#F8F7F0", primary="#173A2A",
                      onprimary="#FBFAF5", dot="#7E5C10", dotsoft="#F1E5C6", second="#2E6B45",
                      secondsoft="#D9EADF", card="#1F4D36", oncard="#FBFAF5"),
        "dark": dict(bg="#0B1410", surface="#111D17", surface2="#18271F", border="#294033", rule="#3F5A4A",
                     text="#E9F0EA", muted="#A6B8AC", ink="#EEF3EE", page="#0F1A14", primary="#9FD4B3",
                     onprimary="#0B2116", dot="#E1BE6A", dotsoft="#352B14", second="#8ED0A6", secondsoft="#17301F",
                     card="#2F6B4B", oncard="#F4F8F4"),
    },
    "mountains": {
        "name": {"ar": "الجبال — تباين عالٍ", "en": "Mountains — high contrast"}, "min": 7.0,
        "light": dict(bg="#FFFFFF", surface="#FFFFFF", surface2="#F0F0F0", border="#767676", rule="#3D3D3D",
                      text="#000000", muted="#333333", ink="#000000", page="#FFFFFF", primary="#000000",
                      onprimary="#FFFFFF", dot="#8E0016", dotsoft="#FFFFFF", second="#000000",
                      secondsoft="#F0F0F0", card="#000000", oncard="#FFFFFF"),
        "dark": dict(bg="#000000", surface="#000000", surface2="#1A1A1A", border="#8A8A8A", rule="#C8C8C8",
                     text="#FFFFFF", muted="#D6D6D6", ink="#FFFFFF", page="#000000", primary="#FFFFFF",
                     onprimary="#000000", dot="#FF9C9C", dotsoft="#000000", second="#FFFFFF", secondsoft="#1A1A1A",
                     card="#FFFFFF", oncard="#000000"),
    },
}

PAIRS = [("text", "bg"), ("text", "surface"), ("text", "surface2"), ("muted", "bg"), ("muted", "surface"),
         ("muted", "surface2"), ("muted", "page"), ("ink", "page"), ("onprimary", "primary"), ("dot", "bg"),
         ("dot", "surface"), ("dot", "dotsoft"), ("dot", "page"), ("second", "surface"), ("second", "secondsoft"),
         ("oncard", "card")]


def luminance(hex_colour):
    c = [int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def check():
    """Returns (lowest ratio per direction and theme, list of failures)."""
    lowest, failures = {}, []
    for did, d in DIRECTIONS.items():
        for theme in ("light", "dark"):
            c = d[theme]
            worst = min((ratio(c[f], c[b]), f, b) for f, b in PAIRS)
            lowest[did + "/" + theme] = worst
            for f, b in PAIRS:
                r = ratio(c[f], c[b])
                if r < d["min"]:
                    failures.append("%s/%s %s on %s = %.2f (needs %.1f)" % (did, theme, f, b, r, d["min"]))
    return lowest, failures


def css():
    out = []
    for did, d in DIRECTIONS.items():
        for theme in ("light", "dark"):
            c = d[theme]
            props = ";".join("--%s:%s" % (k, v) for k, v in c.items())
            out.append('body[data-direction="%s"][data-theme="%s"]{%s}' % (did, theme, props))
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    low, bad = check()
    for k, (r, f, b) in low.items():
        print("%-18s lowest %.2f (%s on %s)" % (k, r, f, b))
    print("\n".join(bad) or "all pairs pass")
    sys.exit(1 if bad else 0)
