"""Write the screens the author asked for on 2026-11-20 into the three designs, and the day / night switch.

The author's message of 2026-11-20 asked for: a duas section, a misbaha (tasbeeh counter), a counter on the adhkar,
coloured ayah markers like the Ayah application, actions on a chosen ayah or range (a reciter of the user's choice,
all the tafsirs), the Hijri calendar and the current time for the location, downloading a recitation for offline
listening, and the virtues (فضائل) from authentic hadiths; and the light / dark choice as one switch beside the
colour directions. They are the same screens in every design, drawn with each design's own colours, so they are
written once, here, between marker comments in round-1.html, round-2.html and round-3.html:

  - home: three tiles (misbaha, duas, Hijri calendar) added to the section grid;
  - first launch: the day / night switch beside the colour directions (the two buttons removed);
  - six phones: misbaha, adhkar with counter, duas, ayah markers (ribbon and tint, to compare), ayah actions,
    Hijri calendar and clock.

What is real and what is a placeholder (AGENTS.md §6.10):
  - The ayahs (Al-Fatihah for the markers and the actions; 2:201, 3:8 and 25:74 for the duas from the Quran) are
    copied whole from the Tanzil file (checksum checked) and each is checked to contain the word it is cited for.
  - The misbaha shows the four words of tasbeeh without vowels, as labels; the words of each dhikr and its count,
    every dhikr of the adhkar, every dua of the Sunnah, every tafsir text and every virtue are dashed placeholders
    naming their source — nothing religious is written by us.
  - Reciter and tafsir names are names only (AGENTS.md §7.2, §7.3); the location is a sample; the time and the
    Hijri date are the device's own (the Umm al-Qura calendar of the browser, with the user's adjustment).
Interface texts: i18n/extras/ (checked by i18n_check.py).

Usage: python -I build_extras.py   (after build_round1.py, build_round2.py, build_round3.py; with build_lives.py)
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
FATIHA = [(1, n) for n in range(1, 8)]
DUAS = {"2:201": "حسنة", "3:8": "تزغ", "25:74": "قرة"}   # ayah -> a word it must contain
MARKED = {2: "green", 5: "red", 7: "blue"}               # the sample markers on Al-Fatihah
DHIKR = ["سبحان الله", "الحمد لله", "الله أكبر", "لا إله إلا الله"]
ADHKAR = [1, 3, 1, 3, 7, 100]                             # sample counts, marked as samples on the screen
RECITERS = [("محمد صديق المنشاوي", "Muhammad Siddiq al-Minshawi"), ("محمود خليل الحصري", "Mahmoud Khalil al-Husary"),
            ("عبد الباسط عبد الصمد", "Abdul Basit Abdul Samad"), ("محمد محمود الطبلاوي", "Muhammad Mahmoud al-Tablawi")]
TAFSIRS = [("التفسير الميسر", "al-Tafsir al-Muyassar"), ("تفسير السعدي", "Tafsir al-Sa'di"),
           ("تفسير ابن كثير", "Tafsir Ibn Kathir"), ("تفسير الطبري", "Tafsir al-Tabari"),
           ("تفسير القرطبي", "Tafsir al-Qurtubi"), ("تفسير البغوي", "Tafsir al-Baghawi")]

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <!-- icons of the new sections (no person, no cross shape): a ring of beads, open hands raised in dua, a calendar with a crescent -->
  <symbol id="i-ex-misbaha" viewBox="0 0 24 24"><circle cx="12" cy="3.2" r="1.4"/><circle cx="17" cy="5.3" r="1.4"/><circle cx="19" cy="10" r="1.4"/><circle cx="17" cy="14.7" r="1.4"/><circle cx="7" cy="14.7" r="1.4"/><circle cx="5" cy="10" r="1.4"/><circle cx="7" cy="5.3" r="1.4"/><circle cx="12" cy="16.8" r="1.6"/><path d="M12 18.4v1.8M12 20.2l-2 2.3M12 20.2l2 2.3"/></symbol>
  <symbol id="i-ex-dua" viewBox="0 0 24 24"><path d="M4.5 12.5c0 4.4 3.4 7.5 7.5 7.5s7.5-3.1 7.5-7.5"/><path d="M4.5 12.5V8a1.5 1.5 0 0 1 3 0v4.2M19.5 12.5V8a1.5 1.5 0 0 0-3 0v4.2"/><path d="M7.5 12.2c1.4 1 3 1.5 4.5 1.5s3.1-.5 4.5-1.5"/></symbol>
  <symbol id="i-ex-pin" viewBox="0 0 24 24"><path d="M12 21s-6.5-6.2-6.5-11.2a6.5 6.5 0 0 1 13 0C18.5 14.8 12 21 12 21z"/><circle cx="12" cy="9.8" r="2.3"/></symbol>
  <symbol id="i-ex-cal" viewBox="0 0 24 24"><rect x="4" y="5.5" width="16" height="15" rx="2"/><path d="M4 10h16M8.5 3v2.5M15.5 3v2.5"/><path d="M14.2 12.6a3.4 3.4 0 1 0 0 6.2 2.8 2.8 0 1 1 0-6.2z"/></symbol>
</svg>"""

CSS = """/* the day / night switch, beside the colour directions (the author, 2026-11-20) */
.qrow{display:flex;align-items:center;justify-content:space-between;gap:10px}
.tsw{display:inline-flex;align-items:center;gap:6px;border:0;background:transparent;color:var(--muted);cursor:pointer;padding:0;font:inherit}
.tsw .ic{width:16px;height:16px}
.tsw i{position:relative;width:40px;height:22px;border-radius:999px;background:var(--border);display:inline-block;transition:background .2s}
.tsw i::after{content:"";position:absolute;top:3px;inset-inline-start:3px;width:16px;height:16px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.3);transition:transform .2s}
.tsw[aria-checked="true"] i{background:var(--primary)}
.tsw[aria-checked="true"] i::after{transform:translateX(18px)}
.tsw[aria-checked="true"]:dir(rtl) i::after{transform:translateX(-18px)}
/* the home grid of designs 2 and 3 in four columns, with the three new tiles */
.grid.g4{grid-template-columns:repeat(4,1fr)}
.grid.g4 .tile{border-inline-start:1px solid var(--border);padding:10px 2px 8px;font-size:10.5px}
.grid.g4 .tile:nth-child(4n+1){border-inline-start:0}
.grid.g4 .tile .ic{width:22px;height:22px}
/* design 1: four rows of tiles now, so each tile is a little shorter */
.grid:has(.ib) .tile{padding:8px 2px 6px;gap:4px}
/* the screens */
.extras .ex-body{flex:1;overflow:auto;padding:8px 14px 14px;display:flex;flex-direction:column;gap:10px}
.ex-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:10px 12px;display:flex;flex-direction:column;gap:7px}
.ex-card h4{margin:0;font-size:12.5px;color:var(--lv-accent,var(--dot))}
.ex-note{font-size:11px;color:var(--muted);line-height:1.5}
.ex-ph{border:1.5px dashed var(--lv-rule,var(--rule));border-radius:12px;padding:8px 10px;font-size:11.5px;color:var(--muted);line-height:1.5}
.ex-seg{display:flex;gap:4px;padding:4px;border-radius:12px;background:var(--lv-soft,var(--surface2))}
.ex-seg button{flex:1;border:0;background:transparent;color:var(--muted);font:inherit;font-size:11.5px;font-weight:700;padding:6px 4px;border-radius:9px;cursor:pointer}
.ex-seg button[aria-pressed="true"]{background:var(--surface);color:var(--primary);box-shadow:0 1px 3px rgba(0,0,0,.12)}
.ex-chips{display:flex;flex-wrap:wrap;gap:6px}
.ex-chip{border:1px solid var(--border);background:var(--surface);color:var(--text);border-radius:999px;padding:5px 11px;font:inherit;font-size:12.5px;cursor:pointer}
.ex-chip[aria-pressed="true"]{border-color:var(--primary);color:var(--primary);font-weight:700}
.ex-chip.ar{font-family:"Amiri","IBM Plex Sans Arabic",serif;font-size:14px}
.ex-row{display:flex;align-items:center;gap:8px;font-size:12.5px}
.ex-row .grow{flex:1}
.ex-btn{border:0;border-radius:12px;padding:8px 14px;background:var(--primary);color:var(--lv-on,var(--onprimary));font:inherit;font-size:12.5px;font-weight:700;cursor:pointer}
.ex-btn.line{background:transparent;color:var(--primary);border:1.5px solid var(--primary)}
.ex-tag{font-size:10px;font-weight:700;padding:1px 7px;border-radius:999px;border:1px solid var(--lv-rule,var(--rule));color:var(--muted);white-space:nowrap}
/* misbaha */
.ex-dhikr{text-align:center;font-family:"Amiri","IBM Plex Sans Arabic",serif;font-size:26px;line-height:1.5;color:var(--text);direction:rtl}
.ex-ring{position:relative;width:220px;height:220px;margin:0 auto;cursor:pointer;-webkit-tap-highlight-color:transparent;border-radius:50%}
.ex-ring svg{position:absolute;inset:0;width:100%;height:100%}
.ex-ring .c{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;pointer-events:none}
.ex-ring .c b{font-size:46px;line-height:1.1;color:var(--primary)}
.ex-ring .c span{font-size:12px;color:var(--muted)}
.ex-ring.pulse{animation:expulse .35s}
@keyframes expulse{50%{transform:scale(.97)}}
/* adhkar counter */
.ex-count{width:128px;height:128px;border-radius:50%;margin:2px auto;border:0;background:var(--primary);color:var(--lv-on,var(--onprimary));display:flex;flex-direction:column;align-items:center;justify-content:center;font:inherit;cursor:pointer;box-shadow:0 0 0 7px var(--lv-soft,var(--surface2))}
.ex-count b{font-size:38px;line-height:1.1}
.ex-count span{font-size:11px;opacity:.9}
.ex-list{display:flex;flex-direction:column;gap:5px}
.ex-li{display:flex;align-items:center;gap:8px;padding:7px 10px;border-radius:10px;background:var(--surface);border:1px solid var(--border);font-size:12px}
.ex-li.on{border-color:var(--primary)}
.ex-li.done{opacity:.55}
.ex-li .k{width:22px;height:22px;border-radius:50%;display:grid;place-items:center;font-size:11px;font-weight:700;background:var(--lv-soft,var(--surface2));color:var(--primary);flex:none}
/* ayahs (Quran text copied from Tanzil; display layers only) */
.ex-ayah{direction:rtl;font-family:"Amiri Quran",serif;font-size:18px;line-height:2.1;color:var(--ink);background:var(--page);border-radius:8px;padding:2px 10px;text-align:right}
.ex-ref{font-size:11px;color:var(--muted)}
.ex-page{position:relative;background:var(--page);color:var(--ink);border:1.5px solid var(--border);border-radius:6px;padding:16px 14px 10px;direction:rtl}
.ex-page .sh{text-align:center;font-family:"Amiri","IBM Plex Sans Arabic",serif;font-weight:700;font-size:14px;color:var(--muted);margin-bottom:4px}
.ex-page .ex-q{white-space:normal;font-family:"Amiri Quran",serif;font-size:19px;line-height:2.25;text-align:justify;text-align-last:center}
.ex-page .ex-n{font-size:.85em;padding:0 2px;color:var(--muted);white-space:nowrap}
.ex-page .ex-a.tint{border-radius:6px;box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:2px 0}
.ex-page .mk{display:inline-block;width:7px;height:11px;margin:0 2px;vertical-align:middle;clip-path:polygon(0 0,100% 0,100% 100%,50% 72%,0 100%)}
.ex-page .rib{position:absolute;top:-2px;width:11px;height:30px;clip-path:polygon(0 0,100% 0,100% 100%,50% 80%,0 100%)}
.ex-dot{width:12px;height:12px;border-radius:50%;flex:none}
.ex-dots{display:flex;gap:10px}
.ex-dots button{width:26px;height:26px;border-radius:50%;border:2px solid var(--surface);box-shadow:0 0 0 1px var(--border);cursor:pointer}
.ex-pick{display:flex;align-items:center;gap:8px;border:1px solid var(--border);border-radius:12px;padding:8px 10px;background:var(--surface);font-size:12.5px;font-weight:600}
.ex-pick .ic{width:16px;height:16px;margin-inline-start:auto;color:var(--muted)}
/* Hijri calendar and clock */
.ex-clock{text-align:center;font-size:40px;font-weight:700;letter-spacing:.5px;color:var(--primary);font-variant-numeric:tabular-nums}
.ex-date{text-align:center;font-size:12.5px;color:var(--muted);line-height:1.6}
.ex-date b{color:var(--text);font-size:14px}
.ex-cal{display:grid;grid-template-columns:repeat(7,1fr);gap:3px;text-align:center}
.ex-cal .h{font-size:10.5px;color:var(--muted);font-weight:700;padding:2px 0}
.ex-cal .d{font-size:12px;padding:6px 0;border-radius:8px}
.ex-cal .d.today{background:var(--primary);color:var(--lv-on,var(--onprimary));font-weight:700}
.ex-adj{display:flex;align-items:center;justify-content:center;gap:10px;font-size:12.5px}
.ex-adj button{width:30px;height:30px;border-radius:50%;border:1px solid var(--border);background:var(--surface);color:var(--text);font:inherit;font-size:16px;cursor:pointer}
"""

PHONE = """  <div class="unit"><div class="cap">%(cap)s</div>
  <div class="%(phone)s lives extras">
    <div class="topbar"><div class="title kufi"><span data-ex="%(title)s"></span><div class="sub"%(sub)s></div></div>%(icon)s</div>
    <div class="ex-body" id="%(id)s"></div>
  </div></div>
"""


def phones(phone):
    out = [ICONS]
    for cap, title, sub, ident, icon in [
        ("New 2026-11-20 · Misbaha (F24)", "ex_misbaha", " data-ex='ex_tap'", "ex-misbaha", "i-ex-misbaha"),
        ("New · Adhkar with a counter (F12)", "ex_adhkar", "", "ex-adhkar", "i-ex-misbaha"),
        ("New · Duas (F23)", "ex_duas", "", "ex-duas", "i-ex-dua"),
        ("New · Coloured ayah markers (F25) — two styles to compare", "ex_markers", " data-ex='ex_m_local'", "ex-markers", "i-mark"),
        ("New · Actions on an ayah or a range (F26, F28, F29)", "ex_actions_t", " id='ex-act-sub'", "ex-actions", "i-mark"),
        ("New · Hijri calendar and the time (F27)", "ex_hijri", " data-ex='ex_local_time'", "ex-hijri", "i-ex-cal"),
    ]:
        out.append(PHONE % {"cap": cap, "phone": phone, "title": title, "sub": sub, "id": ident,
                            "icon": "<svg class='ic' style='color:var(--primary)'><use href='#%s'/></svg>" % icon})
    return "\n".join(out)


JS = r"""window.EXTRAS = (function () {
  var D = %(data)s;
  var RTL = ["ar", "ur", "fa", "ps"], DIG = "٠١٢٣٤٥٦٧٨٩", cur = "ar", tick = null;
  var COL = { red: "#C0392B", green: "#2E8B57", blue: "#2F6FB0", gold: "#B8860B" };
  var st = { dhikr: 0, count: 0, target: 33, total: 0, rounds: 0, list: "m", item: 0, done: 0, style: "ribbon", tab: "q", adj: 0 };
  function T(id, vars) {
    var e = D.t[id], s = e[cur] || e.en;
    return vars ? s.replace(/\{(\w+)\}/g, function (m, k) { return vars[k] != null ? vars[k] : m; }) : s;
  }
  function tag(cal) {
    var u = [];
    if (cal) u.push("ca-" + cal);
    if (cur === "ps") u.push("nu-arabext");
    return ({ zh: "zh-CN" }[cur] || cur) + (u.length ? "-u-" + u.join("-") : "");
  }
  function num(n) {
    if (cur === "ar") return String(n).replace(/[0-9]/g, function (d) { return DIG[d]; });
    try { return new Intl.NumberFormat(tag(), { useGrouping: false }).format(n); } catch (e) { return String(n); }
  }
  function nm(p) { return RTL.indexOf(cur) >= 0 ? p[0] : p[1]; }
  function sname() { return RTL.indexOf(cur) >= 0 ? D.fatiha.name[0] : D.fatiha.name[1]; }
  function el(t, cls, text) { var e = document.createElement(t); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function btn(cls, text, fn, pressed) {
    var b = el("button", cls, text); b.type = "button";
    if (pressed != null) b.setAttribute("aria-pressed", String(pressed));
    if (fn) b.addEventListener("click", fn);
    return b;
  }
  function svgIcon(id) { var s = document.createElementNS("http://www.w3.org/2000/svg", "svg"); s.setAttribute("class", "ic"); s.innerHTML = "<use href='#" + id + "'/>"; return s; }
  function host(id) { var h = document.getElementById(id); h.textContent = ""; return h; }
  function ref(s, a, name) { return cur === "ar" ? "سورة " + name[0] + " · " + num(a) : (RTL.indexOf(cur) >= 0 ? name[0] : name[1]) + " " + num(s) + ":" + num(a); }

  /* ---- the home tiles and the day / night switch (once) ---- */
  function init() {
    var home = document.querySelectorAll(".phone")[1], grid = home && home.querySelector(".grid");
    if (grid && !grid.querySelector("[data-ex-tile]")) {
      var d1 = !!grid.querySelector(".ib");
      if (!d1) grid.classList.add("g4");
      [["misbaha", "i-ex-misbaha", "ex_misbaha"], ["duas", "i-ex-dua", "ex_duas"], ["hijri", "i-ex-cal", "ex_hijri_s"]].forEach(function (x) {
        var t = el("div", "tile" + (d1 ? " alt" : " g")); t.dataset.exTile = x[0];
        t.innerHTML = d1 ? "<div class='ib'><svg class='ic'><use href='#" + x[1] + "'/></svg></div><span></span>" : "<svg class='ic'><use href='#" + x[1] + "'/></svg><span></span>";
        t.querySelector("span").dataset.ex = x[2];
        grid.appendChild(t);
      });
    }
    document.querySelectorAll(".tsw").forEach(function (b) {
      if (b.dataset.on) return;
      b.dataset.on = "1";
      b.addEventListener("click", function () { if (window.__set) window.__set("theme", document.body.dataset.theme === "dark" ? "light" : "dark"); });
    });
  }

  /* ---- misbaha: tap the ring; a round ends at the chosen count ---- */
  function misbaha() {
    var h = host("ex-misbaha"), n = 33;
    var chips = el("div", "ex-chips");
    D.dhikr.forEach(function (w, i) { var b = btn("ex-chip ar", w, function () { st.dhikr = i; st.count = 0; misbaha(); }, i === st.dhikr); b.lang = "ar"; chips.appendChild(b); });
    h.appendChild(chips);
    var w = el("div", "ex-dhikr", D.dhikr[st.dhikr]); w.lang = "ar"; h.appendChild(w);
    var ring = el("div", "ex-ring"), lit = st.target ? Math.round(st.count / st.target * n) : st.count %% n;
    var s = "<svg viewBox='0 0 220 220' aria-hidden='true'><circle cx='110' cy='110' r='92' fill='none' stroke='var(--border)' stroke-width='1'/>";
    for (var i = 0; i < n; i++) {
      var a = i / n * 2 * Math.PI - Math.PI / 2;
      s += "<circle cx='" + (110 + 92 * Math.cos(a)).toFixed(1) + "' cy='" + (110 + 92 * Math.sin(a)).toFixed(1) + "' r='7' fill='" + (i < lit ? "var(--primary)" : "var(--surface)") + "' stroke='var(--border)' stroke-width='1.2'/>";
    }
    ring.innerHTML = s + "</svg><div class='c'><b></b><span></span></div>";
    ring.querySelector("b").textContent = num(st.count);
    ring.querySelector("span").textContent = st.target ? "/ " + num(st.target) : T("ex_free");
    ring.addEventListener("click", function () {
      st.count++; st.total++;
      if (st.target && st.count >= st.target) { st.count = 0; st.rounds++; }
      misbaha();
      var r = document.querySelector("#ex-misbaha .ex-ring"); r.classList.add("pulse");
    });
    h.appendChild(ring);
    var seg = el("div", "ex-seg");
    [[33, num(33)], [100, num(100)], [0, T("ex_free")]].forEach(function (x) { seg.appendChild(btn("", x[1], function () { st.target = x[0]; st.count = 0; misbaha(); }, st.target === x[0])); });
    var row = el("div", "ex-row"); row.appendChild(el("span", "", T("ex_target"))); row.appendChild(seg); seg.style.flex = "1"; h.appendChild(row);
    var r2 = el("div", "ex-row");
    r2.appendChild(el("span", "grow", T("ex_today_total", { n: num(st.total) }) + " · " + T("ex_round", { n: num(st.rounds) })));
    r2.appendChild(btn("ex-btn line", T("ex_reset"), function () { st.count = 0; st.rounds = 0; st.total = 0; misbaha(); }));
    h.appendChild(r2);
    h.appendChild(el("div", "ex-note", T("ex_vibrate")));
    h.appendChild(el("div", "ex-ph", T("ex_m_note")));
  }

  /* ---- adhkar with a counter: the count goes down; at zero the next dhikr opens ---- */
  function adhkar() {
    var h = host("ex-adhkar"), list = D.adhkar, it = Math.min(st.item, list.length - 1);
    var seg = el("div", "ex-seg");
    [["m", "ex_morning"], ["e", "ex_evening"]].forEach(function (x) { seg.appendChild(btn("", T(x[1]), function () { st.list = x[0]; st.item = 0; st.done = 0; adhkar(); }, st.list === x[0])); });
    h.appendChild(seg);
    var card = el("div", "ex-card");
    var top = el("div", "ex-row"); top.appendChild(el("b", "grow", T("ex_progress", { n: num(it + 1), k: num(list.length) })));
    top.appendChild(el("span", "ex-tag", T("ex_sample_count"))); card.appendChild(top);
    card.appendChild(el("div", "ex-ph", T("ex_ph_dhikr")));
    card.appendChild(el("div", "ex-note", T("ex_times", { n: num(list[it]) })));
    h.appendChild(card);
    var c = btn("ex-count", null, function () {
      st.done++;
      if (st.done >= list[it]) { st.done = 0; st.item = (it + 1) %% list.length; }
      adhkar();
    });
    c.innerHTML = "<b></b><span></span>";
    c.querySelector("b").textContent = num(list[it] - st.done);
    c.querySelector("span").textContent = T("ex_tap_count");
    h.appendChild(c);
    h.appendChild(el("div", "ex-note", T("ex_next_auto")));
    var ul = el("div", "ex-list");
    list.forEach(function (n, i) {
      var li = el("div", "ex-li" + (i === it ? " on" : i < it ? " done" : ""));
      li.appendChild(el("span", "k", num(i + 1))); li.appendChild(el("span", "grow", "—"));
      li.appendChild(el("span", "ex-tag", "× " + num(n))); ul.appendChild(li);
    });
    h.appendChild(ul);
  }

  /* ---- duas: from the Quran (copied from Tanzil) and from the Sunnah (from their sources) ---- */
  function duas() {
    var h = host("ex-duas"), seg = el("div", "ex-seg");
    [["q", "ex_from_quran"], ["s", "ex_from_sunnah"]].forEach(function (x) { seg.appendChild(btn("", T(x[1]), function () { st.tab = x[0]; duas(); }, st.tab === x[0])); });
    h.appendChild(seg);
    if (st.tab === "q") {
      D.duas.forEach(function (d) {
        var c = el("div", "ex-card"); c.appendChild(el("div", "ex-ayah", d.text));   /* the ayah exactly as in Tanzil */
        c.appendChild(el("div", "ex-ref", ref(d.s, d.a, d.name))); h.appendChild(c);
      });
    } else {
      for (var i = 0; i < 3; i++) { var c = el("div", "ex-card"); c.appendChild(el("div", "ex-ph", T("ex_dua_ph"))); h.appendChild(c); }
    }
    var v = el("div", "ex-card"); v.appendChild(el("h4", null, T("ex_virtue"))); v.appendChild(el("div", "ex-ph", T("ex_virtue_ph"))); h.appendChild(v);
  }

  /* ---- coloured ayah markers on Al-Fatihah, in two styles to compare ---- */
  function fatihaPage(style) {
    var p = el("div", "ex-page"); p.appendChild(el("div", "sh", "سورة " + D.fatiha.name[0]));
    var q = el("div", "ex-q"), ribs = 0;
    D.fatiha.ayahs.forEach(function (a) {
      var span = el("span", "ex-a", a.t), m = D.marked[a.n];
      if (m && style === "tint") { span.className = "ex-a tint"; span.style.background = COL[m] + "2E"; }
      q.appendChild(span); q.appendChild(document.createTextNode(" "));
      if (m && style === "ribbon") { var mk = el("span", "mk"); mk.style.background = COL[m]; q.appendChild(mk); }
      q.appendChild(el("span", "ex-n", "۝" + String(a.n).replace(/[0-9]/g, function (d) { return DIG[d]; })));
      q.appendChild(document.createTextNode(" "));
      if (m && style === "ribbon") { var r = el("span", "rib"); r.style.background = COL[m]; r.style.left = (14 + 16 * ribs++) + "px"; p.appendChild(r); }
    });
    p.appendChild(q);
    return p;
  }
  function markers() {
    var h = host("ex-markers"), seg = el("div", "ex-seg");
    [["ribbon", "ex_ribbon"], ["tint", "ex_tint"]].forEach(function (x) { seg.appendChild(btn("", T(x[1]), function () { st.style = x[0]; markers(); }, st.style === x[0])); });
    var row = el("div", "ex-row"); row.appendChild(el("span", "", T("ex_compare"))); seg.style.flex = "1"; row.appendChild(seg); h.appendChild(row);
    h.appendChild(fatihaPage(st.style));
    var ul = el("div", "ex-list");
    [[2, "green", "ex_m_review"], [5, "red", "ex_m_memo"], [7, "blue", "ex_m_reflect"]].forEach(function (x) {
      var li = el("div", "ex-li"), d = el("span", "ex-dot"); d.style.background = COL[x[1]];
      li.appendChild(d); li.appendChild(el("span", "grow", T(x[2]))); li.appendChild(el("span", "ex-ref", ref(1, x[0], D.fatiha.name)));
      ul.appendChild(li);
    });
    h.appendChild(ul);
  }

  /* ---- actions on an ayah or a range: marker, reciter, range, tafsirs, download, virtue ---- */
  function actions() {
    var h = host("ex-actions"), a5 = D.fatiha.ayahs[4];
    document.getElementById("ex-act-sub").textContent = ref(1, 5, D.fatiha.name);
    var c0 = el("div", "ex-card"); c0.appendChild(el("div", "ex-ayah", a5.t)); h.appendChild(c0);
    var c1 = el("div", "ex-card"); c1.appendChild(el("h4", null, T("ex_add_marker")));
    var dots = el("div", "ex-dots");
    ["red", "green", "blue", "gold"].forEach(function (k) { var b = btn("", null, null); b.style.background = COL[k]; b.setAttribute("aria-label", k); dots.appendChild(b); });
    c1.appendChild(dots); h.appendChild(c1);
    var c2 = el("div", "ex-card"); c2.appendChild(el("h4", null, T("ex_listen")));
    var pick = el("div", "ex-pick"); pick.appendChild(el("span", "", T("ex_reciter") + ": " + nm(D.reciters[0]))); pick.appendChild(svgIcon("i-down")); c2.appendChild(pick);
    var r = el("div", "ex-chips");
    r.appendChild(el("span", "ex-chip", T("ex_range", { a: num(1), b: num(7) })));
    r.appendChild(el("span", "ex-chip", T("ex_repeat", { n: num(3) })));
    c2.appendChild(r);
    var pr = el("div", "ex-row"); pr.appendChild(el("span", "grow ex-note", D.reciters.slice(1).map(nm).join(" · ")));
    pr.appendChild(btn("ex-btn", T("ex_play"))); c2.appendChild(pr);
    h.appendChild(c2);
    var c3 = el("div", "ex-card"); c3.appendChild(el("h4", null, T("ex_tafsirs") + " · " + T("ex_range", { a: num(1), b: num(7) })));
    var ul = el("div", "ex-list");
    D.tafsirs.forEach(function (t) { var li = el("div", "ex-li"); li.appendChild(el("span", "grow", nm(t))); li.appendChild(el("span", "ex-tag", "☐")); ul.appendChild(li); });
    c3.appendChild(ul); c3.appendChild(el("div", "ex-note", T("ex_tafsir_ph"))); h.appendChild(c3);
    var c4 = el("div", "ex-card"); var dr = el("div", "ex-row");
    dr.appendChild(el("b", "grow", T("ex_download"))); dr.appendChild(btn("ex-btn line", "↓")); c4.appendChild(dr);
    c4.appendChild(el("div", "ex-note", T("ex_dl_note"))); h.appendChild(c4);
    var c5 = el("div", "ex-card"); c5.appendChild(el("h4", null, T("ex_virtue"))); c5.appendChild(el("div", "ex-ph", T("ex_virtue_ph"))); h.appendChild(c5);
  }

  /* ---- the Hijri calendar (Umm al-Qura, with the user's adjustment) and the time of the device ---- */
  function parts(d, cal) {
    var o = {};
    try { new Intl.DateTimeFormat("en-u-ca-" + cal, { day: "numeric", month: "numeric", year: "numeric" }).formatToParts(d).forEach(function (p) { o[p.type] = Number(p.value); }); } catch (e) {}
    return o;
  }
  function fmt(d, opts, cal) { try { return new Intl.DateTimeFormat(tag(cal), opts).format(d); } catch (e) { return ""; } }
  function hijri() {
    var h = host("ex-hijri"), now = new Date(), base = new Date(now.getTime() + st.adj * 864e5);
    var loc = el("div", "ex-pick"); loc.appendChild(svgIcon("i-ex-pin")); loc.lastChild.style.marginInlineStart = "0"; loc.appendChild(el("span", "", T("ex_location"))); h.appendChild(loc);
    var clock = el("div", "ex-clock"); clock.id = "ex-clock"; h.appendChild(clock);
    var date = el("div", "ex-date"); date.innerHTML = "<b></b><br><span></span>";
    date.querySelector("b").textContent = fmt(base, { day: "numeric", month: "long", year: "numeric" }, "islamic-umalqura");
    date.querySelector("span").textContent = fmt(now, { weekday: "long" }) + " · " + fmt(now, { day: "numeric", month: "long", year: "numeric" });
    h.appendChild(date);
    var hp = parts(base, "islamic-umalqura");
    var card = el("div", "ex-card");
    card.appendChild(el("h4", null, fmt(base, { month: "long", year: "numeric" }, "islamic-umalqura")));
    var grid = el("div", "ex-cal"), first = new Date(base.getTime() - ((hp.day || 1) - 1) * 864e5);
    for (var w = 0; w < 7; w++) grid.appendChild(el("div", "h", fmt(new Date(2026, 10, 15 + w), { weekday: "narrow" })));
    for (var b = 0; b < first.getDay(); b++) grid.appendChild(el("div", "d", ""));
    for (var i = 0; i < 31; i++) {
      var d = new Date(first.getTime() + i * 864e5), p = parts(d, "islamic-umalqura");
      if (i > 0 && p.month !== hp.month) break;
      grid.appendChild(el("div", "d" + (p.day === hp.day ? " today" : ""), num(p.day)));
    }
    card.appendChild(grid); h.appendChild(card);
    var adj = el("div", "ex-adj");
    adj.appendChild(btn("", "−", function () { if (st.adj > -2) { st.adj--; hijri(); } }));
    adj.appendChild(el("span", "", T("ex_adjust", { n: (st.adj > 0 ? "+" : "") + num(st.adj) })));
    adj.appendChild(btn("", "+", function () { if (st.adj < 2) { st.adj++; hijri(); } }));
    h.appendChild(adj);
    h.appendChild(el("div", "ex-note", T("ex_cal_note")));
    function upd() { var c = document.getElementById("ex-clock"); if (c) c.textContent = fmt(new Date(), { hour: "numeric", minute: "2-digit" }); }
    upd();
    if (!tick) tick = setInterval(upd, 15000);
  }

  function render(lang) {
    if (lang) cur = (lang === "ar" || lang === "en" || D.t.ex_misbaha[lang]) ? lang : "en";
    init();
    document.querySelectorAll("[data-ex]").forEach(function (e) { e.textContent = T(e.dataset.ex); });
    document.querySelectorAll(".tsw").forEach(function (b) {
      b.setAttribute("aria-checked", String(document.body.dataset.theme === "dark"));
      b.setAttribute("aria-label", T("ex_night"));
    });
    misbaha(); adhkar(); duas(); markers(); actions(); hijri();
  }
  return { render: render };
})();
"""

# The day / night switch replaces the two buttons of the first launch (the author, 2026-11-20).
SWITCH = ('<button class="tsw" type="button" role="switch" aria-checked="false"><svg class="ic"><use href="#i-sun"/></svg>'
          '<i></i><svg class="ic"><use href="#i-moon"/></svg></button>')
FIRST_LAUNCH = {
    "round-1.html": [
        ('<div class="q" data-ar="الألوان" data-en="Colours"></div>',
         '<div class="q qrow"><span data-ar="الألوان" data-en="Colours"></span>' + SWITCH + '</div>'),
        ('      <div class="q" data-ar="المظهر" data-en="Theme"></div>\n      <div class="pills" data-set="theme"><button class="pill" data-v="light"><svg class="ic"><use href="#i-sun"/></svg><span data-ar="فاتح" data-en="Light"></span></button><button class="pill" data-v="dark"><svg class="ic"><use href="#i-moon"/></svg><span data-ar="داكن" data-en="Dark"></span></button></div>\n', ''),
    ],
    "round-2.html": [
        ('<div class="q kufi" data-ar="الألوان" data-en="Colours"></div>',
         '<div class="q kufi qrow"><span data-ar="الألوان" data-en="Colours"></span>' + SWITCH + '</div>'),
        ('      <div class="q kufi" data-ar="المظهر" data-en="Theme"></div>\n      <div class="pills" data-set="theme"><button class="pill" data-v="light"><svg class="ic"><use href="#i-sun"/></svg><span data-ar="نهاري" data-en="Day"></span></button><button class="pill" data-v="dark"><svg class="ic"><use href="#i-moon"/></svg><span data-ar="ليلي" data-en="Night"></span></button></div>\n', ''),
    ],
}
FIRST_LAUNCH["round-3.html"] = FIRST_LAUNCH["round-2.html"]


def ensure_markers(html, page):
    """Insert the marker comments, the switch and the page hooks once (2026-11-20)."""
    if "/*EXTRAS-CSS-BEGIN*/" in html:
        return html
    for a, b in [("/*LIVES-CSS-BEGIN*/", "/*EXTRAS-CSS-BEGIN*/\n/*EXTRAS-CSS-END*/\n/*LIVES-CSS-BEGIN*/"),
                 ("<!--LIVES-HTML-END-->\n", "<!--LIVES-HTML-END-->\n<!--EXTRAS-HTML-BEGIN-->\n<!--EXTRAS-HTML-END-->\n"),
                 ('<script id="lives">', '<script id="extras">\n/*EXTRAS-JS-BEGIN*/\n/*EXTRAS-JS-END*/\n</script>\n<script id="lives">'),
                 ("    if (window.LIVES) window.LIVES.render(L());\n",
                  "    if (window.LIVES) window.LIVES.render(L());\n    if (window.EXTRAS) window.EXTRAS.render(L());\n"),
                 ("  function set(k, v) { body.dataset[k] = v; renderAll(); }\n",
                  "  function set(k, v) { body.dataset[k] = v; renderAll(); }\n  window.__set = set;   /* used by the day / night switch (build_extras.py) */\n")] + FIRST_LAUNCH[page]:
        if html.count(a) != 1:
            R1.fail("%s: not found once: %s" % (page, a[:70]))
        html = html.replace(a, b)
    print("%s: markers, switch and hooks inserted" % page)
    return html


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    rel = "tanzil/quran-uthmani.txt"
    R1.check_sources({rel: R1.SHA256[rel], "tanzil/quran-data.xml": R1.SHA256["tanzil/quran-data.xml"]})
    tanzil = V.parse_tanzil(os.path.join(R1.ASSETS, rel))
    root = ET.parse(os.path.join(R1.ASSETS, "tanzil/quran-data.xml")).getroot()
    names = {int(s.get("index")): [s.get("name"), s.get("tname")] for s in root.iter("sura")}

    def ayah(key):
        text = tanzil[key]
        if key[1] == 1 and key[0] not in (1, 9):
            text = " ".join(text.split(" ")[4:])   # Tanzil writes the basmala before ayah 1; it is not part of the ayah
        return text
    fatiha = [{"n": a, "t": ayah((s, a))} for s, a in FATIHA]
    duas = []
    for refkey, word in DUAS.items():
        s, a = (int(x) for x in refkey.split(":"))
        text = ayah((s, a))
        if not any(word == V.skeleton(w) or (len(word) > 2 and word in V.skeleton(w)) for w in text.split(" ")):
            R1.fail("ayah %s does not contain %s" % (refkey, word))
        duas.append({"s": s, "a": a, "text": text, "name": names[s]})
    i18n = I.build_i18n("extras")
    keys = json.load(io.open(os.path.join(I.I18N, "extras", "keys.json"), encoding="utf-8"))
    texts = {k["id"]: dict({"ar": k["ar"], "en": k["en"]}, **{c: i18n["tr"][c][k["id"]] for c in I.LANG_CODES}) for k in keys}
    data = {"t": texts, "fatiha": {"name": names[1], "ayahs": fatiha}, "marked": MARKED, "duas": duas, "dhikr": DHIKR,
            "adhkar": ADHKAR, "reciters": RECITERS, "tafsirs": TAFSIRS}
    js = JS % {"data": json.dumps(data, ensure_ascii=False)}
    for page, phone in PAGES.items():
        path = os.path.join(HERE, "..", page)
        html = ensure_markers(open(path, encoding="utf-8", newline="").read(), page)
        html = R1.replace_block(html, "/*EXTRAS-CSS-BEGIN*/", "/*EXTRAS-CSS-END*/", CSS)
        html = R1.replace_block(html, "<!--EXTRAS-HTML-BEGIN-->", "<!--EXTRAS-HTML-END-->", phones(phone))
        html = R1.replace_block(html, "/*EXTRAS-JS-BEGIN*/", "/*EXTRAS-JS-END*/", js)
        open(path, "w", encoding="utf-8", newline="\n").write(html)
        print("written the new screens into %s" % page)
    print("ayahs copied from Tanzil and checked: Al-Fatihah 1-7, %s" % ", ".join(DUAS))


if __name__ == "__main__":
    main()
