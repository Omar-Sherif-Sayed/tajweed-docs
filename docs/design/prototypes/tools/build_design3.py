"""Design 3 only (the author chose it on 2026-11-20): screens and changes that are made in round-3.html alone.

The author's message of 2026-11-21:
  - the list of scholars approved; add books such as «الداء والدواء» by Ibn al-Qayyim; the scholars ordered by group
    or by time;
  - the Names (of Allah and of the Prophet ﷺ) and other sections on the home screen above «السِّيَر», with the radio
    and the rest — the Lives last; where is the design of every feature?;
  - the Sources screen updated: what is verified and what is waiting.

What this script writes into round-3.html, between the D3-* marker comments (and one hook after the Extras):
  - home: four more tiles (the Names of Allah, the names of the Prophet ﷺ, memorisation, all sections), the home
    scrolls; the Lives row gets a fourth part, the scholars, and stays last;
  - «كل الأقسام»: every feature F1 – F51 by group, each marked drawn / inside another screen / to come, so the author
    sees which screens exist; a drawn one opens its screen;
  - F51 the scholars of Islam: the approved list, by group or by time (in order of death — the year of birth is not
    recorded for some and differs for others), and one sample entry (Ibn al-Qayyim) whose life and dates are
    placeholders naming the books of biographies they will be copied from, with his books linked to the library;
  - F14 the library: the scholars' books by subject, each edition a placeholder;
  - the Sources screen (F17) with four states: verified · letter sent, waiting · letter ready, to send · to check
    (docs/permissions/README.md, 2026-11-21).

Nothing religious is written here: names, titles and authors are data to be checked again against the chosen
editions (P8-D1, P9-D5); every date and every biography is a placeholder naming its source.
Interface texts: i18n/design3/ (write_design3_i18n.py, checked by i18n_check.py).
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_round1 as R1  # noqa: E402
import i18n_check as I  # noqa: E402

PAGE = os.path.join(HERE, "..", "round-3.html")

# ---- F51: the approved list (the author, 2026-11-21: «موافق»), by group, in the order of the proposal ----
GROUPS = ["d3_sg_imams", "d3_sg_salaf", "d3_sg_hadith", "d3_sg_huffaz", "d3_sg_tafsir", "d3_sg_aqeeda",
          "d3_sg_seerah", "d3_sg_qiraat", "d3_sg_recent"]
SCHOLARS = {   # id: Arabic, transliteration, group
    "abuhanifa": ("أبو حنيفة", "Abu Hanifa", 0), "malik": ("مالك بن أنس", "Malik ibn Anas", 0),
    "shafii": ("الشافعي", "al-Shafi'i", 0), "ahmad": ("أحمد بن حنبل", "Ahmad ibn Hanbal", 0),
    "ibnmusayyib": ("سعيد بن المسيب", "Sa'id ibn al-Musayyib", 1), "hasan": ("الحسن البصري", "al-Hasan al-Basri", 1),
    "ibnsirin": ("محمد بن سيرين", "Muhammad ibn Sirin", 1), "zuhri": ("الزهري", "al-Zuhri", 1),
    "thawri": ("سفيان الثوري", "Sufyan al-Thawri", 1), "awzai": ("الأوزاعي", "al-Awza'i", 1),
    "layth": ("الليث بن سعد", "al-Layth ibn Sa'd", 1), "ibnmubarak": ("عبد الله بن المبارك", "Abdullah ibn al-Mubarak", 1),
    "ibnuyaynah": ("سفيان بن عيينة", "Sufyan ibn Uyaynah", 1),
    "bukhari": ("البخاري", "al-Bukhari", 2), "muslim": ("مسلم", "Muslim", 2), "abudawud": ("أبو داود", "Abu Dawud", 2),
    "tirmidhi": ("الترمذي", "al-Tirmidhi", 2), "nasai": ("النسائي", "al-Nasa'i", 2), "ibnmajah": ("ابن ماجه", "Ibn Majah", 2),
    "darimi": ("الدارمي", "al-Darimi", 2), "ibnkhuzaymah": ("ابن خزيمة", "Ibn Khuzaymah", 2), "ibnhibban": ("ابن حبان", "Ibn Hibban", 2),
    "daraqutni": ("الدارقطني", "al-Daraqutni", 2), "hakim": ("الحاكم", "al-Hakim", 2), "bayhaqi": ("البيهقي", "al-Bayhaqi", 2),
    "ibnmain": ("يحيى بن معين", "Yahya ibn Ma'in", 2), "ibnmadini": ("علي بن المديني", "Ali ibn al-Madini", 2),
    "nawawi": ("النووي", "al-Nawawi", 3), "ibnabdalbarr": ("ابن عبد البر", "Ibn Abd al-Barr", 3), "mizzi": ("المزي", "al-Mizzi", 3),
    "dhahabi": ("الذهبي", "al-Dhahabi", 3), "ibnrajab": ("ابن رجب", "Ibn Rajab", 3), "ibnhajar": ("ابن حجر العسقلاني", "Ibn Hajar al-Asqalani", 3),
    "tabari": ("الطبري", "al-Tabari", 4), "baghawi": ("البغوي", "al-Baghawi", 4), "qurtubi": ("القرطبي", "al-Qurtubi", 4),
    "ibnkathir": ("ابن كثير", "Ibn Kathir", 4), "suyuti": ("السيوطي", "al-Suyuti", 4), "saadi": ("السعدي", "al-Sa'di", 4),
    "shinqiti": ("الشنقيطي", "al-Shinqiti", 4),
    "ibnqudamah": ("ابن قدامة", "Ibn Qudamah", 5), "ibntaymiyyah": ("ابن تيمية", "Ibn Taymiyyah", 5),
    "ibnqayyim": ("ابن القيم", "Ibn al-Qayyim", 5), "ibnabdalwahhab": ("محمد بن عبد الوهاب", "Muhammad ibn Abd al-Wahhab", 5),
    "ibnishaq": ("ابن إسحاق", "Ibn Ishaq", 6), "ibnhisham": ("ابن هشام", "Ibn Hisham", 6), "ibnsad": ("ابن سعد", "Ibn Sa'd", 6),
    "ibnathir": ("ابن الأثير", "Ibn al-Athir", 6),
    "shatibi": ("الشاطبي", "al-Shatibi", 7), "ibnjazari": ("ابن الجزري", "Ibn al-Jazari", 7),
    "ibnbaz": ("ابن باز", "Ibn Baz", 8), "ibnuthaymeen": ("ابن عثيمين", "Ibn Uthaymeen", 8), "albani": ("الألباني", "al-Albani", 8),
}
GROUP_ORDER = ["abuhanifa", "malik", "shafii", "ahmad", "ibnmusayyib", "hasan", "ibnsirin", "zuhri", "thawri", "awzai",
               "layth", "ibnmubarak", "ibnuyaynah", "bukhari", "muslim", "abudawud", "tirmidhi", "nasai", "ibnmajah",
               "darimi", "ibnkhuzaymah", "ibnhibban", "daraqutni", "hakim", "bayhaqi", "ibnmain", "ibnmadini", "nawawi",
               "ibnabdalbarr", "mizzi", "dhahabi", "ibnrajab", "ibnhajar", "tabari", "baghawi", "qurtubi", "ibnkathir",
               "suyuti", "saadi", "shinqiti", "ibnqudamah", "ibntaymiyyah", "ibnqayyim", "ibnabdalwahhab", "ibnishaq",
               "ibnhisham", "ibnsad", "ibnathir", "shatibi", "ibnjazari", "ibnbaz", "ibnuthaymeen", "albani"]
# "by time": in order of death — the year of birth of some is not recorded (e.g. Ibn Hisham, al-Qurtubi) and differs
# between sources for others; the order is a draft until every year is copied from the books of biographies (P9-D5).
TIME_ORDER = ["ibnmusayyib", "hasan", "ibnsirin", "zuhri", "abuhanifa", "ibnishaq", "awzai", "thawri", "layth", "malik",
              "ibnmubarak", "ibnuyaynah", "shafii", "ibnhisham", "ibnsad", "ibnmain", "ibnmadini", "ahmad", "darimi",
              "bukhari", "muslim", "ibnmajah", "abudawud", "tirmidhi", "nasai", "tabari", "ibnkhuzaymah", "ibnhibban",
              "daraqutni", "hakim", "bayhaqi", "ibnabdalbarr", "baghawi", "shatibi", "ibnqudamah", "ibnathir", "qurtubi",
              "nawawi", "ibntaymiyyah", "mizzi", "dhahabi", "ibnqayyim", "ibnkathir", "ibnrajab", "ibnjazari", "ibnhajar",
              "suyuti", "ibnabdalwahhab", "saadi", "shinqiti", "ibnbaz", "albani", "ibnuthaymeen"]
SAMPLE = "ibnqayyim"
# the books of biographies his life will be copied from (each edition chosen and cleared — P9-D5)
SAMPLE_SOURCES = [("الدرر الكامنة في أعيان المائة الثامنة — ابن حجر العسقلاني", "al-Durar al-Kaminah — Ibn Hajar al-Asqalani"),
                  ("ذيل طبقات الحنابلة — ابن رجب (تلميذه)", "Dhayl Tabaqat al-Hanabilah — Ibn Rajab (his student)")]

# ---- F14: the library — the scholars' books by subject (the author, 2026-11-21: «وزد في الكتب مثل الداء والدواء») ----
BOOK_CATS = ["f13", "f5", "d3_bc_aqeeda", "d3_bc_fiqh", "d3_bc_seerah", "d3_bc_heart", "d3_sg_qiraat"]
BOOKS = [   # Arabic title, transliteration, category index, author (a scholar id, or [Arabic, transliteration])
    ("صحيح البخاري", "Sahih al-Bukhari", 0, "bukhari"), ("الأدب المفرد", "al-Adab al-Mufrad", 0, "bukhari"),
    ("صحيح مسلم", "Sahih Muslim", 0, "muslim"), ("سنن أبي داود", "Sunan Abi Dawud", 0, "abudawud"),
    ("جامع الترمذي", "Jami' al-Tirmidhi", 0, "tirmidhi"), ("سنن النسائي", "Sunan al-Nasa'i", 0, "nasai"),
    ("سنن ابن ماجه", "Sunan Ibn Majah", 0, "ibnmajah"), ("الموطأ", "al-Muwatta'", 0, "malik"),
    ("المسند", "al-Musnad", 0, "ahmad"), ("سنن الدارمي", "Sunan al-Darimi", 0, "darimi"),
    ("صحيح ابن خزيمة", "Sahih Ibn Khuzaymah", 0, "ibnkhuzaymah"), ("صحيح ابن حبان", "Sahih Ibn Hibban", 0, "ibnhibban"),
    ("سنن الدارقطني", "Sunan al-Daraqutni", 0, "daraqutni"), ("المستدرك على الصحيحين", "al-Mustadrak", 0, "hakim"),
    ("شعب الإيمان", "Shu'ab al-Iman", 0, "bayhaqi"), ("رياض الصالحين", "Riyad al-Salihin", 0, "nawawi"),
    ("الأربعون النووية", "al-Arba'un al-Nawawiyyah", 0, "nawawi"), ("الأذكار", "al-Adhkar", 0, "nawawi"),
    ("التمهيد", "al-Tamhid", 0, "ibnabdalbarr"), ("تهذيب الكمال", "Tahdhib al-Kamal", 0, "mizzi"),
    ("جامع العلوم والحكم", "Jami' al-Ulum wa al-Hikam", 0, "ibnrajab"), ("فتح الباري", "Fath al-Bari", 0, "ibnhajar"),
    ("بلوغ المرام", "Bulugh al-Maram", 0, "ibnhajar"),
    ("جامع البيان", "Jami' al-Bayan", 1, "tabari"), ("معالم التنزيل", "Ma'alim al-Tanzil", 1, "baghawi"),
    ("الجامع لأحكام القرآن", "al-Jami' li-Ahkam al-Quran", 1, "qurtubi"), ("تفسير القرآن العظيم", "Tafsir al-Quran al-Azim", 1, "ibnkathir"),
    ("تيسير الكريم الرحمن", "Taysir al-Karim al-Rahman", 1, "saadi"), ("أضواء البيان", "Adwa' al-Bayan", 1, "shinqiti"),
    ("الإتقان في علوم القرآن", "al-Itqan fi Ulum al-Quran", 1, "suyuti"),
    ("العقيدة الواسطية", "al-Aqidah al-Wasitiyyah", 2, "ibntaymiyyah"), ("كتاب التوحيد", "Kitab al-Tawhid", 2, "ibnabdalwahhab"),
    ("الأصول الثلاثة", "al-Usul al-Thalathah", 2, "ibnabdalwahhab"), ("لمعة الاعتقاد", "Lum'at al-I'tiqad", 2, "ibnqudamah"),
    ("القواعد المثلى", "al-Qawa'id al-Muthla", 2, "ibnuthaymeen"),
    ("الأم", "al-Umm", 3, "shafii"), ("الرسالة", "al-Risalah", 3, "shafii"), ("المغني", "al-Mughni", 3, "ibnqudamah"),
    ("إعلام الموقعين", "I'lam al-Muwaqqi'in", 3, "ibnqayyim"), ("الشرح الممتع", "al-Sharh al-Mumti'", 3, "ibnuthaymeen"),
    ("صفة صلاة النبي ﷺ", "Sifat Salat al-Nabi ﷺ", 3, "albani"),
    ("زاد المعاد", "Zad al-Ma'ad", 4, "ibnqayyim"), ("السيرة النبوية", "al-Sirah al-Nabawiyyah", 4, "ibnhisham"),
    ("الطبقات الكبرى", "al-Tabaqat al-Kubra", 4, "ibnsad"), ("البداية والنهاية", "al-Bidayah wa al-Nihayah", 4, "ibnkathir"),
    ("قصص الأنبياء", "Qasas al-Anbiya'", 4, "ibnkathir"), ("تاريخ الخلفاء", "Tarikh al-Khulafa'", 4, "suyuti"),
    ("أسد الغابة", "Usd al-Ghabah", 4, "ibnathir"), ("الإصابة في تمييز الصحابة", "al-Isabah fi Tamyiz al-Sahabah", 4, "ibnhajar"),
    ("الاستيعاب", "al-Isti'ab", 4, "ibnabdalbarr"), ("سير أعلام النبلاء", "Siyar A'lam al-Nubala'", 4, "dhahabi"),
    ("الدرر الكامنة", "al-Durar al-Kaminah", 4, "ibnhajar"),
    ("مدارج السالكين", "Madarij al-Salikin", 5, "ibnqayyim"),
    ("الداء والدواء (الجواب الكافي)", "al-Da' wa al-Dawa' (al-Jawab al-Kafi)", 5, "ibnqayyim"),
    ("الوابل الصيب", "al-Wabil al-Sayyib", 5, "ibnqayyim"), ("الفوائد", "al-Fawa'id", 5, "ibnqayyim"),
    ("حادي الأرواح", "Hadi al-Arwah", 5, "ibnqayyim"), ("طريق الهجرتين", "Tariq al-Hijratayn", 5, "ibnqayyim"),
    ("مفتاح دار السعادة", "Miftah Dar al-Sa'adah", 5, "ibnqayyim"), ("الزهد", "al-Zuhd", 5, "ibnmubarak"),
    ("لطائف المعارف", "Lata'if al-Ma'arif", 5, "ibnrajab"),
    ("حرز الأماني (الشاطبية)", "Hirz al-Amani (al-Shatibiyyah)", 6, "shatibi"), ("المقدمة الجزرية", "al-Muqaddimah al-Jazariyyah", 6, "ibnjazari"),
    ("النشر في القراءات العشر", "al-Nashr fi al-Qira'at al-Ashr", 6, "ibnjazari"),
    ("تحفة الأطفال", "Tuhfat al-Atfal", 6, ["سليمان الجمزوري", "Sulayman al-Jamzuri"]),
]

# ---- all sections: every feature by group, the Lives last (the author, 2026-11-21) ----
# status: d = drawn in design 3, p = inside another screen, t = to come, b = behaviour without a screen
FEATURE_GROUPS = [
    ("d3_g_quran", [("f2", "d", "reader-page"), ("f16", "t"), ("f5", "p", "ex-actions"), ("f6", "t"), ("f25", "d", "ex-markers"),
                    ("f26", "d", "ex-actions"), ("f33", "t"), ("f34", "t")]),
    ("d3_g_listen", [("f3", "p", "ex-actions"), ("f4", "t"), ("f7", "t"), ("f28", "p", "ex-actions"), ("f11", "b")]),
    ("d3_g_hifz", [("f30", "t"), ("f31", "t"), ("f32", "t")]),
    ("d3_g_prayer", [("f8", "d", "times"), ("f9", "t"), ("f10", "t"), ("f27", "d", "ex-hijri"), ("f36", "t"), ("f35", "t"),
                     ("f37", "t"), ("f46", "t")]),
    ("d3_g_dhikr", [("f12", "d", "ex-adhkar-list"), ("f24", "d", "ex-misbaha"), ("f23", "d", "ex-duas"), ("f38", "t")]),
    ("d3_g_know", [("f13", "t"), ("f29", "p", "ex-actions"), ("f14", "d", "d3-books"), ("f39", "d", "ex-names"),
                   ("f48", "d", "ex-pnames"), ("f49", "t"), ("f50", "t")]),
    ("d3_g_guides", [("f40", "t"), ("f41", "t"), ("f42", "t")]),
    ("d3_g_app", [("f1", "d", "lsel"), ("f18", "d", "dirs"), ("f43", "t"), ("f44", "t"), ("f45", "t"), ("f47", "t"),
                  ("f17", "d", "sources"), ("f19", "d", "why"), ("f15", "t")]),
    ("d3_g_lives", [("f20", "d", "lv-list"), ("f21", "d", "lv-list"), ("f22", "d", "lv-list"), ("f51", "d", "d3-scholars")]),
]

# ---- the Sources screen (F17): the state of every source on 2026-11-21 (docs/permissions/README.md) ----
# s: 1 verified · 2 letter sent, waiting · 3 letter ready, to send · 0 to check
SOURCES = [
    ("d3_g_quran", [("Tanzil Quran Text (Uthmani 1.1)", "s81", "CC BY 3.0", 1, "tanzil.net"),
                    ("Tanzil Quran Metadata 1.0", "s82", "CC BY 3.0", 1, "tanzil.net"),
                    ("DigitalKhatt — old Madinah layout", "s83", "MIT", 1, "github.com/DigitalKhatt")]),
    ("s84", [("KFGQPC — Madinah mushaf page fonts (1405H)", "s85", "© KFGQPC", 2, "qurancomplex.gov.sa"),
             ("DigitalKhatt Old Madina font", "u_dk_font", "OFL 1.1", 1, "github.com/DigitalKhatt")]),
    ("s86", [("Noto Kufi Arabic", "s87", "OFL 1.1", 1, "github.com/notofonts/arabic"),
             ("IBM Plex Sans Arabic", "s88", "OFL 1.1", 1, "github.com/IBM/plex"),
             ("Inter", "s89", "OFL 1.1", 1, "rsms.me/inter"),
             ("Amiri", "r4_head", "OFL 1.1", 1, "github.com/aliftype/amiri"),
             ("Noto Sans Devanagari / Bengali / KR / JP / SC, Noto Nastaliq Urdu, Vazirmatn", "other_scripts", "OFL 1.1", 1, "github.com/notofonts")]),
    ("d3_sg_audio", [("mp3quran.net", "s91", "Free use (site terms)", 1, "mp3quran.net"),
                     ("EveryAyah", "u_everyayah", "—", 2, "everyayah.com"),
                     ("Radio stations", "u_radio", "—", 0, "—")]),
    ("d3_sg_tafsirs", [("QuranEnc", "u_quranenc", "—", 2, "quranenc.com"),
                       ("Quran Foundation — Content APIs", "u_qf", "Developer terms", 3, "api-docs.quran.foundation")]),
    ("f13", [("sunnah.com", "u_sunnah", "API key", 3, "sunnah.com/developers"),
             ("HadeethEnc — موسوعة الأحاديث النبوية", "u_hadeethenc", "—", 3, "hadeethenc.com"),
             ("الدرر السنية — Dorar", "u_dorar", "API terms", 2, "dorar.net/api-services")]),
    ("d3_sg_adhkar", [("حصن المسلم — Hisn al-Muslim", "u_hisn", "© edition", 2, "hisn-almuslim.com"),
                      ("مؤسسة الشيخ ابن عثيمين — Ibn Uthaymeen Foundation", "u_uthaymeen", "© edition", 2, "binothaimeen.net"),
                      ("الشيخ عبد الرزاق البدر — al-Badr", "u_badr", "© edition", 2, "al-badr.net")]),
    ("d3_sg_books", [("Book editions (تحقيق)", "u_editions", "—", 0, "—")]),
    ("d3_sg_prayer", [("Adhan (Batoul Apps)", "s92", "MIT", 1, "github.com/batoulapps"),
                      ("Muezzin recordings", "u_muezzin", "—", 0, "—"),
                      ("OpenStreetMap", "u_osm", "ODbL", 0, "openstreetmap.org")]),
]

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <!-- design 3 icons (no person, no cross shape): a name plate; a round plate; a book with a returning arrow
       (repetition); a list; a stack of books -->
  <symbol id="i-d3-names" viewBox="0 0 24 24"><rect x="3.5" y="6" width="17" height="12" rx="6"/><path d="M8 11h8M9.5 14h5"/></symbol>
  <symbol id="i-d3-pnames" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M8.5 10h7M9.5 13h5M11 16h2"/></symbol>
  <symbol id="i-d3-hifz" viewBox="0 0 24 24"><path d="M4 5.5h6a2 2 0 0 1 2 2V19a2 2 0 0 0-2-2H4z"/><path d="M12 7.5a2 2 0 0 1 2-2h2"/><path d="M20 12.5a4 4 0 1 1-1.2-2.9M20 7v2.8h-2.8"/></symbol>
  <symbol id="i-d3-all" viewBox="0 0 24 24"><circle cx="5" cy="6.5" r="1.3"/><circle cx="5" cy="12" r="1.3"/><circle cx="5" cy="17.5" r="1.3"/><path d="M9 6.5h11M9 12h11M9 17.5h11"/></symbol>
  <symbol id="i-d3-scholars" viewBox="0 0 24 24"><rect x="4" y="15.5" width="16" height="4" rx="1"/><rect x="5.5" y="11" width="13" height="4.5" rx="1"/><rect x="4.5" y="6.5" width="14" height="4.5" rx="1"/><path d="M8 8.75h6M8 13.25h5"/></symbol>
</svg>"""

CSS = """/* design 3 only (build_design3.py, 2026-11-21) */
.d3-home{overflow:auto!important}
.lv-row.d3-4{grid-template-columns:repeat(4,1fr)}
.lv-chip[data-d3],.tile[data-d3]{cursor:pointer}
.d3-legend{display:flex;flex-wrap:wrap;gap:6px;font-size:10.5px;color:var(--muted)}
.d3-legend span{border:1px solid var(--border);border-radius:999px;padding:1px 8px;background:var(--surface)}
.d3-g h4{margin:4px 2px 4px;font-size:12px;color:var(--lv-accent,var(--dot));font-family:var(--head)}
.d3-f{display:flex;align-items:center;gap:8px;padding:6px 10px;border-radius:10px;background:var(--surface);border:1px solid var(--border);margin-bottom:4px;font-size:12.5px}
.d3-f .k{font-size:10px;color:var(--muted);font-variant-numeric:tabular-nums;min-width:26px}
.d3-f .n{flex:1;font-weight:600}
.d3-f .s{font-size:10px;white-space:nowrap;border-radius:999px;padding:1px 7px}
.d3-f .s.d{background:var(--secondsoft);color:var(--second)}
.d3-f .s.p{background:var(--dotsoft);color:var(--dot)}
.d3-f .s.t,.d3-f .s.b{color:var(--muted);border:1px dashed var(--rule)}
.d3-f.go{cursor:pointer}
.d3-f.go:hover{border-color:var(--primary)}
.d3-seg{display:flex;gap:4px;padding:4px;border-radius:12px;background:var(--lv-soft,var(--surface2))}
.d3-seg button{flex:1;border:0;background:transparent;color:var(--muted);font:inherit;font-size:11.5px;font-weight:700;padding:6px 4px;border-radius:9px;cursor:pointer}
.d3-seg button[aria-pressed="true"]{background:var(--surface);color:var(--primary);box-shadow:0 1px 3px rgba(0,0,0,.12)}
.d3-row{display:flex;align-items:center;gap:8px;padding:6px 10px;border-radius:10px;background:var(--surface);border:1px solid var(--border)}
.d3-row .o{font-size:10.5px;color:var(--muted);min-width:20px;font-variant-numeric:tabular-nums}
.d3-row .nm{flex:1;font-weight:700;font-size:13px}
.d3-row .s{font-size:10.5px;color:var(--muted)}
.d3-row.go{cursor:pointer;border-color:var(--primary)}
.d3-bk{padding:6px 10px;border-radius:10px;background:var(--surface);border:1px solid var(--border)}
.d3-bk .t{font-weight:700;font-size:13px}
.d3-bk .a{font-size:11px;color:var(--muted)}
.d3-bk.on{border-color:var(--primary);box-shadow:0 0 0 1px var(--primary)}
.d3-chips{display:flex;flex-wrap:wrap;gap:5px}
.d3-chips span{font-size:11.5px;border:1px solid var(--border);border-radius:999px;padding:2px 9px;background:var(--bg);cursor:pointer}
.st.sent{background:var(--dotsoft);color:var(--dot)}
.st.ready{color:var(--primary);border:1px dashed var(--primary)}
.st.check{color:var(--muted);border:1px dashed var(--rule)}
.d3-sum{font-size:11px;color:var(--muted);line-height:1.5;padding:2px 2px 0}
"""

PHONE = """  <div class="unit"><div class="cap">%(cap)s</div>
  <div class="phone parch screen lives extras">
    <div class="topbar"><div class="title kufi"><span%(title)s></span><div class="sub"%(sub)s></div></div>%(icon)s</div>
    <div class="lv-body" id="%(id)s"></div>
  </div></div>
"""


def phones():
    out = [ICONS]
    for cap, title, sub, ident, icon in [
        ("New 2026-11-21 · All sections — every feature, and where its screen is (design 3)", " data-d3='d3_all'", " id='d3-all-sub'", "d3-all", "i-d3-all"),
        ("New · The scholars of Islam (F51) — by group or by time", " data-d3='f51'", " id='d3-sch-sub'", "d3-scholars", "i-search"),
        ("New · One scholar — his life from the books of biographies, his books (F51, F14)", " id='d3-e-name'", " data-d3='d3_entry_sub'", "d3-scholar", "i-mark"),
        ("New · The library — the scholars' books by subject (F14)", " data-d3='f14'", " id='d3-bk-sub'", "d3-books", "i-search"),
    ]:
        out.append(PHONE % {"cap": cap, "title": title, "sub": sub, "id": ident,
                            "icon": "<svg class='ic' style='color:var(--primary)'><use href='#%s'/></svg>" % icon})
    return "\n".join(out)


JS = r"""window.D3 = (function () {
  var D = %(data)s;
  var RTL = ["ar", "ur", "fa", "ps"], DIG = "٠١٢٣٤٥٦٧٨٩", cur = "ar", mode = "group";
  function T(id, vars) {
    var e = D.t[id], s = e[cur] || e.en;
    return vars ? s.replace(/\{(\w+)\}/g, function (m, k) { return vars[k] != null ? vars[k] : m; }) : s;
  }
  function num(n) {
    if (cur === "ar") return String(n).replace(/[0-9]/g, function (d) { return DIG[d]; });
    try { return new Intl.NumberFormat({ zh: "zh-CN", ps: "ps-u-nu-arabext" }[cur] || cur, { useGrouping: false }).format(n); }
    catch (e) { return String(n); }
  }
  /* names and titles: Arabic for Arabic-script languages, transliterated for the others; honorifics in Arabic */
  function nm(p) { return RTL.indexOf(cur) >= 0 ? p[0] : p[1]; }
  function el(t, cls, text) { var e = document.createElement(t); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function host(id) { var h = document.getElementById(id); h.textContent = ""; return h; }
  function go(id) {
    var e = document.getElementById(id), u = e && e.closest(".unit");
    if (u) u.scrollIntoView({ behavior: "smooth", block: "center", inline: "center" });
  }
  function author(a) { return typeof a === "string" ? nm(D.scholars[a]) : nm(a); }

  /* ---- home: four more tiles above the Lives; the Lives row with the scholars, last ---- */
  function home() {
    var ph = document.querySelectorAll(".phone")[1], grid = ph && ph.querySelector(".grid");
    if (!grid) return;
    var body = ph.querySelector(".body");
    if (body) body.classList.add("d3-home");
    if (!grid.querySelector("[data-d3]")) {
      [["f39", "i-d3-names", "ex-names"], ["f48", "i-d3-pnames", "ex-pnames"], ["f30", "i-d3-hifz", "d3-all"], ["d3_all", "i-d3-all", "d3-all"]].forEach(function (x) {
        var t = el("div", "tile"); t.dataset.d3 = x[0]; t.setAttribute("role", "button");
        t.innerHTML = "<svg class='ic'><use href='#" + x[1] + "'/></svg><span></span>";
        t.addEventListener("click", function () { go(x[2]); });
        grid.appendChild(t);
      });
    }
    var row = ph.querySelector(".lv-row");
    if (row && !row.querySelector("[data-d3]")) {
      row.classList.add("d3-4");
      var c = el("div", "lv-chip"); c.dataset.d3 = "d3_scholars"; c.setAttribute("role", "button");
      c.innerHTML = "<svg class='ic'><use href='#i-d3-scholars'/></svg><span></span>";
      c.addEventListener("click", function () { go("d3-scholars"); });
      row.appendChild(c);
    }
    var tabs = document.querySelector(".lv-tabs");   /* the Lives screen: a fourth tab that opens the scholars */
    if (tabs && !tabs.querySelector("[data-d3]")) {
      var b = el("button"); b.type = "button"; b.dataset.d3 = "d3_scholars";
      b.addEventListener("click", function () { go("d3-scholars"); });
      tabs.appendChild(b);
    }
    document.querySelectorAll("[data-lv='lv_sub']").forEach(function (e) { e.dataset.d3 = "d3_lv_sub"; e.removeAttribute("data-lv"); });
  }

  /* ---- all sections ---- */
  function all() {
    var h = host("d3-all"), n = 0;
    D.groups.forEach(function (g) { n += g[1].length; });
    document.getElementById("d3-all-sub").textContent = T("d3_all_sub", { n: num(n) });
    var lg = el("div", "d3-legend");
    ["d3_st_drawn", "d3_st_part", "d3_st_todo"].forEach(function (k) { lg.appendChild(el("span", null, T(k))); });
    h.appendChild(lg);
    h.appendChild(el("div", "lv-note", T("d3_tap_open")));
    var ST = { d: "d3_st_drawn", p: "d3_st_part", t: "d3_st_todo", b: "d3_st_beh" };
    D.groups.forEach(function (g) {
      var box = el("div", "d3-g"); box.appendChild(el("h4", null, T(g[0])));
      g[1].forEach(function (f) {
        var r = el("div", "d3-f" + (f[2] ? " go" : ""));
        r.appendChild(el("span", "k", "F" + f[0].slice(1)));
        r.appendChild(el("span", "n", T(f[0])));
        r.appendChild(el("span", "s " + f[1], f[1] === "b" ? T("d3_st_beh").split(" — ")[0] : T(ST[f[1]]).split(" ")[0]));
        if (f[1] === "b") r.title = T("d3_st_beh");
        if (f[2]) { r.setAttribute("role", "button"); r.addEventListener("click", function () { go(f[2]); }); }
        box.appendChild(r);
      });
      h.appendChild(box);
    });
  }

  /* ---- the scholars: by group or by time ---- */
  function scholarRow(id, order, sub) {
    var s = D.scholars[id], r = el("div", "d3-row" + (id === D.sample ? " go" : ""));
    if (order) r.appendChild(el("span", "o", num(order)));
    var nmEl = el("span", "nm", nm(s)); r.appendChild(nmEl);
    if (sub) r.appendChild(el("span", "s", sub));
    if (id === D.sample) { r.setAttribute("role", "button"); r.addEventListener("click", function () { go("d3-scholar"); }); }
    return r;
  }
  function scholars() {
    var h = host("d3-scholars");
    document.getElementById("d3-sch-sub").textContent = T("d3_sch_sub", { n: num(D.byGroup.length) });
    var seg = el("div", "d3-seg");
    [["group", "d3_by_group"], ["time", "d3_by_time"]].forEach(function (m) {
      var b = el("button", null, T(m[1])); b.type = "button"; b.setAttribute("aria-pressed", String(mode === m[0]));
      b.addEventListener("click", function () { mode = m[0]; scholars(); });
      seg.appendChild(b);
    });
    h.appendChild(seg);
    if (mode === "group") {
      D.sgroups.forEach(function (g, gi) {
        var box = el("div", "d3-g"); box.appendChild(el("h4", null, T(g)));
        D.byGroup.filter(function (id) { return D.scholars[id][2] === gi; }).forEach(function (id) { box.appendChild(scholarRow(id)); });
        h.appendChild(box);
      });
    } else {
      h.appendChild(el("div", "lv-ph", T("d3_time_note")));
      D.byTime.forEach(function (id, i) { h.appendChild(scholarRow(id, i + 1, T(D.sgroups[D.scholars[id][2]]))); });
    }
  }
  function scholar() {
    var h = host("d3-scholar"), s = D.scholars[D.sample], t = document.getElementById("d3-e-name");
    t.textContent = nm(s);
    var hon = el("span", "lv-hon", "رحمه الله"); hon.dir = "rtl"; hon.lang = "ar"; t.appendChild(hon);
    var g = el("div", "d3-chips"); g.appendChild(el("span", null, T(D.sgroups[s[2]]))); h.appendChild(g);
    var c1 = el("div", "lv-card"); c1.appendChild(el("h4", null, T("d3_birth_death"))); c1.appendChild(el("div", "lv-ph", T("d3_date_ph"))); h.appendChild(c1);
    var c2 = el("div", "lv-card"); c2.appendChild(el("h4", null, T("lv_k_life")));
    c2.appendChild(el("div", "lv-ref", T("d3_life_from")));
    D.sampleSources.forEach(function (b) { c2.appendChild(el("div", "lv-src", nm(b))); });
    var ph = el("div", "lv-ph"); ph.appendChild(el("div", null, T("d3_life_ph")));
    var bars = el("div", "lv-bars"); bars.innerHTML = "<i></i><i></i><i></i>"; ph.appendChild(bars);
    c2.appendChild(ph); h.appendChild(c2);
    var c3 = el("div", "lv-card"); c3.appendChild(el("h4", null, T("d3_his_books")));
    var ch = el("div", "d3-chips");
    D.books.forEach(function (b, i) {
      if (b[3] !== D.sample) return;
      var x = el("span", null, nm(b)); x.setAttribute("role", "button");
      x.addEventListener("click", function () { mark = i; books(); go("d3-books"); });
      ch.appendChild(x);
    });
    c3.appendChild(ch); h.appendChild(c3);
    var rep = el("button", "lv-report", T("d3_report")); rep.type = "button"; h.appendChild(rep);
  }

  /* ---- the library ---- */
  var mark = -1;
  function books() {
    var h = host("d3-books");
    document.getElementById("d3-bk-sub").textContent = T("d3_books_sub", { n: num(D.books.length) });
    h.appendChild(el("div", "lv-ph", T("d3_edition_ph")));
    D.bookCats.forEach(function (c, ci) {
      var box = el("div", "d3-g"); box.appendChild(el("h4", null, T(c)));
      D.books.forEach(function (b, i) {
        if (b[2] !== ci) return;
        var r = el("div", "d3-bk" + (i === mark ? " on" : ""));
        r.appendChild(el("div", "t", nm(b)));
        r.appendChild(el("div", "a", author(b[3])));
        box.appendChild(r);
      });
      h.appendChild(box);
    });
  }

  /* ---- the Sources screen (F17) — called by renderSources() of the page ---- */
  function sources() {
    var h = host("sources"), cnt = [0, 0, 0, 0];
    var CLS = ["check", "ok", "sent", "ready"], LBL = ["d3_s_check", "d3_s_ok", "d3_s_sent", "d3_s_ready"];
    D.sources.forEach(function (g) { g[1].forEach(function (it) { cnt[it[3]]++; }); });
    h.appendChild(el("div", "d3-sum", T("d3_s_sum", { a: num(cnt[1]), b: num(cnt[2]), c: num(cnt[3]), d: num(cnt[0]) }) + " · " + T("d3_s_nouse")));
    D.sources.forEach(function (g) {
      h.appendChild(el("h3", null, T(g[0])));
      g[1].forEach(function (it) {
        var d = el("div", "si");
        d.appendChild(el("div", "n", it[0]));
        d.appendChild(el("div", "u", T(it[1])));
        var row = el("div", "row");
        if (it[2] !== "—") row.appendChild(el("span", "lic", it[2]));
        row.appendChild(el("span", "st " + CLS[it[3]], T(LBL[it[3]])));
        if (it[4] !== "—") { var a = el("a", null, it[4]); a.href = "#"; row.appendChild(a); }
        d.appendChild(row); h.appendChild(d);
      });
    });
  }

  function render(lang) {
    if (lang) cur = (lang === "ar" || lang === "en" || D.t.d3_all[lang]) ? lang : "en";
    home();
    document.querySelectorAll("[data-d3]").forEach(function (e) {
      var s = e.querySelector("span"); (e.classList.contains("tile") || e.classList.contains("lv-chip") ? s : e).textContent = T(e.dataset.d3);
    });
    all(); scholars(); scholar(); books(); sources();
  }
  return { render: render, sources: sources };
})();
"""

RENDER_SOURCES = """  /* the Sources screen (F17) is written by tools/build_design3.py (window.D3), with four states — 2026-11-21 */
  function renderSources() { if (window.D3) window.D3.sources(); }
"""


def ensure_markers(html):
    """Insert the marker comments and the hook once (2026-11-21); the old Sources data gives way to window.D3."""
    if "/*D3-CSS-BEGIN*/" in html:
        return html
    for a, b in [("/*EXTRAS-CSS-END*/\n", "/*EXTRAS-CSS-END*/\n/*D3-CSS-BEGIN*/\n/*D3-CSS-END*/\n"),
                 ("<!--EXTRAS-HTML-END-->\n", "<!--EXTRAS-HTML-END-->\n<!--D3-HTML-BEGIN-->\n<!--D3-HTML-END-->\n"),
                 ('<script id="extras">', '<script id="design3">\n/*D3-JS-BEGIN*/\n/*D3-JS-END*/\n</script>\n<script id="extras">'),
                 ("    if (window.EXTRAS) window.EXTRAS.render(L());\n",
                  "    if (window.EXTRAS) window.EXTRAS.render(L());\n    if (window.D3) window.D3.render(L());\n")]:
        if html.count(a) != 1:
            R1.fail("round-3.html: not found once: %s" % a[:70])
        html = html.replace(a, b)
    m = re.search(r"^  var SOURCES = \[\n.*?^  function renderSources\(\) \{\n.*?^  \}\n", html, re.S | re.M)
    if not m:
        R1.fail("round-3.html: the old Sources block was not found")
    html = html[:m.start()] + RENDER_SOURCES + html[m.end():]
    print("round-3.html: design-3 markers and hook inserted; the Sources screen now comes from build_design3.py")
    return html


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    # the lists must agree: every scholar once in each order, every book's author a scholar of the list
    for name, order in [("GROUP_ORDER", GROUP_ORDER), ("TIME_ORDER", TIME_ORDER)]:
        if sorted(order) != sorted(SCHOLARS) or len(order) != len(set(order)):
            R1.fail("%s does not hold every scholar exactly once" % name)
    if [SCHOLARS[i][2] for i in GROUP_ORDER] != sorted(SCHOLARS[i][2] for i in GROUP_ORDER):
        R1.fail("GROUP_ORDER is not in group order")
    for b in BOOKS:
        if isinstance(b[3], str) and b[3] not in SCHOLARS:
            R1.fail("book %s: unknown author %s" % (b[1], b[3]))
    if not any(b[0].startswith("الداء والدواء") for b in BOOKS):
        R1.fail("«الداء والدواء» must be in the library (the author, 2026-11-21)")
    feats = sorted(int(f[0][1:]) for _, fs in FEATURE_GROUPS for f in fs)
    if feats != list(range(1, 52)):
        R1.fail("all sections must list F1 – F51 exactly once: %s" % feats)
    if FEATURE_GROUPS[-1][0] != "d3_g_lives":
        R1.fail("the Lives must be the last group (the author, 2026-11-21)")
    keys = json.load(io.open(os.path.join(I.I18N, "design3", "keys.json"), encoding="utf-8"))
    i18n = I.build_i18n("design3")
    texts = {k["id"]: dict({"ar": k["ar"], "en": k["en"]}, **{c: i18n["tr"][c][k["id"]] for c in I.LANG_CODES}) for k in keys}
    lives = I.build_i18n("lives")
    lkeys = json.load(io.open(os.path.join(I.I18N, "lives", "keys.json"), encoding="utf-8"))
    for k in lkeys:
        if k["id"] == "lv_k_life":
            texts["lv_k_life"] = dict({"ar": k["ar"], "en": k["en"]}, **{c: lives["tr"][c][k["id"]] for c in I.LANG_CODES})
    used = set(GROUPS) | set(BOOK_CATS) | {g for g, _ in FEATURE_GROUPS} | {f[0] for _, fs in FEATURE_GROUPS for f in fs} \
        | {g for g, _ in SOURCES} | {it[1] for _, items in SOURCES for it in items}
    missing = sorted(u for u in used if u not in texts)
    if missing:
        R1.fail("texts missing in i18n/design3: %s" % missing)
    data = {"t": texts, "scholars": {k: list(v) for k, v in SCHOLARS.items()}, "sgroups": GROUPS, "byGroup": GROUP_ORDER,
            "byTime": TIME_ORDER, "sample": SAMPLE, "sampleSources": SAMPLE_SOURCES, "bookCats": BOOK_CATS,
            "books": [list(b) for b in BOOKS], "groups": [[g, [list(f) for f in fs]] for g, fs in FEATURE_GROUPS],
            "sources": [[g, [list(it) for it in items]] for g, items in SOURCES]}
    html = ensure_markers(open(PAGE, encoding="utf-8", newline="").read())
    html = R1.replace_block(html, "/*D3-CSS-BEGIN*/", "/*D3-CSS-END*/", CSS)
    html = R1.replace_block(html, "<!--D3-HTML-BEGIN-->", "<!--D3-HTML-END-->", phones())
    html = R1.replace_block(html, "/*D3-JS-BEGIN*/", "/*D3-JS-END*/", JS % {"data": json.dumps(data, ensure_ascii=False)})
    open(PAGE, "w", encoding="utf-8", newline="\n").write(html)
    print("round-3.html: all sections (F1 – F51), %d scholars, %d books, %d sources written"
          % (len(SCHOLARS), len(BOOKS), sum(len(i) for _, i in SOURCES)))


if __name__ == "__main__":
    main()
