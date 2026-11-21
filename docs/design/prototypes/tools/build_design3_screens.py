"""Design 3 only: the remaining screens, in six batches (the author approved them all on 2026-11-21: «الأقتراحات يمكنك
عملها الأن, اوافق عليها كلها, اعملها كلها في تصميم 3»).

  1. Quran and listening — reciter picker, player (F3, F4, F11), search (F16), tafsir (F5), a tajweed lesson (F6), radio (F7)
  2. Prayer — adhan settings (F9), Qibla (F10), the last third of the night (F36), blessed days (F35), tracker (F37),
     nearby mosques (F46)
  3. Knowledge — hadith with every scholar's ruling (F13), virtues (F29), the book reader (F14), ethics and manners
     (F49, F50), word meanings and occasions of revelation (F34)
  4. Memorisation — hifz (F30), khatma (F31), notes (F32), share (F33)
  5. Guides and tools — guides (F40), kids (F41), Zakat (F42), ruqyah (F38)
  6. The app — settings with the settings file (F47), About (F15), widgets, watch and car (F43 – F45)

What is real on these screens, and where it comes from:
  - every ayah is copied by script from the untouched Tanzil file (its SHA-256 checked) and its words checked;
  - the search results are found by script in that text (whole words only) and marked as a sample;
  - reciters and their recitation styles: AGENTS.md §7.3 (checked on mp3quran.net and EveryAyah, 2026-11-16);
  - the radio names: mp3quran.net/api/v3/radios, read 2026-11-21 (Warsh channels left out: the text shown is Hafs);
  - the Qibla bearing: calculated here from sample coordinates (Cairo) to the Kaaba;
  - the last third of the night: calculated from the sample Maghrib and Fajr of the prayer screen;
  - the blessed days: their Hijri dates (fixed) shown in the platform's Umm al-Qura calendar.
Everything else religious — a hadith, a ruling, a tafsir, a guide's steps, the nisab, the ruqyah's order — is a dashed
placeholder naming the source it will be copied from (AGENTS.md §6.10). No picture of a person, no cross shape.
Interface texts: i18n/design3-screens/ (write_design3_screens_i18n.py). Run after build_design3.py.
"""
import io
import json
import math
import os
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_round1 as R1  # noqa: E402
import i18n_check as I  # noqa: E402
import verify_mushaf_layout as V  # noqa: E402

PAGE = os.path.join(HERE, "..", "round-3.html")

# AGENTS.md §7.3 — complete recitations only (Rifaat and al-Bahtimi left out: no complete mushaf found)
RECITERS = [  # Arabic, transliteration, {style: surahs, or "ayah" for per-ayah files}, note key
    ("محمد صديق المنشاوي", "Muhammad Siddiq al-Minshawi", {"p_murattal": 114, "p_mujawwad": 114, "p_muallim": 114}, None),
    ("محمود خليل الحصري", "Mahmoud Khalil al-Husary", {"p_murattal": 114, "p_mujawwad": 114, "p_muallim": "ayah"}, None),
    ("عبد الباسط عبد الصمد", "Abdul Basit Abdul Samad", {"p_murattal": 114, "p_mujawwad": 114}, None),
    ("محمد محمود الطبلاوي", "Muhammad Mahmoud al-Tablawi", {"p_murattal": 114, "p_mujawwad": 114}, None),
    ("ماهر المعيقلي", "Maher al-Muaiqly", {"p_murattal": 114, "p_mujawwad": 114, "p_muallim": 38}, None),
    ("أيمن رشدي سويد", "Ayman Rushdi Suwayd", {"p_muallim": 114}, None),
    ("ياسر الدوسري", "Yasser al-Dosari", {"": 114}, None), ("عبد الرحمن السديس", "Abdul Rahman al-Sudais", {"": 114}, None),
    ("سعود الشريم", "Saud al-Shuraim", {"": 114}, None), ("فارس عباد", "Fares Abbad", {"": 114}, None),
    ("سعد الغامدي", "Saad al-Ghamdi", {"": 114}, None), ("علي بن عبد الرحمن الحذيفي", "Ali al-Hudhaifi", {"": 114}, None),
    ("نورين محمد صديق", "Noreen Muhammad Siddiq", {"": 114}, "p_riwayah"),
]
# mp3quran.net/api/v3/radios (language=ar and language=eng), read 2026-11-21 — id, Arabic, English; sample states
RADIOS = [(109082, "إذاعة القرآن الكريم - السعودية", "Holy Quran from Saudia Arabia", "live"),
          (69, "محمد صديق المنشاوي", "Radio Mohammed Siddiq Al-Minshawi", "live"),
          (74, "محمود خليل الحصري", "Radio Mahmoud Khalil Al-Hussary", "reconnect"),
          (32, "عبدالباسط عبدالصمد", "Radio Abdulbasit Abdulsamad", "live"),
          (64, "محمد الطبلاوي", "Radio Mohammad Al-Tablaway", "hidden"),
          (63, "ماهر المعيقلي", "Radio Maher Al Meaqli", "live")]
TAFSIR_BOOKS = [("المختصر في التفسير", "al-Mukhtasar fi al-Tafsir", "QuranEnc"), ("التفسير الميسر", "al-Tafsir al-Muyassar", "QuranEnc"),
                ("تفسير السعدي", "Tafsir al-Sa'di", "QuranEnc"), ("تفسير ابن كثير", "Tafsir Ibn Kathir", "Quran Foundation"),
                ("تفسير الطبري", "Tafsir al-Tabari", "Quran Foundation"), ("تفسير القرطبي", "Tafsir al-Qurtubi", "Quran Foundation"),
                ("تفسير البغوي", "Tafsir al-Baghawi", "Quran Foundation")]
TAJWEED_TOPICS = [("النون الساكنة والتنوين", "Nun sakinah and tanwin"), ("الميم الساكنة", "Mim sakinah"),
                  ("النون والميم المشددتان", "The doubled nun and mim"), ("اللام", "The lam"), ("المدود", "The madd"),
                  ("مخارج الحروف", "Where the letters are pronounced"), ("صفات الحروف", "The qualities of the letters"),
                  ("التفخيم والترقيق", "Heavy and light letters"), ("المتماثلان والمتجانسان والمتقاربان", "Similar and close letters"),
                  ("الوقف والابتداء", "Stopping and starting")]          # AGENTS.md §8.7
LESSON = (("الإظهار الحلقي", "al-Izhar al-Halqi"), "ء هـ ع ح غ خ",
          ("تحفة الأطفال — سليمان الجمزوري", "Tuhfat al-Atfal — Sulayman al-Jamzuri"))
HADITH_BOOKS = [("الأربعون النووية", "al-Arba'un al-Nawawiyyah"), ("صحيح البخاري", "Sahih al-Bukhari"), ("صحيح مسلم", "Sahih Muslim")]
WORD_SOURCES = [("كتاب في غريب القرآن — ☐ يُختار ويُطلب حقه", "A book of the rare words of the Quran — ☐ to be chosen and cleared"),
                ("أسباب النزول — الواحدي ☐", "Asbab al-Nuzul — al-Wahidi ☐")]
BOOK = ("الداء والدواء (الجواب الكافي) — ابن القيم", "al-Da' wa al-Dawa' (al-Jawab al-Kafi) — Ibn al-Qayyim")
LETTERS = "ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي".split()
KIDS = [114, 113, 112, 111, 110, 109, 108, 107, 106, 105]
KAABA, SAMPLE_PLACE = (21.4225, 39.8262), (30.0444, 31.2357)     # the Kaaba; Cairo, the sample place of the prayer screen
SAMPLE_NIGHT = ((17, 2), (4, 48))                                  # Maghrib 5:02 PM, Fajr 4:48 AM — the prayer screen's sample
SEARCH = ("الصبر", {"الصبر", "بالصبر", "والصبر", "فالصبر"})          # the query, and the whole words that match it here
KHATMA = (30, 12)                                                  # days, today's day


def bearing(a, b):
    p1, p2, dl = math.radians(a[0]), math.radians(b[0]), math.radians(b[1] - a[1])
    x = math.sin(dl) * math.cos(p2)
    y = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)
    return round((math.degrees(math.atan2(x, y)) + 360) % 360)


SCREENS = [  # caption, title key, element id, icon
    ("Batch 1 · Choose a reciter — complete recitations only (F3, F4)", "p_choose", "d3-reciters", "i-search"),
    ("Batch 1 · The player — one surah, a range, or to the end and again; reconnecting (F3, F11)", "t_f3", "d3-player", "i-ear"),
    ("Batch 1 · Quran search — a word, a surah, an ayah (F16)", "t_f16", "d3-search", "i-search"),
    ("Batch 1 · Tafsir — all the tafsirs of an ayah (F5)", "t_f5", "d3-tafsir", "i-tafsir"),
    ("Batch 1 · A tajweed lesson (F6)", "t_f6", "d3-tajweed", "i-madd"),
    ("Batch 1 · Radio — streams the broadcasters publish (F7, F11)", "t_f7", "d3-radio", "i-radio"),
    ("Batch 2 · Adhan settings — the only notification (F9)", "t_f9", "d3-adhan", "i-shadow"),
    ("Batch 2 · Qibla (F10)", "t_f10", "d3-qibla", "i-kaaba"),
    ("Batch 2 · The last third of the night (F36)", "t_f36", "d3-night", "i-moon"),
    ("Batch 2 · Blessed days (F35)", "t_f35", "d3-days", "i-ex-cal"),
    ("Batch 2 · Prayer and fasting tracker (F37)", "t_f37", "d3-tracker", "i-mark"),
    ("Batch 2 · Nearby mosques — OpenStreetMap (F46)", "t_f46", "d3-mosques", "i-pin"),
    ("Batch 3 · Hadith — every scholar's ruling (F13)", "t_f13", "d3-hadith", "i-sheet"),
    ("Batch 3 · Virtues — authentic hadiths only (F29)", "t_f29", "d3-virtues", "i-search"),
    ("Batch 3 · The book reader (F14)", "", "d3-bookread", "i-qalam"),
    ("Batch 3 · Ethics and conduct · Islamic manners — from Dorar (F49, F50)", "t_f49", "d3-akhlaq", "i-search"),
    ("Batch 3 · Word meanings and occasions of revelation (F34)", "t_f34", "d3-words", "i-tafsir"),
    ("Batch 4 · Memorisation (F30)", "t_f30", "d3-hifz", "i-d3-hifz"),
    ("Batch 4 · Khatma and daily portion (F31)", "t_f31", "d3-khatma", "i-book"),
    ("Batch 4 · My notes (F32)", "t_f32", "d3-notes", "i-mark"),
    ("Batch 4 · Share an ayah (F33)", "t_f33", "d3-share", "i-mark"),
    ("Batch 5 · Guides: wudu, prayer, Hajj, Umrah (F40)", "t_f40", "d3-guides", "i-search"),
    ("Batch 5 · Kids (F41)", "t_f41", "d3-kids", "i-ear"),
    ("Batch 5 · Zakat calculator (F42)", "t_f42", "d3-zakat", "i-search"),
    ("Batch 5 · Ruqyah (F38)", "t_f38", "d3-ruqyah", "i-book"),
    ("Batch 6 · Settings, with the settings file (F47)", "st_title", "d3-settings", "i-search"),
    ("Batch 6 · About (F15)", "t_f15", "d3-about", "i-mark"),
    ("Batch 6 · Widgets, watch and car (F43, F44, F45)", "t_f43", "d3-devices", "i-search"),
]

PHONE = """  <div class="unit"><div class="cap">%(cap)s</div>
  <div class="phone parch screen lives extras">
    <div class="topbar"><div class="title kufi"><span%(title)s></span><div class="sub" id="%(id)s-sub"></div></div>%(icon)s</div>
    <div class="lv-body" id="%(id)s"></div>
  </div></div>
"""

CSS = """/* design 3 only — the remaining screens (build_design3_screens.py, 2026-11-21) */
.s3-row{display:flex;align-items:center;gap:8px;padding:7px 10px;border-radius:10px;background:var(--surface);border:1px solid var(--border);font-size:12.5px}
.s3-row .n{flex:1;font-weight:700}
.s3-row .v{font-size:11.5px;color:var(--muted)}
.s3-chip{display:inline-block;font-size:10.5px;border:1px solid var(--border);border-radius:999px;padding:1px 8px;margin:2px 2px 0 0;background:var(--bg)}
.s3-chip.on{background:var(--primary);color:var(--lv-on,var(--onprimary));border-color:var(--primary)}
.s3-note{font-size:11px;color:var(--muted);line-height:1.55}
.s3-big{font-size:30px;font-weight:700;color:var(--primary);text-align:center;font-variant-numeric:tabular-nums}
.s3-bar{height:6px;border-radius:4px;background:var(--lv-soft,var(--surface2));overflow:hidden}
.s3-bar i{display:block;height:100%;background:var(--primary)}
.s3-banner{border-radius:12px;padding:8px 10px;background:var(--dotsoft);color:var(--dot);font-size:11.5px;line-height:1.5}
.s3-banner b{display:block;font-size:13px}
.s3-ctl{display:flex;justify-content:center;gap:18px;align-items:center}
.s3-ctl svg{width:26px;height:26px;fill:var(--primary)}
.s3-ctl .pl{width:46px;height:46px;border-radius:50%;background:var(--primary);display:grid;place-items:center}
.s3-ctl .pl svg{fill:var(--lv-on,var(--onprimary));width:20px;height:20px}
.s3-input{border:1px solid var(--border);border-radius:12px;padding:8px 11px;background:var(--surface);font-size:14px;display:flex;gap:8px;align-items:center}
.s3-input .ic{width:18px;height:18px;color:var(--muted)}
.s3-ayah{direction:rtl;font-family:"Amiri Quran",serif;font-size:18px;line-height:2.1;color:var(--ink);background:var(--page);border-radius:8px;padding:2px 10px;text-align:right}
.s3-ayah mark{background:var(--dotsoft);color:inherit;border-radius:4px;padding:0 2px}
.s3-ayah .hid{display:inline-block;width:3.2em;height:.9em;border-bottom:2px dashed var(--rule);vertical-align:middle}
.s3-ayah .nn{font-family:"Amiri Quran",serif;color:var(--dot)}
.s3-grid{display:grid;gap:4px;font-size:11px;text-align:center;align-items:center}
.s3-grid .h{color:var(--muted);font-weight:700}
.s3-grid .c{height:22px;border-radius:6px;border:1px solid var(--border);background:var(--surface)}
.s3-grid .c.y{background:var(--secondsoft);border-color:var(--second)}
.s3-letters{display:grid;grid-template-columns:repeat(7,1fr);gap:5px;direction:rtl}
.s3-letters span{font-family:"Amiri",serif;font-size:21px;text-align:center;border:1px solid var(--border);border-radius:9px;background:var(--surface);padding:2px 0}
.s3-dot{width:9px;height:9px;border-radius:50%;flex:none;background:var(--second)}
.s3-dot.reconnect{background:var(--dot)}
.s3-dot.hidden{background:transparent;border:1.5px dashed var(--muted)}
.s3-svg{display:block;margin:0 auto}
.s3-dev{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.s3-widget{border-radius:16px;padding:9px 11px;background:var(--surface);border:1px solid var(--border);font-size:11.5px;display:flex;flex-direction:column;gap:3px}
.s3-watch{width:112px;height:112px;border-radius:50%;background:#111;color:#eee;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;font-size:10.5px;margin:0 auto;border:4px solid #333}
.s3-watch b{font-size:17px;color:#fff}
.s3-car{border-radius:12px;background:#15181c;color:#e8e8e8;padding:10px 12px;display:flex;align-items:center;gap:10px;font-size:11.5px}
.s3-car .pl{width:34px;height:34px;border-radius:50%;background:#2c7a5b;display:grid;place-items:center}
.s3-car .pl svg{width:14px;height:14px;fill:#fff}
"""

JS = r"""window.D3S = (function () {
  var D = %(data)s;
  var RTL = ["ar", "ur", "fa", "ps"], DIG = "٠١٢٣٤٥٦٧٨٩", cur = "ar", tab = { ak: 0, gd: 0 };
  function T(id, vars) {
    var e = D.t[id], s = e[cur] || e.en;
    return vars ? s.replace(/\{(\w+)\}/g, function (m, k) { return vars[k] != null ? vars[k] : m; }) : s;
  }
  function tag(cal) {
    var u = [];
    if (cal) u.push("ca-" + cal);
    if (cur === "ar") u.push("nu-arab");
    if (cur === "ps") u.push("nu-arabext");
    return ({ zh: "zh-CN" }[cur] || cur) + (u.length ? "-u-" + u.join("-") : "");
  }
  function num(n, opt) {
    if (cur === "ar" && !opt) return String(n).replace(/[0-9]/g, function (d) { return DIG[d]; });
    try { return new Intl.NumberFormat(tag(), Object.assign({ useGrouping: false }, opt || {})).format(n); } catch (e) { return String(n); }
  }
  function arnum(n) { return String(n).replace(/[0-9]/g, function (d) { return DIG[d]; }); }
  function clock(h, m) {
    try { return new Intl.DateTimeFormat(tag(), { hour: "numeric", minute: "2-digit" }).format(new Date(2026, 10, 21, h, m)); }
    catch (e) { return h + ":" + (m < 10 ? "0" : "") + m; }
  }
  function nm(p) { return RTL.indexOf(cur) >= 0 ? p[0] : p[1]; }
  function sname(s) { return RTL.indexOf(cur) >= 0 ? D.names[s][0] : D.names[s][1]; }
  function ref(s, a, b) {
    var r = b && b !== a ? num(a) + "–" + num(b) : num(a);
    return cur === "ar" ? "سورة " + D.names[s][0] + " · " + r : sname(s) + " " + num(s) + ":" + r;
  }
  function el(t, cls, text) { var e = document.createElement(t); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function host(id) { var h = document.getElementById(id); h.textContent = ""; return h; }
  function sub(id, text) { document.getElementById(id + "-sub").textContent = text || ""; }
  function card(h, title) { var c = el("div", "lv-card"); if (title) c.appendChild(el("h4", null, title)); h.appendChild(c); return c; }
  function ph(box, text) { var p = el("div", "lv-ph", text || T("g_ph")); box.appendChild(p); return p; }
  function note(box, text) { box.appendChild(el("div", "s3-note", text)); }
  function chip(box, text, on) { box.appendChild(el("span", "s3-chip" + (on ? " on" : ""), text)); }
  function row(box, n, v, lead) {
    var r = el("div", "s3-row"); if (lead) r.appendChild(lead);
    r.appendChild(el("span", "n", n)); if (v != null) r.appendChild(el("span", "v", v)); box.appendChild(r); return r;
  }
  function bars(box) { var b = el("div", "lv-bars"); b.innerHTML = "<i></i><i></i><i></i>"; box.appendChild(b); }
  function ayahBox(box, ayahs, s, opt) {   /* ayahs as Tanzil gives them; marks and hidden words are a display layer */
    var a = el("div", "s3-ayah"); a.dir = "rtl"; a.lang = "ar";
    ayahs.forEach(function (x) {
      x.t.split(" ").forEach(function (w, i) {
        if (opt && opt.hide && opt.hide(x.n, i)) a.appendChild(el("span", "hid"));
        else if (opt && opt.mark === x.n + ":" + i) a.appendChild(el("mark", null, w));
        else a.appendChild(document.createTextNode(w));
        a.appendChild(document.createTextNode(" "));
      });
      a.appendChild(el("span", "nn", "۝" + arnum(x.n))); a.appendChild(document.createTextNode(" "));
    });
    box.appendChild(a);
    if (s) box.appendChild(el("div", "lv-ref", ref(s, ayahs[0].n, ayahs[ayahs.length - 1].n)));
  }
  function svg(w, h, inner) { var s = document.createElementNS("http://www.w3.org/2000/svg", "svg"); s.setAttribute("viewBox", "0 0 " + w + " " + h); s.setAttribute("width", w); s.setAttribute("height", h); s.setAttribute("class", "s3-svg"); s.innerHTML = inner; return s; }
  var PLAY = "<path d='M7 4.5v15l13-7.5z'/>", PREV = "<path d='M18 5v14L8 12zM6 5h2v14H6z'/>", NEXT = "<path d='M6 5v14l10-7zM16 5h2v14h-2z'/>";
  function ctl(box, mid) {
    var c = el("div", "s3-ctl");
    c.appendChild(svg(24, 24, RTL.indexOf(cur) >= 0 ? NEXT : PREV));
    var p = el("div", "pl"); p.appendChild(svg(24, 24, mid || PLAY)); c.appendChild(p);
    c.appendChild(svg(24, 24, RTL.indexOf(cur) >= 0 ? PREV : NEXT));
    box.appendChild(c);
  }
  var PRAYERS = ["pr_fajr", "pr_dhuhr", "pr_asr", "pr_maghrib", "pr_isha"];

  /* ---------- batch 1 ---------- */
  function reciters() {
    var h = host("d3-reciters"); sub("d3-reciters", T("p_complete"));
    D.reciters.forEach(function (r, i) {
      var c = el("div", "lv-card" + (i === 0 ? " d3-bk on" : "")); c.appendChild(el("div", "nm", nm(r))).style.fontWeight = "700";
      var ch = el("div");
      Object.keys(r[2]).forEach(function (k) {
        var v = r[2][k];
        chip(ch, (k ? T(k) + " · " : "") + (v === "ayah" ? T("p_ayahfiles") : T("p_surahs", { n: num(v) })), i === 0 && k === "p_murattal");
      });
      c.appendChild(ch);
      if (r[3]) note(c, T(r[3]));
      h.appendChild(c);
    });
  }
  function player() {
    var h = host("d3-player"), r = D.reciters[0]; sub("d3-player", nm(r) + " · " + T("p_murattal"));
    var c = card(h, T("p_now"));
    ayahBox(c, [D.player.ayah], D.player.s);
    var b = el("div", "s3-bar"); b.innerHTML = "<i style='width:34%%'></i>"; c.appendChild(b);
    ctl(c, "<path d='M7 5h3.5v14H7zM13.5 5H17v14h-3.5z'/>");
    var m = card(h); var ch = el("div");
    ["p_m_surah", "p_m_range", "p_m_endless"].forEach(function (k, i) { chip(ch, T(k), i === 2); }); m.appendChild(ch);
    var ban = el("div", "s3-banner"); ban.appendChild(el("b", null, T("p_reconnect"))); ban.appendChild(document.createTextNode(T("p_reconnect_note")));
    h.appendChild(ban); note(h, T("g_sample"));
  }
  function search() {
    var h = host("d3-search"), S = D.search; sub("d3-search", T("s_results", { n: num(S.n) }));
    var inp = el("div", "s3-input"); inp.innerHTML = "<svg class='ic'><use href='#i-search'/></svg>";
    var q = el("span", null, S.q); q.dir = "rtl"; q.lang = "ar"; inp.appendChild(q); h.appendChild(inp);
    var ch = el("div"); ["s_k_word", "s_k_surah", "s_k_ayah"].forEach(function (k, i) { chip(ch, T(k), i === 0); }); h.appendChild(ch);
    S.results.forEach(function (r) { var c = card(h); ayahBox(c, [{ n: r.a, t: r.t }], r.s, { mark: r.a + ":" + r.w }); });
    note(h, T("s_note"));
  }
  function tafsir() {
    var h = host("d3-tafsir"); sub("d3-tafsir", ref(1, 2));
    var c = card(h); ayahBox(c, [D.tafsir.ayah], 1);
    h.appendChild(el("div", "d3-g")).appendChild(el("h4", null, T("t_all")));
    D.tafsir.books.forEach(function (b, i) {
      var k = card(h, nm(b)); k.appendChild(el("div", "lv-src", T("g_from", { src: b[2] })));
      if (i < 2) ph(k);
    });
  }
  function tajweed() {
    var h = host("d3-tajweed"), L = D.lesson; sub("d3-tajweed", nm(D.topics[0]));
    var ch = el("div"); D.topics.forEach(function (t, i) { chip(ch, nm(t), i === 0); }); h.appendChild(ch);
    var c = card(h, nm(L[0]));
    c.appendChild(el("div", "lv-ref", T("tj_letters")));
    var lt = el("div", "s3-big", L[1]); lt.dir = "rtl"; lt.lang = "ar"; lt.style.fontFamily = "Amiri,serif"; c.appendChild(lt);
    var m = card(h, T("tj_memory")); ph(m); m.appendChild(el("div", "lv-src", T("g_from", { src: nm(L[2]) })));
    var e = card(h, T("tj_examples")); ph(e);
    note(h, T("tj_review"));
  }
  function radio() {
    var h = host("d3-radio"); sub("d3-radio", T("r_list"));
    D.radios.forEach(function (r) {
      var d = el("span", "s3-dot " + r[3]);
      row(h, RTL.indexOf(cur) >= 0 ? r[1] : r[2], r[3] === "live" ? T("r_live") : r[3] === "reconnect" ? T("p_reconnect") : T("r_hidden"), d);
    });
    note(h, T("g_from", { src: "mp3quran.net/api/v3/radios · 2026-11-21" }) + " · " + T("g_sample"));
    var ban = el("div", "s3-banner"); ban.appendChild(el("b", null, T("p_reconnect"))); ban.appendChild(document.createTextNode(T("p_reconnect_note"))); h.appendChild(ban);
  }

  /* ---------- batch 2 ---------- */
  function adhan() {
    var h = host("d3-adhan"); sub("d3-adhan", T("g_noremind"));
    PRAYERS.forEach(function (p, i) {
      var c = card(h, T(p)); var ch = el("div");
      ["a_full", "a_short", "a_none"].forEach(function (k, j) { chip(ch, T(k), j === (i === 4 ? 2 : i === 0 ? 0 : 1)); });
      c.appendChild(ch);
    });
    var m = card(h, T("a_muezzin")); ph(m, T("a_no_rec"));
    note(h, T("a_ios")); note(h, T("a_web"));
  }
  function qibla() {
    var h = host("d3-qibla"), b = D.qibla; sub("d3-qibla", T("g_sample"));
    var ticks = "";
    for (var i = 0; i < 36; i++) { var a = i * 10 * Math.PI / 180; ticks += "<circle cx='" + (100 + 82 * Math.sin(a)).toFixed(1) + "' cy='" + (100 - 82 * Math.cos(a)).toFixed(1) + "' r='" + (i %% 9 === 0 ? 3 : 1.4) + "' fill='currentColor' opacity='.55'/>"; }
    var r = b * Math.PI / 180, x = 100 + 64 * Math.sin(r), y = 100 - 64 * Math.cos(r);
    var inner = "<g style='color:var(--muted)'><circle cx='100' cy='100' r='92' fill='var(--surface)' stroke='var(--border)' stroke-width='2'/>" + ticks + "</g>" +
      "<path d='M100 10 l-6 12 h12z' fill='var(--muted)'/>" +
      "<line x1='100' y1='100' x2='" + x.toFixed(1) + "' y2='" + y.toFixed(1) + "' stroke='var(--primary)' stroke-width='4' stroke-linecap='round'/>" +
      "<circle cx='100' cy='100' r='6' fill='var(--primary)'/>" +
      "<rect x='" + (x - 9).toFixed(1) + "' y='" + (y - 9).toFixed(1) + "' width='18' height='18' rx='2' fill='#1b1b1b' stroke='var(--dot)' stroke-width='2'/>";
    h.appendChild(svg(200, 200, inner));
    h.appendChild(el("div", "s3-big", T("q_deg", { d: num(b) })));
    note(h, T("q_calc")); note(h, T("q_calib")); note(h, T("q_web"));
  }
  function night() {
    var h = host("d3-night"), m = D.night, mg = m[0][0] * 60 + m[0][1], fj = m[1][0] * 60 + m[1][1] + 1440;
    var start = mg + Math.round((fj - mg) * 2 / 3), sh = Math.floor(start / 60) %% 24, sm = start %% 60;
    sub("d3-night", T("g_sample"));
    var c = card(h); c.appendChild(el("div", "lv-ref", T("n_from", { a: clock(m[0][0], m[0][1]), b: clock(m[1][0], m[1][1]) })));
    c.appendChild(el("div", "lv-ref", T("n_starts"))); c.appendChild(el("div", "s3-big", clock(sh, sm)));
    var hd = card(h); ph(hd, T("n_hadith"));
    note(h, T("g_noremind"));
  }
  function days() {
    var h = host("d3-days"); sub("d3-days", T("g_noremind"));
    function parts(d) {
      var o = {};
      try { new Intl.DateTimeFormat("en-u-ca-islamic-umalqura", { day: "numeric", month: "numeric" }).formatToParts(d).forEach(function (p) { o[p.type] = Number(p.value); }); } catch (e) {}
      return o;
    }
    function next(mo, da) {
      var t = new Date(); for (var i = 0; i < 400; i++) { var d = new Date(t.getTime() + i * 864e5), p = parts(d); if (p.month === mo && p.day === da) return d; } return null;
    }
    function hdate(d, opt) { try { return new Intl.DateTimeFormat(tag("islamic-umalqura"), opt || { day: "numeric", month: "long" }).format(d); } catch (e) { return ""; } }
    [["dy_ramadan", 9, 1, { month: "long" }], ["dy_fitr", 10, 1], ["dy_arafah", 12, 9], ["dy_adha", 12, 10], ["dy_ashura", 1, 10]].forEach(function (x) {
      var d = next(x[1], x[2]); row(h, T(x[0]), d ? hdate(d, x[3]) : "");
    });
    row(h, T("dy_white"), T("dy_month")); row(h, T("dy_monthu"), T("dy_every"));
    var c = card(h); ph(c, T("dy_hadith"));
  }
  function tracker() {
    var h = host("d3-tracker"); sub("d3-tracker", T("g_device"));
    var g = el("div", "s3-grid"); g.style.gridTemplateColumns = "auto repeat(7,1fr)";
    var base = new Date(2026, 10, 15);
    g.appendChild(el("span"));
    for (var i = 0; i < 7; i++) { var dn = ""; try { dn = new Intl.DateTimeFormat(tag(), { weekday: "short" }).format(new Date(base.getTime() + i * 864e5)); } catch (e) {} g.appendChild(el("span", "h", dn)); }
    PRAYERS.concat(["tr_fast"]).forEach(function (p, r) {
      g.appendChild(el("span", "h", T(p)));
      for (var j = 0; j < 7; j++) g.appendChild(el("span", "c" + ((r * 3 + j * 2) %% 5 !== 0 && j < 6 ? (p === "tr_fast" ? (j === 1 || j === 4 ? " y" : "") : " y") : "")));
    });
    h.appendChild(g); note(h, T("g_sample") + " · " + T("g_noremind"));
  }
  function mosques() {
    var h = host("d3-mosques"); sub("d3-mosques", T("m_loc"));
    /* streets meet only at T-junctions — no four-way crossing, so no cross shape (AGENTS.md §8.10) */
    var roads = "<rect width='300' height='210' fill='var(--page)'/><path d='M0 70 H300 M90 70 V210 M210 0 V70 M90 150 H300 M0 192 Q45 160 90 178' stroke='var(--border)' stroke-width='9' fill='none' stroke-linecap='butt'/>" +
      "<rect x='225' y='85' width='60' height='50' rx='8' fill='var(--secondsoft)'/>";
    function pin(x, y) { return "<path d='M" + x + " " + y + " c-8 -10 -11 -14 -11 -20 a11 11 0 0 1 22 0 c0 6 -3 10 -11 20z' fill='var(--primary)'/><circle cx='" + x + "' cy='" + (y - 20) + "' r='4' fill='var(--surface)'/>"; }
    var me = "<circle cx='150' cy='110' r='14' fill='var(--primary)' opacity='.18'/><circle cx='150' cy='110' r='6' fill='var(--primary)' stroke='#fff' stroke-width='2'/>";
    h.appendChild(svg(300, 210, roads + pin(70, 60) + pin(230, 150) + pin(120, 190) + me));
    [[320], [540], [880]].forEach(function (d) { row(h, T("m_name"), num(d[0], { style: "unit", unit: "meter", useGrouping: true })); });
    var at = el("div", "s3-note", "© OpenStreetMap contributors (ODbL)"); at.dir = "ltr"; h.appendChild(at);
    note(h, T("g_sample"));
  }

  /* ---------- batch 3 ---------- */
  function hadith() {
    var h = host("d3-hadith"); sub("d3-hadith", nm(D.hadithBooks[0]));
    var ch = el("div"); D.hadithBooks.forEach(function (b, i) { chip(ch, nm(b), i === 0); }); h.appendChild(ch);
    var t = card(h, T("h_text")); ph(t);
    var r = card(h, T("h_rulings"));
    for (var i = 0; i < 3; i++) ph(r, T("h_ruling_ph"));
    r.appendChild(el("div", "lv-src", T("g_dorar") + " · " + T("g_online")));
    note(h, T("h_offline"));
    var e = card(h, T("h_explain")); ph(e); e.appendChild(el("div", "lv-src", T("g_from", { src: "HadeethEnc · sunnah.com" })));
    var rep = el("button", "lv-report", T("g_report")); rep.type = "button"; h.appendChild(rep);
  }
  function virtues() {
    var h = host("d3-virtues"); sub("d3-virtues", T("v_only"));
    ["v_prayer", "v_surahs", "v_ayahs", "v_other"].forEach(function (k) { var c = card(h, T(k)); ph(c, T("h_ruling_ph") + " — " + T("g_ph")); });
  }
  function bookread() {
    var h = host("d3-bookread"), t = document.querySelector("[data-d3s-book]");
    t.textContent = nm(D.book); sub("d3-bookread", T("br_page", { v: num(1), p: num(1) }));
    var c = card(h, T("br_chapters")); for (var i = 0; i < 4; i++) bars(c);
    var p = card(h); ph(p); bars(p); bars(p);
    h.appendChild(el("div", "lv-ph", T("d3_edition_ph") ));
  }
  function akhlaq() {
    var h = host("d3-akhlaq"), seg = el("div", "d3-seg");
    ["t_f49", "t_f50"].forEach(function (k, i) {
      var b = el("button", null, T(k)); b.type = "button"; b.setAttribute("aria-pressed", String(tab.ak === i));
      b.addEventListener("click", function () { tab.ak = i; akhlaq(); }); seg.appendChild(b);
    });
    h.appendChild(seg); sub("d3-akhlaq", T("g_online"));
    for (var i = 0; i < 4; i++) { var c = card(h); ph(c, T("ak_topic")); }
    note(h, T("g_dorar"));
  }
  function words() {
    var h = host("d3-words"); sub("d3-words", ref(1, 2));
    var c = card(h); ayahBox(c, [D.words.ayah], 1);
    var m = card(h, T("w_meanings"));
    D.words.ayah.t.split(" ").forEach(function (w) { var r = row(m, "", "—"); var a = el("span", null, w); a.dir = "rtl"; a.lang = "ar"; a.style.fontFamily = "'Amiri Quran',serif"; r.querySelector(".n").appendChild(a); });
    m.appendChild(el("div", "lv-src", T("g_from", { src: nm(D.words.src[0]) })));
    var s = card(h, T("w_asbab")); ph(s); s.appendChild(el("div", "lv-src", T("g_from", { src: nm(D.words.src[1]) })));
  }

  /* ---------- batch 4 ---------- */
  function hifz() {
    var h = host("d3-hifz"), H = D.hifz; sub("d3-hifz", ref(H.s, H.ayahs[0].n, H.ayahs[H.ayahs.length - 1].n));
    var ch = el("div"); chip(ch, T("hf_hide"), true); h.appendChild(ch);
    var c = card(h); ayahBox(c, H.ayahs, null, { hide: function (n, i) { return (i + n) %% 4 === 1; } });
    var p = card(h, T("hf_progress", { n: num(3), m: num(H.ayahs.length) })); var b = el("div", "s3-bar"); b.innerHTML = "<i style='width:60%%'></i>"; p.appendChild(b);
    var r = card(h, T("hf_review")); r.appendChild(el("div", "s3-note", T("hf_days")));
    note(h, T("g_device") + " · " + T("g_noremind"));
  }
  function khatma() {
    var h = host("d3-khatma"), K = D.khatma; sub("d3-khatma", T("k_days", { n: num(K.days) }));
    var c = card(h, T("k_today")); c.appendChild(el("div", "s3-big", T("k_pages", { a: num(K.a), b: num(K.b) })));
    var p = card(h, T("k_progress", { p: num(K.p) })); var b = el("div", "s3-bar"); b.innerHTML = "<i style='width:" + K.p + "%%'></i>"; p.appendChild(b);
    note(h, T("g_device") + " · " + T("g_noremind"));
  }
  function notes() {
    var h = host("d3-notes"); sub("d3-notes", T("g_device"));
    [[2, 255], [67, 1]].forEach(function (x) { var c = card(h, ref(x[0], x[1])); bars(c); });
    var b = el("button", "lv-report", T("nt_add")); b.type = "button"; h.appendChild(b);
    note(h, T("g_sample"));
  }
  function share() {
    var h = host("d3-share"), S = D.share; sub("d3-share", ref(S.s, S.ayahs[0].n, S.ayahs[S.ayahs.length - 1].n));
    var c = card(h); ayahBox(c, S.ayahs, S.s);
    var ch = el("div"); chip(ch, T("sh_image")); chip(ch, T("sh_text"), true); h.appendChild(ch);
    note(h, T("sh_font"));
  }

  /* ---------- batch 5 ---------- */
  function guides() {
    var h = host("d3-guides"), seg = el("div", "d3-seg");
    ["gd_wudu", "v_prayer", "gd_hajj", "gd_umrah"].forEach(function (k, i) {
      var b = el("button", null, T(k)); b.type = "button"; b.setAttribute("aria-pressed", String(tab.gd === i));
      b.addEventListener("click", function () { tab.gd = i; guides(); }); seg.appendChild(b);
    });
    h.appendChild(seg); sub("d3-guides", T("gd_steps"));
    for (var i = 1; i <= 4; i++) {
      var c = el("div", "s3-row"); c.appendChild(el("span", "s3-chip on", num(i)));
      var p = el("div", "lv-ph", T("g_ph")); p.style.flex = "1"; c.appendChild(p);
      c.appendChild(svg(42, 30, "<rect x='2' y='2' width='38' height='26' rx='5' fill='none' stroke='var(--rule)' stroke-dasharray='3 3'/><path d='M8 22 L18 12 L26 18 L34 9' stroke='var(--muted)' fill='none'/>"));
      h.appendChild(c);
    }
    note(h, T("gd_rule")); note(h, T("gd_nusuk"));
  }
  function kids() {
    var h = host("d3-kids"); sub("d3-kids", T("kd_repeat"));
    var c = card(h, T("kd_surahs")), ch = el("div"); D.kids.forEach(function (s, i) { chip(ch, sname(s), i === 0); }); c.appendChild(ch);
    c.appendChild(el("div", "lv-src", T("g_reciter") + ": " + nm(D.reciters[1]) + " · " + T("p_muallim")));
    var l = card(h, T("kd_letters")), g = el("div", "s3-letters"); D.letters.forEach(function (x) { g.appendChild(el("span", null, x)); }); l.appendChild(g);
  }
  function zakat() {
    var h = host("d3-zakat"); sub("d3-zakat", T("g_sample"));
    [["z_cash", 25000], ["z_gold", 40], ["z_silver", 0], ["z_trade", 12000]].forEach(function (x) { row(h, T(x[0]), num(x[1], { useGrouping: true })); });
    var c = card(h, T("z_due")); c.appendChild(el("div", "s3-big", "—")); ph(c, T("z_rules"));
    note(h, T("z_noinh"));
  }
  function ruqyah() {
    var h = host("d3-ruqyah"); sub("d3-ruqyah", T("rq_src"));
    for (var i = 0; i < 4; i++) { var c = card(h); ph(c); }
  }

  /* ---------- batch 6 ---------- */
  function settings() {
    var h = host("d3-settings"), langsel = document.getElementById("langsel"), method = document.querySelector(".method b");
    sub("d3-settings", T("g_device"));
    row(h, T("t_f1"), langsel && langsel.selectedOptions[0] ? langsel.selectedOptions[0].textContent.split(" — ")[0] : "");
    row(h, T("t_f18"), ""); row(h, T("st_font"), nm(D.font)); row(h, T("g_reciter"), nm(D.reciters[0]));
    row(h, T("st_method"), method ? method.textContent : ""); row(h, T("st_asr"), nm(D.asr)); row(h, T("st_hijri"), num(0));
    row(h, T("t_f9"), "");
    var f = card(h, T("t_f47")); var ch = el("div"); chip(ch, T("st_export"), true); chip(ch, T("st_import")); f.appendChild(ch); note(f, T("st_file_note"));
    row(h, T("t_f17"), ""); row(h, T("t_f19"), ""); row(h, T("t_f15"), "");
  }
  function about() {
    var h = host("d3-about"); sub("d3-about", T("ab_version", { v: num("0.1") }));
    var c = card(h); var n = el("div", "s3-big", nm(D.app)); n.style.fontSize = "17px"; c.appendChild(n); note(c, T("ab_free"));
    var a = card(h, T("ab_by")); a.appendChild(el("div", "nm", nm(D.author))).style.fontWeight = "700";
    var l = el("a", "lv-link", "linkedin.com/in/omarsherif21"); l.href = "https://www.linkedin.com/in/omarsherif21/"; l.dir = "ltr"; a.appendChild(l);
    note(h, T("ab_privacy")); note(h, T("ab_draft"));
    row(h, T("t_f17"), ""); row(h, T("t_f19"), "");
  }
  function devices() {
    var h = host("d3-devices"); sub("d3-devices", T("dv_nonotif"));
    var w = el("div", "s3-widget"); w.appendChild(el("b", null, T("g_next") + " · " + T("pr_asr") + " " + clock(15, 12)));
    var hd = ""; try { hd = new Intl.DateTimeFormat(tag("islamic-umalqura"), { day: "numeric", month: "long", year: "numeric" }).format(new Date()); } catch (e) {}
    w.appendChild(el("span", null, hd)); w.appendChild(el("span", "lv-ref", T("dv_ayah"))); ayahBox(w, [D.share.ayahs[0]], D.share.s);
    h.appendChild(el("div", "d3-g")).appendChild(el("h4", null, T("t_f43"))); h.appendChild(w);
    var row2 = el("div", "s3-dev"), wb = el("div"); wb.appendChild(el("div", "d3-g")).appendChild(el("h4", null, T("t_f44")));
    var watch = el("div", "s3-watch"); watch.appendChild(el("span", null, T("pr_asr"))); watch.appendChild(el("b", null, clock(15, 12))); watch.appendChild(el("span", null, num(33)));
    wb.appendChild(watch); row2.appendChild(wb);
    var cb = el("div"); cb.appendChild(el("div", "d3-g")).appendChild(el("h4", null, T("t_f45")));
    var car = el("div", "s3-car"), pl = el("div", "pl"); pl.appendChild(svg(24, 24, PLAY)); car.appendChild(pl);
    var tx = el("div"); tx.appendChild(el("b", null, sname(D.player.s))); tx.appendChild(el("div", null, nm(D.reciters[0]))); car.appendChild(tx);
    cb.appendChild(car); row2.appendChild(cb); h.appendChild(row2);
    note(h, T("g_sample"));
  }

  function render(lang) {
    if (lang) cur = (lang === "ar" || lang === "en" || D.t.g_sample[lang]) ? lang : "en";
    document.querySelectorAll("[data-d3s]").forEach(function (e) { e.textContent = T(e.dataset.d3s); });
    reciters(); player(); search(); tafsir(); tajweed(); radio();
    adhan(); qibla(); night(); days(); tracker(); mosques();
    hadith(); virtues(); bookread(); akhlaq(); words();
    hifz(); khatma(); notes(); share();
    guides(); kids(); zakat(); ruqyah();
    settings(); about(); devices();
  }
  return { render: render };
})();
"""


def ensure_markers(html):
    if "/*D3S-CSS-BEGIN*/" in html:
        return html
    for a, b in [("/*D3-CSS-END*/\n", "/*D3-CSS-END*/\n/*D3S-CSS-BEGIN*/\n/*D3S-CSS-END*/\n"),
                 ("<!--D3-HTML-END-->\n", "<!--D3-HTML-END-->\n<!--D3S-HTML-BEGIN-->\n<!--D3S-HTML-END-->\n"),
                 ('<script id="design3">', '<script id="design3-screens">\n/*D3S-JS-BEGIN*/\n/*D3S-JS-END*/\n</script>\n<script id="design3">'),
                 ("    if (window.D3) window.D3.render(L());\n", "    if (window.D3) window.D3.render(L());\n    if (window.D3S) window.D3S.render(L());\n")]:
        if html.count(a) != 1:
            R1.fail("round-3.html: not found once: %s" % a[:70])
        html = html.replace(a, b)
    print("round-3.html: markers and hook of the remaining screens inserted")
    return html


def phones():
    out = []
    for cap, title, ident, icon in SCREENS:
        t = " data-d3s='%s'" % title if title else " data-d3s-book='1'"
        out.append(PHONE % {"cap": cap, "title": t, "id": ident, "icon": "<svg class='ic' style='color:var(--primary)'><use href='#%s'/></svg>" % icon})
    return "\n".join(out)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    rel = "tanzil/quran-uthmani.txt"
    R1.check_sources({rel: R1.SHA256[rel], "tanzil/quran-data.xml": R1.SHA256["tanzil/quran-data.xml"]})
    tanzil = V.parse_tanzil(os.path.join(R1.ASSETS, rel))
    root = ET.parse(os.path.join(R1.ASSETS, "tanzil/quran-data.xml")).getroot()
    names = {int(s.get("index")): [s.get("name"), s.get("tname")] for s in root.iter("sura")}

    def ayah(s, a):
        text = tanzil[(s, a)]
        if a == 1 and s not in (1, 9):
            text = " ".join(text.split(" ")[4:])   # Tanzil writes the basmala before ayah 1; it is not part of the ayah
        return {"n": a, "t": text}

    def check(s, a, word):
        if not any(word in V.skeleton(w) for w in ayah(s, a)["t"].split(" ")):
            R1.fail("ayah %d:%d does not contain %s" % (s, a, word))
    check(67, 1, "الملك"); check(1, 2, "الحمد"); check(94, 5, "العسر"); check(94, 6, "يسرا")
    # the search sample: whole words of the Uthmani text whose letters are the query (with a joined و / ب / ف)
    hits = []
    for (s, a) in sorted(tanzil):
        for i, w in enumerate(ayah(s, a)["t"].split(" ")):
            if V.skeleton(w) in SEARCH[1]:
                hits.append((s, a, i))
                break
    if not hits:
        R1.fail("the search sample found nothing")
    results = [{"s": s, "a": a, "w": i, "t": ayah(s, a)["t"]} for s, a, i in hits[:3]]
    day, (days, today) = None, KHATMA
    k_a, k_b = (today - 1) * 604 // days + 1, today * 604 // days
    keys = json.load(io.open(os.path.join(I.I18N, "design3-screens", "keys.json"), encoding="utf-8"))
    i18n = I.build_i18n("design3-screens")
    texts = {k["id"]: dict({"ar": k["ar"], "en": k["en"]}, **{c: i18n["tr"][c][k["id"]] for c in I.LANG_CODES}) for k in keys}
    d3 = I.build_i18n("design3")
    for k in json.load(io.open(os.path.join(I.I18N, "design3", "keys.json"), encoding="utf-8")):
        if k["id"] == "d3_edition_ph":
            texts[k["id"]] = dict({"ar": k["ar"], "en": k["en"]}, **{c: d3["tr"][c][k["id"]] for c in I.LANG_CODES})
    used = {s[1] for s in SCREENS if s[1]}
    missing = sorted(u for u in used if u not in texts)
    if missing:
        R1.fail("texts missing: %s" % missing)
    data = {
        "t": texts, "names": {s: names[s] for s in set([1, 2, 67, 94] + KIDS + [h[0] for h in hits[:3]])},
        "reciters": [list(r) for r in RECITERS], "radios": [list(r) for r in RADIOS],
        "player": {"s": 67, "ayah": ayah(67, 1)},
        "search": {"q": SEARCH[0], "n": len(hits), "results": results},
        "tafsir": {"ayah": ayah(1, 2), "books": [list(b) for b in TAFSIR_BOOKS]},
        "topics": TAJWEED_TOPICS, "lesson": LESSON, "qibla": bearing(SAMPLE_PLACE, KAABA), "night": SAMPLE_NIGHT,
        "hadithBooks": HADITH_BOOKS, "book": BOOK, "words": {"ayah": ayah(1, 2), "src": WORD_SOURCES},
        "hifz": {"s": 67, "ayahs": [ayah(67, a) for a in range(1, 6)]},
        "khatma": {"days": days, "a": k_a, "b": k_b, "p": round((k_a - 1) * 100 / 604)},
        "share": {"s": 94, "ayahs": [ayah(94, 5), ayah(94, 6)]}, "kids": KIDS, "letters": LETTERS,
        "font": ["مصحف المدينة ١٤٠٥هـ — مجمع الملك فهد", "Madinah mushaf 1405H — King Fahd Complex"],
        "asr": ["الشافعي · الحنفي", "Shafi'i · Hanafi"],
        "app": ["تجويد - القرآن الكريم وعلومه", "Tajweed - The Noble Quran and Its Sciences"],
        "author": ["عمر شريف — Omar Sherif", "Omar Sherif — عمر شريف"],
    }
    html = ensure_markers(open(PAGE, encoding="utf-8", newline="").read())
    html = R1.replace_block(html, "/*D3S-CSS-BEGIN*/", "/*D3S-CSS-END*/", CSS)
    html = R1.replace_block(html, "<!--D3S-HTML-BEGIN-->", "<!--D3S-HTML-END-->", phones())
    html = R1.replace_block(html, "/*D3S-JS-BEGIN*/", "/*D3S-JS-END*/", JS % {"data": json.dumps(data, ensure_ascii=False)})
    open(PAGE, "w", encoding="utf-8", newline="\n").write(html)
    print("round-3.html: %d screens written; search sample «%s»: %d ayahs; Qibla from the sample place %d°; khatma day %d: pages %d – %d"
          % (len(SCREENS), SEARCH[0], len(hits), data["qibla"], today, k_a, k_b))


if __name__ == "__main__":
    main()
