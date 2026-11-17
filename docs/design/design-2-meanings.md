# Design 2 — "early Islam": why every colour, icon and mark was chosen

The author asked on 2026-11-17 for an explanation of every element of design 2: the colours, the colour
directions, the logo and the icons. He asked that the choices come from reflection on the Quran, the hadith and the
first era of Islam, and that the explanation can later become a section inside the application. This document is that
explanation. The section in the application is feature **F19** (parent `AGENTS.md` §2, §8.10).

Prototype: [`prototypes/round-3.html`](prototypes/round-3.html). Colour values: [`tokens-design-2.json`](tokens-design-2.json),
generated from `prototypes/tools/design2_palettes.py`.

## 1. The rules this explanation follows

These follow from §6 of the parent `AGENTS.md`, because a Quran application must not attach a meaning to a verse
that its scholars did not give it.

1. **A colour is "taken from a word", never "the meaning of a verse".** We write *"this green is named after the word
   for green in 76:21"*. We never write *"green is the colour of Paradise"* or *"green means hope in Islam"*. The first
   is a fact about the text; the others are interpretation, which is tafsir and is not ours to give.
2. **The Quran gives words, not shades.** Where a verse names a colour, the exact shade (its hex value) is a design
   choice, and the in-app section says so.
3. **Ayahs are copied, never typed.** Every ayah in this document and in the prototype is copied whole from the
   verified Tanzil file by `tools/build_round3.py`, which also checks that the ayah contains the word it is cited
   for (the table in section 8).
4. **Meanings of words come from a named tafsir, quoted verbatim.** Where a word needs explaining (for example
   «مدهامتان»), the in-app section shows the explanation of a published tafsir, word for word, with its name. This
   waits until a tafsir licence is settled (§7.2). This document only notes what the tafsirs say, and marks it ☐.
5. **Hadith are cited by book and number, with the grading stated by the source.** The text of a hadith is not
   quoted here. In the application it is shown only as published by its source, with its grading (§6.10).
6. **Only what is true of the era.** Domes, arches, minarets, the green dome of Madinah, the black and gold covering
   of the Kaaba and the golden dome in Jerusalem came later. Each is named in section 6 with its date, and none is
   used as if it belonged to the first era.
7. **Nothing from verses of punishment or of the Day of Judgement** is used for an interface colour, even where a
   colour word appears in them.

Status: everything below is a **design proposal written by the agent**, with no scholar's review. Before F19 is
published, a qualified reviewer reads it (§6.6), or it stays limited to rules 1–5.

## 2. Why colour is treated with care

The Quran points to the variety of colours as one of the signs of creation: fruits of different colours, streaks in
the mountains that are white, red and intensely black, and people and animals of different colours (35:27–28; see
also 16:13 and 39:21). So the design does not use colour as decoration only: each direction is built from colours
that are named in the Quran, or that were really seen in the places and objects of the first era.

## 3. The nine colour directions

Six directions were made on 2026-11-17; the author asked for more on 2026-11-18, and three were added (3.7 – 3.9).
Each direction has a day theme and a night theme. Every text / background pair passes 4.5 : 1, checked by script.
Only Mountains is made for readers with colour blindness or weak sight (section 3.10). The roles are the same in every direction: background, text, main button, the
small "dot" marks, a second colour (prayer, Qibla, adhkar, "verified"), and the prayer card.

### 3.1 الرَّقّ — Parchment (the first one, unchanged)

| Colour | Taken from |
| --- | --- |
| Parchment background `#EFE5CE` | The Quran names parchment itself: «فِى رَقٍّ مَّنشُورٍ» (52:3), after «وَكِتَـٰبٍ مَّسْطُورٍ» (52:2). The earliest Quran manuscripts that survive are written on parchment. ☐ The tafsir of «رق» is quoted in F19 from a licensed tafsir. |
| Brown-black ink `#2A2018` | The ink of those manuscripts is brown-black, not the pure black of print. |
| Red dots `#9E2F1D` | Early copies marked the vowels with red dots, a system attributed by tradition to Abu al-Aswad al-Du'ali (d. 69 AH). Used for the active item and the page number, **never on the Quran text**. |
| Palm green `#45602F`, mud brick `#7E4B2E` | Shared with Madinah (3.2). |

### 3.2 المدينة — Madinah: the Prophet's mosque

| Colour | Taken from |
| --- | --- |
| Sand `#EEE2C6` | The ground of Madinah and the floor of the first mosque. |
| Mud brick `#8A5A36` (prayer card) | The mosque was built of mud brick, its roof of palm fronds, its pillars of palm trunks — Sahih al-Bukhari 446 (Ibn Umar; dorar.net/h/wVDAbFDs). |
| Palm green `#2F4A2A` (buttons), `#3D6633` | The palm trees of Madinah; the Quran mentions the tall palms «وَٱلنَّخْلَ بَاسِقَـٰتٍ» (50:10). |
| Date red-brown `#8B3A22` (dots) | The colour of ripe dates. |

What it avoids: the **green dome**. It was first painted green in **1253 AH (1837)**, under the Ottomans; before that
it was known as white, and later blue (islamqa.info/ar/answers/110061 and other histories). It is not of the first
era, so it is not used.

### 3.3 مكة — Makkah: the House

| Colour | Taken from |
| --- | --- |
| Milk white `#F6F4EF` and stone black `#161514` | The Black Stone. A hadith in Sunan al-Tirmidhi 877 (Ibn Abbas) says it came down from Paradise whiter than milk and was blackened by the sins of the sons of Adam. ☐ Al-Tirmidhi graded it *hasan sahih*; some scholars criticised one narrator. The grading is copied verbatim from Dorar before it is shown in F19 (§6.10). |
| Granite grey-blue `#3E4E57` | The dark granite mountains around Makkah. |
| Red-brown `#7B4030` (dots) | The reddish rock of the same mountains. |
| The verse | «إِنَّ أَوَّلَ بَيْتٍ وُضِعَ لِلنَّاسِ لَلَّذِى بِبَكَّةَ» (3:96) — the reason for the direction, not a colour. |

What it avoids: the **black and gold covering (kiswa)** as we know it today. Its colour and embroidery changed over
the centuries, and the black with gold calligraphy belongs to much later periods. ☐ The history is not needed for
the design, so it was not researched further.

### 3.4 القدس — Al-Quds: al-Masjid al-Aqsa

| Colour | Taken from |
| --- | --- |
| Limestone `#F0EADB` | The pale stone of Jerusalem. |
| Olive `#3B4722`, `#4F6230` | The olive tree. The Quran swears by the fig and the olive (95:1), and describes the lamp lit from the oil of a blessed olive tree (24:35). ☐ Some tafsirs connect 95:1 with the land of al-Aqsa; that is quoted in F19 from a licensed tafsir, or left out. |
| Oil amber `#7C5010` (dots) | Olive oil in lamplight — the oil «يَكَادُ زَيْتُهَا يُضِىٓءُ» in 24:35. |
| The verse | «مِّنَ ٱلْمَسْجِدِ ٱلْحَرَامِ إِلَى ٱلْمَسْجِدِ ٱلْأَقْصَا» (17:1). |

What it avoids: the **golden dome** of the Dome of the Rock. The building dates from 72 AH (its own inscription);
its mosaics inside are of plants and jewels, with no figures. The gold covering seen today is modern, and the blue
tiles outside are Ottoman. The Dome of the Rock is also not al-Masjid al-Aqsa itself, and images of it are often used
as if they were; this direction uses no image of either building.

### 3.5 الجنّات — Gardens: colours named in the Quran's descriptions of Paradise

| Colour | Taken from the word… |
| --- | --- |
| Deep green `#173A2A` (buttons) | «مُدْهَآمَّتَانِ» (55:64). ☐ Al-Tabari reports from Ibn Abbas that it means "two green ones", and al-Tafsir al-Muyassar describes a green so intense that it nears black; F19 quotes the tafsir verbatim. |
| Green `#2E6B45` | «خُضْرًا» (18:31), «خُضْرٍ» (55:76), «خُضْرٌ» (76:21) — the green garments and cushions. |
| Silk green `#1F4D36` (prayer card) | «سُندُسٍ» (18:31, 76:21) — fine silk, described with the green. |
| Gold `#7E5C10` (dots) | «مِن ذَهَبٍ» (18:31, 35:33). |
| Pearl white `#F2F0E8` (background) | «وَلُؤْلُؤًا» (35:33). |
| Silver grey `#A9ABA1` (thin rules) | «أَسَاوِرَ مِن فِضَّةٍ» (76:21). |

What it avoids: colours that the Quran uses to describe the women of Paradise (55:58). A word that describes people
is not used to colour buttons.

### 3.6 الجبال — Mountains: the high-contrast direction

The author asked for one direction with strong contrast, for bright sunlight and for readers with weak eyesight.
It takes its three colours from one verse: «وَمِنَ ٱلْجِبَالِ جُدَدٌۢ بِيضٌ وَحُمْرٌ مُّخْتَلِفٌ أَلْوَٰنُهَا وَغَرَابِيبُ سُودٌ»
(35:27) — streaks of **white** and **red**, and **intensely black**.

| Colour | Role | Contrast |
| --- | --- | --- |
| White `#FFFFFF` | background (day) | — |
| Intense black `#000000` | text, buttons (day); background (night) | 21 : 1 |
| Red `#8E0016` (day) / `#FF9C9C` (night) | the dot marks | at least 9.7 : 1 |

No grain texture and no soft colours in this direction: everything is drawn at full strength. It is **the only
direction made for readers with colour blindness, weak colour vision or weak sight** (the author's decision of
2026-11-18): as simulated for protanopia, deuteranopia and tritanopia, every pair stays at 8.4 : 1 or more
(section 3.10). Its name says so: «الجبال — لضعف البصر وعمى الألوان».

### 3.7 البحران — Two seas

| Colour | Taken from |
| --- | --- |
| Sea blue `#0F4A5A` (buttons), `#1D6470` | The two seas, «مَرَجَ ٱلْبَحْرَيْنِ يَلْتَقِيَانِ» (55:19). The Quran does not name the colour of the sea; the blue is our choice. |
| Pearl `#EEF2F0` (background) | «يَخْرُجُ مِنْهُمَا ٱللُّؤْلُؤُ وَٱلْمَرْجَانُ» (55:22) — the pearl. |
| Coral red `#9C3628` (dots) | The coral of the same ayah. |

Note: «ٱلْمَرْجَانُ» also appears in 55:58, which describes people; this direction cites 55:22 only, where pearl and
coral are what comes out of the seas.

### 3.8 المصابيح — Lamps: the night sky

| Colour | Taken from |
| --- | --- |
| Night blue `#0B0F22` (night background), indigo `#1F2A55` (day buttons) | The lowest heaven adorned with lamps: «وَزَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِمَصَـٰبِيحَ» (41:12). The night blue is our choice. |
| Lamplight gold `#F2C766` (night dots), `#765708` (day) | «وَجَعَلَ فِيهَا سِرَٰجًا وَقَمَرًا مُّنِيرًا» (25:61) — a lamp and a shining moon. |

Made to be at its best in the night theme, for reading at night. 67:5 also speaks of the lamps of the sky, but it
ends with a mention of punishment, so it is not cited (rule 7).

### 3.9 النحل — Honey

| Colour | Taken from |
| --- | --- |
| Amber `#854808` (dots), honey `#8A5208` (prayer card), dark comb `#5A3A0C` (buttons) | Honey: «شَرَابٌ مُّخْتَلِفٌ أَلْوَٰنُهُۥ» (16:69) — a drink of varying colours, from the bees. |
| Beeswax cream `#F4EBD6` (background) | The bees and their homes. |
| Leaf green `#556218` | The trees in which the bees make their homes, «وَمِنَ ٱلشَّجَرِ» (16:68). |

### 3.10 Colour vision — for readers who cannot tell colours apart

The author asked on 2026-11-18 that one direction serve people who cannot distinguish colours, and then decided
that **only Mountains** is made for them — not every direction, and not the night themes of the other directions.
What was done:

1. **Mountains is the direction for colour blindness, weak colour vision and weak sight:** black and white at full
   strength, at least 7 : 1 everywhere.
2. **Mountains is checked as a colour-blind reader sees it.** The build simulates protanopia, deuteranopia and
   tritanopia with the published model of Machado, Oliveira & Fernandes (IEEE TVCG 2009, severity 1.0, matrices
   read on the authors' page) and stops if any text pair of Mountains falls below 7 : 1; today it stays at 8.4 : 1
   or more. The other eight directions are checked for normal colour vision only (4.5 : 1).
3. **In Mountains, colour is never the only signal:** the active tab has a dot *and* bold text; a selected choice
   has a thicker border; the current prayer has a filled dot *and* bold text; a source's status is written in words.
4. The prototype has a **"Colour vision" switch** that shows the screens through the same simulation, to check
   Mountains.

### 3.11 The language choice — 30:22

Asked by the author on 2026-11-18: read the tafsirs of 30:22 and decide. The ayah:
«وَمِنْ ءَايَـٰتِهِۦ خَلْقُ ٱلسَّمَـٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَـٰفُ أَلْسِنَتِكُمْ وَأَلْوَٰنِكُمْ» (30:22).

What the tafsirs say (read 2026-11-18; ☐ quoted word for word in F19 only from a licensed tafsir): al-Tafsir
al-Muyassar, al-Sa'di, al-Baghawi, al-Jalalayn and al-Muntakhab agree that «أَلْسِنَتِكُمْ» are people's languages
(Arabic, non-Arabic and others) and «أَلْوَٰنِكُمْ» are people's colours (white, black and others), though all
come from one origin — a sign for those who have knowledge.

Decision: the ayah is shown **beside the language choice only** — on the "Why more than one language?" card of
F19. It is **not** used for the colour directions, because its colours are the colours of people, not of things.


## 4. The logo

| Part | Taken from |
| --- | --- |
| Two thin rings | The rings around the inscriptions of early Islamic coins. |
| A ring of red dots | The dotted borders of the same coins, drawn with the red of the vowel dots. |
| Three dots in a triangle, in the centre | The way the earliest manuscripts mark the end of a verse: a small group of dots or strokes. |
| «تجويد» in Kufic letters | Kufic is the script of the early Quran manuscripts. The font is modern (Noto Kufi Arabic). |

The logo contains no word of the Quran and no name of Allah, so that it can be printed, resized and shown anywhere
without concern.

## 5. The icons

Generic icons (search, back, bookmark) are kept generic, so that they are understood at once. The icons of the
sections each come from something of the first era:

| Icon | Section | Drawn as | Why |
| --- | --- | --- | --- |
| Home | Home | Two palm trunks under a roof of fronds | The Prophet's mosque as Sahih al-Bukhari 446 describes it: palm-trunk pillars, a palm-frond roof. |
| Quran | Quran | A closed book with a strap | The Quran was gathered between two covers as a codex (mushaf) in the first era. |
| Ear | Recitation, Listen | An ear with sound | «وَإِذَا قُرِئَ ٱلْقُرْءَانُ فَٱسْتَمِعُوا۟ لَهُۥ وَأَنصِتُوا۟» (7:204). |
| Bars of 2, 4 and 6 | Tajweed | Sound bars of three lengths | The lengths of madd in tajweed are counted in 2, 4 and 6 counts; and «وَرَتِّلِ ٱلْقُرْءَانَ تَرْتِيلًا» (73:4). |
| Stick and shadow | Prayer times | An upright stick, its shadow, the sun | The times were taught by the length of shadows: in the hadith of Jibril leading the Prophet ﷺ in prayer at the House, Asr begins when the shadow of a thing equals the thing (Abu Dawud 393, al-Tirmidhi 149; ☐ grading from Dorar). |
| Cube | Qibla | The Kaaba as a plain cube | «فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ» (2:144). Drawn with no covering, as a shape only. |
| Hand | Adhkar | A hand with the joints of the fingers marked | The Prophet ﷺ counted tasbih on his fingers — Sunan Abi Dawud 1502 (graded *sahih* by al-Albani; the words "with his right hand" are disputed, so the icon shows a hand, not a side). |
| Sheet | Hadith | A sheet with lines and a rolled edge | Hadith were written on sheets (صحف) in the first generations. |
| Open book with notes | Tafsir | Two pages with lines at the sides | Explanation written beside the text. |
| Reed pen | Books | A cut reed pen (qalam) | «ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ» (96:4). |
| Chain | Sources | Two linked rings | The isnad — every narration carried by a chain of named narrators. The Sources screen does the same for every file the application uses. |
| Radio | Radio | A radio | Nothing in the first era corresponds; kept generic on purpose. |

## 6. Ideas considered and not used

| Idea | Why not |
| --- | --- |
| 30:22 for the colour directions | Its colours are people's colours (the tafsirs, 3.11); it is used for the language choice only. |
| 67:5 for the Lamps direction | It ends with a mention of punishment (rule 7); 41:12 and 25:61 are used instead. |
| The green dome | 1253 AH — not of the first era (3.2). |
| Domes, pointed arches, minarets, star patterns | They developed after the first era; the first mosque had none of them. |
| The black and gold kiswa | Its present look is from much later periods (3.3). |
| The golden Dome of the Rock | The building is from 72 AH, but the gold covering is modern (3.4). |
| 55:58 (ruby and coral) | It describes people (3.5). |
| Any colour from verses of punishment or of the Day of Judgement | Rule 7. |
| A coloured name of Allah in the text | Withdrawn on 2026-11-17 (§8.1); the Quran text has one colour in every direction. |

## 7. The in-app section (feature F19) — how it will work

A section «لماذا هذا التصميم؟ — Why this design?», reached from the About page and from the colour choice:

- one card per direction, the logo and each icon: its colours or drawing, a **design note** (ours, labelled
  "design note"), the **ayah** copied from the Quran text the application ships (never typed), and the **hadith
  reference** (book, number, grading as published by its source);
- where a word needs explaining: the **verbatim** explanation of a named, licensed tafsir;
- a line on every card: "هذا اختيار تصميم، وليس تفسيرًا" / "This is a design choice, not an interpretation";
- in Arabic and English; the English of an ayah is shown only from a published translation (§6.10).

A draft of one card is phone 6 in the prototype.

## 8. The ayahs cited (generated — do not edit by hand)

<!--AYAHS-BEGIN-->
| Reference | Ayah — copied whole from the Tanzil file by `tools/build_round3.py` |
| --- | --- |
| Al-Baqara 2:144 (البقرة) | قَدْ نَرَىٰ تَقَلُّبَ وَجْهِكَ فِى ٱلسَّمَآءِ ۖ فَلَنُوَلِّيَنَّكَ قِبْلَةً تَرْضَىٰهَا ۚ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ ۗ وَإِنَّ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَـٰبَ لَيَعْلَمُونَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّهِمْ ۗ وَمَا ٱللَّهُ بِغَـٰفِلٍ عَمَّا يَعْمَلُونَ |
| Aal-i-Imraan 3:96 (آل عمران) | إِنَّ أَوَّلَ بَيْتٍ وُضِعَ لِلنَّاسِ لَلَّذِى بِبَكَّةَ مُبَارَكًا وَهُدًى لِّلْعَـٰلَمِينَ |
| Al-A'raaf 7:204 (الأعراف) | وَإِذَا قُرِئَ ٱلْقُرْءَانُ فَٱسْتَمِعُوا۟ لَهُۥ وَأَنصِتُوا۟ لَعَلَّكُمْ تُرْحَمُونَ |
| An-Nahl 16:68 (النحل) | وَأَوْحَىٰ رَبُّكَ إِلَى ٱلنَّحْلِ أَنِ ٱتَّخِذِى مِنَ ٱلْجِبَالِ بُيُوتًا وَمِنَ ٱلشَّجَرِ وَمِمَّا يَعْرِشُونَ |
| An-Nahl 16:69 (النحل) | ثُمَّ كُلِى مِن كُلِّ ٱلثَّمَرَٰتِ فَٱسْلُكِى سُبُلَ رَبِّكِ ذُلُلًا ۚ يَخْرُجُ مِنۢ بُطُونِهَا شَرَابٌ مُّخْتَلِفٌ أَلْوَٰنُهُۥ فِيهِ شِفَآءٌ لِّلنَّاسِ ۗ إِنَّ فِى ذَٰلِكَ لَـَٔايَةً لِّقَوْمٍ يَتَفَكَّرُونَ |
| Al-Israa 17:1 (الإسراء) | سُبْحَـٰنَ ٱلَّذِىٓ أَسْرَىٰ بِعَبْدِهِۦ لَيْلًا مِّنَ ٱلْمَسْجِدِ ٱلْحَرَامِ إِلَى ٱلْمَسْجِدِ ٱلْأَقْصَا ٱلَّذِى بَـٰرَكْنَا حَوْلَهُۥ لِنُرِيَهُۥ مِنْ ءَايَـٰتِنَآ ۚ إِنَّهُۥ هُوَ ٱلسَّمِيعُ ٱلْبَصِيرُ |
| Al-Kahf 18:31 (الكهف) | أُو۟لَـٰٓئِكَ لَهُمْ جَنَّـٰتُ عَدْنٍ تَجْرِى مِن تَحْتِهِمُ ٱلْأَنْهَـٰرُ يُحَلَّوْنَ فِيهَا مِنْ أَسَاوِرَ مِن ذَهَبٍ وَيَلْبَسُونَ ثِيَابًا خُضْرًا مِّن سُندُسٍ وَإِسْتَبْرَقٍ مُّتَّكِـِٔينَ فِيهَا عَلَى ٱلْأَرَآئِكِ ۚ نِعْمَ ٱلثَّوَابُ وَحَسُنَتْ مُرْتَفَقًا |
| An-Noor 24:35 (النور) | ٱللَّهُ نُورُ ٱلسَّمَـٰوَٰتِ وَٱلْأَرْضِ ۚ مَثَلُ نُورِهِۦ كَمِشْكَوٰةٍ فِيهَا مِصْبَاحٌ ۖ ٱلْمِصْبَاحُ فِى زُجَاجَةٍ ۖ ٱلزُّجَاجَةُ كَأَنَّهَا كَوْكَبٌ دُرِّىٌّ يُوقَدُ مِن شَجَرَةٍ مُّبَـٰرَكَةٍ زَيْتُونَةٍ لَّا شَرْقِيَّةٍ وَلَا غَرْبِيَّةٍ يَكَادُ زَيْتُهَا يُضِىٓءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌ ۚ نُّورٌ عَلَىٰ نُورٍ ۗ يَهْدِى ٱللَّهُ لِنُورِهِۦ مَن يَشَآءُ ۚ وَيَضْرِبُ ٱللَّهُ ٱلْأَمْثَـٰلَ لِلنَّاسِ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌ |
| Al-Furqaan 25:61 (الفرقان) | تَبَارَكَ ٱلَّذِى جَعَلَ فِى ٱلسَّمَآءِ بُرُوجًا وَجَعَلَ فِيهَا سِرَٰجًا وَقَمَرًا مُّنِيرًا |
| Ar-Room 30:22 (الروم) | وَمِنْ ءَايَـٰتِهِۦ خَلْقُ ٱلسَّمَـٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَـٰفُ أَلْسِنَتِكُمْ وَأَلْوَٰنِكُمْ ۚ إِنَّ فِى ذَٰلِكَ لَـَٔايَـٰتٍ لِّلْعَـٰلِمِينَ |
| Faatir 35:27 (فاطر) | أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءً فَأَخْرَجْنَا بِهِۦ ثَمَرَٰتٍ مُّخْتَلِفًا أَلْوَٰنُهَا ۚ وَمِنَ ٱلْجِبَالِ جُدَدٌۢ بِيضٌ وَحُمْرٌ مُّخْتَلِفٌ أَلْوَٰنُهَا وَغَرَابِيبُ سُودٌ |
| Faatir 35:28 (فاطر) | وَمِنَ ٱلنَّاسِ وَٱلدَّوَآبِّ وَٱلْأَنْعَـٰمِ مُخْتَلِفٌ أَلْوَٰنُهُۥ كَذَٰلِكَ ۗ إِنَّمَا يَخْشَى ٱللَّهَ مِنْ عِبَادِهِ ٱلْعُلَمَـٰٓؤُا۟ ۗ إِنَّ ٱللَّهَ عَزِيزٌ غَفُورٌ |
| Faatir 35:33 (فاطر) | جَنَّـٰتُ عَدْنٍ يَدْخُلُونَهَا يُحَلَّوْنَ فِيهَا مِنْ أَسَاوِرَ مِن ذَهَبٍ وَلُؤْلُؤًا ۖ وَلِبَاسُهُمْ فِيهَا حَرِيرٌ |
| Fussilat 41:12 (فصلت) | فَقَضَىٰهُنَّ سَبْعَ سَمَـٰوَاتٍ فِى يَوْمَيْنِ وَأَوْحَىٰ فِى كُلِّ سَمَآءٍ أَمْرَهَا ۚ وَزَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِمَصَـٰبِيحَ وَحِفْظًا ۚ ذَٰلِكَ تَقْدِيرُ ٱلْعَزِيزِ ٱلْعَلِيمِ |
| Qaaf 50:10 (ق) | وَٱلنَّخْلَ بَاسِقَـٰتٍ لَّهَا طَلْعٌ نَّضِيدٌ |
| At-Tur 52:2 (الطور) | وَكِتَـٰبٍ مَّسْطُورٍ |
| At-Tur 52:3 (الطور) | فِى رَقٍّ مَّنشُورٍ |
| Ar-Rahmaan 55:19 (الرحمن) | مَرَجَ ٱلْبَحْرَيْنِ يَلْتَقِيَانِ |
| Ar-Rahmaan 55:22 (الرحمن) | يَخْرُجُ مِنْهُمَا ٱللُّؤْلُؤُ وَٱلْمَرْجَانُ |
| Ar-Rahmaan 55:64 (الرحمن) | مُدْهَآمَّتَانِ |
| Ar-Rahmaan 55:76 (الرحمن) | مُتَّكِـِٔينَ عَلَىٰ رَفْرَفٍ خُضْرٍ وَعَبْقَرِىٍّ حِسَانٍ |
| Al-Muzzammil 73:4 (المزمل) | أَوْ زِدْ عَلَيْهِ وَرَتِّلِ ٱلْقُرْءَانَ تَرْتِيلًا |
| Al-Insaan 76:21 (الانسان) | عَـٰلِيَهُمْ ثِيَابُ سُندُسٍ خُضْرٌ وَإِسْتَبْرَقٌ ۖ وَحُلُّوٓا۟ أَسَاوِرَ مِن فِضَّةٍ وَسَقَىٰهُمْ رَبُّهُمْ شَرَابًا طَهُورًا |
| At-Tin 95:1 (التين) | وَٱلتِّينِ وَٱلزَّيْتُونِ |
| Al-Alaq 96:4 (العلق) | ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ |
<!--AYAHS-END-->

## 9. Sources checked on 2026-11-17

- Sahih al-Bukhari 446, the building of the Prophet's mosque — https://dorar.net/h/wVDAbFDs
- The hadith of Jibril and the prayer times (Abu Dawud 393, al-Tirmidhi 149) — https://dorar.net/h/yVPS80BX
- Counting tasbih on the fingers (Abu Dawud 1502) — https://surahquran.com/Hadith-58649.html · https://khaledalsabt.com/explanations/590
- The Black Stone (al-Tirmidhi 877) — https://surahquran.com/Hadith-41457.html · https://www.alukah.net/homayed/12438/135950/
- The green dome, 1253 AH — https://islamqa.info/ar/answers/110061 · https://areq.net/m/القبة_الخضراء.html
- The Dome of the Rock, 72 AH — https://smarthistory.org/?p=1256 · https://courses.lumenlearning.com/suny-arthistory1/chapter/dome-of-the-rock/
- «مدهامتان» in the tafsirs — https://quran.ksu.edu.sa/tafseer/tabary/sura55-aya64.html · https://qurano.com/ar/55-ar-rahman/aya-64/
- Early manuscripts and the red dots — https://en.wikipedia.org/wiki/Hijazi_script · https://al-islam.org/ar/node/39578
- The tafsirs of 30:22 (read 2026-11-18) — https://quran-tafsir.net/baghawy-saady-tantawy-qotb-katheer-atia-mobdii/sura30-aya22.html · https://surahquran.org/aya-tafsser-22-30.html
- Colour-vision simulation (Machado, Oliveira & Fernandes 2009) — https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html

The short Quranic excerpts in sections 3–6 only point at the verse. The build checks each vowelled excerpt in «»
against the Tanzil file and stops if it is not an exact part of a cited ayah. The whole ayahs, copied from the
verified file, are in section 8; F19 shows only whole ayahs.
