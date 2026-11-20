"""Export the design elements of the three designs as standalone SVG files (the author, 2026-11-19: the logo and every
drawing used in the designs kept in Figma and in this repository, to be used at any time).

Writes docs/design/elements/design-<N>/:
  logo.svg                 the logo, in the colours of the design's first direction (day)
  icons/<name>.svg         every icon of the page (its <symbol>), 24 x 24, stroke in the design's primary colour
  design 2: colonnade.svg  the palm-trunk colonnade of the home screen
  design 3: landscapes/<direction>-<day|night>.svg   the landscape of each of the twelve directions
and elements/manifest.json (every file with its size), read when the elements are imported into Figma.

Nothing is redrawn by hand: icons are copied from the pages, the logos and the colonnade follow the pages' own
drawing code (the same numbers), and the landscapes are drawn by the page's own scene() function, run with Node.
Usage: python -I export_elements.py
"""
import io
import json
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROTO = os.path.join(HERE, "..")
DESIGN = os.path.join(PROTO, "..")
OUT = os.path.join(DESIGN, "elements")
NS = "xmlns='http://www.w3.org/2000/svg'"

D1 = {"primary": "#0F5B45", "frame": "#B8893A", "text": "#1E2A26"}           # design 1, direction A, light
T2 = json.load(io.open(os.path.join(DESIGN, "tokens-design-2.json"), encoding="utf-8"))["directions"]
T3 = json.load(io.open(os.path.join(DESIGN, "tokens-design-3.json"), encoding="utf-8"))["directions"]
P2, P3 = T2["parchment"]["light"], T3["suhuf"]["light"]
FILLED = {"i-play", "i-pause", "i-skipn", "i-skipp"}   # drawn filled in design 1 (class "ic fill")


def write(rel, svg, manifest):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(svg + "\n")
    manifest.append({"file": rel.replace(os.sep, "/"), "bytes": len(svg.encode("utf-8"))})


def symbols(page):
    html = io.open(os.path.join(PROTO, page), encoding="utf-8").read()
    return re.findall(r'<symbol id="([\w-]+)" viewBox="([\d .-]+)">(.*?)</symbol>', html, re.S)


def icon_svg(sid, box, inner, colour, width, fill_colour):
    filled = sid in FILLED
    inner = inner.replace('fill="currentColor"', 'fill="%s"' % colour).replace("currentColor", colour)
    attrs = ("fill='%s' stroke='none'" % colour) if filled else \
        ("fill='none' stroke='%s' stroke-width='%s' stroke-linecap='round' stroke-linejoin='round'" % (colour, width))
    inner = inner.replace('class="g"', 'stroke="%s"' % fill_colour)
    size = box.split()[2:]
    return "<svg %s viewBox='%s' width='%s' height='%s' %s>%s</svg>" % (NS, box, size[0], size[1], attrs, inner)


def coin(text, dot, rule, kind="brand"):
    """Design 2's medallion, as coinSVG() in round-2.html, with the three dots of its centre."""
    out = ["<circle cx='50' cy='50' r='48.5' fill='none' stroke='%s' stroke-width='1.1'/>" % text,
           "<circle cx='50' cy='50' r='45' fill='none' stroke='%s' stroke-width='0.6'/>" % text]
    n, rr = (60, 41.5) if kind == "dial" else (36, 40.5)
    for i in range(n):
        a = i / n * 2 * math.pi - math.pi / 2
        col = rule if kind == "dial" and i >= round(n * 0.62) else dot
        out.append("<circle cx='%.2f' cy='%.2f' r='%s' fill='%s'/>" % (50 + rr * math.cos(a), 50 + rr * math.sin(a),
                                                                       1.05 if kind == "dial" else 1.45, col))
    out.append("<circle cx='50' cy='50' r='37' fill='none' stroke='%s' stroke-width='0.6'/>" % text)
    if kind == "brand":   # i-dots (viewBox 0 0 22 12) drawn 18 x 10 in the centre
        for cx, cy in [(7, 9), (15, 9), (11, 3)]:
            out.append("<circle cx='%.2f' cy='%.2f' r='%.2f' fill='%s'/>" % (41 + cx * 18 / 22, 45 + cy * 10 / 12, 1.9 * 18 / 22, dot))
    return "<svg %s viewBox='0 0 100 100' width='200' height='200'>%s</svg>" % (NS, "".join(out))


def colonnade(colour):
    """Design 2's colonnade, as drawColonnade() in round-2.html."""
    out = ["<path d='M0 9H344M0 12.5H344' stroke='%s' stroke-width='1' fill='none'/>" % colour]
    out += ["<path d='M%d 2 L%d 9' stroke='%s' stroke-width='.8'/>" % (x, x + 4, colour) for x in range(0, 345, 6)]
    for cx in range(14, 344, 36):
        out.append("<rect x='%d' y='12.5' width='6' height='45.5' rx='1.5' fill='none' stroke='%s' stroke-width='1'/>" % (cx - 3, colour))
        out += ["<path d='M%d %dh6' stroke='%s' stroke-width='.6'/>" % (cx - 3, y, colour) for y in range(18, 56, 6)]
    return "<svg %s viewBox='0 0 344 58' width='688' height='116'>%s</svg>" % (NS, "".join(out))


def logo3(text, dot):
    """Design 3's logo, as logoSVG() in round-3.html: an arc of light over the horizon."""
    rays = ""
    for a in (-60, -30, 0, 30, 60):
        r = (a - 90) * math.pi / 180
        rays += "<path d='M%.1f %.1f L%.1f %.1f' stroke='%s' stroke-width='3' stroke-linecap='round'/>" % (
            50 + math.cos(r) * 25, 62 + math.sin(r) * 25, 50 + math.cos(r) * 33, 62 + math.sin(r) * 33, dot)
    return ("<svg %s viewBox='0 0 100 100' width='200' height='200'><circle cx='50' cy='50' r='47' fill='none' stroke='%s' stroke-width='1.6'/>"
            "<path d='M31 62 A19 19 0 0 1 69 62 Z' fill='%s'/>%s<path d='M20 63 H80' stroke='%s' stroke-width='2.4' stroke-linecap='round'/>"
            "<path d='M30 72 H70 M38 80 H62' stroke='%s' stroke-width='1.4' stroke-linecap='round' opacity='.55'/></svg>") % (NS, text, dot, rays, text, text)


def landscapes():
    """Run the page's own scene() (round-3.html) with Node for every direction, day and night."""
    html = io.open(os.path.join(PROTO, "round-3.html"), encoding="utf-8").read()
    code = html[html.index("  var SC = 0;"):html.index("  function pal()")]
    job = {k: {"light": d["light"], "dark": d["dark"]} for k, d in T3.items()}
    js = code + "\nvar job = " + json.dumps(job) + ", out = {};\n" + \
        "Object.keys(job).forEach(function (k) { out[k + '-day'] = scene(k, job[k].light, false); out[k + '-night'] = scene(k, job[k].dark, true); });\n" + \
        "process.stdout.write(JSON.stringify(out));\n"
    res = subprocess.run(["node", "-"], input=js, capture_output=True, text=True, encoding="utf-8", check=True)   # stdin: the script is long
    return json.loads(res.stdout)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    manifest = []
    # design 1
    for sid, box, inner in symbols("round-1.html"):
        if sid == "i-star":
            write("design-1/logo.svg", icon_svg(sid, box, inner, D1["primary"], 1.7, D1["frame"]).replace("width='100' height='100'", "width='200' height='200'"), manifest)
        else:
            write("design-1/icons/%s.svg" % sid[2:], icon_svg(sid, box, inner, D1["primary"], 1.7, D1["frame"]), manifest)
    # design 2
    for sid, box, inner in symbols("round-2.html"):
        write("design-2/icons/%s.svg" % sid[2:], icon_svg(sid, box, inner, P2["primary"], 1.6, P2["dot"]), manifest)
    write("design-2/logo.svg", coin(P2["text"], P2["dot"], P2["rule"]), manifest)
    write("design-2/prayer-dial.svg", coin(P2["text"], P2["dot"], P2["rule"], "dial"), manifest)
    write("design-2/colonnade.svg", colonnade(P2["rule"]), manifest)
    # design 3
    for sid, box, inner in symbols("round-3.html"):
        write("design-3/icons/%s.svg" % sid[2:], icon_svg(sid, box, inner, P3["primary"], 1.6, P3["dot"]), manifest)
    write("design-3/logo.svg", logo3(P3["text"], P3["dot"]), manifest)
    for name, svg in landscapes().items():
        svg = svg.replace("<svg ", "<svg %s width='720' height='240' " % NS, 1).replace(" aria-hidden='true'", "")
        write("design-3/landscapes/%s.svg" % name, svg, manifest)
    for m in manifest:
        if re.search(r"var\(--|currentColor", io.open(os.path.join(OUT, m["file"]), encoding="utf-8").read()):
            raise SystemExit("unresolved colour in " + m["file"])
    with io.open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, indent=1)
        f.write("\n")
    print("elements: %d SVG files written to docs/design/elements/" % len(manifest))


if __name__ == "__main__":
    main()
