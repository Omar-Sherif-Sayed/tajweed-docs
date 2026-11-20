"""Write i18n/design3/ — the interface texts of the screens that exist in design 3 only (build_design3.py).

The author chose design 3 on 2026-11-20; every new screen is made there only. Arabic and English are written here;
the other 20 languages are translated by the agent (AGENTS.md §8.9 — no native readers; users report mistakes on
GitHub). A text whose English already exists in another folder takes that folder's translations unchanged (REUSE),
so one word is not translated twice in two ways. Run it, then build_design3.py.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import i18n_check as I  # noqa: E402

OUT = os.path.join(I.I18N, "design3")
STATUS = "by the agent, 2026-11-21 — corrected from users' reports (GitHub issues, LANG-02)"

# id, English, Arabic
KEYS = [
    # home and the Lives row
    ("d3_all", "All sections", "كل الأقسام"),
    ("d3_scholars", "Scholars", "العلماء"),
    ("d3_lv_sub", "Prophets · Companions · Caliphs · Scholars", "الأنبياء · الصحابة · الخلفاء · العلماء"),
    # all sections
    ("d3_all_sub", "{n} sections, by group", "{n} قسمًا في مجموعات"),
    ("d3_st_drawn", "✔ screen drawn", "✔ مرسومة"),
    ("d3_st_part", "◐ inside another screen", "◐ داخل شاشة أخرى"),
    ("d3_st_todo", "☐ screen to come", "☐ لم تُرسم بعد"),
    ("d3_st_beh", "how playback behaves — no screen of its own", "طريقة عمل التشغيل — بلا شاشة خاصة"),
    ("d3_tap_open", "Tap a drawn section to go to its screen.", "المس قسمًا مرسومًا للانتقال إلى شاشته."),
    ("d3_g_quran", "The Noble Quran", "القرآن الكريم"),
    ("d3_g_listen", "Listening", "الاستماع"),
    ("d3_g_hifz", "Memorisation and daily portion", "الحفظ والورد"),
    ("d3_g_prayer", "Prayer and time", "الصلاة والوقت"),
    ("d3_g_dhikr", "Dhikr and dua", "الذكر والدعاء"),
    ("d3_g_know", "Knowledge", "العلم"),
    ("d3_g_guides", "Guides and tools", "الأدلة والأدوات"),
    ("d3_g_app", "The app and your devices", "التطبيق وأجهزتك"),
    ("d3_g_lives", "Lives", "السِّيَر"),
    # the 51 features
    ("f1", "Language", "اللغة"),
    ("f2", "Mushaf reader", "المصحف"),
    ("f3", "Recitation", "التلاوة"),
    ("f4", "Muallim mushaf", "المصحف المعلم"),
    ("f5", "Tafsir", "التفسير"),
    ("f6", "Tajweed", "التجويد"),
    ("f7", "Radio", "الإذاعة"),
    ("f8", "Prayer times", "مواقيت الصلاة"),
    ("f9", "Adhan", "الأذان"),
    ("f10", "Qibla", "القبلة"),
    ("f11", "Uninterrupted playback", "التشغيل دون انقطاع"),
    ("f12", "Adhkar", "الأذكار"),
    ("f13", "Hadith", "الأحاديث"),
    ("f14", "Books", "الكتب"),
    ("f15", "About", "عن التطبيق"),
    ("f16", "Quran search", "البحث في القرآن"),
    ("f17", "Sources", "المصادر"),
    ("f18", "Appearance", "المظهر"),
    ("f19", "Why this design?", "لماذا هذا التصميم؟"),
    ("f20", "Prophets", "الأنبياء"),
    ("f21", "Companions", "الصحابة"),
    ("f22", "Rightly Guided Caliphs", "الخلفاء الراشدون"),
    ("f23", "Duas", "الأدعية"),
    ("f24", "Misbaha", "المسبحة"),
    ("f25", "Ayah markers", "الفواصل"),
    ("f26", "Ayah actions", "أوامر الآية"),
    ("f27", "Hijri calendar", "التقويم الهجري"),
    ("f28", "Download for offline listening", "الاستماع دون إنترنت"),
    ("f29", "Virtues", "الفضائل"),
    ("f30", "Memorisation", "الحفظ"),
    ("f31", "Khatma and daily portion", "الختمة والورد"),
    ("f32", "My notes", "ملاحظاتي"),
    ("f33", "Share an ayah", "مشاركة آية"),
    ("f34", "Word meanings and occasions of revelation", "معاني الكلمات وأسباب النزول"),
    ("f35", "Blessed days", "الأيام الفاضلة"),
    ("f36", "The last third of the night", "الثلث الأخير من الليل"),
    ("f37", "Prayer and fasting tracker", "متابعة الصلاة والصيام"),
    ("f38", "Ruqyah", "الرقية الشرعية"),
    ("f39", "The Names of Allah", "أسماء الله الحسنى"),
    ("f40", "Guides: wudu, prayer, Hajj, Umrah", "أدلة الوضوء والصلاة والحج والعمرة"),
    ("f41", "Kids", "الأطفال"),
    ("f42", "Zakat calculator", "حاسبة الزكاة"),
    ("f43", "Home-screen widgets", "أدوات الشاشة الرئيسية"),
    ("f44", "Watch", "الساعة الذكية"),
    ("f45", "Car", "السيارة"),
    ("f46", "Nearby mosques", "المساجد القريبة"),
    ("f47", "Settings file", "ملف الإعدادات"),
    ("f48", "Names of the Prophet ﷺ", "أسماء النبي ﷺ"),
    ("f49", "Ethics and conduct", "الأخلاق والسلوك"),
    ("f50", "Islamic manners", "الآداب الشرعية"),
    ("f51", "The scholars of Islam", "علماء المسلمين"),
    # scholars
    ("d3_sch_sub", "{n} scholars · their lives from the books of biographies", "{n} عالمًا · سيرهم من كتب التراجم"),
    ("d3_by_group", "By group", "حسب المجموعة"),
    ("d3_by_time", "By time", "حسب الزمن"),
    ("d3_time_note", "In order of death: the year of birth is not recorded for some scholars and differs between sources for others, while the year of death is recorded for all. Every date is copied from the books of biographies.",
     "مرتّبون بسنة الوفاة؛ لأن سنة المولد غير مذكورة لبعضهم ومختلَف فيها عند آخرين، أما سنة الوفاة فمذكورة لهم جميعًا. كل تاريخ يُنقل من كتب التراجم."),
    ("d3_date_ph", "dates: copied from the book of biographies", "التواريخ: تُنقل من كتاب التراجم"),
    ("d3_sg_imams", "The imams of the four schools", "أئمة المذاهب الأربعة"),
    ("d3_sg_salaf", "The early generations (Salaf)", "أعلام السلف"),
    ("d3_sg_hadith", "The imams of hadith", "أئمة الحديث"),
    ("d3_sg_huffaz", "Hadith masters and commentators", "الحفّاظ والشُّرّاح"),
    ("d3_sg_tafsir", "Commentators of the Quran", "المفسرون"),
    ("d3_sg_aqeeda", "Creed and fiqh", "العقيدة والفقه"),
    ("d3_sg_seerah", "Seerah and history", "السيرة والتاريخ"),
    ("d3_sg_qiraat", "Recitations and tajweed", "القراءات والتجويد"),
    ("d3_sg_recent", "Recent scholars", "المعاصرون"),
    # one scholar
    ("d3_entry_sub", "Scholars · sample entry", "العلماء · مثال لصفحة عالم"),
    ("d3_birth_death", "Birth and death", "المولد والوفاة"),
    ("d3_life_from", "His life, word for word from:", "سيرته بنصها من:"),
    ("d3_life_ph", "The text, with book · volume · page — copied when the edition is chosen.", "النص مع الكتاب والجزء والصفحة — يُنقل بعد اختيار الطبعة."),
    ("d3_his_books", "His books in the library", "كتبه في المكتبة"),
    ("d3_report", "Report a mistake", "أبلغ عن خطأ"),
    # books
    ("d3_books_sub", "{n} books · each from a chosen edition", "{n} كتابًا · كلٌّ من طبعة مختارة"),
    ("d3_edition_ph", "Edition: to be chosen, with its rights", "الطبعة: تُختار وتُطلب حقوقها"),
    ("d3_bc_aqeeda", "Creed", "العقيدة"),
    ("d3_bc_fiqh", "Fiqh", "الفقه"),
    ("d3_bc_seerah", "Seerah, history and biographies", "السيرة والتاريخ والتراجم"),
    ("d3_bc_heart", "Purification of the heart", "الرقائق والسلوك"),
    # sources
    ("d3_s_ok", "✔ verified", "✔ تم التحقق"),
    ("d3_s_sent", "✉ letter sent — waiting for the answer", "✉ أُرسلت الرسالة — بانتظار الرد"),
    ("d3_s_ready", "✎ letter ready — to be sent", "✎ الرسالة جاهزة — لم تُرسل بعد"),
    ("d3_s_check", "⏳ to be checked", "⏳ لم يُتحقق منه بعد"),
    ("d3_s_sum", "{a} verified · {b} waiting for an answer · {c} to send · {d} to check", "{a} تم التحقق · {b} بانتظار الرد · {c} للإرسال · {d} للتحقق"),
    ("d3_s_nouse", "Nothing is used before it is verified.", "لا يُستخدم شيء قبل التحقق منه."),
    ("d3_sg_audio", "Recitations, timings and radio", "التلاوات والتوقيت والإذاعة"),
    ("d3_sg_tafsirs", "Tafsir and translations of the meanings", "التفسير وترجمات المعاني"),
    ("d3_sg_adhkar", "Adhkar and the Names of Allah", "الأذكار وأسماء الله الحسنى"),
    ("d3_sg_books", "Books and the Lives", "الكتب والسِّيَر"),
    ("d3_sg_prayer", "Prayer times, adhan and map", "المواقيت والأذان والخريطة"),
    ("s81", "the Quran text in Uthmani script", "نص القرآن الكريم بالرسم العثماني"),
    ("s82", "where each page, juz, hizb and quarter starts", "بداية كل صفحة وجزء وحزب وربع"),
    ("s83", "the words of every printed line", "ترتيب الكلمات في أسطر الصفحات كالمصحف المطبوع"),
    ("s84", "Quran font", "خط المصحف"),
    ("s85", "the printed mushaf's word shapes", "أشكال كلمات المصحف المطبوع"),
    ("s86", "Interface fonts", "خطوط الواجهة"),
    ("s87", "headings — a Kufic font", "العناوين — خط كوفي"),
    ("s88", "Arabic interface text", "النصوص العربية في الواجهة"),
    ("s89", "English interface text", "النصوص الإنجليزية في الواجهة"),
    ("r4_head", "Arabic headings", "العناوين العربية"),
    ("other_scripts", "interface text in other scripts", "نصوص الواجهة بالخطوط الأخرى"),
    ("s91", "recitations, ayah timings, radio", "التلاوات وتوقيت الآيات والإذاعات"),
    ("s92", "prayer times calculated on the device", "حساب مواقيت الصلاة على الجهاز"),
    ("u_dk_font", "the mushaf font if permission is not given — the same layout", "خط المصحف البديل إن لم يُؤذن — بالترتيب نفسه"),
    ("u_everyayah", "one audio file for each ayah", "ملف صوتي لكل آية"),
    ("u_quranenc", "translations of the meanings and tafsirs", "ترجمات معاني القرآن والتفاسير"),
    ("u_qf", "Ibn Kathir, al-Tabari, al-Qurtubi, al-Baghawi and other tafsirs", "تفسير ابن كثير والطبري والقرطبي والبغوي وغيرها"),
    ("u_sunnah", "the complete hadith collections", "كتب الحديث كاملة"),
    ("u_hadeethenc", "hadiths with their grade, explanation and translations", "أحاديث بدرجتها وشرحها وترجماتها"),
    ("u_dorar", "every scholar's ruling on a hadith — seven encyclopedias, online", "أحكام العلماء على الحديث — سبع موسوعات، مع الإنترنت"),
    ("u_hisn", "the adhkar and duas", "الأذكار والأدعية"),
    ("u_uthaymeen", "the list of the Names of Allah and their evidence", "قائمة أسماء الله الحسنى وأدلتها"),
    ("u_badr", "explanations of the Names of Allah", "شرح أسماء الله الحسنى"),
    ("u_editions", "the edition of every book of the library and of the Lives", "طبعة كل كتاب في المكتبة والسِّيَر"),
    ("u_muezzin", "the adhan recordings", "تسجيلات الأذان"),
    ("u_radio", "each station's own published stream", "البث الذي تنشره كل إذاعة بنفسها"),
    ("u_osm", "the map of nearby mosques", "خريطة المساجد القريبة"),
]

# texts that already exist, translated, in another folder: id -> (folder, id there)
REUSE = {
    "f3": ("round2", "m45"), "f5": ("round2", "m49"), "f8": ("round2", "m46"), "f10": ("round2", "m47"),
    "f12": ("round2", "m48"), "f13": ("round2", "m50"), "f14": ("round2", "m51"), "f17": ("round2", "m65"),
    "d3_g_quran": ("round2", "s80"), "d3_s_ok": ("round2", "verified"),
    "f6": ("round2", "m36"), "f7": ("extras", "ex_radio"), "f23": ("extras", "ex_duas"), "f24": ("extras", "ex_misbaha"),
    "f25": ("extras", "ex_markers"), "f26": ("extras", "ex_actions_t"), "f27": ("extras", "ex_hijri"),
    "f28": ("extras", "ex_download"), "f39": ("extras", "ex_n_allah"), "f48": ("extras", "ex_p_names"),
    "f20": ("lives", "lv_prophets"), "f21": ("lives", "lv_companions"), "f22": ("lives", "lv_caliphs"),
    "d3_g_lives": ("lives", "lv_group"),
    "d3_report": ("lives", "lv_report"),
    "s81": ("round2", "s81"), "s82": ("round2", "s82"), "s83": ("round2", "s83"), "s84": ("round2", "s84"),
    "s85": ("round2", "s85"), "s86": ("round2", "s86"), "s87": ("round2", "s87"), "s88": ("round2", "s88"),
    "s89": ("round2", "s89"), "r4_head": ("round3", "r4_head"), "other_scripts": ("round2", "other_scripts"),
    "s91": ("round2", "s91"), "s92": ("round2", "s92"),
}

# the agent's translations, in the order of I.LANG_CODES:
# ru | es | de | it | fr | ur | hi | ko | id | ja | zh | tr | bn | fa | ms | sw | ha | pt | ps | uz
T = {
    "d3_all": "Все разделы|Todas las secciones|Alle Bereiche|Tutte le sezioni|Toutes les sections|تمام حصے|सभी भाग|모든 메뉴|Semua bagian|すべてのセクション|全部栏目|Tüm bölümler|সব বিভাগ|همه بخش‌ها|Semua bahagian|Sehemu zote|Dukkan sassa|Todas as secções|ټولې برخې|Barcha boʻlimlar",
    "d3_scholars": "Учёные|Sabios|Gelehrte|Sapienti|Savants|علما|विद्वान|학자|Ulama|学者|学者|Âlimler|আলেমগণ|علما|Ulama|Wanazuoni|Malamai|Sábios|علما|Olimlar",
    "d3_lv_sub": "Пророки · Сподвижники · Халифы · Учёные|Profetas · Compañeros · Califas · Sabios|Propheten · Gefährten · Kalifen · Gelehrte|Profeti · Compagni · Califfi · Sapienti|Prophètes · Compagnons · Califes · Savants|انبیاء · صحابہ · خلفاء · علما|पैग़म्बर · सहाबा · ख़लीफ़ा · विद्वान|예언자 · 교우 · 칼리프 · 학자|Nabi · Sahabat · Khalifah · Ulama|預言者 · 教友 · カリフ · 学者|先知 · 圣门弟子 · 哈里发 · 学者|Peygamberler · Sahâbe · Halifeler · Âlimler|নবীগণ · সাহাবিগণ · খলিফাগণ · আলেমগণ|پیامبران · صحابه · خلفا · علما|Nabi · Sahabat · Khalifah · Ulama|Manabii · Maswahaba · Makhalifa · Wanazuoni|Annabawa · Sahabbai · Halifofi · Malamai|Profetas · Companheiros · Califas · Sábios|پېغمبران · صحابه · خلفا · علما|Paygʻambarlar · Sahobalar · Xalifalar · Olimlar",
    "d3_all_sub": "Разделов: {n}, по группам|{n} secciones, por grupos|{n} Bereiche, nach Gruppen|{n} sezioni, per gruppi|{n} sections, par groupes|{n} حصے، گروہوں میں|{n} भाग, समूहों में|{n}개 메뉴, 묶음별|{n} bagian, per kelompok|{n}セクション・グループ別|{n} 个栏目，按组排列|{n} bölüm, gruplara göre|{n}টি বিভাগ, দল অনুযায়ী|{n} بخش، به‌تفکیک گروه|{n} bahagian, mengikut kumpulan|Sehemu {n}, kwa makundi|Sassa {n}, bisa rukuni|{n} secções, por grupos|{n} برخې، په ډلو کې|{n} ta boʻlim, guruhlar boʻyicha",
    "d3_st_drawn": "✔ экран нарисован|✔ pantalla dibujada|✔ Bildschirm gezeichnet|✔ schermata disegnata|✔ écran dessiné|✔ اسکرین بن گئی|✔ स्क्रीन बनी|✔ 화면 있음|✔ layar sudah dibuat|✔ 画面あり|✔ 已绘制|✔ ekran çizildi|✔ পর্দা আঁকা হয়েছে|✔ صفحه طراحی شده|✔ skrin sudah dilukis|✔ skrini imechorwa|✔ an zana allo|✔ ecrã desenhado|✔ پاڼه جوړه شوې|✔ ekran chizilgan",
    "d3_st_part": "◐ внутри другого экрана|◐ dentro de otra pantalla|◐ in einem anderen Bildschirm|◐ dentro un'altra schermata|◐ dans un autre écran|◐ کسی اور اسکرین کے اندر|◐ किसी दूसरी स्क्रीन के अंदर|◐ 다른 화면 안에|◐ di dalam layar lain|◐ 別の画面の中|◐ 在其他页面中|◐ başka bir ekranın içinde|◐ অন্য পর্দার ভেতরে|◐ درون صفحه‌ای دیگر|◐ di dalam skrin lain|◐ ndani ya skrini nyingine|◐ cikin wani allo|◐ dentro de outro ecrã|◐ د بلې پاڼې دننه|◐ boshqa ekran ichida",
    "d3_st_todo": "☐ экран будет позже|☐ pantalla pendiente|☐ Bildschirm folgt|☐ schermata in arrivo|☐ écran à venir|☐ اسکرین ابھی باقی ہے|☐ स्क्रीन बाकी है|☐ 화면 예정|☐ layar menyusul|☐ 画面は今後|☐ 待绘制|☐ ekran sonra gelecek|☐ পর্দা পরে আসবে|☐ صفحه بعداً|☐ skrin akan datang|☐ skrini itakuja|☐ allo yana zuwa|☐ ecrã por fazer|☐ پاڼه وروسته|☐ ekran keyin",
    "d3_st_beh": "как работает воспроизведение — без отдельного экрана|cómo funciona la reproducción — sin pantalla propia|wie die Wiedergabe arbeitet — ohne eigenen Bildschirm|come funziona la riproduzione — senza schermata propria|le fonctionnement de la lecture — sans écran propre|پلے بیک کیسے چلتا ہے — اپنی الگ اسکرین کے بغیر|प्लेबैक कैसे चलता है — अलग स्क्रीन नहीं|재생 방식 — 별도 화면 없음|cara pemutaran bekerja — tanpa layar sendiri|再生の仕組み — 専用の画面なし|播放的运作方式 — 无独立页面|oynatmanın işleyişi — kendi ekranı yok|প্লেব্যাক কীভাবে চলে — আলাদা পর্দা নেই|نحوه پخش — بدون صفحه جداگانه|cara main balik berfungsi — tiada skrin sendiri|jinsi uchezaji unavyofanya kazi — bila skrini yake|yadda kunnawa ke aiki — ba shi da allonsa|como a reprodução funciona — sem ecrã próprio|غږېدنه څنګه کار کوي — بې له ځانګړې پاڼې|ijro qanday ishlaydi — alohida ekransiz",
    "d3_tap_open": "Нажмите на нарисованный раздел, чтобы перейти к его экрану.|Toca una sección dibujada para ir a su pantalla.|Tippen Sie auf einen gezeichneten Bereich, um zu seinem Bildschirm zu gehen.|Tocca una sezione disegnata per andare alla sua schermata.|Touchez une section dessinée pour aller à son écran.|بنی ہوئی کسی حصے کو چھوئیں تاکہ اس کی اسکرین کھلے۔|बने हुए किसी भाग को छूकर उसकी स्क्रीन पर जाएँ।|화면이 있는 메뉴를 누르면 그 화면으로 갑니다.|Ketuk bagian yang sudah dibuat untuk membuka layarnya.|画面のあるセクションをタップするとその画面へ移動します。|点按已绘制的栏目即可前往其页面。|Ekranına gitmek için çizilmiş bir bölüme dokunun.|আঁকা কোনো বিভাগে চাপ দিলে তার পর্দায় যাবেন।|روی بخشِ طراحی‌شده بزنید تا به صفحه‌اش بروید.|Ketik bahagian yang sudah dilukis untuk ke skrinnya.|Gusa sehemu iliyochorwa ili kwenda kwenye skrini yake.|Taɓa sashen da aka zana don zuwa allonsa.|Toque numa secção desenhada para ir ao seu ecrã.|جوړه شوې برخه وټکوئ چې خپلې پاڼې ته لاړ شئ.|Ekraniga oʻtish uchun chizilgan boʻlimga bosing.",
    "d3_g_listen": "Слушание|Escuchar|Hören|Ascolto|Écoute|سننا|सुनना|듣기|Mendengarkan|聴く|收听|Dinleme|শোনা|شنیدن|Mendengar|Kusikiliza|Saurare|Ouvir|اورېدل|Tinglash",
    "d3_g_hifz": "Заучивание и ежедневная доля|Memorización y porción diaria|Auswendiglernen und tägliche Portion|Memorizzazione e porzione quotidiana|Mémorisation et portion quotidienne|حفظ اور روزانہ کا ورد|हिफ़्ज़ और रोज़ का हिस्सा|암기와 매일 분량|Hafalan dan wirid harian|暗記と毎日の分量|背诵与每日功课|Hıfz ve günlük vird|হিফজ ও দৈনিক অংশ|حفظ و ورد روزانه|Hafalan dan wirid harian|Kuhifadhi na sehemu ya kila siku|Haddace da wirdin yau da kullum|Memorização e porção diária|حفظ او ورځنی ورد|Yodlash va kunlik vird",
    "d3_g_prayer": "Молитва и время|La oración y el tiempo|Gebet und Zeit|Preghiera e tempo|Prière et temps|نماز اور وقت|नमाज़ और समय|기도와 시간|Salat dan waktu|礼拝と時間|礼拜与时间|Namaz ve vakit|সালাত ও সময়|نماز و زمان|Solat dan waktu|Swala na wakati|Sallah da lokaci|Oração e tempo|لمونځ او وخت|Namoz va vaqt",
    "d3_g_dhikr": "Зикр и дуа|Dhikr y súplica|Dhikr und Bittgebet|Dhikr e supplica|Dhikr et invocation|ذکر اور دعا|ज़िक्र और दुआ|디크르와 두아|Zikir dan doa|ズィクルとドゥアー|记念与祈祷|Zikir ve dua|জিকির ও দোয়া|ذکر و دعا|Zikir dan doa|Dhikri na dua|Zikiri da addu'a|Dhikr e súplica|ذکر او دعا|Zikr va duo",
    "d3_g_know": "Знание|Conocimiento|Wissen|Conoscenza|Savoir|علم|ज्ञान|지식|Ilmu|知識|知识|İlim|জ্ঞান|دانش|Ilmu|Elimu|Ilimi|Conhecimento|علم|Ilm",
    "d3_g_guides": "Руководства и инструменты|Guías y herramientas|Anleitungen und Werkzeuge|Guide e strumenti|Guides et outils|رہنمائی اور اوزار|मार्गदर्शिकाएँ और साधन|안내와 도구|Panduan dan alat|ガイドとツール|指南与工具|Rehberler ve araçlar|নির্দেশিকা ও সরঞ্জাম|راهنماها و ابزارها|Panduan dan alat|Miongozo na zana|Jagorori da kayan aiki|Guias e ferramentas|لارښودونه او وسایل|Qoʻllanmalar va vositalar",
    "d3_g_app": "Приложение и ваши устройства|La aplicación y tus dispositivos|Die App und Ihre Geräte|L'app e i tuoi dispositivi|L'application et vos appareils|ایپ اور آپ کے آلات|ऐप और आपके उपकरण|앱과 기기|Aplikasi dan perangkat Anda|アプリと端末|应用与您的设备|Uygulama ve cihazlarınız|অ্যাপ ও আপনার ডিভাইস|برنامه و دستگاه‌های شما|Aplikasi dan peranti anda|Programu na vifaa vyako|Manhaja da na'urorinka|A aplicação e os seus dispositivos|اپ او ستاسو وسایل|Ilova va qurilmalaringiz",
    "f1": "Язык|Idioma|Sprache|Lingua|Langue|زبان|भाषा|언어|Bahasa|言語|语言|Dil|ভাষা|زبان|Bahasa|Lugha|Harshe|Idioma|ژبه|Til",
    "f2": "Мусхаф|Mushaf|Mushaf|Mushaf|Mushaf|مصحف|मुसहफ़|무스하프|Mushaf|ムスハフ|穆斯哈夫|Mushaf|মুসহাফ|مصحف|Mushaf|Msahafu|Mushafi|Mushaf|مصحف|Mushaf",
    "f4": "Обучающий мусхаф|Mushaf de enseñanza|Lern-Mushaf|Mushaf didattico|Mushaf d'apprentissage|معلم مصحف|शिक्षण मुसहफ़|학습용 무스하프|Mushaf muallim|教習用ムスハフ|教学诵读|Öğretici mushaf|শিক্ষামূলক মুসহাফ|مصحف معلم|Mushaf muallim|Msahafu wa kufundishia|Mushafin koyarwa|Mushaf de ensino|ښوونیز مصحف|Taʼlimiy mushaf",
    "f9": "Азан|Adhan|Adhan|Adhan|Adhan|اذان|अज़ान|아잔|Azan|アザーン|宣礼|Ezan|আজান|اذان|Azan|Adhana|Kiran sallah|Adhan|اذان|Azon",
    "f11": "Непрерывное воспроизведение|Reproducción sin cortes|Unterbrechungsfreie Wiedergabe|Riproduzione senza interruzioni|Lecture sans interruption|بلا تعطل سننا|बिना रुकावट चलाना|끊김 없는 재생|Pemutaran tanpa putus|途切れない再生|不间断播放|Kesintisiz oynatma|নিরবচ্ছিন্ন চালানো|پخش بی‌وقفه|Main balik tanpa henti|Uchezaji bila kukatika|Kunnawa ba tare da tsayawa ba|Reprodução sem interrupções|بې‌درزه غږېدنه|Uzluksiz ijro",
    "f15": "О приложении|Acerca de|Über die App|Informazioni|À propos|ایپ کے بارے میں|ऐप के बारे में|앱 정보|Tentang|このアプリについて|关于|Hakkında|অ্যাপ সম্পর্কে|درباره|Perihal|Kuhusu|Game da manhaja|Sobre|د اپ په اړه|Ilova haqida",
    "f16": "Поиск в Коране|Buscar en el Corán|Koransuche|Ricerca nel Corano|Recherche dans le Coran|قرآن میں تلاش|क़ुरआन में खोज|꾸란 검색|Cari dalam Al-Qur'an|クルアーン検索|古兰经搜索|Kur'an'da arama|কুরআনে অনুসন্ধান|جستجو در قرآن|Carian al-Quran|Tafuta ndani ya Qur'ani|Bincike a cikin Alƙur'ani|Pesquisa no Alcorão|په قرآن کې لټون|Qurʼondan qidirish",
    "f18": "Оформление|Apariencia|Darstellung|Aspetto|Apparence|ظاہری انداز|रूप-रंग|화면 모양|Tampilan|外観|外观|Görünüm|চেহারা|ظاهر|Paparan|Mwonekano|Kamanni|Aparência|بڼه|Koʻrinish",
    "f19": "Почему такой дизайн?|¿Por qué este diseño?|Warum dieses Design?|Perché questo design?|Pourquoi ce design ?|یہ ڈیزائن کیوں؟|यह डिज़ाइन क्यों?|왜 이 디자인인가?|Mengapa desain ini?|なぜこのデザイン?|为何这样设计？|Neden bu tasarım?|কেন এই নকশা?|چرا این طراحی؟|Mengapa reka bentuk ini?|Kwa nini muundo huu?|Me yasa wannan zane?|Porquê este design?|ولې دا ډیزاین؟|Nega bu dizayn?",
    "f29": "Достоинства|Virtudes|Vorzüge|Virtù|Mérites|فضائل|फ़ज़ीलतें|덕목|Keutamaan|功徳|功德|Faziletler|ফজিলত|فضائل|Kelebihan|Fadhila|Falaloli|Virtudes|فضیلتونه|Fazilatlar",
    "f30": "Заучивание|Memorización|Auswendiglernen|Memorizzazione|Mémorisation|حفظ|हिफ़्ज़|암기|Hafalan|暗記|背诵|Hıfz|হিফজ|حفظ|Hafalan|Kuhifadhi|Haddace|Memorização|حفظ|Yodlash",
    "f31": "Хатм и ежедневная доля|Jatma y porción diaria|Khatma und tägliche Portion|Khatma e porzione quotidiana|Khatma et portion quotidienne|ختم اور ورد|ख़त्म और रोज़ का हिस्सा|완독과 매일 분량|Khatam dan wirid|ハトマと毎日の分量|通读与每日功课|Hatim ve vird|খতম ও দৈনিক অংশ|ختم و ورد|Khatam dan wirid|Khitma na sehemu ya kila siku|Sauka da wirdi|Khatma e porção diária|ختم او ورد|Xatm va vird",
    "f32": "Мои заметки|Mis notas|Meine Notizen|Le mie note|Mes notes|میرے نوٹس|मेरे नोट्स|내 메모|Catatan saya|自分のメモ|我的笔记|Notlarım|আমার নোট|یادداشت‌های من|Nota saya|Maelezo yangu|Bayanaina|As minhas notas|زما یادښتونه|Mening qaydlarim",
    "f33": "Поделиться аятом|Compartir una aleya|Einen Vers teilen|Condividi un versetto|Partager un verset|آیت شیئر کریں|आयत साझा करें|아야 공유|Bagikan ayat|アーヤを共有|分享经文|Ayet paylaş|আয়াত শেয়ার|اشتراک آیه|Kongsi ayat|Shiriki aya|Raba aya|Partilhar um versículo|آیت شریکول|Oyatni ulashish",
    "f34": "Значения слов и причины ниспослания|Significado de las palabras y causas de la revelación|Wortbedeutungen und Offenbarungsanlässe|Significato delle parole e occasioni della rivelazione|Sens des mots et circonstances de la révélation|الفاظ کے معانی اور اسباب نزول|शब्दों के अर्थ और अवतरण के कारण|낱말 뜻과 계시 배경|Makna kata dan asbabun nuzul|語の意味と啓示の背景|词义与降示背景|Kelime anlamları ve nüzul sebepleri|শব্দার্থ ও নাজিলের প্রেক্ষাপট|معانی واژه‌ها و اسباب نزول|Makna kalimah dan asbab nuzul|Maana ya maneno na sababu za kushuka|Ma'anonin kalmomi da dalilan saukarwa|Significado das palavras e causas da revelação|د وییو مانا او د نزول اسباب|Soʻz maʼnolari va nuzul sabablari",
    "f35": "Благословенные дни|Días bendecidos|Gesegnete Tage|Giorni benedetti|Jours bénis|فضیلت والے دن|फ़ज़ीलत वाले दिन|복된 날들|Hari-hari utama|恵みの日々|尊贵的日子|Mübarek günler|ফজিলতপূর্ণ দিন|روزهای فضیلت|Hari-hari mulia|Siku zenye fadhila|Ranaku masu falala|Dias abençoados|غوره ورځې|Fazilatli kunlar",
    "f36": "Последняя треть ночи|El último tercio de la noche|Das letzte Drittel der Nacht|L'ultimo terzo della notte|Le dernier tiers de la nuit|رات کا آخری تہائی|रात का आख़िरी तिहाई|밤의 마지막 3분의 1|Sepertiga malam terakhir|夜の最後の三分の一|夜晚的最后三分之一|Gecenin son üçte biri|রাতের শেষ তৃতীয়াংশ|یک‌سوم پایانی شب|Sepertiga malam terakhir|Theluthi ya mwisho ya usiku|Sulusin ƙarshe na dare|O último terço da noite|د شپې وروستۍ دریمه برخه|Tunning soʻnggi uchdan biri",
    "f37": "Учёт молитв и постов|Registro de oración y ayuno|Gebets- und Fastenprotokoll|Registro di preghiera e digiuno|Suivi de la prière et du jeûne|نماز اور روزے کا ریکارڈ|नमाज़ और रोज़े का हिसाब|기도와 단식 기록|Catatan salat dan puasa|礼拝と斎戒の記録|礼拜与斋戒记录|Namaz ve oruç takibi|সালাত ও রোজার হিসাব|پیگیری نماز و روزه|Rekod solat dan puasa|Ufuatiliaji wa swala na saumu|Bin diddigin sallah da azumi|Registo de oração e jejum|د لمانځه او روژې څارنه|Namoz va roʻza hisobi",
    "f38": "Рукья|Ruqyah|Ruqya|Ruqyah|Roqya|رقیہ شرعیہ|रुक़्या|루끼야|Ruqyah|ルクヤ|鲁格亚|Rukye|রুকইয়াহ|رقیه شرعی|Ruqyah|Ruqya|Ruƙiyya|Ruqyah|شرعي رقیه|Ruqya",
    "f40": "Руководства: омовение, молитва, хадж, умра|Guías: ablución, oración, Hajj, Umrah|Anleitungen: Waschung, Gebet, Hadsch, Umra|Guide: abluzione, preghiera, Hajj, Umrah|Guides : ablutions, prière, Hajj, Omra|رہنمائی: وضو، نماز، حج، عمرہ|मार्गदर्शिका: वुज़ू, नमाज़, हज, उमरा|안내: 우두, 기도, 하지, 움라|Panduan: wudu, salat, haji, umrah|ガイド:ウドゥー・礼拝・ハッジ・ウムラ|指南：小净、礼拜、朝觐、副朝|Rehber: abdest, namaz, hac, umre|নির্দেশিকা: অজু, সালাত, হজ, উমরা|راهنما: وضو، نماز، حج، عمره|Panduan: wuduk, solat, haji, umrah|Miongozo: udhu, swala, Hija, Umra|Jagora: alwala, sallah, Hajji, Umra|Guias: ablução, oração, Hajj, Umrah|لارښود: اودس، لمونځ، حج، عمره|Qoʻllanma: tahorat, namoz, haj, umra",
    "f41": "Детям|Niños|Kinder|Bambini|Enfants|بچے|बच्चे|어린이|Anak-anak|子ども|儿童|Çocuklar|শিশু|کودکان|Kanak-kanak|Watoto|Yara|Crianças|ماشومان|Bolalar",
    "f42": "Калькулятор закята|Calculadora de zakat|Zakat-Rechner|Calcolatore della zakat|Calculateur de zakat|زکوٰۃ کیلکولیٹر|ज़कात कैलकुलेटर|자카트 계산기|Kalkulator zakat|ザカート計算|天课计算器|Zekât hesaplayıcı|জাকাত হিসাব|محاسبه زکات|Kalkulator zakat|Kikokotoo cha zaka|Lissafin zakka|Calculadora de zakat|د زکات حساب|Zakot kalkulyatori",
    "f43": "Виджеты главного экрана|Widgets de inicio|Startbildschirm-Widgets|Widget della schermata Home|Widgets d'écran d'accueil|ہوم اسکرین ویجیٹس|होम-स्क्रीन विजेट|홈 화면 위젯|Widget layar utama|ホーム画面ウィジェット|主屏幕小组件|Ana ekran araç takımları|হোম স্ক্রিন উইজেট|ابزارک‌های صفحه اصلی|Widget skrin utama|Wijeti za skrini ya mwanzo|Widget na allon gida|Widgets do ecrã inicial|د کور پاڼې ویجټونه|Bosh ekran vidjetlari",
    "f44": "Часы|Reloj|Uhr|Orologio|Montre|گھڑی|घड़ी|워치|Jam tangan|ウォッチ|手表|Saat|ঘড়ি|ساعت|Jam tangan|Saa|Agogo|Relógio|ګړۍ|Soat",
    "f45": "Автомобиль|Coche|Auto|Auto|Voiture|گاڑی|कार|자동차|Mobil|車|汽车|Araç|গাড়ি|خودرو|Kereta|Gari|Mota|Carro|موټر|Avtomobil",
    "f46": "Мечети поблизости|Mezquitas cercanas|Moscheen in der Nähe|Moschee vicine|Mosquées à proximité|قریبی مساجد|पास की मस्जिदें|가까운 모스크|Masjid terdekat|近くのモスク|附近的清真寺|Yakındaki camiler|কাছের মসজিদ|مساجد نزدیک|Masjid berdekatan|Misikiti iliyo karibu|Masallatai na kusa|Mesquitas próximas|نږدې جوماتونه|Yaqin masjidlar",
    "f47": "Файл настроек|Archivo de ajustes|Einstellungsdatei|File delle impostazioni|Fichier de réglages|سیٹنگز فائل|सेटिंग फ़ाइल|설정 파일|Berkas pengaturan|設定ファイル|设置文件|Ayar dosyası|সেটিংস ফাইল|پرونده تنظیمات|Fail tetapan|Faili la mipangilio|Fayil na saituna|Ficheiro de definições|د امستنو فایل|Sozlamalar fayli",
    "f49": "Нравственность и поведение|Ética y conducta|Ethik und Verhalten|Etica e condotta|Éthique et conduite|اخلاق و سلوک|नैतिकता और आचरण|윤리와 행실|Akhlak dan perilaku|倫理と行い|品德与行为|Ahlak ve davranış|আখলাক ও আচরণ|اخلاق و رفتار|Akhlak dan tingkah laku|Maadili na mwenendo|Halaye da ɗabi'u|Ética e conduta|اخلاق او چلند|Axloq va xulq",
    "f50": "Исламские нормы поведения|Modales islámicos|Islamische Umgangsformen|Buone maniere islamiche|Bienséances islamiques|شرعی آداب|इस्लामी शिष्टाचार|이슬람 예절|Adab-adab syar'i|イスラームの作法|伊斯兰礼仪|İslami adablar|ইসলামি আদব|آداب شرعی|Adab-adab syarie|Adabu za Kiislamu|Ladubban Musulunci|Boas maneiras islâmicas|شرعي آداب|Islomiy odoblar",
    "f51": "Учёные ислама|Los sabios del islam|Die Gelehrten des Islam|I sapienti dell'islam|Les savants de l'islam|علمائے اسلام|इस्लाम के विद्वान|이슬람의 학자들|Ulama Islam|イスラームの学者たち|伊斯兰学者|İslam âlimleri|ইসলামের আলেমগণ|علمای اسلام|Ulama Islam|Wanazuoni wa Uislamu|Malaman Musulunci|Os sábios do islão|د اسلام علما|Islom olimlari",
    "d3_sch_sub": "Учёных: {n} · жизнеописания из книг биографий|{n} sabios · sus vidas, de los libros de biografías|{n} Gelehrte · ihr Leben aus den Biografiewerken|{n} sapienti · le vite dai libri di biografie|{n} savants · leur vie, des livres de biographies|{n} علما · سیرتیں تراجم کی کتابوں سے|{n} विद्वान · जीवनी, जीवनी-ग्रंथों से|학자 {n}명 · 전기 문헌에서 옮긴 생애|{n} ulama · riwayat hidup dari kitab-kitab biografi|学者{n}人・伝記書からの生涯|{n} 位学者 · 生平摘自传记典籍|{n} âlim · hayatları tabakat kitaplarından|{n} জন আলেম · জীবনী, জীবনীগ্রন্থ থেকে|{n} عالم · زندگی‌نامه از کتاب‌های تراجم|{n} ulama · riwayat hidup daripada kitab biografi|Wanazuoni {n} · maisha yao kutoka vitabu vya wasifu|Malamai {n} · tarihinsu daga littattafan tarihin rayuwa|{n} sábios · as suas vidas, dos livros de biografias|{n} علما · ژوند یې د تراجمو له کتابونو|{n} olim · hayotlari tarjimai hol kitoblaridan",
    "d3_by_group": "По группам|Por grupo|Nach Gruppe|Per gruppo|Par groupe|گروہ کے لحاظ سے|समूह के अनुसार|묶음별|Per kelompok|グループ別|按组|Gruba göre|দল অনুযায়ী|به‌تفکیک گروه|Mengikut kumpulan|Kwa kundi|Bisa rukuni|Por grupo|د ډلې له مخې|Guruh boʻyicha",
    "d3_by_time": "По времени|Por época|Nach Zeit|Per epoca|Par époque|زمانے کے لحاظ سے|समय के अनुसार|시대순|Per masa|時代順|按时间|Zamana göre|সময় অনুযায়ী|به‌ترتیب زمان|Mengikut zaman|Kwa wakati|Bisa zamani|Por época|د وخت له مخې|Davr boʻyicha",
    "d3_time_note": "По году смерти: год рождения одних учёных не записан, а у других источники расходятся, тогда как год смерти записан у всех. Каждая дата переносится из книг биографий.|Por año de fallecimiento: el año de nacimiento no consta para algunos sabios y las fuentes discrepan para otros, mientras que el año de fallecimiento consta para todos. Cada fecha se copia de los libros de biografías.|Nach dem Todesjahr: Das Geburtsjahr ist bei einigen Gelehrten nicht überliefert und bei anderen umstritten, das Todesjahr aber bei allen überliefert. Jedes Datum wird aus den Biografiewerken übernommen.|Per anno di morte: l'anno di nascita non è registrato per alcuni sapienti e le fonti divergono per altri, mentre l'anno di morte è registrato per tutti. Ogni data è copiata dai libri di biografie.|Par année de décès : l'année de naissance n'est pas rapportée pour certains savants et diverge selon les sources pour d'autres, alors que l'année du décès est rapportée pour tous. Chaque date est copiée des livres de biographies.|وفات کے سال کی ترتیب سے: بعض علما کا سالِ پیدائش مذکور نہیں اور بعض کے بارے میں اختلاف ہے، جبکہ سالِ وفات سب کا مذکور ہے۔ ہر تاریخ تراجم کی کتابوں سے نقل ہوتی ہے۔|मृत्यु के वर्ष के क्रम में: कुछ विद्वानों का जन्म-वर्ष दर्ज नहीं है और कुछ के बारे में स्रोतों में मतभेद है, जबकि मृत्यु का वर्ष सबका दर्ज है। हर तारीख़ जीवनी-ग्रंथों से ली जाती है।|타계 연도순: 일부 학자는 출생 연도가 기록되지 않았고 일부는 문헌마다 다르지만, 타계 연도는 모두 기록되어 있습니다. 모든 날짜는 전기 문헌에서 옮깁니다.|Menurut tahun wafat: tahun lahir sebagian ulama tidak tercatat dan sebagian lagi diperselisihkan, sedangkan tahun wafat tercatat untuk semuanya. Setiap tanggal disalin dari kitab-kitab biografi.|没年順:生年が記録されていない学者や、資料によって異なる学者がいる一方、没年は全員について記録されています。日付はすべて伝記書から写します。|按去世年份排列：部分学者的出生年份未有记载，另一些则各家说法不一，而去世年份皆有记载。每个日期均摘自传记典籍。|Vefat yılına göre: bazı âlimlerin doğum yılı kayıtlı değildir, bazılarında kaynaklar farklıdır; vefat yılı ise hepsinde kayıtlıdır. Her tarih tabakat kitaplarından aktarılır.|মৃত্যুর বছর অনুযায়ী: কিছু আলেমের জন্মসাল লিপিবদ্ধ নেই এবং কারও ক্ষেত্রে মতভেদ আছে, কিন্তু মৃত্যুর বছর সবারই লিপিবদ্ধ। প্রতিটি তারিখ জীবনীগ্রন্থ থেকে নেওয়া হয়।|به‌ترتیب سال وفات: سال تولد برخی ثبت نشده و درباره برخی اختلاف است، اما سال وفات همه ثبت شده است. هر تاریخ از کتاب‌های تراجم نقل می‌شود.|Mengikut tahun wafat: tahun lahir sebahagian ulama tidak direkodkan dan sebahagian lagi berbeza antara sumber, sedangkan tahun wafat direkodkan untuk semua. Setiap tarikh disalin daripada kitab biografi.|Kwa mwaka wa kufariki: mwaka wa kuzaliwa haujaandikwa kwa baadhi ya wanazuoni na vyanzo vinatofautiana kwa wengine, ilhali mwaka wa kufariki umeandikwa kwa wote. Kila tarehe inanakiliwa kutoka vitabu vya wasifu.|Bisa shekarar rasuwa: ba a rubuta shekarar haihuwar wasu malamai ba, wasu kuma majiyoyi sun saɓa, amma an rubuta shekarar rasuwar kowa. Kowace kwanan wata ana kwafo ta daga littattafan tarihin rayuwa.|Por ano de falecimento: o ano de nascimento não está registado para alguns sábios e as fontes divergem para outros, enquanto o ano de falecimento está registado para todos. Cada data é copiada dos livros de biografias.|د وفات د کال له مخې: د ځینو علماوو د زوکړې کال نه دی ثبت او د ځینو په اړه اختلاف دی، خو د وفات کال د ټولو ثبت دی. هره نېټه د تراجمو له کتابونو اخیستل کېږي.|Vafot yili boʻyicha: baʼzi olimlarning tugʻilgan yili qayd etilmagan, baʼzilarida manbalar farq qiladi, vafot yili esa barchasida qayd etilgan. Har bir sana tarjimai hol kitoblaridan olinadi.",
    "d3_date_ph": "даты: из книги биографий|fechas: copiadas del libro de biografías|Daten: aus dem Biografiewerk übernommen|date: copiate dal libro di biografie|dates : copiées du livre de biographies|تاریخیں: تراجم کی کتاب سے|तारीख़ें: जीवनी-ग्रंथ से|날짜: 전기 문헌에서|tanggal: disalin dari kitab biografi|日付:伝記書から|日期：摘自传记典籍|tarihler: tabakat kitabından|তারিখ: জীবনীগ্রন্থ থেকে|تاریخ‌ها: از کتاب تراجم|tarikh: daripada kitab biografi|tarehe: kutoka kitabu cha wasifu|kwanan wata: daga littafin tarihin rayuwa|datas: copiadas do livro de biografias|نېټې: د تراجمو له کتابه|sanalar: tarjimai hol kitobidan",
    "d3_sg_imams": "Имамы четырёх мазхабов|Los imames de las cuatro escuelas|Die Imame der vier Rechtsschulen|Gli imam delle quattro scuole|Les imams des quatre écoles|چار مذاہب کے ائمہ|चार मज़हबों के इमाम|4대 법학파의 이맘|Imam empat mazhab|四法学派のイマーム|四大教法学派的伊玛目|Dört mezhebin imamları|চার মাজহাবের ইমাম|امامان مذاهب چهارگانه|Imam empat mazhab|Maimamu wa madhehebu manne|Limaman mazhabobi huɗu|Os imames das quatro escolas|د څلورو مذهبونو امامان|Toʻrt mazhab imomlari",
    "d3_sg_salaf": "Ранние поколения (саляф)|Las primeras generaciones (salaf)|Die frühen Generationen (Salaf)|Le prime generazioni (salaf)|Les premières générations (salaf)|اسلاف|सलफ़ (आरंभिक पीढ़ियाँ)|초기 세대(살라프)|Generasi salaf|初期の世代(サラフ)|前辈先贤（萨拉夫）|Selef âlimleri|সালাফগণ|بزرگان سلف|Generasi salaf|Vizazi vya mwanzo (Salaf)|Magabata (Salaf)|As primeiras gerações (salaf)|د سلفو مشران|Salaf olimlari",
    "d3_sg_hadith": "Имамы хадиса|Los imames del hadiz|Die Imame des Hadith|Gli imam dell'hadith|Les imams du hadith|ائمۂ حدیث|हदीस के इमाम|하디스의 이맘|Imam hadis|ハディースのイマーム|圣训学伊玛目|Hadis imamları|হাদিসের ইমাম|امامان حدیث|Imam hadis|Maimamu wa hadithi|Limaman hadisi|Os imames do hadith|د حدیث امامان|Hadis imomlari",
    "d3_sg_huffaz": "Знатоки хадиса и толкователи|Maestros del hadiz y comentaristas|Hadith-Meister und Kommentatoren|Maestri dell'hadith e commentatori|Maîtres du hadith et commentateurs|حفاظِ حدیث اور شارحین|हदीस के हाफ़िज़ और व्याख्याकार|하디스 대가와 주석가|Para hafiz dan pensyarah|ハディースの大家と注釈者|圣训大家与注释家|Hadis hâfızları ve şârihler|হাদিসের হাফিজ ও ব্যাখ্যাকার|حافظان و شارحان|Para hafiz dan pensyarah|Mahafidhi wa hadithi na wafafanuzi|Hafizai da masu sharhi|Mestres do hadith e comentadores|حافظان او شارحان|Hadis hofizlari va sharhlovchilar",
    "d3_sg_tafsir": "Толкователи Корана|Exegetas del Corán|Koran-Exegeten|Esegeti del Corano|Exégètes du Coran|مفسرین|मुफ़स्सिरीन|꾸란 주석가|Para mufasir|クルアーン解釈者|古兰经注释家|Müfessirler|মুফাসসিরগণ|مفسران|Para mufasir|Wafasiri wa Qur'ani|Masu tafsiri|Exegetas do Alcorão|مفسرین|Mufassirlar",
    "d3_sg_aqeeda": "Вероубеждение и фикх|Credo y fiqh|Glaubenslehre und Fiqh|Credo e fiqh|Croyance et fiqh|عقیدہ اور فقہ|अक़ीदा और फ़िक़्ह|신조와 피끄흐|Akidah dan fikih|信条とフィクフ|信仰与教法|Akaid ve fıkıh|আকিদা ও ফিকহ|عقیده و فقه|Akidah dan fiqah|Itikadi na fiqhi|Akida da fikihu|Credo e fiqh|عقیده او فقه|Aqida va fiqh",
    "d3_sg_seerah": "Сира и история|Biografía profética e historia|Prophetenbiografie und Geschichte|Biografia profetica e storia|Sîra et histoire|سیرت اور تاریخ|सीरत और इतिहास|시라와 역사|Sirah dan sejarah|預言者伝と歴史|先知传记与历史|Siyer ve tarih|সিরাত ও ইতিহাস|سیره و تاریخ|Sirah dan sejarah|Sira na historia|Sira da tarihi|Biografia profética e história|سیرت او تاریخ|Siyrat va tarix",
    "d3_sg_qiraat": "Чтения и таджвид|Lecturas y tajwid|Lesarten und Tadschwid|Letture e tajwid|Lectures et tajwid|قراءات اور تجوید|क़िराअत और तजवीद|낭송법과 타즈위드|Qiraat dan tajwid|読誦法とタジュウィード|诵读法与泰吉威德|Kıraat ve tecvid|কিরাআত ও তাজবিদ|قرائات و تجوید|Qiraat dan tajwid|Visomo na tajwidi|Kira'o'i da tajwidi|Leituras e tajwid|قرائتونه او تجوید|Qiroatlar va tajvid",
    "d3_sg_recent": "Современные учёные|Sabios contemporáneos|Zeitgenössische Gelehrte|Sapienti contemporanei|Savants contemporains|معاصر علما|समकालीन विद्वान|현대 학자|Ulama kontemporer|近現代の学者|当代学者|Çağdaş âlimler|সমকালীন আলেম|علمای معاصر|Ulama semasa|Wanazuoni wa zama hizi|Malaman zamani|Sábios contemporâneos|معاصر علما|Zamonaviy olimlar",
    "d3_entry_sub": "Учёные · пример страницы|Sabios · ejemplo de ficha|Gelehrte · Beispieleintrag|Sapienti · esempio di scheda|Savants · exemple de fiche|علما · نمونہ صفحہ|विद्वान · नमूना पृष्ठ|학자 · 예시 항목|Ulama · contoh entri|学者・項目の例|学者 · 示例条目|Âlimler · örnek sayfa|আলেমগণ · নমুনা পাতা|علما · نمونه صفحه|Ulama · contoh entri|Wanazuoni · mfano wa ukurasa|Malamai · misalin shafi|Sábios · exemplo de ficha|علما · بېلګه پاڼه|Olimlar · namuna sahifa",
    "d3_birth_death": "Рождение и смерть|Nacimiento y fallecimiento|Geburt und Tod|Nascita e morte|Naissance et décès|پیدائش اور وفات|जन्म और मृत्यु|출생과 타계|Lahir dan wafat|生誕と逝去|生卒|Doğum ve vefat|জন্ম ও মৃত্যু|تولد و وفات|Lahir dan wafat|Kuzaliwa na kufariki|Haihuwa da rasuwa|Nascimento e falecimento|زوکړه او وفات|Tugʻilishi va vafoti",
    "d3_life_from": "Его жизнь, дословно из:|Su vida, textualmente de:|Sein Leben, wörtlich aus:|La sua vita, alla lettera da:|Sa vie, mot pour mot, d'après :|ان کی سیرت، لفظ بلفظ:|उनकी जीवनी, शब्दशः:|그의 생애, 원문 그대로:|Riwayat hidupnya, kata demi kata dari:|その生涯(原文のまま):|其生平，逐字摘自：|Hayatı, kelimesi kelimesine:|তাঁর জীবনী, হুবহু:|زندگی‌نامه‌اش، عیناً از:|Riwayat hidupnya, kata demi kata daripada:|Maisha yake, neno kwa neno kutoka:|Tarihinsa, kalma da kalma daga:|A sua vida, palavra por palavra, de:|د هغه ژوند، کټ مټ له:|Hayoti, soʻzma-soʻz:",
    "d3_life_ph": "Текст с указанием книги · тома · страницы — переносится после выбора издания.|El texto, con libro · volumen · página — se copia cuando se elija la edición.|Der Text mit Buch · Band · Seite — wird übernommen, sobald die Ausgabe gewählt ist.|Il testo, con libro · volume · pagina — copiato quando sarà scelta l'edizione.|Le texte, avec livre · volume · page — copié une fois l'édition choisie.|متن، کتاب · جلد · صفحہ کے ساتھ — ایڈیشن منتخب ہونے پر نقل ہوگا۔|पाठ, ग्रंथ · खंड · पृष्ठ सहित — संस्करण चुने जाने पर लिया जाएगा।|본문(책 · 권 · 쪽) — 판본이 정해지면 옮깁니다.|Teks dengan kitab · jilid · halaman — disalin setelah edisi dipilih.|本文(書名・巻・頁)— 版が決まってから写します。|正文（书名 · 卷 · 页）— 选定版本后摘录。|Metin, kitap · cilt · sayfa ile — baskı seçilince aktarılır.|মূল পাঠ, গ্রন্থ · খণ্ড · পৃষ্ঠাসহ — সংস্করণ বাছাইয়ের পর নেওয়া হবে।|متن، با کتاب · جلد · صفحه — پس از انتخاب چاپ نقل می‌شود.|Teks, dengan kitab · jilid · halaman — disalin selepas edisi dipilih.|Maandishi, pamoja na kitabu · juzuu · ukurasa — yatanakiliwa toleo litakapochaguliwa.|Rubutun, tare da littafi · juzu'i · shafi — za a kwafo shi idan aka zaɓi bugu.|O texto, com livro · volume · página — copiado quando a edição for escolhida.|متن، د کتاب · ټوک · مخ سره — د چاپ له ټاکلو وروسته نقلېږي.|Matn, kitob · jild · sahifa bilan — nashr tanlangach koʻchiriladi.",
    "d3_his_books": "Его книги в библиотеке|Sus libros en la biblioteca|Seine Bücher in der Bibliothek|I suoi libri nella biblioteca|Ses livres dans la bibliothèque|لائبریری میں ان کی کتابیں|पुस्तकालय में उनकी किताबें|서재에 있는 그의 책|Kitab-kitabnya di perpustakaan|ライブラリにある著作|图书馆中的著作|Kütüphanedeki kitapları|গ্রন্থাগারে তাঁর বই|کتاب‌هایش در کتابخانه|Kitab-kitabnya di perpustakaan|Vitabu vyake maktabani|Littattafansa a ɗakin karatu|Os seus livros na biblioteca|په کتابتون کې د هغه کتابونه|Kutubxonadagi kitoblari",
    "d3_books_sub": "Книг: {n} · каждая из выбранного издания|{n} libros · cada uno de una edición elegida|{n} Bücher · jedes aus einer gewählten Ausgabe|{n} libri · ciascuno da un'edizione scelta|{n} livres · chacun d'une édition choisie|{n} کتابیں · ہر ایک منتخب ایڈیشن سے|{n} किताबें · हर एक चुने हुए संस्करण से|책 {n}권 · 각각 선택한 판본으로|{n} kitab · masing-masing dari edisi terpilih|{n}冊・それぞれ選んだ版から|{n} 本书 · 均采用选定版本|{n} kitap · her biri seçilmiş bir baskıdan|{n}টি বই · প্রতিটি নির্বাচিত সংস্করণ থেকে|{n} کتاب · هرکدام از چاپی برگزیده|{n} kitab · setiap satu daripada edisi terpilih|Vitabu {n} · kila kimoja kutoka toleo lililochaguliwa|Littattafai {n} · kowanne daga zaɓaɓɓen bugu|{n} livros · cada um de uma edição escolhida|{n} کتابونه · هر یو له ټاکل شوي چاپه|{n} ta kitob · har biri tanlangan nashrdan",
    "d3_edition_ph": "Издание: будет выбрано, с правами|Edición: por elegir, con sus derechos|Ausgabe: wird gewählt, mit ihren Rechten|Edizione: da scegliere, con i suoi diritti|Édition : à choisir, avec ses droits|ایڈیشن: منتخب ہوگا، اس کے حقوق کے ساتھ|संस्करण: चुना जाएगा, उसके अधिकारों सहित|판본: 권리와 함께 선정 예정|Edisi: akan dipilih, beserta haknya|版:権利とともに今後選定|版本：待选定，并取得授权|Baskı: hakları ile birlikte seçilecek|সংস্করণ: অধিকারসহ বাছাই হবে|چاپ: همراه با حقوقش انتخاب می‌شود|Edisi: akan dipilih, bersama haknya|Toleo: litachaguliwa, pamoja na haki zake|Bugu: za a zaɓa, tare da haƙƙoƙinsa|Edição: a escolher, com os seus direitos|چاپ: له حقونو سره به وټاکل شي|Nashr: huquqlari bilan tanlanadi",
    "d3_bc_aqeeda": "Вероубеждение|Credo|Glaubenslehre|Credo|Croyance|عقیدہ|अक़ीदा|신조|Akidah|信条|信仰|Akaid|আকিদা|عقیده|Akidah|Itikadi|Akida|Credo|عقیده|Aqida",
    "d3_bc_fiqh": "Фикх|Fiqh|Fiqh|Fiqh|Fiqh|فقہ|फ़िक़्ह|피끄흐|Fikih|フィクフ|教法|Fıkıh|ফিকহ|فقه|Fiqah|Fiqhi|Fikihu|Fiqh|فقه|Fiqh",
    "d3_bc_seerah": "Сира, история и биографии|Biografía profética, historia y biografías|Prophetenbiografie, Geschichte und Biografien|Biografia profetica, storia e biografie|Sîra, histoire et biographies|سیرت، تاریخ اور تراجم|सीरत, इतिहास और जीवनियाँ|시라, 역사, 전기|Sirah, sejarah, dan biografi|預言者伝・歴史・伝記|先知传记、历史与人物传记|Siyer, tarih ve tabakat|সিরাত, ইতিহাস ও জীবনী|سیره، تاریخ و تراجم|Sirah, sejarah dan biografi|Sira, historia na wasifu|Sira, tarihi da tarihin rayuwa|Biografia profética, história e biografias|سیرت، تاریخ او تراجم|Siyrat, tarix va tarjimai hollar",
    "d3_bc_heart": "Очищение сердца|Purificación del corazón|Läuterung des Herzens|Purificazione del cuore|Purification du cœur|رقائق و سلوک|हृदय की शुद्धि|마음의 정화|Penyucian hati|心の浄化|心灵修养|Rekâik ve sülûk|অন্তরের পরিশুদ্ধি|رقائق و سلوک|Penyucian hati|Kutakasa moyo|Tsarkake zuciya|Purificação do coração|د زړه پاکول|Qalb poklanishi",
    "d3_s_sent": "✉ письмо отправлено — ждём ответа|✉ carta enviada — esperando respuesta|✉ Brief gesendet — Antwort ausstehend|✉ lettera inviata — in attesa di risposta|✉ lettre envoyée — réponse attendue|✉ خط بھیج دیا — جواب کا انتظار|✉ पत्र भेजा — उत्तर की प्रतीक्षा|✉ 편지 보냄 — 답변 대기|✉ surat terkirim — menunggu jawaban|✉ 書簡送付済み — 返事待ち|✉ 已发函 — 等待回复|✉ mektup gönderildi — yanıt bekleniyor|✉ চিঠি পাঠানো হয়েছে — উত্তরের অপেক্ষা|✉ نامه فرستاده شد — در انتظار پاسخ|✉ surat dihantar — menunggu jawapan|✉ barua imetumwa — tunasubiri jibu|✉ an aika wasiƙa — ana jiran amsa|✉ carta enviada — à espera de resposta|✉ لیک ولېږل شو — ځواب ته انتظار|✉ xat yuborildi — javob kutilmoqda",
    "d3_s_ready": "✎ письмо готово — ещё не отправлено|✎ carta lista — por enviar|✎ Brief fertig — noch nicht gesendet|✎ lettera pronta — da inviare|✎ lettre prête — à envoyer|✎ خط تیار — ابھی بھیجنا ہے|✎ पत्र तैयार — भेजना बाकी|✎ 편지 준비됨 — 아직 안 보냄|✎ surat siap — belum dikirim|✎ 書簡準備済み — 未送付|✎ 函件已备好 — 尚未发送|✎ mektup hazır — gönderilecek|✎ চিঠি প্রস্তুত — এখনো পাঠানো হয়নি|✎ نامه آماده — هنوز فرستاده نشده|✎ surat sedia — belum dihantar|✎ barua iko tayari — bado kutumwa|✎ wasiƙa ta shirya — ba a aika ba tukuna|✎ carta pronta — por enviar|✎ لیک چمتو دی — لا نه دی لېږل شوی|✎ xat tayyor — hali yuborilmagan",
    "d3_s_check": "⏳ ещё не проверено|⏳ por verificar|⏳ noch zu prüfen|⏳ da verificare|⏳ à vérifier|⏳ ابھی تصدیق نہیں ہوئی|⏳ अभी जाँच बाकी|⏳ 확인 예정|⏳ belum diperiksa|⏳ 未確認|⏳ 待核实|⏳ henüz doğrulanmadı|⏳ এখনো যাচাই হয়নি|⏳ هنوز بررسی نشده|⏳ belum disemak|⏳ bado kuthibitishwa|⏳ ba a tabbatar ba tukuna|⏳ por verificar|⏳ لا نه دی کره شوی|⏳ hali tekshirilmagan",
    "d3_s_sum": "{a} проверено · {b} ждут ответа · {c} к отправке · {d} к проверке|{a} verificados · {b} esperando respuesta · {c} por enviar · {d} por verificar|{a} geprüft · {b} warten auf Antwort · {c} zu senden · {d} zu prüfen|{a} verificati · {b} in attesa di risposta · {c} da inviare · {d} da verificare|{a} vérifiés · {b} en attente de réponse · {c} à envoyer · {d} à vérifier|{a} تصدیق شدہ · {b} جواب کے منتظر · {c} بھیجنے ہیں · {d} جانچنے ہیں|{a} जाँचे गए · {b} उत्तर की प्रतीक्षा · {c} भेजने हैं · {d} जाँचने हैं|확인 {a} · 답변 대기 {b} · 발송 예정 {c} · 확인 예정 {d}|{a} terverifikasi · {b} menunggu jawaban · {c} akan dikirim · {d} akan diperiksa|確認済み{a} · 返事待ち{b} · 送付予定{c} · 確認予定{d}|已核实 {a} · 等待回复 {b} · 待发送 {c} · 待核实 {d}|{a} doğrulandı · {b} yanıt bekliyor · {c} gönderilecek · {d} doğrulanacak|{a}টি যাচাই হয়েছে · {b}টি উত্তরের অপেক্ষায় · {c}টি পাঠাতে হবে · {d}টি যাচাই বাকি|{a} بررسی‌شده · {b} در انتظار پاسخ · {c} برای فرستادن · {d} برای بررسی|{a} disahkan · {b} menunggu jawapan · {c} untuk dihantar · {d} untuk disemak|{a} vimethibitishwa · {b} vinasubiri jibu · {c} vya kutuma · {d} vya kuthibitisha|{a} an tabbatar · {b} suna jiran amsa · {c} za a aika · {d} za a tabbatar|{a} verificados · {b} à espera de resposta · {c} por enviar · {d} por verificar|{a} کره شوي · {b} ځواب ته په تمه · {c} د لېږلو · {d} د کرهولو|{a} tekshirilgan · {b} javob kutmoqda · {c} yuboriladi · {d} tekshiriladi",
    "d3_s_nouse": "Ничего не используется до проверки.|Nada se usa antes de verificarse.|Nichts wird vor der Prüfung verwendet.|Nulla viene usato prima di essere verificato.|Rien n'est utilisé avant d'être vérifié.|تصدیق سے پہلے کچھ استعمال نہیں ہوتا۔|जाँच से पहले कुछ भी उपयोग नहीं होता।|확인 전에는 아무것도 쓰지 않습니다.|Tidak ada yang dipakai sebelum diverifikasi.|確認する前には何も使いません。|未经核实，一概不用。|Doğrulanmadan hiçbir şey kullanılmaz.|যাচাইয়ের আগে কিছুই ব্যবহার করা হয় না।|هیچ چیز پیش از بررسی به کار نمی‌رود.|Tiada apa yang digunakan sebelum disahkan.|Hakuna kinachotumika kabla ya kuthibitishwa.|Ba a amfani da komai kafin a tabbatar da shi.|Nada é usado antes de ser verificado.|تر کرهولو مخکې هېڅ نه کارول کېږي.|Tekshirilmaguncha hech narsa ishlatilmaydi.",
    "d3_sg_audio": "Чтения, тайминги и радио|Recitaciones, tiempos y radio|Rezitationen, Zeitmarken und Radio|Recitazioni, tempi e radio|Récitations, minutages et radio|تلاوتیں، اوقات اور ریڈیو|तिलावतें, समय और रेडियो|낭송, 시간 정보, 라디오|Murattal, waktu ayat, dan radio|朗誦・タイミング・ラジオ|诵读、时间标记与电台|Tilavetler, zamanlamalar ve radyo|তিলাওয়াত, সময় ও রেডিও|تلاوت‌ها، زمان‌بندی و رادیو|Bacaan, masa ayat dan radio|Visomo, nyakati na redio|Karatu, lokuta da rediyo|Recitações, tempos e rádio|تلاوتونه، وختونه او راډیو|Tilovatlar, vaqtlar va radio",
    "d3_sg_tafsirs": "Тафсир и переводы смыслов|Tafsir y traducciones del significado|Tafsir und Übersetzungen der Bedeutungen|Tafsir e traduzioni dei significati|Tafsir et traductions du sens|تفسیر اور ترجمۂ معانی|तफ़सीर और अर्थों के अनुवाद|타프시르와 의미 번역|Tafsir dan terjemahan makna|タフスィールと意味の翻訳|经注与意义译解|Tefsir ve meal|তাফসির ও অর্থের অনুবাদ|تفسیر و ترجمه معانی|Tafsir dan terjemahan makna|Tafsiri na tafsiri za maana|Tafsiri da fassarorin ma'ana|Tafsir e traduções do significado|تفسیر او د مانا ژباړې|Tafsir va maʼnolar tarjimasi",
    "d3_sg_adhkar": "Азкары и имена Аллаха|Adhkar y los nombres de Allah|Adhkar und die Namen Allahs|Adhkar e i nomi di Allah|Adhkar et les noms d'Allah|اذکار اور اسمائے حسنیٰ|अज़कार और अल्लाह के नाम|아드카르와 알라의 이름|Zikir dan Asmaul Husna|ズィクルとアッラーの御名|记念词与真主的尊名|Zikirler ve Esmâ-i Hüsnâ|জিকির ও আল্লাহর নাম|اذکار و اسمای حسنی|Zikir dan Asmaul Husna|Adhkar na Majina ya Allah|Azkar da Sunayen Allah|Adhkar e os nomes de Allah|اذکار او د الله نومونه|Zikrlar va Alloh ismlari",
    "d3_sg_books": "Книги и жизнеописания|Libros y vidas|Bücher und Lebensgeschichten|Libri e vite|Livres et vies|کتابیں اور سیرتیں|किताबें और जीवनियाँ|책과 전기|Kitab dan riwayat hidup|書籍と伝記|典籍与传记|Kitaplar ve hayatlar|বই ও জীবনী|کتاب‌ها و سیره‌ها|Kitab dan riwayat hidup|Vitabu na wasifu|Littattafai da tarihin rayuwa|Livros e vidas|کتابونه او سیرتونه|Kitoblar va siyratlar",
    "d3_sg_prayer": "Время молитв, азан и карта|Horarios de oración, adhan y mapa|Gebetszeiten, Adhan und Karte|Orari di preghiera, adhan e mappa|Heures de prière, adhan et carte|اوقاتِ نماز، اذان اور نقشہ|नमाज़ का समय, अज़ान और नक़्शा|기도 시간, 아잔, 지도|Waktu salat, azan, dan peta|礼拝時刻・アザーン・地図|礼拜时间、宣礼与地图|Namaz vakitleri, ezan ve harita|সালাতের সময়, আজান ও মানচিত্র|اوقات نماز، اذان و نقشه|Waktu solat, azan dan peta|Nyakati za swala, adhana na ramani|Lokutan sallah, kiran sallah da taswira|Horários de oração, adhan e mapa|د لمانځه وختونه، اذان او نقشه|Namoz vaqtlari, azon va xarita",
    "u_dk_font": "шрифт мусхафа, если разрешения не будет — та же вёрстка|la fuente del mushaf si no hay permiso — la misma maquetación|die Mushaf-Schrift, falls keine Erlaubnis kommt — dasselbe Layout|il carattere del mushaf se manca il permesso — la stessa impaginazione|la police du mushaf si l'autorisation n'est pas donnée — même mise en page|اجازت نہ ملنے پر مصحف کا متبادل خط — وہی ترتیب|अनुमति न मिले तो मुसहफ़ का दूसरा फ़ॉन्ट — वही विन्यास|허락이 없을 때의 무스하프 글꼴 — 같은 배치|fon mushaf bila izin tidak diberikan — tata letak sama|許可がない場合のムスハフ書体 — 同じ配置|未获许可时的备用经文字体 — 版式相同|izin verilmezse mushaf yazı tipi — aynı düzen|অনুমতি না পেলে মুসহাফের বিকল্প ফন্ট — একই বিন্যাস|قلم جایگزین مصحف اگر اجازه داده نشود — همان چینش|fon mushaf jika izin tidak diberi — susun atur sama|fonti ya msahafu ikiwa ruhusa haitatolewa — mpangilio uleule|rubutun mushafi idan ba a bayar da izini ba — tsari ɗaya|a fonte do mushaf se não houver autorização — a mesma paginação|که اجازه ورنه کړل شي د مصحف بدیل لیک — هماغه ترتیب|ruxsat berilmasa mushaf shrifti — oʻsha joylashuv",
    "u_everyayah": "аудиофайл для каждого аята|un archivo de audio por aleya|eine Audiodatei für jeden Vers|un file audio per ogni versetto|un fichier audio par verset|ہر آیت کی آڈیو فائل|हर आयत की ऑडियो फ़ाइल|아야마다 음성 파일|satu berkas audio untuk setiap ayat|アーヤごとの音声ファイル|每节经文一个音频文件|her ayet için bir ses dosyası|প্রতিটি আয়াতের অডিও ফাইল|یک فایل صوتی برای هر آیه|satu fail audio bagi setiap ayat|faili la sauti kwa kila aya|fayil ɗin sauti na kowace aya|um ficheiro áudio por versículo|د هرې آیت غږیز فایل|har bir oyat uchun audio fayl",
    "u_quranenc": "переводы смыслов и тафсиры|traducciones del significado y tafsires|Übersetzungen der Bedeutungen und Tafsire|traduzioni dei significati e tafsir|traductions du sens et tafsirs|ترجمۂ معانی اور تفاسیر|अर्थों के अनुवाद और तफ़सीरें|의미 번역과 타프시르|terjemahan makna dan tafsir|意味の翻訳とタフスィール|意义译解与经注|mealler ve tefsirler|অর্থের অনুবাদ ও তাফসির|ترجمه‌های معانی و تفاسیر|terjemahan makna dan tafsir|tafsiri za maana na tafsiri|fassarorin ma'ana da tafsirai|traduções do significado e tafsires|د مانا ژباړې او تفسیرونه|maʼnolar tarjimalari va tafsirlar",
    "u_qf": "Ибн Касир, ат-Табари, аль-Куртуби, аль-Багави и другие тафсиры|Ibn Kazir, at-Tabari, al-Qurtubi, al-Bagawi y otros tafsires|Ibn Kathir, at-Tabari, al-Qurtubi, al-Baghawi und weitere Tafsire|Ibn Kathir, al-Tabari, al-Qurtubi, al-Baghawi e altri tafsir|Ibn Kathir, at-Tabari, al-Qurtubi, al-Baghawi et d'autres tafsirs|ابن کثیر، طبری، قرطبی، بغوی اور دیگر تفاسیر|इब्न कसीर, तबरी, क़ुरतुबी, बग़वी और अन्य तफ़सीरें|이븐 카시르, 따바리, 꾸르뚜비, 바가위 등의 타프시르|Ibnu Katsir, ath-Thabari, al-Qurthubi, al-Baghawi, dan tafsir lain|イブン・カスィール、タバリー、クルトゥビー、バガウィーほか|伊本·凯西尔、泰伯里、古尔图比、白厄威等经注|İbn Kesîr, Taberî, Kurtubî, Begavî ve diğer tefsirler|ইবনে কাসির, তাবারি, কুরতুবি, বাগাবি ও অন্যান্য তাফসির|ابن کثیر، طبری، قرطبی، بغوی و تفاسیر دیگر|Ibn Kathir, al-Tabari, al-Qurtubi, al-Baghawi dan tafsir lain|Ibn Kathir, al-Tabari, al-Qurtubi, al-Baghawi na tafsiri nyingine|Ibn Kasir, Ɗabari, Ƙurɗubi, Bagawi da sauran tafsirai|Ibn Kathir, at-Tabari, al-Qurtubi, al-Baghawi e outros tafsires|ابن کثیر، طبري، قرطبي، بغوي او نور تفسیرونه|Ibn Kasir, Tabariy, Qurtubiy, Bagʻaviy va boshqa tafsirlar",
    "u_sunnah": "полные сборники хадисов|las colecciones completas de hadices|die vollständigen Hadith-Sammlungen|le raccolte complete di hadith|les recueils complets de hadiths|حدیث کی مکمل کتابیں|हदीस के पूरे संग्रह|하디스 모음집 전체|kitab-kitab hadis lengkap|ハディース集の全巻|完整的圣训集|tam hadis külliyatları|হাদিসের পূর্ণ গ্রন্থসমূহ|کتاب‌های کامل حدیث|kitab-kitab hadis lengkap|mikusanyiko kamili ya hadithi|cikakkun littattafan hadisi|as coleções completas de hadith|د حدیث بشپړ کتابونه|toʻliq hadis toʻplamlari",
    "u_hadeethenc": "хадисы со степенью, разъяснением и переводами|hadices con su grado, explicación y traducciones|Hadithe mit Einstufung, Erläuterung und Übersetzungen|hadith con grado, spiegazione e traduzioni|hadiths avec leur degré, leur explication et leurs traductions|احادیث، درجہ، شرح اور تراجم کے ساتھ|दर्जे, व्याख्या और अनुवाद सहित हदीसें|등급·해설·번역이 있는 하디스|hadis beserta derajat, syarah, dan terjemahannya|等級・解説・翻訳付きのハディース|附等级、讲解与译文的圣训|derecesi, şerhi ve tercümeleriyle hadisler|মান, ব্যাখ্যা ও অনুবাদসহ হাদিস|احادیث با درجه، شرح و ترجمه|hadis berserta darjat, syarah dan terjemahan|hadithi pamoja na daraja, maelezo na tafsiri zake|hadisai tare da darajarsu, sharhi da fassarori|hadiths com o seu grau, explicação e traduções|احادیث له درجې، شرحې او ژباړو سره|darajasi, sharhi va tarjimalari bilan hadislar",
    "u_dorar": "суждения всех учёных о хадисе — семь энциклопедий, онлайн|el juicio de cada sabio sobre un hadiz — siete enciclopedias, en línea|das Urteil jedes Gelehrten über einen Hadith — sieben Enzyklopädien, online|il giudizio di ogni sapiente su un hadith — sette enciclopedie, online|le jugement de chaque savant sur un hadith — sept encyclopédies, en ligne|حدیث پر ہر عالم کا حکم — سات انسائیکلوپیڈیا، آن لائن|हदीस पर हर विद्वान का हुक्म — सात विश्वकोश, ऑनलाइन|하디스에 대한 모든 학자의 판정 — 백과사전 7종, 온라인|hukum setiap ulama atas hadis — tujuh ensiklopedia, daring|ハディースへの各学者の判定 — 7つの百科事典、オンライン|各位学者对圣训的判定 — 七部百科，联网使用|her âlimin hadis hakkındaki hükmü — yedi ansiklopedi, çevrimiçi|হাদিস সম্পর্কে প্রত্যেক আলেমের হুকুম — সাতটি বিশ্বকোষ, অনলাইনে|حکم هر عالم درباره حدیث — هفت دانشنامه، برخط|hukum setiap ulama terhadap hadis — tujuh ensiklopedia, dalam talian|hukumu ya kila mwanazuoni juu ya hadithi — ensaiklopidia saba, mtandaoni|hukuncin kowane malami kan hadisi — kundin ilimi bakwai, a intanet|o juízo de cada sábio sobre um hadith — sete enciclopédias, online|په حدیث د هر عالم حکم — اووه پوهنغونډونه، آنلاین|har bir olimning hadis haqidagi hukmi — yetti ensiklopediya, onlayn",
    "u_hisn": "азкары и дуа|los adhkar y las súplicas|Adhkar und Bittgebete|adhkar e suppliche|les adhkar et les invocations|اذکار اور دعائیں|अज़कार और दुआएँ|아드카르와 두아|zikir dan doa|ズィクルとドゥアー|记念词与祈祷词|zikirler ve dualar|জিকির ও দোয়া|اذکار و دعاها|zikir dan doa|adhkar na dua|azkar da addu'o'i|os adhkar e as súplicas|اذکار او دعاګانې|zikrlar va duolar",
    "u_uthaymeen": "список имён Аллаха и их доказательства|la lista de los nombres de Allah y sus pruebas|die Liste der Namen Allahs und ihre Belege|l'elenco dei nomi di Allah e le loro prove|la liste des noms d'Allah et leurs preuves|اسمائے حسنیٰ کی فہرست اور ان کے دلائل|अल्लाह के नामों की सूची और उनके प्रमाण|알라의 이름 목록과 그 근거|daftar Asmaul Husna dan dalilnya|アッラーの御名の一覧とその典拠|真主尊名的列表及其依据|Esmâ-i Hüsnâ listesi ve delilleri|আল্লাহর নামের তালিকা ও দলিল|فهرست اسمای حسنی و دلایل آن|senarai Asmaul Husna dan dalilnya|orodha ya Majina ya Allah na ushahidi wake|jerin Sunayen Allah da hujjojinsu|a lista dos nomes de Allah e as suas provas|د الله د نومونو لړلیک او دلیلونه یې|Alloh ismlari roʻyxati va dalillari",
    "u_badr": "разъяснение имён Аллаха|explicación de los nombres de Allah|Erläuterung der Namen Allahs|spiegazione dei nomi di Allah|explication des noms d'Allah|اسمائے حسنیٰ کی شرح|अल्लाह के नामों की व्याख्या|알라의 이름 해설|syarah Asmaul Husna|アッラーの御名の解説|真主尊名的讲解|Esmâ-i Hüsnâ şerhi|আল্লাহর নামের ব্যাখ্যা|شرح اسمای حسنی|syarah Asmaul Husna|maelezo ya Majina ya Allah|sharhin Sunayen Allah|explicação dos nomes de Allah|د الله د نومونو شرحه|Alloh ismlari sharhi",
    "u_editions": "издание каждой книги библиотеки и жизнеописаний|la edición de cada libro de la biblioteca y de las vidas|die Ausgabe jedes Buches der Bibliothek und der Lebensgeschichten|l'edizione di ogni libro della biblioteca e delle vite|l'édition de chaque livre de la bibliothèque et des vies|لائبریری اور سیرتوں کی ہر کتاب کا ایڈیشن|पुस्तकालय और जीवनियों की हर किताब का संस्करण|서재와 전기의 모든 책 판본|edisi setiap kitab di perpustakaan dan riwayat hidup|ライブラリと伝記の各書の版|图书馆与传记中每本书的版本|kütüphane ve hayatlar bölümündeki her kitabın baskısı|গ্রন্থাগার ও জীবনীর প্রতিটি বইয়ের সংস্করণ|چاپ هر کتاب کتابخانه و سیره‌ها|edisi setiap kitab perpustakaan dan riwayat hidup|toleo la kila kitabu cha maktaba na wasifu|bugun kowane littafi na ɗakin karatu da tarihin rayuwa|a edição de cada livro da biblioteca e das vidas|د کتابتون او سیرتونو د هر کتاب چاپ|kutubxona va siyratlardagi har bir kitob nashri",
    "u_muezzin": "записи азана|las grabaciones del adhan|die Adhan-Aufnahmen|le registrazioni dell'adhan|les enregistrements de l'adhan|اذان کی ریکارڈنگز|अज़ान की रिकॉर्डिंग|아잔 녹음|rekaman azan|アザーンの録音|宣礼录音|ezan kayıtları|আজানের রেকর্ডিং|ضبط‌های اذان|rakaman azan|rekodi za adhana|rakodin kiran sallah|as gravações do adhan|د اذان ثبتونه|azon yozuvlari",
    "u_radio": "поток, публикуемый самой станцией|la emisión que publica cada emisora|der von jedem Sender selbst veröffentlichte Stream|il flusso pubblicato da ogni stazione|le flux publié par chaque station|ہر اسٹیشن کی اپنی شائع کردہ نشریات|हर स्टेशन का अपना प्रकाशित प्रसारण|방송국이 직접 공개한 스트림|siaran yang diterbitkan setiap stasiun sendiri|各局が自ら公開する配信|各电台自行公开的音频流|her istasyonun kendi yayımladığı yayın|প্রতিটি স্টেশনের নিজস্ব প্রকাশিত সম্প্রচার|پخشی که هر ایستگاه خود منتشر می‌کند|siaran yang diterbitkan sendiri oleh setiap stesen|mtiririko unaochapishwa na kila kituo chenyewe|watsa shirin da kowace tasha ke wallafawa da kanta|a emissão publicada por cada estação|هغه خپرونه چې هر سټیشن پخپله خپروي|har bir stansiya oʻzi eʼlon qilgan efir",
    "u_osm": "карта ближайших мечетей|el mapa de mezquitas cercanas|die Karte der Moscheen in der Nähe|la mappa delle moschee vicine|la carte des mosquées à proximité|قریبی مساجد کا نقشہ|पास की मस्जिदों का नक़्शा|가까운 모스크 지도|peta masjid terdekat|近くのモスクの地図|附近清真寺地图|yakındaki camilerin haritası|কাছের মসজিদের মানচিত্র|نقشه مساجد نزدیک|peta masjid berdekatan|ramani ya misikiti iliyo karibu|taswirar masallatai na kusa|o mapa das mesquitas próximas|د نږدې جوماتونو نقشه|yaqin masjidlar xaritasi",
}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ids = [k[0] for k in KEYS]
    if len(ids) != len(set(ids)):
        raise SystemExit("FAILED: a key is written twice")
    src = {}
    for folder in sorted({f for f, _ in REUSE.values()}):
        src[folder] = {c: json.load(io.open(os.path.join(I.I18N, folder, c + ".json"), encoding="utf-8")) for c in I.LANG_CODES}
    out = {c: {"_status": STATUS} for c in I.LANG_CODES}
    for kid, en, ar in KEYS:
        if kid in REUSE:
            folder, sid = REUSE[kid]
            for c in I.LANG_CODES:
                out[c][kid] = src[folder][c][sid]
            continue
        if kid not in T:
            raise SystemExit("FAILED: no translation for %s" % kid)
        vals = T[kid].split("|")
        if len(vals) != len(I.LANG_CODES):
            raise SystemExit("FAILED: %s has %d languages, not %d" % (kid, len(vals), len(I.LANG_CODES)))
        for c, v in zip(I.LANG_CODES, vals):
            out[c][kid] = v.strip()
    extra = [k for k in T if k not in ids]
    if extra:
        raise SystemExit("FAILED: translations without a key: %s" % extra)
    os.makedirs(OUT, exist_ok=True)
    json.dump([{"id": k, "en": e, "ar": a} for k, e, a in KEYS], io.open(os.path.join(OUT, "keys.json"), "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    for c in I.LANG_CODES:
        json.dump(out[c], io.open(os.path.join(OUT, c + ".json"), "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print("i18n/design3: %d keys written (%d reused) in %d languages" % (len(KEYS), len(REUSE), len(I.LANG_CODES)))
    I.build_i18n("design3")


if __name__ == "__main__":
    main()
