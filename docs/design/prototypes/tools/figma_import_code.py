"""Write the Figma Plugin API code that imports docs/design/elements/ into the Figma file «Tajweed — designs».

Each design has a page in Figma ("Design 1 (round 1)", ...). On it, one frame "Design N — elements" holds sections:
Logo, Icons, Drawings (design 2), Landscapes (design 3) and Colours (the swatches of every direction, day and night,
from the design's tokens). Every logo, icon and drawing is an editable vector made from its SVG file
(figma.createNodeFromSvg) — the SVG files in this repository stay the source.

The code is split into parts below the 50 000-character limit of the Figma tool; each part is written to
<out>/figma-<design>-<n>.js and pasted into the tool by the agent, in order.
Usage: python -I figma_import_code.py <out folder>
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DESIGN = os.path.join(HERE, "..", "..")
ELEMENTS = os.path.join(DESIGN, "elements")
LIMIT = 46000
PAGES = {1: "Design 1", 2: "Design 2", 3: "Design 3"}
ROLES = ["bg", "surface", "primary", "dot", "second", "text", "muted", "page", "ink", "sky", "far", "near", "glow"]

HEAD = r"""const page = figma.root.children.find(p => p.name.startsWith(%(page)s));
await figma.setCurrentPageAsync(page);
await figma.loadFontAsync({ family: "Inter", style: "Regular" });
await figma.loadFontAsync({ family: "Inter", style: "Bold" });
function text(s, size, bold) { const t = figma.createText(); t.fontName = { family: "Inter", style: bold ? "Bold" : "Regular" }; t.fontSize = size; t.characters = s; return t; }
function auto(f, dir) { f.layoutMode = dir; f.primaryAxisSizingMode = "AUTO"; f.counterAxisSizingMode = "AUTO"; f.fills = []; f.clipsContent = false; return f; }
let root = page.children.find(n => n.name === %(root)s);
if (!root) {
  root = auto(figma.createFrame(), "VERTICAL"); root.name = %(root)s; root.itemSpacing = 40;
  root.paddingTop = root.paddingBottom = root.paddingLeft = root.paddingRight = 48; root.cornerRadius = 24;
  root.fills = [{ type: "SOLID", color: { r: 0.96, g: 0.95, b: 0.93 } }];
  root.appendChild(text(%(root)s, 40, true));
  root.appendChild(text(%(note)s, 16, false));
  page.appendChild(root); root.x = 0; root.y = 0;
}
function section(title) {
  let s = root.children.find(n => n.name === title);
  if (!s) {
    s = auto(figma.createFrame(), "VERTICAL"); s.name = title; s.itemSpacing = 16; root.appendChild(s);
    s.appendChild(text(title, 26, true));
    const g = figma.createFrame(); g.name = "items"; g.layoutMode = "HORIZONTAL"; g.layoutWrap = "WRAP";
    g.itemSpacing = 28; g.counterAxisSpacing = 28; g.primaryAxisSizingMode = "FIXED"; g.counterAxisSizingMode = "AUTO";
    g.resize(1600, 10); g.counterAxisSizingMode = "AUTO"; g.clipsContent = false; g.fills = []; s.appendChild(g);
  }
  return s.children.find(n => n.name === "items");
}
function add(title, name, svg, scale) {
  const cell = auto(figma.createFrame(), "VERTICAL"); cell.name = name; cell.itemSpacing = 8; cell.counterAxisAlignItems = "CENTER";
  const v = figma.createNodeFromSvg(svg); v.name = name; if (scale !== 1) v.rescale(scale);
  cell.appendChild(v); cell.appendChild(text(name, 12, false)); section(title).appendChild(cell);
}
function swatches(title, rows) {
  rows.forEach(r => {
    const row = auto(figma.createFrame(), "VERTICAL"); row.name = r[0]; row.itemSpacing = 6;
    row.appendChild(text(r[0], 13, true));
    const line = auto(figma.createFrame(), "HORIZONTAL"); line.itemSpacing = 6; row.appendChild(line);
    r[1].forEach(c => {
      const sw = figma.createRectangle(); sw.name = c[0] + " " + c[1]; sw.resize(44, 44); sw.cornerRadius = 8;
      const h = c[1].replace("#", ""); sw.fills = [{ type: "SOLID", color: { r: parseInt(h.slice(0, 2), 16) / 255, g: parseInt(h.slice(2, 4), 16) / 255, b: parseInt(h.slice(4, 6), 16) / 255 } }];
      sw.strokes = [{ type: "SOLID", color: { r: 0.6, g: 0.6, b: 0.6 } }]; sw.strokeWeight = 0.5; line.appendChild(sw);
    });
    section(title).appendChild(row);
  });
}
"""

NOTE = ("Editable vectors made from docs/design/elements/design-%d/ in the tajweed-docs repository (the SVG files are "
        "the source). The full screens are the HTML prototype docs/design/prototypes/round-%d.html.")


def palettes(n):
    if n == 1:
        t = json.load(io.open(os.path.join(DESIGN, "tokens.json"), encoding="utf-8"))
        dirs = t.get("directions") or t
        out = []
        for k, d in dirs.items():
            if not isinstance(d, dict) or "light" not in d:
                continue
            for theme in ("light", "dark"):
                cols = d[theme]
                out.append(["%s · %s" % (d.get("name", k) if isinstance(d.get("name"), str) else k.upper(), theme),
                            [[r, v] for r, v in cols.items() if isinstance(v, str) and v.startswith("#") and len(v) == 7]])
        return out
    t = json.load(io.open(os.path.join(DESIGN, "tokens-design-%d.json" % n), encoding="utf-8"))["directions"]
    out = []
    for k, d in t.items():
        for theme, label in (("light", "day"), ("dark", "night")):
            out.append(["%s · %s" % (d["name"]["en"], label), [[r, d[theme][r]] for r in ROLES if r in d[theme]]])
    return out


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    manifest = json.load(io.open(os.path.join(ELEMENTS, "manifest.json"), encoding="utf-8"))
    for n, page in PAGES.items():
        head = HEAD % {"page": json.dumps(page), "root": json.dumps("Design %d — elements" % n),
                       "note": json.dumps(NOTE % (n, n))}
        calls = []
        for m in manifest:
            parts = m["file"].split("/")
            if parts[0] != "design-%d" % n:
                continue
            svg = io.open(os.path.join(ELEMENTS, m["file"]), encoding="utf-8").read().strip()
            name = parts[-1][:-4]
            if len(parts) == 2:
                title, scale = ("Logo", 1) if name == "logo" else ("Drawings", 1)
            elif parts[1] == "icons":
                title, scale = "Icons", 2
            else:
                title, scale = "Landscapes", 0.6
            calls.append("add(%s, %s, %s, %s);" % (json.dumps(title), json.dumps(name), json.dumps(svg), scale))
        order = {"Logo": 0, "Drawings": 1, "Landscapes": 2, "Icons": 3}
        calls.sort(key=lambda c: order[json.loads(c[4:c.index(",")])])
        calls.append("swatches(\"Colours\", %s);" % json.dumps(palettes(n)))
        chunks, cur = [], []
        for c in calls:
            if cur and len(head) + sum(len(x) + 1 for x in cur) + len(c) > LIMIT:
                chunks.append(cur)
                cur = []
            cur.append(c)
        chunks.append(cur)
        for i, ch in enumerate(chunks, 1):
            code = head + "\n".join(ch) + "\nreturn root.id;\n"
            with io.open(os.path.join(out, "figma-%d-%d.js" % (n, i)), "w", encoding="utf-8", newline="\n") as f:
                f.write(code)
            print("figma-%d-%d.js  %d chars" % (n, i, len(code)))


if __name__ == "__main__":
    main()
