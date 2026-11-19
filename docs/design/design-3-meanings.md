# Design 3 — "the first era": why every colour, landscape and mark was chosen

The author asked on 2026-11-19 for a fourth round (design 3, now `round-3.html`): a new design for the same application, taken from the beginning of
Islam — the time of the Prophet ﷺ, the Companions and the Rightly Guided Caliphs, "the best eras of Islam" — much
better than design 2, with many colour directions drawn from reflection on the meanings and tafsirs of the Quran, each
with a day and a night theme; only the last direction is for low vision and colour blindness.

Prototype: [`prototypes/round-3.html`](prototypes/round-3.html). Colours: [`tokens-design-3.json`](tokens-design-3.json),
generated from `prototypes/tools/design3_palettes.py`. Design 2 and its reasons stay in
[`design-2-meanings.md`](design-2-meanings.md).

## 1. The rules (unchanged from design 2)

1. A colour or a scene is **taken from a word or a place** — never presented as "the meaning" of an ayah (that is
   tafsir, §6.10 of `AGENTS.md`).
2. The Quran gives words, not shades: every exact colour is our choice, and the in-app section says so.
3. Ayahs are **copied, never typed**: the build copies every cited ayah whole from the Tanzil file and checks it
   contains its word; every vowelled excerpt in «» in this document is checked word for word (section 7).
4. A hadith is cited by book and number; its text and grading are shown in the application only as published by
   its source (§6.10). No hadith text is quoted here.
5. Only what is true of the era: nothing in the design is a building or an ornament that came later (domes, arches,
   minarets, the green dome, star patterns). The landscapes are mountains, caves, palms, deserts, rain and sky — they
   were there.
6. Nothing from ayahs of punishment or of the Day of Judgement.
7. **Only the last direction, Mountains, is made for low vision and colour blindness** (the author, 2026-11-18 and
   2026-11-19). The other eleven are for ordinary sight: 4.5 : 1 for every text, and the six night rules.
8. **No cross shape anywhere** — no plus sign, no four-armed star or spark (the author, 2026-11-19: it is a symbol
   of Christianity, and this is an Islamic application). A star or a light is a round dot with a soft glow.

Status: a design proposal written by the agent, with no scholar's review (§6.6).

## 2. What is new in design 3

| | Design 2 (round 2) | Design 3 (round 3) |
| --- | --- | --- |
| Idea | the materials of the first manuscripts | the **places and moments** of the first era, and what the Quran asks us to look at |
| Each direction | a palette | a palette **and its own landscape**, drawn in that palette, on the home screen, on the web reader and in miniature on the first-launch cards |
| Prayer times | a dial | the **path of the sun** across the sky: sunrise and sunset on the horizon, dhuhr at the top, fajr and isha below — the prayer times are fixed by the sun and the shadows (the hadith of Jibril, Abu Dawud 393, al-Tirmidhi 149) |
| Headings | Kufic | **Amiri**, a classical naskh (OFL) — also for the surah header and the page header of the mushaf |
| Logo | coin rings | **an arc of light rising over the horizon** |
| Texture | parchment grain everywhere | grain only in the first direction, the sheets; the others are clean |

## 3. The twelve directions

Each has a day and a night theme. The night themes follow the six night rules (deep tinted background, cards
lighter step by step, the mushaf page a little lighter, soft text 11 – 16 : 1, calm accents, no bright block).

### 3.1 الصُّحُف — The first sheets (the default for reading)

The Quran was gathered in the time of Abu Bakr from palm stalks, thin white stones and the hearts of men — Sahih
al-Bukhari 4986 (Zayd ibn Thabit). The landscape: three palm stalks and two white stones with lines of writing.

| Colour | From |
| --- | --- |
| Limestone white `#F3F0E8` (day background) | the thin white stones (اللِّخاف) |
| Palm-stalk brown `#8C5A2B` (dots), `#6E5A3E` (card) | the palm stalks (العُسُب) |
| Dark ink `#3A3024` (buttons) | the writing |
| The ayah | «ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ» (96:4) |

### 3.2 حِراء — Hira

The revelation began in the cave of Hira — Sahih al-Bukhari 3. The first revealed ayahs: «ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ»
(96:1–3). The landscape: the dark peak with the cave near its top, and the first light behind it.

| Colour | From |
| --- | --- |
| Granite `#2B2722` (buttons), `#3A3530` (card) | the dark rock of the mountain |
| First light `#785A13` (day dots), `#DDBE78` (night dots) | the light of the morning |

### 3.3 الغار — The Cave

«ثَانِىَ ٱثْنَيْنِ إِذْ هُمَا فِى ٱلْغَارِ» (9:40) — the night of the Hijrah. The landscape: a cave in the rock above sand
dunes; at night, stars.

| Colour | From |
| --- | --- |
| Night blue `#24304A` (buttons), `#2C3A57` (card) | the night of the journey |
| Sand `#F1ECE2` (day background), rock `#7E5229` (dots) | the desert and the rock |

### 3.4 طابة — Taybah

Taybah (طابة) is a name of Madinah — Sahih Muslim 1385. «وَٱلنَّخْلَ بَاسِقَـٰتٍ» (50:10). The landscape: tall palms and
the first low mud houses.

| Colour | From |
| --- | --- |
| Palm green `#2F4D2B` (buttons), `#3F6A38` | the palms |
| Date brown `#874422` (dots) | the dates |
| Mud brick `#7A5232` (card) | the first houses |

### 3.5 أُحُد — Uhud

Mount Uhud, of which the Prophet ﷺ spoke in Sahih al-Bukhari 4084. The landscape: the long red ridge under the sky.
No ayah is cited for this direction.

| Colour | From |
| --- | --- |
| Red rock `#6B2E22` (buttons), `#8E3B26` (dots), `#7A3A2A` (card) | the red granite of Uhud |
| Sky `#4F6170` | the sky of Madinah |

### 3.6 أفلا ينظرون — Look at the camels

Four consecutive ayahs ask us to look: «أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ» (88:17), then at the sky, the
mountains and the earth (88:18–20). The landscape draws exactly these four: a camel, the sky, the mountains, the
flat earth.

| Colour | From |
| --- | --- |
| Camel tan `#80592E` (card), `#8B5A2B` (dots) | the camels |
| Sky blue `#2E4A63` (buttons) | the sky |
| Mountain grey `#5C6470` | the mountains |
| Earth ochre (landscape) | the earth |

### 3.7 الفجر — Dawn

«وَٱلْفَجْرِ» (89:1) and «وَٱلصُّبْحِ إِذَا تَنَفَّسَ» (81:18). The landscape: the light rising from the horizon, a bright line
where the night ends.

| Colour | From |
| --- | --- |
| Pre-dawn indigo `#3B3560` (buttons) | the last of the night |
| Dawn rose `#93445A` (dots) | the first light |

### 3.8 الضحى — The forenoon and the still night

«وَٱلضُّحَىٰ» (93:1) and «وَٱلَّيْلِ إِذَا سَجَىٰ» (93:2): two oaths, so this direction's **day theme** is the forenoon (a
high sun with rays) and its **night theme** is the still night (a small, calm light, no rays).

| Colour | From |
| --- | --- |
| Sunlight `#F7F2E4`, sun brown `#5C4410` (day) | the forenoon |
| Still night `#161922`, moonlight `#C7D2E8` (night) | the night when it is still |

### 3.9 الغيث — Rain

«فَتُصْبِحُ ٱلْأَرْضُ مُخْضَرَّةً» (22:63). The landscape: clouds, rain and green hills.

| Colour | From |
| --- | --- |
| Rain-cloud slate `#2F4B5B` (buttons), `#3E5C6C` (card) | the clouds |
| Fresh green `#2E6A3A` (dots) | the earth becoming green |

### 3.10 الجنّتان — The two gardens

«مُدْهَآمَّتَانِ» (55:64) and «فِيهِمَا فَـٰكِهَةٌ وَنَخْلٌ وَرُمَّانٌ» (55:68). The landscape: trees on two hills, a palm, and
pomegranates. ☐ The tafsir of «مدهامتان» (a green so deep it nears black, al-Tafsir al-Muyassar) is quoted in F19 only
from a licensed tafsir.

| Colour | From |
| --- | --- |
| Deep green `#14402C` (buttons) | 55:64 |
| Pomegranate red `#9A2B39` (dots) | the pomegranates of 55:68 |
| Palm green `#2F6B44` | the palms of 55:68 |

### 3.11 النور — Light

From 24:35: a niche, a lamp, its glass «ٱلزُّجَاجَةُ كَأَنَّهَا كَوْكَبٌ دُرِّىٌّ», and its oil. The landscape: a lamp
in its glass inside a niche, its glow, and a star drawn as a round dot with a soft glow (rule 8). It is drawn as a scene of words of the ayah, not as an explanation of
the parable — the parable is explained only by a tafsir (rule 1).

| Colour | From |
| --- | --- |
| Lamplight amber `#86610E` (day dots), `#DCC58E` (night) | the lamp and its oil |
| Glass blue `#4B6175` | the glass |

### 3.12 الجبال — Mountains (the only direction for low vision and colour blindness)

Unchanged from design 2: white, red and intense black streaks from one ayah, 35:27. At least 7 : 1 everywhere and as
simulated for protanopia, deuteranopia and tritanopia (8.4 : 1 or more). The landscape: two black mountains with a
white and a red streak — drawn at full strength, with no texture.

## 4. The logo

An arc of light rising over a horizon, inside a ring, with five short rays, and two lines of writing below the
horizon. It recalls the dawn (89:1, 81:18) and the first light of the revelation at Hira (Sahih al-Bukhari 3). It
contains no word of the Quran and no name of Allah. The wordmark «تجويد» is set in Amiri.

## 5. The prayer times on the path of the sun

The prayer screen draws the path of the sun as an arc: sunrise and sunset on the horizon, dhuhr at the top, fajr and
isha below the horizon, the coming prayer marked. The prayer times are fixed by the position of the sun and the
length of the shadows (the hadith of Jibril leading the Prophet ﷺ at the House, Abu Dawud 393, al-Tirmidhi 149; ☐ the
grading is copied from Dorar before it is shown). The positions on the arc are a drawing, not a calculation; the real
times are calculated on the device (`AGENTS.md` §8.5). The day runs in the reading direction: from right to left in
Arabic, Urdu, Persian and Pashto, from left to right in the other languages.

On the web reader the landscape of the chosen direction is a card at the top of the side list, at the same 3 : 1
shape as on the phone, so it is never stretched or cut on a wide screen.

## 6. Icons, languages, ideas left out

- The section icons are those of design 2, each from the first era (`design-2-meanings.md` §5).
- All 22 languages work: the interface texts of design 2 and the new texts of design 3 (the direction names and the
  design notes), translated by the agent and corrected from users' reports on GitHub (`LANG-02`).
- Left out: Badr and the other battles (not a theme for colours); the cave of Thawr by name (the Quran says «الغار»;
  the name comes from the books of Seerah — ☐ cited only with its source); the Kaaba and the two mosques as buildings
  (their present look is later); the parable of 24:35 explained in our words.

## 7. The ayahs cited (generated — do not edit by hand)

<!--AYAHS-BEGIN-->
| Reference | Ayah — copied whole from the Tanzil file by `tools/build_round3.py` |
| --- | --- |
| At-Tawba 9:40 (التوبة) | إِلَّا تَنصُرُوهُ فَقَدْ نَصَرَهُ ٱللَّهُ إِذْ أَخْرَجَهُ ٱلَّذِينَ كَفَرُوا۟ ثَانِىَ ٱثْنَيْنِ إِذْ هُمَا فِى ٱلْغَارِ إِذْ يَقُولُ لِصَـٰحِبِهِۦ لَا تَحْزَنْ إِنَّ ٱللَّهَ مَعَنَا ۖ فَأَنزَلَ ٱللَّهُ سَكِينَتَهُۥ عَلَيْهِ وَأَيَّدَهُۥ بِجُنُودٍ لَّمْ تَرَوْهَا وَجَعَلَ كَلِمَةَ ٱلَّذِينَ كَفَرُوا۟ ٱلسُّفْلَىٰ ۗ وَكَلِمَةُ ٱللَّهِ هِىَ ٱلْعُلْيَا ۗ وَٱللَّهُ عَزِيزٌ حَكِيمٌ |
| Al-Hajj 22:63 (الحج) | أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءً فَتُصْبِحُ ٱلْأَرْضُ مُخْضَرَّةً ۗ إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌ |
| An-Noor 24:35 (النور) | ٱللَّهُ نُورُ ٱلسَّمَـٰوَٰتِ وَٱلْأَرْضِ ۚ مَثَلُ نُورِهِۦ كَمِشْكَوٰةٍ فِيهَا مِصْبَاحٌ ۖ ٱلْمِصْبَاحُ فِى زُجَاجَةٍ ۖ ٱلزُّجَاجَةُ كَأَنَّهَا كَوْكَبٌ دُرِّىٌّ يُوقَدُ مِن شَجَرَةٍ مُّبَـٰرَكَةٍ زَيْتُونَةٍ لَّا شَرْقِيَّةٍ وَلَا غَرْبِيَّةٍ يَكَادُ زَيْتُهَا يُضِىٓءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌ ۚ نُّورٌ عَلَىٰ نُورٍ ۗ يَهْدِى ٱللَّهُ لِنُورِهِۦ مَن يَشَآءُ ۚ وَيَضْرِبُ ٱللَّهُ ٱلْأَمْثَـٰلَ لِلنَّاسِ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌ |
| Ar-Room 30:22 (الروم) | وَمِنْ ءَايَـٰتِهِۦ خَلْقُ ٱلسَّمَـٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَـٰفُ أَلْسِنَتِكُمْ وَأَلْوَٰنِكُمْ ۚ إِنَّ فِى ذَٰلِكَ لَـَٔايَـٰتٍ لِّلْعَـٰلِمِينَ |
| Faatir 35:27 (فاطر) | أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءً فَأَخْرَجْنَا بِهِۦ ثَمَرَٰتٍ مُّخْتَلِفًا أَلْوَٰنُهَا ۚ وَمِنَ ٱلْجِبَالِ جُدَدٌۢ بِيضٌ وَحُمْرٌ مُّخْتَلِفٌ أَلْوَٰنُهَا وَغَرَابِيبُ سُودٌ |
| Qaaf 50:10 (ق) | وَٱلنَّخْلَ بَاسِقَـٰتٍ لَّهَا طَلْعٌ نَّضِيدٌ |
| Ar-Rahmaan 55:64 (الرحمن) | مُدْهَآمَّتَانِ |
| Ar-Rahmaan 55:68 (الرحمن) | فِيهِمَا فَـٰكِهَةٌ وَنَخْلٌ وَرُمَّانٌ |
| At-Takwir 81:18 (التكوير) | وَٱلصُّبْحِ إِذَا تَنَفَّسَ |
| Al-Ghaashiya 88:17 (الغاشية) | أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ |
| Al-Ghaashiya 88:18 (الغاشية) | وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ |
| Al-Ghaashiya 88:19 (الغاشية) | وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ |
| Al-Ghaashiya 88:20 (الغاشية) | وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ |
| Al-Fajr 89:1 (الفجر) | وَٱلْفَجْرِ |
| Ad-Dhuhaa 93:1 (الضحى) | وَٱلضُّحَىٰ |
| Ad-Dhuhaa 93:2 (الضحى) | وَٱلَّيْلِ إِذَا سَجَىٰ |
| Al-Alaq 96:1 (العلق) | ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ |
| Al-Alaq 96:2 (العلق) | خَلَقَ ٱلْإِنسَـٰنَ مِنْ عَلَقٍ |
| Al-Alaq 96:3 (العلق) | ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ |
| Al-Alaq 96:4 (العلق) | ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ |
<!--AYAHS-END-->

## 8. Sources checked on 2026-11-19

- Sahih al-Bukhari 3, the beginning of revelation in the cave of Hira — https://dorar.net/h/3hiYYDhL · https://en.tohed.com/hadith/bukhari/3/
- Sahih al-Bukhari 4084, Mount Uhud — https://hadithprophet.com/hadith-37741.html · https://surahquran.com/Hadith-3818.html
- Sahih Muslim 1385, Madinah named Taba — https://surahquran.com/Hadith-17604.html · https://hadithprophet.com/hadith-49709.html
- Sahih al-Bukhari 4986, the gathering of the Quran under Abu Bakr — https://dorar.net/h/IZ3YoOwu · https://en.tohed.com/hadith/bukhari/4986
- The hadith of Jibril and the prayer times (Abu Dawud 393, al-Tirmidhi 149) — https://dorar.net/h/yVPS80BX

The short Quranic excerpts above only point at the verse; the build checks each vowelled excerpt in «» against the
Tanzil file and stops if it is not an exact part of a cited ayah.
