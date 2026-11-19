"""Write the Lives screens (F20 prophets, F21 Companions, F22 Rightly Guided Caliphs) into the three designs.

The author (2026-11-19) asked to see the three new sections in the rounds. They are the same screens in every design —
a group «السِّيَر» on the home screen, a Lives screen with three tabs (an index of prophets, the groups of Companions,
a timeline of the four caliphates) and one sample entry — drawn with each design's own colours, so they are written
once, here, into round-1.html, round-2.html and round-3.html between marker comments.

What is real and what is a placeholder (AGENTS.md §6.10, §8.11):
  - The ayah of the sample entry (71:1) is copied whole from the Tanzil file (checksum checked) and checked to contain
    the prophet's name; it is shown as a design sample, since the ayahs of each prophet will come from a named index.
  - Names: only names that are beyond doubt — Adam, Nuh, Ibrahim, Musa, Isa and Muhammad ﷺ (each named in the Quran;
    the order of these six in time is stated by the Quran itself), the four caliphs in the order of their caliphates,
    and two of the Mothers of the Believers. The full lists, their order, every story, hadith, date and event come
    from the source books (P9-D1 … D4) and are shown here as dashed placeholders that say so.
  - No picture of any prophet or Companion, no cross shape; honorifics always written in Arabic.
Interface texts: i18n/lives/ (checked by i18n_check.py).

Usage: python -I build_lives.py   (after build_round1.py, build_round2.py and build_round3.py)
"""
import io
import json
import os
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_round1 as R1  # noqa: E402  (our own scripts beside this one)
import i18n_check as I  # noqa: E402
import verify_mushaf_layout as V  # noqa: E402

PAGES = {"round-1.html": "phone screen", "round-2.html": "phone parch screen", "round-3.html": "phone parch screen"}
VERSE, WORD = (71, 1), "نوحا"   # the sample entry: Nuh; the ayah must contain his name

PROPHETS = [("آدم", "Adam"), ("نوح", "Nuh"), ("إبراهيم", "Ibrahim"), ("موسى", "Musa"), ("عيسى", "Isa")]
LAST = ("محمد", "Muhammad")
CALIPHS = [("أبو بكر الصديق", "Abu Bakr al-Siddiq"), ("عمر بن الخطاب", "Umar ibn al-Khattab"),
           ("عثمان بن عفان", "Uthman ibn Affan"), ("علي بن أبي طالب", "Ali ibn Abi Talib")]
MOTHERS = [("خديجة بنت خويلد", "Khadijah bint Khuwaylid"), ("عائشة بنت أبي بكر", "Aishah bint Abi Bakr")]

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <!-- Lives icons (no person, no cross shape): a line of descent (3:34 «ذرية بعضها من بعض»), a palm of Madinah, the steps of a minbar -->
  <symbol id="i-lv-prophets" viewBox="0 0 24 24"><circle cx="12" cy="4.5" r="2"/><circle cx="12" cy="11.5" r="2"/><circle cx="6.5" cy="19" r="2"/><circle cx="17.5" cy="19" r="2"/><path d="M12 6.5v3M10.8 13.1 7.7 17.3M13.2 13.1l3.1 4.2"/></symbol>
  <symbol id="i-lv-companions" viewBox="0 0 24 24"><path d="M12 21v-9"/><path d="M12 12c-1.5-3-4.5-4-7.5-3.5M12 12c1.5-3 4.5-4 7.5-3.5M12 12c-.5-3.5-2.5-6-5-7M12 12c.5-3.5 2.5-6 5-7"/><path d="M8 21h8"/></symbol>
  <symbol id="i-lv-caliphs" viewBox="0 0 24 24"><path d="M4 20.5h16"/><path d="M6 20.5V17h3v-3h3v-3h3V8h3v12.5"/><path d="M6 14 15 5.5"/></symbol>
</svg>"""

CSS = """/* the home group: one compact row, so that the home screen keeps its height */
.body:has(>.lv-home){gap:6px}
.body:has(>.lv-home)>.scene-home{height:116px}   /* design 3: the landscape gives the Lives group its room */
.lv-home{border:1px solid var(--border);border-radius:14px;padding:5px 8px;display:grid;grid-template-columns:auto 1fr;align-items:center;gap:8px;background:var(--surface)}
.lv-home .lv-h{font-size:12.5px;font-weight:700;color:var(--muted);padding-inline:2px 4px;border-inline-end:1px solid var(--border)}
.lv-row{display:grid;grid-template-columns:repeat(3,1fr);gap:4px}
.lv-chip{display:flex;flex-direction:column;align-items:center;gap:2px;font-size:10.5px;font-weight:600;text-align:center;line-height:1.12;color:var(--text)}
.lv-chip .ic{width:20px;height:20px;color:var(--lv-accent,var(--dot))}
.lives .lv-tabs{display:flex;gap:4px;margin:2px 14px 0;padding:4px;border-radius:12px;background:var(--lv-soft,var(--surface2))}
.lv-tabs button{flex:1;border:0;background:transparent;color:var(--muted);font:inherit;font-size:11.5px;font-weight:700;padding:7px 4px;border-radius:9px;cursor:pointer;line-height:1.25}
.lv-tabs button[aria-selected="true"]{background:var(--surface);color:var(--primary);box-shadow:0 1px 3px rgba(0,0,0,.12)}
.lv-body{flex:1;overflow:auto;padding:10px 14px 14px;display:flex;flex-direction:column;gap:8px}
.lv-search{display:flex;align-items:center;gap:8px;border:1px solid var(--border);border-radius:12px;padding:7px 10px;background:var(--surface);color:var(--muted);font-size:12.5px}
.lv-search .ic{width:18px;height:18px}
.lv-note{font-size:11px;color:var(--muted);line-height:1.5}
.lv-ph{border:1.5px dashed var(--lv-rule,var(--rule));border-radius:12px;padding:8px 10px;font-size:11.5px;color:var(--muted);line-height:1.5}
.lv-it{display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:12px;background:var(--surface);border:1px solid var(--border)}
.lv-it.on{border-color:var(--primary);box-shadow:0 0 0 1px var(--primary)}
.lv-it .d{width:9px;height:9px;border-radius:50%;background:var(--lv-accent,var(--dot));flex:none}
.lv-it .nm,.lv-tl .nm{font-weight:700;font-size:13.5px}
.lv-it .s,.lv-tl .s,.lv-grp .s{font-size:11px;color:var(--muted)}
.lv-hon{display:inline-block;font-family:"Amiri","Amiri Quran",serif;font-weight:400;color:var(--lv-accent,var(--dot));font-size:12.5px;margin:0 .45em;white-space:nowrap}
.lv-grp{border:1px solid var(--border);border-radius:12px;background:var(--surface);padding:9px 11px;display:flex;flex-direction:column;gap:3px}
.lv-grp b{font-size:13.5px}
.lv-src{font-size:10.5px;color:var(--muted);border-top:1px solid var(--border);padding-top:6px}
.lv-tl{position:relative;display:flex;flex-direction:column;gap:10px;padding-inline-start:22px}
.lv-tl::before{content:"";position:absolute;top:10px;bottom:10px;inset-inline-start:8px;width:2px;background:var(--lv-rule,var(--rule))}
.lv-tl .it{position:relative;background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:8px 11px}
.lv-tl .it::before{content:"";position:absolute;inset-inline-start:-19px;top:13px;width:10px;height:10px;border-radius:50%;background:var(--primary);box-shadow:0 0 0 3px var(--bg)}
.lv-tl .k{font-size:10.5px;font-weight:700;color:var(--lv-accent,var(--dot))}
.lv-link{display:inline-block;margin-top:5px;font-size:11px;font-weight:700;color:var(--primary);border:1px solid var(--primary);border-radius:999px;padding:1px 9px}
.lv-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:9px 12px;display:flex;flex-direction:column;gap:6px}
.lv-card h4{margin:0;font-size:12.5px;color:var(--lv-accent,var(--dot))}
.lv-ayah{direction:rtl;font-family:"Amiri Quran",serif;font-size:18.5px;line-height:2.1;color:var(--ink);background:var(--page);border-radius:8px;padding:2px 10px;text-align:right}
.lv-ref{font-size:11px;color:var(--muted)}
.lv-bars i{display:block;height:6px;border-radius:4px;background:var(--lv-soft,var(--surface2));margin:6px 0}
.lv-bars i:nth-child(2){width:86%}.lv-bars i:nth-child(3){width:64%}
.lv-report{align-self:flex-start;border:1px solid var(--border);border-radius:999px;padding:4px 12px;font:inherit;font-size:11.5px;font-weight:600;color:var(--text);background:transparent}
"""

HOME = """<div class="lv-home"><div class="lv-h" data-lv="lv_group"></div><div class="lv-row">
  <div class="lv-chip"><svg class="ic"><use href="#i-lv-prophets"/></svg><span data-lv="lv_prophets"></span></div>
  <div class="lv-chip"><svg class="ic"><use href="#i-lv-companions"/></svg><span data-lv="lv_companions"></span></div>
  <div class="lv-chip"><svg class="ic"><use href="#i-lv-caliphs"/></svg><span data-lv="lv_caliphs"></span></div>
</div></div>
"""

PHONES = """%(icons)s
  <div class="unit"><div class="cap">Lives — prophets, Companions, Rightly Guided Caliphs (F20, F21, F22)</div>
  <div class="%(phone)s lives">
    <div class="topbar"><div class="title kufi"><span data-lv="lv_group"></span><div class="sub" data-lv="lv_sub"></div></div><div class="iconbtn"><svg class="ic"><use href="#i-search"/></svg></div></div>
    <div class="lv-tabs" role="tablist"><button type="button" role="tab" data-lvtab="p" data-lv="lv_prophets"></button><button type="button" role="tab" data-lvtab="c" data-lv="lv_companions"></button><button type="button" role="tab" data-lvtab="k" data-lv="lv_caliphs"></button></div>
    <div class="lv-body" id="lv-list"></div>
  </div></div>

  <div class="unit"><div class="cap">Lives — one entry (a prophet)</div>
  <div class="%(phone)s lives">
    <div class="topbar"><div class="title kufi"><span id="lv-e-name"></span><div class="sub" data-lv="lv_entry_sub"></div></div><div class="iconbtn"><svg class="ic"><use href="#i-mark"/></svg></div></div>
    <div class="lv-body" id="lv-entry"></div>
  </div></div>
"""

JS = r"""window.LIVES = (function () {
  var D = %(data)s;
  var RTL = ["ar", "ur", "fa", "ps"], DIG = "٠١٢٣٤٥٦٧٨٩", tab = "p", cur = "ar";
  function T(id, vars) {
    var e = D.t[id], s = e[cur] || e.en;
    return vars ? s.replace(/\{(\w+)\}/g, function (m, k) { return vars[k] != null ? vars[k] : m; }) : s;
  }
  function num(n) {
    if (cur === "ar") return String(n).replace(/[0-9]/g, function (d) { return DIG[d]; });
    try { return new Intl.NumberFormat({ zh: "zh-CN", ps: "ps-u-nu-arabext" }[cur] || cur, { useGrouping: false }).format(n); }
    catch (e) { return String(n); }
  }
  /* names: Arabic for Arabic-script languages, transliterated for the others; honorifics always in Arabic */
  function nm(p) { return RTL.indexOf(cur) >= 0 ? p[0] : p[1]; }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function hon(text) { var s = el("span", "lv-hon", text); s.dir = "rtl"; s.lang = "ar"; return s; }
  function named(cls, p, h) { var d = el("div", cls, nm(p)); if (h) d.appendChild(hon(h)); return d; }

  function prophets(host) {
    var s = el("div", "lv-search"); s.innerHTML = "<svg class='ic'><use href='#i-search'/></svg><span></span>";
    s.lastChild.textContent = T("lv_search"); host.appendChild(s);
    host.appendChild(el("div", "lv-note", T("lv_p_note")));
    D.prophets.forEach(function (p, i) {
      var r = el("div", "lv-it" + (i === 1 ? " on" : "")); r.appendChild(el("span", "d"));
      r.appendChild(named("nm", p, "عليه السلام")); host.appendChild(r);
    });
    host.appendChild(el("div", "lv-ph", T("lv_more")));
    var last = el("div", "lv-it"); last.appendChild(el("span", "d"));
    var w = el("div"); w.appendChild(named("nm", D.last, "ﷺ")); w.appendChild(el("div", "s", T("lv_seerah")));
    last.appendChild(w); host.appendChild(last);
  }
  function companions(host) {
    host.appendChild(el("div", "lv-note", T("lv_c_note")));
    function grp(title, h, people) {
      var g = el("div", "lv-grp"), b = el("b", null, T(title)); b.appendChild(hon(h)); g.appendChild(b);
      if (people) g.appendChild(el("div", "s", people.map(nm).join(RTL.indexOf(cur) >= 0 ? "، " : ", ") + " …"));
      else g.appendChild(el("div", "lv-ph", T("lv_more")));
      host.appendChild(g);
    }
    grp("lv_g_ten", "رضي الله عنهم", D.caliphs);
    grp("lv_g_mothers", "رضي الله عنهن", D.mothers);
    grp("lv_g_badr", "رضي الله عنهم", null);
    host.appendChild(el("div", "lv-src", T("lv_c_src")));
  }
  function caliphs(host) {
    host.appendChild(el("div", "lv-note", T("lv_k_note")));
    var tl = el("div", "lv-tl");
    D.caliphs.forEach(function (p, i) {
      var it = el("div", "it");
      it.appendChild(el("div", "k", num(i + 1)));
      it.appendChild(named("nm", p, "رضي الله عنه"));
      it.appendChild(el("div", "lv-ph", T("lv_k_years")));
      it.appendChild(el("span", "lv-link", T("lv_k_life")));
      tl.appendChild(it);
    });
    host.appendChild(tl);
    host.appendChild(el("div", "lv-src", T("lv_k_src")));
  }
  function entry() {
    var t = document.getElementById("lv-e-name"); t.textContent = nm(D.prophets[1]); t.appendChild(hon("عليه السلام"));
    var host = document.getElementById("lv-entry"); host.textContent = "";
    var q = el("div", "lv-card"); q.appendChild(el("h4", null, T("lv_from_quran")));
    q.appendChild(el("div", "lv-ayah", D.verse.text));   /* copied from Tanzil by build_lives.py, unchanged */
    q.appendChild(el("div", "lv-ref", cur === "ar" ? T("lv_ref", { name: D.verse.name[0], a: num(D.verse.a) })
      : T("lv_ref", { name: RTL.indexOf(cur) >= 0 ? D.verse.name[0] : D.verse.name[1], s: num(D.verse.s), a: num(D.verse.a) })));
    q.appendChild(el("div", "lv-note", T("lv_ayah_note"))); host.appendChild(q);
    var h = el("div", "lv-card"); h.appendChild(el("h4", null, T("lv_from_sunnah"))); h.appendChild(el("div", "lv-ph", T("lv_hadith_ph"))); host.appendChild(h);
    var s = el("div", "lv-card"); s.appendChild(el("h4", null, T("lv_story")));
    var bars = el("div", "lv-bars"); bars.innerHTML = "<i></i><i></i><i></i>"; s.appendChild(bars);
    s.appendChild(el("div", "lv-ph", T("lv_story_ph"))); host.appendChild(s);
    host.appendChild(el("div", "lv-note", T("lv_nopic")));
    host.appendChild(el("button", "lv-report", T("lv_report")));
  }
  function render(lang) {
    if (lang) cur = (lang === "ar" || lang === "en" || D.t.lv_group[lang]) ? lang : "en";
    document.querySelectorAll("[data-lv]").forEach(function (e) { e.textContent = T(e.dataset.lv); });
    document.querySelectorAll("[data-lvtab]").forEach(function (b) { b.setAttribute("aria-selected", String(b.dataset.lvtab === tab)); });
    var host = document.getElementById("lv-list"); host.textContent = "";
    ({ p: prophets, c: companions, k: caliphs })[tab](host);
    entry();
  }
  document.querySelectorAll("[data-lvtab]").forEach(function (b) { b.addEventListener("click", function () { tab = b.dataset.lvtab; render(); }); });
  return { render: render };
})();
"""


def ensure_markers(html, page):
    """Designs 2 and 3 got the Lives markers on 2026-11-19; insert them once where they belong."""
    if "/*LIVES-CSS-BEGIN*/" in html:
        return html
    head_end = html.index("</head>")
    style_end = html.rindex("</style>", 0, head_end)
    html = html[:style_end] + "/* Lives (F20, F21, F22): written by tools/build_lives.py, shared by the three designs */\n/*LIVES-CSS-BEGIN*/\n/*LIVES-CSS-END*/\n" + html[style_end:]
    grid = html.index('<div class="grid">', html.index("<!-- 2. home -->"))
    grid_end = html.index("</div>\n    </div>", grid) + len("</div>\n")
    html = html[:grid_end] + "<!--LIVES-HOME-BEGIN-->\n<!--LIVES-HOME-END-->\n" + html[grid_end:]
    stage_end = html.index('</div>\n\n<h2 class="sec">8 ·')
    html = html[:stage_end] + "<!--LIVES-HTML-BEGIN-->\n<!--LIVES-HTML-END-->\n" + html[stage_end:]
    main = html.index("<script>\n(function () {")
    html = html[:main] + '<script id="lives">\n/*LIVES-JS-BEGIN*/\n/*LIVES-JS-END*/\n</script>\n' + html[main:]
    a = "    renderTimes(); renderSpread(); renderSources(); renderWhy(); renderMade(); renderIndex();\n"
    if html.count(a) != 1:
        R1.fail(page + ": renderAll not found")
    html = html.replace(a, a + "    if (window.LIVES) window.LIVES.render(L());\n")
    print("%s: Lives markers inserted" % page)
    return html


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    rel = "tanzil/quran-uthmani.txt"
    R1.check_sources({rel: R1.SHA256[rel], "tanzil/quran-data.xml": R1.SHA256["tanzil/quran-data.xml"]})
    tanzil = V.parse_tanzil(os.path.join(R1.ASSETS, rel))
    text = tanzil[VERSE]
    if VERSE[1] == 1 and VERSE[0] not in (1, 9):
        text = " ".join(text.split(" ")[4:])   # Tanzil writes the basmala before ayah 1; it is not part of the ayah
    if not any(WORD == V.skeleton(w) for w in text.split(" ")):
        R1.fail("ayah %d:%d does not contain %s" % (VERSE + (WORD,)))
    root = ET.parse(os.path.join(R1.ASSETS, "tanzil/quran-data.xml")).getroot()
    sura = [s for s in root.iter("sura") if int(s.get("index")) == VERSE[0]][0]
    i18n = I.build_i18n("lives")
    keys = json.load(io.open(os.path.join(I.I18N, "lives", "keys.json"), encoding="utf-8"))
    texts = {k["id"]: dict({"ar": k["ar"], "en": k["en"]}, **{c: i18n["tr"][c][k["id"]] for c in I.LANG_CODES}) for k in keys}
    data = {"t": texts, "prophets": PROPHETS, "last": LAST, "caliphs": CALIPHS, "mothers": MOTHERS,
            "verse": {"s": VERSE[0], "a": VERSE[1], "text": text, "name": [sura.get("name"), sura.get("tname")]}}
    js = JS % {"data": json.dumps(data, ensure_ascii=False)}
    for page, phone in PAGES.items():
        path = os.path.join(HERE, "..", page)
        html = ensure_markers(open(path, encoding="utf-8", newline="").read(), page)
        html = R1.replace_block(html, "/*LIVES-CSS-BEGIN*/", "/*LIVES-CSS-END*/", CSS)
        html = R1.replace_block(html, "<!--LIVES-HOME-BEGIN-->", "<!--LIVES-HOME-END-->", HOME)
        html = R1.replace_block(html, "<!--LIVES-HTML-BEGIN-->", "<!--LIVES-HTML-END-->", PHONES % {"icons": ICONS, "phone": phone})
        html = R1.replace_block(html, "/*LIVES-JS-BEGIN*/", "/*LIVES-JS-END*/", js)
        open(path, "w", encoding="utf-8", newline="\n").write(html)
        print("written Lives into %s" % page)
    print("ayah %d:%d copied from Tanzil and checked to contain %s" % (VERSE + (WORD,)))


if __name__ == "__main__":
    main()
