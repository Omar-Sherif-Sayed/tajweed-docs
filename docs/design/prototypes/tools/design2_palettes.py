"""The colour directions of design 2 ("early Islam"), with their contrast check.

One place for the values: build_round3.py writes them into round-3.html (CSS) and docs/design/tokens-design-2.json.
Why each colour was chosen: docs/design/design-2-meanings.md.

Roles (the same in every direction):
  bg, surface, surface2  page background and cards       text, muted   body text, secondary text
  border, rule           card edges, thin ink rules      ink, page     Quran text and the mushaf page
  primary, onprimary     main buttons                    dot, dotsoft  the small marks (active item, page number)
  second, secondsoft     prayer / qibla / adhkar, "verified"   card, oncard   the prayer card
Rule: every text / background pair below reaches 4.5 : 1 with normal colour vision. The direction marked
"accessible" (Mountains — the only direction made for readers with colour blindness or weak sight, the author's
decision of 2026-11-18) must reach 7 : 1, also as simulated for protanopia, deuteranopia and tritanopia.
"""

DIRECTIONS = {
    "parchment": {
        "name": {"ar": "الرَّقّ", "en": "Parchment"}, "min": 4.5,
        "light": dict(bg="#EFE5CE", surface="#F8F1E0", surface2="#E7DABD", border="#D2BF99", rule="#B9A27A",
                      text="#2A2018", muted="#665443", ink="#1F1811", page="#F6EDD8", primary="#2E231A",
                      onprimary="#F8F1E0", dot="#9E2F1D", dotsoft="#F1DACB", second="#45602F",
                      secondsoft="#DDE5CB", card="#7E4B2E", oncard="#FFF6E6"),
        "dark": dict(bg="#1A1611", surface="#231E17", surface2="#2D261D", border="#463B2E", rule="#625240",
                     text="#E8DFCC", muted="#B5A78D", ink="#ECE3D0", page="#201B14", primary="#E3D5B5",
                     onprimary="#1E1711", dot="#DC9078", dotsoft="#3E261D", second="#A9B98E", secondsoft="#29301F",
                     card="#5C3B26", oncard="#F2E6D2"),
    },
    "madinah": {
        "name": {"ar": "المدينة", "en": "Madinah"}, "min": 4.5,
        "light": dict(bg="#EEE2C6", surface="#F8F0DC", surface2="#E5D5B2", border="#CDB98F", rule="#B09A6E",
                      text="#2B2416", muted="#62553C", ink="#211B10", page="#F6ECD3", primary="#2F4A2A",
                      onprimary="#F8F0DC", dot="#8B3A22", dotsoft="#EFD8C6", second="#3D6633",
                      secondsoft="#DCE6C9", card="#8A5A36", oncard="#FFF6E6"),
        "dark": dict(bg="#171811", surface="#20211A", surface2="#2A2B22", border="#424434", rule="#5D5F49",
                     text="#E7E2CE", muted="#B2AC93", ink="#EBE6D2", page="#1D1E16", primary="#B5CDA0",
                     onprimary="#16220F", dot="#DC9F86", dotsoft="#3B2619", second="#A8C590", secondsoft="#263222",
                     card="#5E4128", oncard="#F3E8D3"),
    },
    "makkah": {
        "name": {"ar": "مكة", "en": "Makkah"}, "min": 4.5,
        "light": dict(bg="#F6F4EF", surface="#FFFFFF", surface2="#ECE9E2", border="#D6D1C7", rule="#A9A397",
                      text="#1A1918", muted="#57534D", ink="#121110", page="#FBFAF6", primary="#161514",
                      onprimary="#FBFAF6", dot="#7B4030", dotsoft="#F0DFD7", second="#3E4E57",
                      secondsoft="#E0E5E8", card="#24211F", oncard="#FBFAF6"),
        "dark": dict(bg="#191817", surface="#22211F", surface2="#2C2A28", border="#3E3B37", rule="#5A5650",
                     text="#E6E3DC", muted="#B0ABA2", ink="#EAE7E0", page="#1B1A18", primary="#E3DFD6",
                     onprimary="#161514", dot="#D8A393", dotsoft="#3A2722", second="#A6B5BE", secondsoft="#232B30",
                     card="#46413C", oncard="#F1EDE5"),
    },
    "quds": {
        "name": {"ar": "القدس", "en": "Al-Quds"}, "min": 4.5,
        "light": dict(bg="#F0EADB", surface="#FAF6EC", surface2="#E6DEC9", border="#D1C6A9", rule="#B3A684",
                      text="#24221B", muted="#5E5946", ink="#1C1A14", page="#F7F2E4", primary="#3B4722",
                      onprimary="#FAF6EC", dot="#7C5010", dotsoft="#F0E0C2", second="#4F6230",
                      secondsoft="#E1E6CF", card="#4B5A2A", oncard="#FAF6EC"),
        "dark": dict(bg="#16170F", surface="#1F2018", surface2="#292A20", border="#3F4132", rule="#5B5D48",
                     text="#E8E5D6", muted="#B1AD95", ink="#ECE9DA", page="#1C1D14", primary="#C6D19E",
                     onprimary="#1A2010", dot="#DAB074", dotsoft="#3A2E18", second="#B0C08C", secondsoft="#283019",
                     card="#4A562C", oncard="#F1EFE2"),
    },
    "gardens": {
        "name": {"ar": "الجنّات", "en": "Gardens"}, "min": 4.5,
        "light": dict(bg="#F2F0E8", surface="#FBFAF5", surface2="#E7E5DB", border="#CFCEC4", rule="#A9ABA1",
                      text="#13241B", muted="#4C5A51", ink="#0F1C15", page="#F8F7F0", primary="#173A2A",
                      onprimary="#FBFAF5", dot="#7E5C10", dotsoft="#F1E5C6", second="#2E6B45",
                      secondsoft="#D9EADF", card="#1F4D36", oncard="#FBFAF5"),
        "dark": dict(bg="#0F1813", surface="#16211B", surface2="#1E2B24", border="#2D4237", rule="#435C4E",
                     text="#E4ECE6", muted="#A3B5A9", ink="#E9F0EA", page="#131D17", primary="#9FCFB1",
                     onprimary="#0B2116", dot="#D9BF80", dotsoft="#352C16", second="#8ECBA4", secondsoft="#1A3122",
                     card="#2A5C42", oncard="#F1F6F2"),
    },
    "seas": {
        "name": {"ar": "البحران", "en": "Two seas"}, "min": 4.5,
        "light": dict(bg="#EEF2F0", surface="#FAFCFB", surface2="#E1E8E5", border="#C3CFCA", rule="#9DAEA7",
                      text="#132227", muted="#4A5B60", ink="#0E1A1E", page="#F6F9F7", primary="#0F4A5A",
                      onprimary="#FAFCFB", dot="#9C3628", dotsoft="#F6DDD6", second="#1D6470",
                      secondsoft="#D6E8EA", card="#174F5E", oncard="#F6F9F7"),
        "dark": dict(bg="#0E171B", surface="#152126", surface2="#1C2B31", border="#2A434D", rule="#405C66",
                     text="#E2ECED", muted="#A0B3B6", ink="#E8F1F1", page="#121C21", primary="#94CBD5",
                     onprimary="#072128", dot="#E2A698", dotsoft="#3A2622", second="#8BC2CA", secondsoft="#18313A",
                     card="#255F6B", oncard="#F1F7F7"),
    },
    "lamps": {
        "name": {"ar": "المصابيح", "en": "Lamps"}, "min": 4.5,
        "light": dict(bg="#ECEDF3", surface="#F8F8FB", surface2="#E1E3EC", border="#C6CAD9", rule="#9EA4BA",
                      text="#141A2E", muted="#4E5470", ink="#10152A", page="#F6F6F9", primary="#1F2A55",
                      onprimary="#F8F8FB", dot="#765708", dotsoft="#F1E6C6", second="#2F4C7A",
                      secondsoft="#DCE3F0", card="#1F2A55", oncard="#F4F1E6"),
        "dark": dict(bg="#13172C", surface="#1A1F37", surface2="#232843", border="#30375A", rule="#474F79",
                     text="#E6E5F0", muted="#AEB1C9", ink="#ECEBE2", page="#14182D", primary="#E5D4A2",
                     onprimary="#1A1606", dot="#E0C584", dotsoft="#332B15", second="#AABCE0", secondsoft="#1E2A47",
                     card="#353F78", oncard="#F2EFE2"),
    },
    "honey": {
        "name": {"ar": "النحل", "en": "Honey"}, "min": 4.5,
        "light": dict(bg="#F4EBD6", surface="#FBF6EA", surface2="#EBDDBC", border="#D7C293", rule="#B99E62",
                      text="#2A1E0C", muted="#66532F", ink="#21170A", page="#F9F1DE", primary="#5A3A0C",
                      onprimary="#FBF6EA", dot="#854808", dotsoft="#F3DDBE", second="#556218",
                      secondsoft="#E6EACB", card="#8A5208", oncard="#FFF8EA"),
        "dark": dict(bg="#1D170F", surface="#261F15", surface2="#30271B", border="#473A27", rule="#655238",
                     text="#EEE5D2", muted="#BBAA89", ink="#F1E8D6", page="#20190F", primary="#E0C48F",
                     onprimary="#231705", dot="#D9B47F", dotsoft="#3D2A10", second="#C2CB8C", secondsoft="#2C3018",
                     card="#6A4A1C", oncard="#F7EEDC"),
    },
    "mountains": {
        "name": {"ar": "الجبال — لضعف البصر وعمى الألوان", "en": "Mountains — for low vision and colour blindness"},
        "min": 7.0, "accessible": True,
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


# Colour vision deficiency: Machado, Oliveira & Fernandes, "A Physiologically-based Model for Simulation of Color
# Vision Deficiency", IEEE TVCG 15(6), 2009 — Table 1, severity 1.0 (read on the authors' page
# inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html, 2026-11-18). Applied to linear RGB.
CVD = {
    "protanopia": [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]],
    "deuteranopia": [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]],
    "tritanopia": [[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]],
}


def _lin(x):
    return x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4


def _enc(x):
    x = min(1.0, max(0.0, x))
    return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055


def simulate(hex_colour, kind):
    """The colour as a person with the given full colour-vision deficiency would see it."""
    rgb = [_lin(int(hex_colour[i:i + 2], 16) / 255) for i in (1, 3, 5)]
    m = CVD[kind]
    out = [_enc(sum(m[r][k] * rgb[k] for k in range(3))) for r in range(3)]
    return "#" + "".join("%02X" % round(v * 255) for v in out)


def lightness(hex_colour):
    """CIE L* (0 = black, 100 = white)."""
    y = luminance(hex_colour)
    return 116 * y ** (1 / 3) - 16 if y > 0.008856 else 903.3 * y


def saturation(hex_colour):
    r, g, b = [int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    hi, lo = max(r, g, b), min(r, g, b)
    if hi == lo:
        return 0.0
    l = (hi + lo) / 2
    return (hi - lo) / (2 - hi - lo) if l > 0.5 else (hi - lo) / (hi + lo)


# Night themes (author's request, 2026-11-18: make every night theme better; Mountains stays as it is).
DARK_RULES = [
    ("background is a deep tint, not black (L* 7 – 11)", lambda c: 7 <= lightness(c["bg"]) <= 11),
    ("cards are lighter than the background, step by step", lambda c: lightness(c["surface"]) - lightness(c["bg"]) >= 2.5
     and lightness(c["surface2"]) - lightness(c["surface"]) >= 2.5),
    ("the mushaf page is a little lighter than the background", lambda c: 0 < lightness(c["page"]) - lightness(c["bg"]) <= 4),
    ("body text is soft, not harsh (11 – 16 : 1)", lambda c: 11 <= ratio(c["text"], c["bg"]) <= 16),
    ("accents are calm (saturation at most 0.65)", lambda c: max(saturation(c[k]) for k in ("primary", "dot", "second")) <= 0.65),
    ("no bright block: the prayer card is mid-dark (L* 20 – 42)", lambda c: 20 <= lightness(c["card"]) <= 42),
]


def check_dark():
    """The night-theme rules, for every direction except the accessible one."""
    failures = []
    for did, d in DIRECTIONS.items():
        if d.get("accessible"):
            continue
        for text, rule in DARK_RULES:
            if not rule(d["dark"]):
                failures.append("%s/dark: %s" % (did, text))
    return failures


def check():
    """Returns (lowest ratio per direction and theme, list of failures).

    Every pair must pass with normal colour vision. The accessible direction (Mountains) must also pass as seen with
    protanopia, deuteranopia and tritanopia; the other directions are not made for colour-blind readers.
    """
    lowest, failures = {}, []
    for did, d in DIRECTIONS.items():
        for theme in ("light", "dark"):
            c = d[theme]
            worst = (99, "", "", "")
            for vision in ("normal",) + (tuple(CVD) if d.get("accessible") else ()):
                cc = c if vision == "normal" else {k: simulate(v, vision) for k, v in c.items()}
                for f, b in PAIRS:
                    r = ratio(cc[f], cc[b])
                    worst = min(worst, (r, f, b, vision))
                    if r < d["min"]:
                        failures.append("%s/%s %s on %s, %s = %.2f (needs %.1f)"
                                        % (did, theme, f, b, vision, r, d["min"]))
            lowest[did + "/" + theme] = worst
    return lowest, failures + check_dark()


def svg_filters():
    """SVG filters that let the prototype show every screen as a colour-blind reader would see it."""
    out = []
    for kind, m in CVD.items():
        values = " ".join("%s %s %s 0 0" % tuple(row) for row in m) + " 0 0 0 1 0"
        out.append('<filter id="cvd-%s" color-interpolation-filters="linearRGB"><feColorMatrix type="matrix" '
                   'values="%s"/></filter>' % (kind, values))
    return "\n".join(out) + "\n"


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
    for k, (r, f, b, vision) in low.items():
        print("%-18s lowest %.2f (%s on %s, %s)" % (k, r, f, b, vision))
    print("\n".join(bad) or "all pairs pass")
    sys.exit(1 if bad else 0)
