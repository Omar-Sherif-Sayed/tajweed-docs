"""Collect every interface text of round-3.html into i18n/keys.json: an id, the English text and the Arabic text.

Sources: the data-en / data-ar attributes of the page, every { ar: "…", en: "…" } pair in its script, the names of
the colour directions (design2_palettes.py), and the templates below (texts that hold numbers or names). Times are not
collected: they are written by each language's own clock format. The other languages translate this file
(i18n/<code>.json, same ids); build_round3.py checks them.

Usage: python -I extract_i18n_keys.py
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import design2_palettes as P  # noqa: E402

PAGE = os.path.join(HERE, "..", "round-3.html")
OUT = os.path.join(HERE, "..", "i18n", "keys.json")

TEMPLATES = [  # id, English, Arabic — {name} slots are filled by the page
    ("page_n", "Page {n}", "الصفحة {n}"),
    ("juz_n", "Juz {n}", "الجزء {n}"),
    ("hizb_n", "Hizb {n}", "الحزب {n}"),
    ("surah_line", "{type} · {n} ayahs · surah {k}", "{type} · آياتها {n} · ترتيبها {k}"),
    ("index_line", "{type} · {n} ayahs", "{type} · آياتها {n}"),
    ("juz_starts", "Starts: {name} {s}:{a}", "يبدأ: سورة {name} · {a}"),
    ("n_languages", "{n} languages", "{n} لغة"),
    ("device_language", "Your device's language", "لغة جهازك"),
    ("all_languages", "All languages", "كل اللغات"),
    ("search_languages", "Search: Arabic, Deutsch, اردو…", "ابحث: عربي، Deutsch، Urdu…"),
    ("right_to_left", "right to left", "من اليمين"),
    ("no_language", "No language by that name.", "لا توجد لغة بهذا الاسم."),
    ("verified", "✔ verified", "✔ تم التحقق"),
    ("pending", "⏳ check or permission pending", "⏳ بانتظار التحقق أو الإذن"),
    ("design_note", "Design note", "ملاحظة التصميم"),
    ("from_quran", "From the Noble Quran", "من القرآن الكريم"),
    ("from_sunnah", "From the Sunnah", "من السنة"),
    ("why_languages", "Why more than one language?", "لماذا أكثر من لغة؟"),
    ("note_30_22", "Shown beside the language choice. Its meaning is quoted word for word from a recognised tafsir "
                   "(☐ al-Tafsir al-Muyassar, after permission) — never in our words.",
     "تظهر هذه الآية بجوار اختيار اللغة. ومعناها يُنقل بنصه من تفسير معتمد (☐ التفسير الميسر، بعد الإذن)، لا بكلامنا."),
    ("disclaimer", "This is a design choice, not an interpretation. The Quran names colours; the exact shades here are "
                   "our choice.",
     "هذا اختيار تصميم، وليس تفسيرًا. القرآن الكريم يذكر أسماء الألوان؛ أما درجاتها هنا فاختيارنا."),
    ("ayah_note", "The ayahs are shown in Arabic; a meaning in this language is added only from a published "
                  "translation by a named translator.", ""),
    ("draft", "Interface translation by the project. Found a mistake? Report it on GitHub.", ""),
    ("other_scripts", "interface text in other scripts", "نصوص الواجهة بالخطوط الأخرى"),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    html = io.open(PAGE, encoding="utf-8").read()
    keys, seen = [], set()

    def add(kid, en, ar):
        if en in seen:
            return
        seen.add(en)
        keys.append({"id": kid, "en": en, "ar": ar})

    for kid, en, ar in TEMPLATES:
        add(kid, en, ar)
    for m in re.finditer(r'data-ar="([^"]*)" data-en="([^"]*)"', html):
        add("m%02d" % (len(keys) + 1), m.group(2), m.group(1))
    script = html.split("/*ROUND3-DATA-END*/")[1]
    for m in re.finditer(r'ar: "([^"]*)", en: "([^"]*)"', script):
        en = m.group(2)
        if re.fullmatch(r"\d{1,2}:\d{2} [AP]M", en):
            continue  # times: each language's own clock format
        add("s%02d" % (len(keys) + 1), en, m.group(1))
    for did, d in P.DIRECTIONS.items():
        add("dir_" + did, d["name"]["en"], d["name"]["ar"])
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(keys, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("%d keys -> i18n/keys.json" % len(keys))
    for k in keys:
        print("%-16s %s" % (k["id"], k["en"]))


if __name__ == "__main__":
    main()
