"""The colour directions of design 3 (round 3, "the first era": the time of the Prophet ﷺ, the Companions and the
Rightly Guided Caliphs), with their checks.

Same roles and rules as design 2 (design2_palettes.py): every text / background pair 4.5 : 1 with normal colour
vision; the night themes follow the six night rules; the last direction, Mountains, is the only one made for low
vision and colour blindness (7 : 1, also as simulated for the three kinds of colour blindness — the author's
decision of 2026-11-18, repeated for design 3 on 2026-11-19).
Extra roles for the landscape drawn in each direction (decoration, no text on them): sky, far, near, glow.
Why each colour was chosen: docs/design/design-3-meanings.md.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import design2_palettes as P2  # noqa: E402  (our own script beside this one)


def d(**kw):
    return kw


DIRECTIONS = {
    "suhuf": {
        "name": {"ar": "الصُّحُف", "en": "The first sheets"}, "min": 4.5,
        "light": d(bg="#F3F0E8", surface="#FBFAF6", surface2="#E9E4D8", border="#D6CDBB", rule="#B5A88E", text="#26211A",
                   muted="#5E5546", ink="#1D1913", page="#F8F6F0", primary="#3A3024", onprimary="#FBFAF6", dot="#8C5A2B",
                   dotsoft="#F1E3D0", second="#5B6B3E", secondsoft="#E2E7D3", card="#6E5A3E", oncard="#FBF7EE",
                   sky="#E8E1D2", far="#CFC2A8", near="#B39E7C", glow="#F7EBD0"),
        "dark": d(bg="#1A1814", surface="#232019", surface2="#2D2920", border="#45403A", rule="#615848", text="#E9E3D6",
                  muted="#B3A994", ink="#EDE7DA", page="#1F1C17", primary="#E3D8C2", onprimary="#1D1913", dot="#D5A574",
                  dotsoft="#3A2A1A", second="#AEBB92", secondsoft="#2A3020", card="#4E4232", oncard="#F1EBDD",
                  sky="#24211B", far="#3A342A", near="#4B4335", glow="#6A5A3E"),
    },
    "hira": {
        "name": {"ar": "حِراء", "en": "Hira"}, "min": 4.5,
        "light": d(bg="#EEECE8", surface="#FAF9F7", surface2="#E3E0DA", border="#CCC7BE", rule="#A49D90", text="#1F1D1A",
                   muted="#57524A", ink="#181613", page="#F6F5F2", primary="#2B2722", onprimary="#FAF9F7", dot="#785A13",
                   dotsoft="#F2E7C9", second="#4C5A4F", secondsoft="#DFE5E0", card="#3A3530", oncard="#F7F2E6",
                   sky="#F3E3C0", far="#7A7268", near="#4A443D", glow="#F6D88A"),
        "dark": d(bg="#191816", surface="#22201E", surface2="#2C2926", border="#423E39", rule="#5D5750", text="#E8E4DC",
                  muted="#B0A99D", ink="#ECE7DE", page="#1E1C1A", primary="#E6D3A3", onprimary="#201A0C", dot="#DDBE78",
                  dotsoft="#3A3018", second="#A9B8AC", secondsoft="#263028", card="#46403A", oncard="#F3EDE1",
                  sky="#1E1C22", far="#2E2B28", near="#3B3733", glow="#C9A458"),
    },
    "ghar": {
        "name": {"ar": "الغار", "en": "The Cave"}, "min": 4.5,
        "light": d(bg="#F1ECE2", surface="#FBF8F2", surface2="#E7DFD0", border="#D2C6AF", rule="#B0A184", text="#22201C",
                   muted="#5D5547", ink="#1B1915", page="#F7F3EA", primary="#24304A", onprimary="#FBF8F2", dot="#7E5229",
                   dotsoft="#F0DFCC", second="#4A5E73", secondsoft="#DDE4EB", card="#2C3A57", oncard="#F4F1EA",
                   sky="#DCE3EC", far="#C9B79A", near="#A88F6B", glow="#F3E6C8"),
        "dark": d(bg="#13171F", surface="#1A1F29", surface2="#222833", border="#353C4A", rule="#4C5566", text="#E5E7EC",
                  muted="#A9AFBC", ink="#ECEDF0", page="#171B24", primary="#D9C9A5", onprimary="#1A1408", dot="#D9A877",
                  dotsoft="#352718", second="#A3B6CC", secondsoft="#1D2836", card="#2E3A55", oncard="#EEF0F5",
                  sky="#141A2A", far="#2A2C33", near="#3A3631", glow="#C7B48A"),
    },
    "taybah": {
        "name": {"ar": "طابة", "en": "Taybah"}, "min": 4.5,
        "light": d(bg="#EFEDE2", surface="#FAF9F2", surface2="#E4E2D3", border="#CDC9B3", rule="#A8A388", text="#1F241A",
                   muted="#535A45", ink="#181D13", page="#F7F6EE", primary="#2F4D2B", onprimary="#FAF9F2", dot="#874422",
                   dotsoft="#F1DCCE", second="#3F6A38", secondsoft="#DDE8D6", card="#7A5232", oncard="#FDF7EC",
                   sky="#E5EDE4", far="#9DB08A", near="#5E7A4D", glow="#F2E4BD"),
        "dark": d(bg="#151A11", surface="#1D2318", surface2="#262C20", border="#3A4230", rule="#556047", text="#E6EADF",
                  muted="#AEB7A2", ink="#EBEEE5", page="#191F15", primary="#B4D2A0", onprimary="#142010", dot="#DFA081",
                  dotsoft="#3A2418", second="#A6C796", secondsoft="#233021", card="#5C4128", oncard="#F4EBDD",
                  sky="#161C17", far="#24301F", near="#2F3D27", glow="#8C7A4E"),
    },
    "uhud": {
        "name": {"ar": "أُحُد", "en": "Uhud"}, "min": 4.5,
        "light": d(bg="#F2ECE8", surface="#FBF8F6", surface2="#E8DED8", border="#D4C4BB", rule="#B39B8E", text="#241C19",
                   muted="#5E4E47", ink="#1C1512", page="#F8F3F0", primary="#6B2E22", onprimary="#FBF8F6", dot="#8E3B26",
                   dotsoft="#F4DDD5", second="#4F6170", secondsoft="#DFE5EA", card="#7A3A2A", oncard="#FCF4EF",
                   sky="#E4ECF2", far="#C79A86", near="#9A5B45", glow="#F3D9C3"),
        "dark": d(bg="#1C1615", surface="#251D1B", surface2="#2F2522", border="#463733", rule="#634E47", text="#EEE4E0",
                  muted="#BCA9A2", ink="#F1E8E4", page="#211A18", primary="#E6B6A5", onprimary="#2A0F09", dot="#E39A84",
                  dotsoft="#3E221B", second="#A9B9C6", secondsoft="#222C34", card="#5B2D23", oncard="#F7ECE8",
                  sky="#1A1820", far="#3A2622", near="#4E2F27", glow="#A55E45"),
    },
    "ibil": {
        "name": {"ar": "أفلا ينظرون", "en": "Look at the camels"}, "min": 4.5,
        "light": d(bg="#F2EEE6", surface="#FBF9F4", surface2="#E8E1D5", border="#D3C8B5", rule="#B1A389", text="#23201B",
                   muted="#5B5446", ink="#1B1814", page="#F8F5EF", primary="#2E4A63", onprimary="#FBF9F4", dot="#8B5A2B",
                   dotsoft="#F1E1CD", second="#5C6470", secondsoft="#E2E5E9", card="#80592E", oncard="#FDF8EF",
                   sky="#D7E6F2", far="#9AA3AE", near="#C8A574", glow="#F5E9CF"),
        "dark": d(bg="#14181D", surface="#1C2127", surface2="#252B32", border="#384049", rule="#4F5A66", text="#E6E9EC",
                  muted="#ABB3BC", ink="#ECEEF0", page="#181D22", primary="#A9C8E3", onprimary="#0D1C2A", dot="#DCAA77",
                  dotsoft="#352717", second="#B5BDC7", secondsoft="#222930", card="#5E4628", oncard="#F6EEE2",
                  sky="#141B26", far="#2C333C", near="#4A3B28", glow="#8A7550"),
    },
    "fajr": {
        "name": {"ar": "الفجر", "en": "Dawn"}, "min": 4.5,
        "light": d(bg="#F4EFF0", surface="#FCFAFA", surface2="#EAE2E4", border="#D6CACD", rule="#B3A2A7", text="#221D22",
                   muted="#5A5059", ink="#1A161A", page="#F9F5F6", primary="#3B3560", onprimary="#FCFAFA", dot="#93445A",
                   dotsoft="#F4DCE2", second="#5A5E86", secondsoft="#E3E3EE", card="#45406E", oncard="#F8F4F6",
                   sky="#F0D8D6", far="#B9A6C2", near="#6E6890", glow="#F7CFB4"),
        "dark": d(bg="#191823", surface="#21202D", surface2="#2A2837", border="#3B384C", rule="#534F67", text="#E9E6EE",
                  muted="#B1ACBE", ink="#EEEBF1", page="#191824", primary="#D8C7E6", onprimary="#1C1428", dot="#E5A0B2",
                  dotsoft="#3B2129", second="#B3B5DA", secondsoft="#24253A", card="#3C3760", oncard="#F2EFF7",
                  sky="#1A1830", far="#2C2840", near="#3A3452", glow="#B7798B"),
    },
    "duha": {
        "name": {"ar": "الضحى", "en": "Forenoon"}, "min": 4.5,
        "light": d(bg="#F7F2E4", surface="#FFFCF4", surface2="#EFE7D2", border="#DCCFAE", rule="#BBA97F", text="#25200F",
                   muted="#5F5536", ink="#1D190B", page="#FCF8EC", primary="#5C4410", onprimary="#FFFCF4", dot="#8A5B06",
                   dotsoft="#F6E6BF", second="#3E6380", secondsoft="#DCE7F0", card="#7E570E", oncard="#FFFCF4",
                   sky="#F9E9B8", far="#E6CF92", near="#CFAE62", glow="#FFE6A0"),
        "dark": d(bg="#161922", surface="#1D212B", surface2="#262B36", border="#343A48", rule="#4A5262", text="#E4E7ED",
                  muted="#A8AEBA", ink="#EAECF1", page="#161A23", primary="#C7D2E8", onprimary="#121A2A", dot="#D6C08A",
                  dotsoft="#332D1A", second="#9FB3CF", secondsoft="#1D2738", card="#2E3850", oncard="#EEF1F7",
                  sky="#121826", far="#1E2533", near="#283041", glow="#6F7DA0"),
    },
    "ghaith": {
        "name": {"ar": "الغيث", "en": "Rain"}, "min": 4.5,
        "light": d(bg="#EEF1EF", surface="#FAFBFA", surface2="#E2E7E4", border="#C8D0CB", rule="#A0ACA5", text="#1C2320",
                   muted="#4F5A54", ink="#151B18", page="#F6F8F7", primary="#2F4B5B", onprimary="#FAFBFA", dot="#2E6A3A",
                   dotsoft="#DCEBDF", second="#3D5F73", secondsoft="#DCE6EC", card="#3E5C6C", oncard="#F4F8F9",
                   sky="#D9E3E8", far="#A7B7BF", near="#6E9A6A", glow="#E5F0E2"),
        "dark": d(bg="#12181C", surface="#192228", surface2="#212B32", border="#314049", rule="#475A65", text="#E3EAEE",
                  muted="#A6B4BC", ink="#E9EFF2", page="#161D22", primary="#A9C9DB", onprimary="#0E1D27", dot="#8FCB99",
                  dotsoft="#1C3022", second="#9EBACB", secondsoft="#1C2A34", card="#2D4552", oncard="#EEF4F7",
                  sky="#142029", far="#233139", near="#2A3F2D", glow="#5E7F6A"),
    },
    "jannatan": {
        "name": {"ar": "الجنّتان", "en": "The two gardens"}, "min": 4.5,
        "light": d(bg="#EFF1EB", surface="#FAFBF7", surface2="#E3E7DC", border="#C9D0BF", rule="#A3AD98", text="#17221A",
                   muted="#4A5649", ink="#111A13", page="#F7F8F3", primary="#14402C", onprimary="#FAFBF7", dot="#9A2B39",
                   dotsoft="#F4D9DD", second="#2F6B44", secondsoft="#D9EADF", card="#1E5236", oncard="#F6FAF6",
                   sky="#E4EDE2", far="#6E9A70", near="#2D5E40", glow="#F0D9DC"),
        "dark": d(bg="#101913", surface="#16221B", surface2="#1E2C23", border="#2C4334", rule="#3E5B48", text="#E3EDE6",
                  muted="#A4B8AA", ink="#E9F1EB", page="#141F18", primary="#9CCFB0", onprimary="#0A2116", dot="#E59AA5",
                  dotsoft="#3A1E23", second="#8FCCA4", secondsoft="#17301F", card="#245A3F", oncard="#F0F7F2",
                  sky="#0F1A14", far="#1C3426", near="#234030", glow="#7E3A45"),
    },
    "nur": {
        "name": {"ar": "النور", "en": "Light"}, "min": 4.5,
        "light": d(bg="#F5F3EC", surface="#FDFCF8", surface2="#EBE7DC", border="#D7D0BF", rule="#B4AA94", text="#222019",
                   muted="#59544A", ink="#1A1813", page="#FAF8F2", primary="#4A3A12", onprimary="#FDFCF8", dot="#86610E",
                   dotsoft="#F4E7C3", second="#4B6175", secondsoft="#DFE7EE", card="#5A4718", oncard="#FBF6E8",
                   sky="#F3ECD6", far="#E2D3A8", near="#C9AE6A", glow="#FFF1C4"),
        "dark": d(bg="#181712", surface="#201F19", surface2="#2A2820", border="#3E3C33", rule="#565246", text="#EDEAE0",
                  muted="#B4AE9F", ink="#F1EEE4", page="#1D1C16", primary="#E4D3A6", onprimary="#221A06", dot="#DCC58E",
                  dotsoft="#3A3016", second="#ABC0D2", secondsoft="#222C35", card="#4E4220", oncard="#F7F1E1",
                  sky="#17160F", far="#2A271C", near="#3A3420", glow="#C9A24A"),
    },
    "mountains": {
        "name": P2.DIRECTIONS["mountains"]["name"], "min": 7.0, "accessible": True,
        "light": dict(P2.DIRECTIONS["mountains"]["light"], sky="#FFFFFF", far="#9A9A9A", near="#000000", glow="#FFFFFF"),
        "dark": dict(P2.DIRECTIONS["mountains"]["dark"], sky="#000000", far="#6A6A6A", near="#FFFFFF", glow="#000000"),
    },
}


def check():
    """The checks of design 2, run on these directions."""
    keep = P2.DIRECTIONS
    P2.DIRECTIONS = DIRECTIONS
    try:
        return P2.check()
    finally:
        P2.DIRECTIONS = keep


def css():
    keep = P2.DIRECTIONS
    P2.DIRECTIONS = DIRECTIONS
    try:
        return P2.css()
    finally:
        P2.DIRECTIONS = keep


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    low, bad = check()
    for k, (r, f, b, vision) in low.items():
        print("%-18s lowest %.2f (%s on %s, %s)" % (k, r, f, b, vision))
    print("\n".join(bad) or "all pairs pass")
    sys.exit(1 if bad else 0)
