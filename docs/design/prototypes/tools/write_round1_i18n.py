"""Write the interface texts of design 1 (round 1) for the 20 languages after Arabic and English.

Design 1 became one file on 2026-11-19 (the author's request) and works in all 22 languages like designs 2 and 3.
Its texts are collected from round-1.html (the data-ar / data-en attributes, the { ar, en } pairs and the T(...) calls of
its script), so the English and Arabic cannot drift from the page. A text that design 2 already has (same English) takes
design 2's translation from i18n/round2/; the texts only design 1 has are translated below, by the agent (no native
readers — users report mistakes on GitHub, AGENTS.md §8.9). Font names stay as their makers wrote them.

Writes i18n/round1/keys.json and i18n/round1/<code>.json; build_round1.py checks them (i18n_check.py).
Usage: python -I write_round1_i18n.py
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
I18N = os.path.join(HERE, "..", "i18n")
PAGE = os.path.join(HERE, "..", "round-1.html")
STATUS = "by the agent, 2026-11-19 — corrected from users' reports (GitHub issues, LANG-02)"

NEW = [  # id, English — in the order of the lists in T
    ("r1_dir_a", "Emerald & gold"), ("r1_dir_b", "Teal & sand"), ("r1_dir_c", "Mushaf"), ("r1_light", "Light"),
    ("r1_dark", "Dark"), ("r1_example", "Example"), ("r1_later", "All of this can be changed later in Settings"),
    ("r1_radio", "Radio"), ("r1_bookmark", "Bookmark"), ("r1_minshawi", "Muhammad Siddiq Al-Minshawi"),
    ("r1_reconnect", "Reconnecting… playback will resume by itself"), ("r1_murattal", "Murattal"),
    ("r1_hafs", "Hafs from Asim"), ("r1_surah", "Surah"), ("r1_range", "Ayah range"), ("r1_noend", "Without end"),
    ("r1_noend_note", "Without end: to the end of the Quran, then again from Al-Fatihah"),
    ("r1_f_qcf", "Madinah mushaf 1405H (page fonts)"), ("r1_fonts", "Quran fonts"), ("r1_u_hafs", "Uthmanic Hafs font"),
    ("r1_u_dk", "two digital Madinah fonts"), ("r1_u_ui", "interface text of the other languages"),
    ("r1_u_ayah", "one audio file per ayah"), ("r1_pending", "⏳ permission pending"),
    ("r1_pos", "{name} · Ayah {n} of {k}"), ("r1_ayahs", "{n} ayahs"),
]
NAMES = [("r1_f_hafs", "KFGQPC Uthmanic Script HAFS"), ("r1_f_dkold", "DigitalKhatt Old Madina"),
         ("r1_f_dknew", "DigitalKhatt New Madina"), ("r1_f_amiri", "Amiri Quran"), ("r1_f_sch", "Scheherazade New")]

T = {
 "ru": ["Изумруд и золото", "Бирюза и песок", "Мусхаф", "Светлая", "Тёмная", "Пример",
        "Всё это можно изменить позже в настройках", "Радио", "Закладка", "Мухаммад Сиддик аль-Миншави",
        "Переподключение… воспроизведение продолжится само", "Мураттал", "Хафс от Асыма", "Сура", "Диапазон аятов",
        "Без конца", "Без конца: до конца Корана, затем снова с аль-Фатихи", "Мусхаф Медины 1405 г. х. (шрифты страниц)",
        "Шрифты Корана", "Османский шрифт Хафс", "два цифровых шрифта мединского мусхафа",
        "текст интерфейса на других языках", "один аудиофайл на каждый аят", "⏳ ожидается разрешение",
        "{name} · аят {n} из {k}", "{n} аятов"],
 "es": ["Esmeralda y oro", "Verde azulado y arena", "Mushaf", "Claro", "Oscuro", "Ejemplo",
        "Todo esto se puede cambiar después en Ajustes", "Radio", "Marcador", "Muhammad Siddiq al-Minshawi",
        "Reconectando… la recitación continuará sola", "Murattal", "Hafs de Asim", "Sura", "Rango de aleyas", "Sin fin",
        "Sin fin: hasta el final del Corán y de nuevo desde Al-Fátiha", "Mushaf de Medina 1405 H (fuentes de página)",
        "Fuentes del Corán", "Fuente uthmani Hafs", "dos fuentes digitales del mushaf de Medina",
        "texto de la interfaz en los demás idiomas", "un archivo de audio por aleya", "⏳ permiso pendiente",
        "{name} · aleya {n} de {k}", "{n} aleyas"],
 "de": ["Smaragd und Gold", "Petrol und Sand", "Mushaf", "Hell", "Dunkel", "Beispiel",
        "All das lässt sich später in den Einstellungen ändern", "Radio", "Lesezeichen", "Muhammad Siddiq al-Minshawi",
        "Verbindung wird wiederhergestellt… die Rezitation läuft von selbst weiter", "Murattal", "Hafs von Asim", "Sure",
        "Versbereich", "Ohne Ende", "Ohne Ende: bis zum Ende des Korans, dann wieder ab al-Fatiha",
        "Medina-Mushaf 1405 n. H. (Seitenschriften)", "Koran-Schriften", "Uthmanische Hafs-Schrift",
        "zwei digitale Schriften des Medina-Mushaf", "Oberflächentext der anderen Sprachen", "eine Audiodatei pro Vers",
        "⏳ Erlaubnis ausstehend", "{name} · Vers {n} von {k}", "{n} Verse"],
 "it": ["Smeraldo e oro", "Verde acqua e sabbia", "Mushaf", "Chiaro", "Scuro", "Esempio",
        "Tutto questo si può cambiare più tardi nelle Impostazioni", "Radio", "Segnalibro", "Muhammad Siddiq al-Minshawi",
        "Riconnessione… la recitazione riprenderà da sola", "Murattal", "Hafs da Asim", "Sura", "Intervallo di versetti",
        "Senza fine", "Senza fine: fino alla fine del Corano, poi di nuovo da al-Fatiha",
        "Mushaf di Medina 1405 H (caratteri di pagina)", "Caratteri del Corano", "Carattere uthmani Hafs",
        "due caratteri digitali del mushaf di Medina", "testo dell'interfaccia nelle altre lingue",
        "un file audio per versetto", "⏳ permesso in attesa", "{name} · versetto {n} di {k}", "{n} versetti"],
 "fr": ["Émeraude et or", "Bleu canard et sable", "Mushaf", "Clair", "Sombre", "Exemple",
        "Tout cela peut être modifié plus tard dans les Réglages", "Radio", "Signet", "Muhammad Siddiq al-Minshawi",
        "Reconnexion… la récitation reprendra d'elle-même", "Murattal", "Hafs d'après Asim", "Sourate",
        "Plage de versets", "Sans fin", "Sans fin : jusqu'à la fin du Coran, puis de nouveau depuis al-Fatiha",
        "Mushaf de Médine 1405 H (polices de page)", "Polices du Coran", "Police uthmani Hafs",
        "deux polices numériques du mushaf de Médine", "texte de l'interface dans les autres langues",
        "un fichier audio par verset", "⏳ autorisation en attente", "{name} · verset {n} sur {k}", "{n} versets"],
 "ur": ["زمردی اور سنہری", "فیروزی اور ریتلا", "مصحف", "ہلکا", "گہرا", "مثال",
        "یہ سب بعد میں ترتیبات سے بدلا جا سکتا ہے", "ریڈیو", "بُک مارک", "محمد صدیق المنشاوی",
        "دوبارہ رابطہ ہو رہا ہے… تلاوت خود بخود جاری ہو جائے گی", "مرتل", "حفص عن عاصم", "سورت", "آیات کی حد",
        "بلا توقف", "بلا توقف: قرآن کے آخر تک، پھر دوبارہ الفاتحہ سے", "مصحفِ مدینہ ۱۴۰۵ھ (صفحات کے فونٹ)",
        "قرآن کے فونٹ", "عثمانی حفص فونٹ", "مصحفِ مدینہ کے دو ڈیجیٹل فونٹ", "دوسری زبانوں میں انٹرفیس کا متن",
        "ہر آیت کی ایک آڈیو فائل", "⏳ اجازت کا انتظار", "{name} · آیت {n} از {k}", "{n} آیات"],
 "hi": ["पन्ना और सोना", "टील और रेत", "मुसहफ़", "हल्का", "गहरा", "उदाहरण",
        "यह सब बाद में सेटिंग्स में बदला जा सकता है", "रेडियो", "बुकमार्क", "मुहम्मद सिद्दीक़ अल-मिनशावी",
        "फिर से जुड़ रहा है… पाठ अपने आप फिर शुरू होगा", "मुरत्तल", "आसिम से हफ़्स", "सूरह", "आयतों की सीमा",
        "बिना रुके", "बिना रुके: क़ुरआन के अंत तक, फिर अल-फ़ातिहा से दोबारा", "मदीना मुसहफ़ 1405 हि. (पृष्ठ फ़ॉन्ट)",
        "क़ुरआन के फ़ॉन्ट", "उस्मानी हफ़्स फ़ॉन्ट", "मदीना मुसहफ़ के दो डिजिटल फ़ॉन्ट", "अन्य भाषाओं में इंटरफ़ेस पाठ",
        "हर आयत की एक ऑडियो फ़ाइल", "⏳ अनुमति प्रतीक्षित", "{name} · आयत {n} / {k}", "{n} आयतें"],
 "ko": ["에메랄드와 금색", "청록과 모래색", "무스하프", "밝게", "어둡게", "예시",
        "이 모든 것은 나중에 설정에서 바꿀 수 있습니다", "라디오", "책갈피", "무함마드 시디크 알민샤위",
        "다시 연결 중… 낭송이 자동으로 이어집니다", "무랏탈", "아심에게서 전해진 하프스", "수라", "아야 범위",
        "끝없이", "끝없이: 꾸란 끝까지, 그다음 알파티하부터 다시", "메디나 무스하프 1405H (페이지 글꼴)", "꾸란 글꼴",
        "우스마니 하프스 글꼴", "메디나 무스하프 디지털 글꼴 두 가지", "다른 언어의 인터페이스 텍스트",
        "아야마다 오디오 파일 하나", "⏳ 허가 대기 중", "{name} · {k}개 중 {n}번째 아야", "아야 {n}개"],
 "id": ["Zamrud dan emas", "Hijau kebiruan dan pasir", "Mushaf", "Terang", "Gelap", "Contoh",
        "Semua ini dapat diubah nanti di Pengaturan", "Radio", "Penanda", "Muhammad Siddiq al-Minshawi",
        "Menyambung kembali… bacaan akan berlanjut sendiri", "Murattal", "Hafs dari Ashim", "Surah", "Rentang ayat",
        "Tanpa henti", "Tanpa henti: sampai akhir Al-Qur'an, lalu kembali dari Al-Fatihah",
        "Mushaf Madinah 1405 H (font halaman)", "Font Al-Qur'an", "Font Utsmani Hafs", "dua font digital mushaf Madinah",
        "teks antarmuka dalam bahasa lain", "satu berkas audio per ayat", "⏳ izin menunggu",
        "{name} · ayat {n} dari {k}", "{n} ayat"],
 "ja": ["エメラルドと金", "ティールと砂", "ムスハフ", "ライト", "ダーク", "例", "これらはすべて後で設定から変更できます",
        "ラジオ", "ブックマーク", "ムハンマド・シッディーク・アル＝ミンシャーウィー", "再接続中… 朗誦は自動で再開します",
        "ムラッタル", "アースィムからのハフス", "スーラ", "節の範囲", "終わりなく",
        "終わりなく：クルアーンの最後まで、その後アル＝ファーティハから再び", "マディーナのムスハフ 1405H（ページフォント）",
        "クルアーンのフォント", "ウスマーニー・ハフス書体", "マディーナのムスハフのデジタル書体2種", "他の言語のインターフェース文字",
        "各節ごとの音声ファイル", "⏳ 許可待ち", "{name} · 第{n}節／全{k}節", "{n}節"],
 "zh": ["翡翠绿与金", "青绿与沙色", "经本", "浅色", "深色", "示例", "这些都可以稍后在设置中更改", "电台", "书签",
        "穆罕默德·西迪克·明沙维", "正在重新连接…诵读将自动继续", "慢诵（穆朗泰勒）", "阿绥姆传述的哈夫斯", "章", "节的范围",
        "不停", "不停：读到《古兰经》末尾，再从开端章重新开始", "麦地那经本 1405H（页面字体）", "《古兰经》字体",
        "奥斯曼哈夫斯字体", "两种麦地那经本数字字体", "其他语言的界面文字", "每节一个音频文件", "⏳ 等待许可",
        "{name} · 第{n}节，共{k}节", "{n}节"],
 "tr": ["Zümrüt ve altın", "Petrol mavisi ve kum", "Mushaf", "Açık", "Koyu", "Örnek",
        "Bunların hepsi daha sonra Ayarlar'dan değiştirilebilir", "Radyo", "Yer imi", "Muhammed Sıddık el-Minşavi",
        "Yeniden bağlanıyor… tilavet kendiliğinden devam edecek", "Murattal", "Âsım'dan Hafs", "Sure", "Ayet aralığı",
        "Durmadan", "Durmadan: Kur'an'ın sonuna kadar, sonra yeniden Fatiha'dan",
        "Medine Mushafı 1405 H (sayfa yazı tipleri)", "Kur'an yazı tipleri", "Osmanî Hafs yazı tipi",
        "Medine Mushafı'nın iki dijital yazı tipi", "diğer dillerde arayüz metni", "her ayet için bir ses dosyası",
        "⏳ izin bekleniyor", "{name} · Ayet {n} / {k}", "{n} ayet"],
 "bn": ["পান্না ও সোনালি", "টিল ও বালি", "মুসহাফ", "হালকা", "গাঢ়", "উদাহরণ", "এসব পরে সেটিংসে বদলানো যাবে",
        "রেডিও", "বুকমার্ক", "মুহাম্মাদ সিদ্দিক আল-মিনশাভি", "আবার সংযোগ হচ্ছে… তিলাওয়াত নিজে থেকে আবার চলবে",
        "মুরাত্তাল", "আসিম থেকে হাফস", "সূরা", "আয়াতের পরিসর", "বিরতিহীন",
        "বিরতিহীন: কুরআনের শেষ পর্যন্ত, তারপর আবার আল-ফাতিহা থেকে", "মদিনা মুসহাফ ১৪০৫ হি. (পৃষ্ঠা ফন্ট)",
        "কুরআনের ফন্ট", "উসমানি হাফস ফন্ট", "মদিনা মুসহাফের দুটি ডিজিটাল ফন্ট", "অন্যান্য ভাষার ইন্টারফেস লেখা",
        "প্রতিটি আয়াতের একটি অডিও ফাইল", "⏳ অনুমতির অপেক্ষায়", "{name} · আয়াত {n} / {k}", "{n} আয়াত"],
 "fa": ["زمردی و طلایی", "سبزآبی و شنی", "مصحف", "روشن", "تیره", "نمونه",
        "همهٔ این‌ها را بعداً می‌توان در تنظیمات تغییر داد", "رادیو", "نشانک", "محمد صدیق منشاوی",
        "در حال اتصال دوباره… تلاوت خودبه‌خود ادامه می‌یابد", "مرتل", "حفص از عاصم", "سوره", "بازهٔ آیات", "بی‌وقفه",
        "بی‌وقفه: تا پایان قرآن، سپس دوباره از فاتحه", "مصحف مدینه ۱۴۰۵ ق (قلم‌های صفحه)", "قلم‌های قرآن",
        "قلم عثمانی حفص", "دو قلم دیجیتال مصحف مدینه", "متن رابط در زبان‌های دیگر", "یک فایل صوتی برای هر آیه",
        "⏳ در انتظار اجازه", "{name} · آیهٔ {n} از {k}", "{n} آیه"],
 "ms": ["Zamrud dan emas", "Hijau kebiruan dan pasir", "Mushaf", "Cerah", "Gelap", "Contoh",
        "Semua ini boleh diubah kemudian dalam Tetapan", "Radio", "Penanda buku", "Muhammad Siddiq al-Minshawi",
        "Menyambung semula… bacaan akan bersambung sendiri", "Murattal", "Hafs daripada Asim", "Surah", "Julat ayat",
        "Tanpa henti", "Tanpa henti: hingga akhir al-Quran, kemudian semula dari al-Fatihah",
        "Mushaf Madinah 1405H (fon halaman)", "Fon al-Quran", "Fon Uthmani Hafs", "dua fon digital mushaf Madinah",
        "teks antara muka dalam bahasa lain", "satu fail audio bagi setiap ayat", "⏳ menunggu kebenaran",
        "{name} · ayat {n} daripada {k}", "{n} ayat"],
 "sw": ["Zumaridi na dhahabu", "Kijani-buluu na mchanga", "Msahafu", "Mwanga", "Giza", "Mfano",
        "Haya yote yanaweza kubadilishwa baadaye katika Mipangilio", "Redio", "Alamisho", "Muhammad Siddiq al-Minshawi",
        "Inaunganisha tena… usomaji utaendelea wenyewe", "Murattal", "Hafs kutoka kwa Asim", "Sura", "Aya kadhaa",
        "Bila kikomo", "Bila kikomo: hadi mwisho wa Qur'ani, kisha tena kuanzia Al-Fatiha",
        "Msahafu wa Madina 1405H (fonti za kurasa)", "Fonti za Qur'ani", "Fonti ya Uthmani Hafs",
        "fonti mbili za kidijitali za Msahafu wa Madina", "maandishi ya kiolesura katika lugha nyingine",
        "faili moja ya sauti kwa kila aya", "⏳ ruhusa inasubiriwa", "{name} · aya {n} kati ya {k}", "aya {n}"],
 "ha": ["Kore da zinariya", "Shuɗi-kore da yashi", "Mushafi", "Haske", "Duhu", "Misali",
        "Duk wannan za a iya canza shi daga baya a Saituna", "Rediyo", "Alamar shafi", "Muhammad Siddiq al-Minshawi",
        "Ana sake haɗawa… karatun zai ci gaba da kansa", "Murattal", "Hafs daga Asim", "Sura", "Kewayon ayoyi",
        "Ba tsayawa", "Ba tsayawa: har zuwa ƙarshen Alƙur'ani, sannan kuma daga Fatiha",
        "Mushafin Madina 1405H (rubutun shafuka)", "Rubutun Alƙur'ani", "Rubutun Usmani na Hafs",
        "rubutun dijital biyu na Mushafin Madina", "rubutun fuskar manhaja a sauran harsuna",
        "fayil ɗaya na sauti ga kowace aya", "⏳ ana jiran izini", "{name} · aya {n} cikin {k}", "ayoyi {n}"],
 "pt": ["Esmeralda e ouro", "Azul-petróleo e areia", "Mushaf", "Claro", "Escuro", "Exemplo",
        "Tudo isto pode ser alterado depois nas Definições", "Rádio", "Marcador", "Muhammad Siddiq al-Minshawi",
        "A religar… a recitação continuará sozinha", "Murattal", "Hafs de Asim", "Surata", "Intervalo de versículos",
        "Sem fim", "Sem fim: até ao fim do Alcorão, depois de novo desde a Al-Fátiha",
        "Mushaf de Medina 1405 H (fontes de página)", "Fontes do Alcorão", "Fonte uthmani Hafs",
        "duas fontes digitais do mushaf de Medina", "texto da interface nas outras línguas",
        "um ficheiro de áudio por versículo", "⏳ permissão pendente", "{name} · versículo {n} de {k}",
        "{n} versículos"],
 "ps": ["زمرد او طلايي", "شنه-اسماني او شګلن", "مصحف", "روښانه", "تیاره", "بېلګه",
        "دا ټول وروسته په امستنو کې بدلېدای شي", "راډیو", "نښه", "محمد صدیق المنشاوي",
        "بیا نښلول کېږي… تلاوت به پخپله دوام وکړي", "مرتل", "حفص له عاصم څخه", "سورت", "د آیتونو حد", "بې ودرېدو",
        "بې ودرېدو: د قرآن تر پایه، بیا له فاتحې څخه", "د مدینې مصحف ۱۴۰۵ هـ (د پاڼو فونټونه)", "د قرآن فونټونه",
        "عثماني حفص فونټ", "د مدینې مصحف دوه ډیجیټل فونټونه", "په نورو ژبو کې د ښکارندې متن",
        "د هر آیت لپاره یو غږیز فایل", "⏳ د اجازې په تمه", "{name} · آیت {n} له {k}", "{n} آیتونه"],
 "uz": ["Zumrad va oltin", "Moviy-yashil va qum", "Mushaf", "Yorugʻ", "Qorongʻi", "Namuna",
        "Bularning barchasini keyinroq Sozlamalarda oʻzgartirish mumkin", "Radio", "Xatchoʻp",
        "Muhammad Siddiq al-Minshoviy", "Qayta ulanmoqda… tilovat oʻzi davom etadi", "Murattal", "Osimdan Hafs", "Sura",
        "Oyatlar oraligʻi", "Toʻxtovsiz", "Toʻxtovsiz: Qurʼon oxirigacha, soʻng yana Fotihadan",
        "Madina mushafi 1405 h. (sahifa shriftlari)", "Qurʼon shriftlari", "Usmoniy Hafs shrifti",
        "Madina mushafining ikki raqamli shrifti", "boshqa tillardagi interfeys matni",
        "har bir oyat uchun bitta audio fayl", "⏳ ruxsat kutilmoqda", "{name} · {k} oyatdan {n}-oyat", "{n} oyat"],
}


def page_texts():
    """Every interface text of the page: (English, Arabic), in the order they appear."""
    html = io.open(PAGE, encoding="utf-8").read()
    out, seen = [], set()

    def add(en, ar):
        if en not in seen:
            seen.add(en)
            out.append((en, ar))
    for m in re.finditer(r'data-ar="([^"]*)" data-en="([^"]*)"', html):
        add(m.group(2).replace("&amp;", "&"), m.group(1))
    script = html.split("/*LIVES-JS-END*/")[1]
    for m in re.finditer(r'ar: "([^"]*)", en: "([^"]*)"', script):
        add(m.group(2), m.group(1))
    for m in re.finditer(r'T\("([^"]*)", "([^"]*)"', script):
        add(m.group(1), m.group(2))
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    base_keys = json.load(io.open(os.path.join(I18N, "round2", "keys.json"), encoding="utf-8"))
    base_id = {k["en"]: k["id"] for k in base_keys}
    own_id = {en: kid for kid, en in NEW + NAMES}
    keys = []
    for en, ar in page_texts():
        kid = base_id.get(en) or own_id.get(en)
        if not kid:
            raise SystemExit("no id and no translation for: " + en)
        keys.append({"id": kid, "en": en, "ar": ar})
    os.makedirs(os.path.join(I18N, "round1"), exist_ok=True)
    with io.open(os.path.join(I18N, "round1", "keys.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(keys, f, ensure_ascii=False, indent=1)
        f.write("\n")
    for code, texts in T.items():
        if len(texts) != len(NEW):
            raise SystemExit("%s: %d texts, %d expected" % (code, len(texts), len(NEW)))
        base = json.load(io.open(os.path.join(I18N, "round2", code + ".json"), encoding="utf-8"))
        own = dict(zip([kid for kid, _ in NEW], texts))
        own.update({kid: en for kid, en in NAMES})
        out = {"_status": STATUS}
        for k in keys:
            out[k["id"]] = own[k["id"]] if k["id"] in own else base[k["id"]]
        with io.open(os.path.join(I18N, "round1", code + ".json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
            f.write("\n")
    shared = sum(1 for k in keys if k["id"] in base_id.values())
    print("i18n/round1: %d keys (%d shared with design 2, %d its own) x %d languages" % (len(keys), shared, len(keys) - shared, len(T)))


if __name__ == "__main__":
    main()
