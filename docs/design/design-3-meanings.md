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

## 3. The twenty-eight directions (twelve on 2026-11-19, then six, five and five more on 2026-11-20)

The five added on the author's second message of 2026-11-20 (§3.19 – §3.23) come **from the Quran only** — he asked
that the sources be the Quran and the authentic Sunnah. The same day he asked for better pictures: ten landscapes were
**redrawn** with layers, light and more detail — the Cave, Uhud, look at the camels, dawn, the forenoon, al-Kawthar, the
sun and the moon, the scattering winds, the pasture and light. The earlier drawings are kept, in Figma («Earlier
landscapes») and in `elements/design-3/landscapes-earlier/`.

Each has a day and a night theme. The night themes follow the six night rules (deep tinted background, cards
lighter step by step, the mushaf page a little lighter, soft text 11 – 16 : 1, calm accents, no bright block).

### 3.0 Every direction checked against its ayah's tafsir (the author's request, 2026-11-20)

The author asked that each direction rest on its ayah **and its authentic tafsirs**, and that the descriptions of
Paradise in the Quran be used. Every ayah was read in **tafsir al-Sa'di** and **tafsir Ibn Kathir** (the texts of
quran.ksu.edu.sa, read on 2026-11-20); every hadith number below was checked on sunnah.com the same day. The
tafsirs are cited, not quoted here; in the application only the verbatim text of a licensed tafsir is shown (§1).

| Direction | What the tafsirs say | Drawing |
| --- | --- | --- |
| The first sheets, Hira, the Cave, Taybah, Uhud, the camels, dawn, the forenoon, rain, the fig and the olive, the sun and the moon, the winds, the crop, the pasture, the birds, light, mountains | the drawing agrees with al-Sa'di and Ibn Kathir (e.g. 87:5 «أحوى»: black, dry; 67:19: wings spread for flight, drawn in to land; 25:61 lamps; 51:1 the winds) | kept |
| Two Gardens (55:62 – 68) | the two gardens below are of silver, their vessels and what is in them (al-Bukhari 4878, cited by Ibn Kathir); «نضاختان» gushing (al-Sa'di) | **redrawn**: silver domes, two gushing springs |
| Al-Kawthar (108:1) | a river whose banks are domes of hollow pearl (al-Bukhari 4964); it runs without a dug channel, its pebbles pearls (Ibn Kathir); its water whiter than milk (al-Sa'di) | **redrawn**: a white river level with the land, pearl domes on its banks |
| The good tree (14:24) | it is the palm (al-Bukhari 4698 and 61; al-Sa'di; Ibn Kathir from Ibn Mas'ud and Anas) | **redrawn** as a palm |
| The shade (25:45) | the time between dawn and sunrise (Ibn Kathir from Ibn Abbas and others; al-Sa'di) | **redrawn**: soft shade over all, the sun just rising |
| Al-Asr (103:1) | time — the night and the day (al-Sa'di); the time in which people's deeds happen, the better-known view (Ibn Kathir) | **redrawn**: the day passing into night; the earlier note ("the afternoon") withdrawn |
| The ships (55:24) | so great they are like the mountains (al-Sa'di) | ships enlarged |

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
mountains and the earth (88:18–20). The landscape draws exactly these four: camels walking, the raised sky, the mountains set up, the
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
high sun in its glow) and its **night theme** is the still night (a small, calm light, no rays).

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

«مُدْهَآمَّتَانِ» (55:64), «نَضَّاخَتَانِ» (55:66) and «وَرُمَّانٌ» (55:68). **Redrawn twice on 2026-11-20** — the second time after the tafsirs (§3.0), with «وَمِن دُونِهِمَا جَنَّتَانِ» (55:62): these two gardens are
"of silver, their vessels and what is in them" (Sahih al-Bukhari 4878); "mudhammatan" — dark from the depth of their
green, "naddakhatan" — gushing (al-Sa'di). The landscape: two gardens of dense deep-green trees with silver domes, two
springs rising in arcs between them, palms and pomegranates.

| Colour | From |
| --- | --- |
| Deep green `#14402C` (buttons) | 55:64 |
| Pomegranate red `#9A2B39` (dots) | the pomegranates of 55:68 |
| Palm green `#2F6B44` | the palms of 55:68 |
| The springs, in the sky colour of the direction | 55:66 |

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

### 3.13 التين والزيتون — The fig and the olive (2026-11-20)

From «وَٱلتِّينِ» (95:1): the two trees the surah opens with. The landscape: an olive tree with narrow leaves on the left, a fig tree
with its purple fruit on the right, on low hills.

| Colour | From |
| --- | --- |
| Olive green `#3F4A1E` (buttons) | the olive |
| Fig purple `#6E2E55` (dots) | the fig |

### 3.14 الكوثر — Al-Kawthar (2026-11-20)

Named after the word «ٱلْكَوْثَرَ» (108:1). **Redrawn after the tafsirs (§3.0):** "I came upon a river whose banks were domes of hollow pearl … this is
al-Kawthar" (Sahih al-Bukhari 4964); it runs without a dug channel and its pebbles are pearls (the hadith of Anas cited
by Ibn Kathir); its water is whiter than milk (al-Sa'di). The landscape: a white river winding toward us, level with the
land, its pebbles pearls, domes of pearl along both banks.

| Colour | From |
| --- | --- |
| Deep water blue `#1D4E6B` (buttons) | water |
| Gold `#7A5A14` (dots) | light on the water |

### 3.15 الشمس والقمر — The sun and the moon (2026-11-20)

Two oaths, like the forenoon (§3.8): «وَٱلشَّمْسِ» (91:1) and «وَٱلْقَمَرِ» (91:2). The day theme shows the sun, the night theme the full moon (a round
disc — no cross, no star shape).

| Colour | From |
| --- | --- |
| Night indigo `#2E3157` (buttons) | the sky |
| Sun gold `#F6E2A6` (day landscape), moon silver `#D9DCEB` (night landscape) | 91:1, 91:2 |

### 3.16 الذاريات — The scattering winds (2026-11-20)

From «وَٱلذَّٰرِيَـٰتِ» (51:1). The landscape: sand dunes, the lines of the wind above them, and sand blown off a crest.

| Colour | From |
| --- | --- |
| Ochre `#6A4416` (buttons) | sand |
| Rust `#8A3F1E` (dots) | the dunes at sunset |

### 3.17 الزرع — The crop (2026-11-20)

From the word «كَزَرْعٍ» (48:29) in the last ayah of Surah al-Fath. The landscape: young stalks with their ears of grain and their
shoots. The ayah is long; it is shown whole in F19, and the design takes only the word.

| Colour | From |
| --- | --- |
| Shoot green `#2E5422` (buttons) | the shoots |
| Grain gold `#7A5A0E` (dots), `#EED9A0` (the ears) | the ears of grain |

### 3.18 المرعى — The pasture (2026-11-20)

Two words of colour: «ٱلْمَرْعَىٰ» (87:4) and «أَحْوَىٰ» (87:5). The day theme is the green pasture, the night theme the dark colour.

| Colour | From |
| --- | --- |
| Pasture green `#3B4F2E` (buttons) | 87:4 |
| The dark night theme (background `#171A12`) | 87:5 |

### 3.19 الشجرة الطيبة — The good tree (second message of 2026-11-20)

From «كَشَجَرَةٍ طَيِّبَةٍ أَصْلُهَا ثَابِتٌ وَفَرْعُهَا فِى ٱلسَّمَآءِ» (14:24) and «تُؤْتِىٓ أُكُلَهَا» (14:25). The landscape: one tree, its roots spread deep in the earth below the ground line,
its trunk rising and its branches reaching the top of the sky, with fruit on them. **Corrected after the tafsirs
(§3.0):** the good tree is the palm — the Prophet ﷺ said “it is the palm” (Sahih al-Bukhari 4698, in the tafsir of 14:24;
also 61), as al-Sa'di and Ibn Kathir say; it is now drawn as a palm with its roots spread deep and its dates.

| Colour | From |
| --- | --- |
| Leaf green `#2D4A1E` (buttons), `#365524` (card) | the tree |
| Root brown `#7A4E1E` (dots) | the root, firm in the earth |

### 3.20 الطير — The birds (second message of 2026-11-20)

From «ٱلطَّيْرِ فَوْقَهُمْ صَـٰٓفَّـٰتٍ وَيَقْبِضْنَ» (67:19). The landscape: birds over open land, most with their wings spread, some with their wings
drawn in — the two words of the ayah.

| Colour | From |
| --- | --- |
| Sky blue `#1D5E6B` (buttons), `#246E7C` (card) | the sky above them |
| `#7A4614` (dots) | the land below |

### 3.21 الظل — The shade (second message of 2026-11-20)

From «كَيْفَ مَدَّ ٱلظِّلَّ» and «جَعَلْنَا ٱلشَّمْسَ عَلَيْهِ دَلِيلًا» (25:45). The landscape: a low sun at the horizon and the long shadows of two palms and a rock
stretched over the plain. **Corrected after the tafsirs (§3.0):** the extended shade is the time between dawn and sunrise
(Ibn Kathir, from Ibn Abbas and others; al-Sa'di) — the landscape now shows the whole land in soft shade and the sun only
beginning to rise, its guide.

| Colour | From |
| --- | --- |
| Shade brown `#5C5310` (buttons), `#7E6D0E` (card) | the shade |
| Low-sun gold `#716005` (dots) | the sun |

### 3.22 الجوار المنشآت — The ships (second message of 2026-11-20)

From «ٱلْجَوَارِ ٱلْمُنشَـَٔاتُ فِى ٱلْبَحْرِ كَٱلْأَعْلَـٰمِ» (55:24). The landscape: ships with tall sails on the sea, and mountains on the horizon beside them. The sails are
lateen sails on a slanting yard, so no mast and yard ever make a cross (rule 8).

| Colour | From |
| --- | --- |
| Sea blue `#1D376B` (buttons), `#24427C` (card) | the sea |
| `#646310` (dots) | the sails in the light |

### 3.23 العصر — Al-Asr (second message of 2026-11-20)

Named after the word «وَٱلْعَصْرِ» (103:1). **Corrected after the tafsirs (§3.0):** al-Sa'di explains al-Asr as time —
the night and the day; Ibn Kathir gives as the better-known view the time in which the deeds of people happen, and
mentions the afternoon as a second view. The first note (the time of the Asr prayer) is withdrawn. The landscape: the
sky passing from day on one side to night on the other, over warm hills and palms.

| Colour | From |
| --- | --- |
| Warm brown `#5C3510` (buttons), `#7E410E` (card) | the light of that hour |
| `#8A4106` (dots) | the sun |

### 3.24 ظل ممدود — The extended shade (Paradise, 2026-11-20)

«سِدْرٍ مَّخْضُودٍ», «وَطَلْحٍ مَّنضُودٍ» and «وَظِلٍّ مَّمْدُودٍ» (56:28–30). Al-Sa'di: lote trees whose thorns are taken away, talh whose branches are set with fruit; on
56:30 Ibn Kathir cites "In Paradise is a tree in whose shade a rider travels a hundred years without crossing it; recite
if you wish: ‘and an extended shade’" (Sahih al-Bukhari 4881; also 3251). The landscape: one vast canopy whose shade covers the
whole land, thornless lote trees, talh with rows of fruit, poured water (56:31). No rider is drawn.

| Colour | From |
| --- | --- |
| Shade green `#144035` (buttons), `#1E5240` (card) | the extended shade |
| `#9A332B` (dots) | the fruit |

### 3.25 الأنهار — The rivers (Paradise, 2026-11-20)

«فِيهَآ» (47:15): rivers of water that does not change, of milk whose taste does not change, of a drink delightful to those who
drink, and of pure honey. Al-Sa'di (on 13:35): the rivers run without a channel; Ibn Kathir (on 47:15) cites "from it
[al-Firdaws] the rivers of Paradise burst forth". The landscape: four streams side by side flowing down from a height,
level with the land. The colour of the river of drink is a design choice — the sources read do not describe it.

| Colour | From |
| --- | --- |
| `#1D626B` (buttons), `#24727C` (card) | water |
| `#7A4014` (dots) | honey |

### 3.26 الغرف — Lofty dwellings (Paradise, 2026-11-20)

«غُرَفٌ مِّن فَوْقِهَا غُرَفٌ مَّبْنِيَّةٌ تَجْرِى» (39:20). Al-Sa'di: high, adorned dwellings, so clear that their outside is seen from their inside, seen from afar
like a bright star on the horizon, built one above another, of gold and silver; Ibn Kathir: high palaces, storey above
storey. The landscape: four storeys of gold and silver, see-through, a star-like light above them, a river beneath.
Windows are arches only, so no window makes a cross.

| Colour | From |
| --- | --- |
| `#4A3A12` (buttons), `#5A4718` (card) | gold |
| `#86610E` (dots) | the light |

### 3.27 قطوفها دانية — Fruit hanging near (Paradise, 2026-11-20)

«قُطُوفُهَا دَانِيَةٌ» (69:23) and «قُطُوفُهَا تَذْلِيلًا» (76:14). Al-Sa'di: its fruit near and easy to reach, standing, sitting or reclining. The landscape:
fruit trees whose branches bow so their clusters hang near the ground, their shade close.

| Colour | From |
| --- | --- |
| `#254A1E` (buttons), `#2D5524` (card) | the trees |
| `#6E2E30` (dots) | the fruit |

### 3.28 الخيام — The tents (Paradise, 2026-11-20)

"In Paradise there is a tent of a single hollow pearl, sixty miles wide" (Sahih al-Bukhari 4879; Sahih Muslim 2838); the
word «ٱلْخِيَامِ» (55:72). The landscape: domed tents with the sheen of pearl, in a garden. Tents only — no person is drawn.

| Colour | From |
| --- | --- |
| Pearl lilac `#201D6B` (buttons), `#27247C` (card) | the pearl |
| `#4A6A10` (dots) | the garden |

**Never drawn in any direction** (the author, 2026-11-20): a person, a face, clothing on a body, a cup, or the unseen
(for example Sidrat al-Muntaha, 53:14).

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
| Ibrahim 14:24 (ابراهيم) | أَلَمْ تَرَ كَيْفَ ضَرَبَ ٱللَّهُ مَثَلًا كَلِمَةً طَيِّبَةً كَشَجَرَةٍ طَيِّبَةٍ أَصْلُهَا ثَابِتٌ وَفَرْعُهَا فِى ٱلسَّمَآءِ |
| Ibrahim 14:25 (ابراهيم) | تُؤْتِىٓ أُكُلَهَا كُلَّ حِينٍۭ بِإِذْنِ رَبِّهَا ۗ وَيَضْرِبُ ٱللَّهُ ٱلْأَمْثَالَ لِلنَّاسِ لَعَلَّهُمْ يَتَذَكَّرُونَ |
| Al-Hajj 22:63 (الحج) | أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءً فَتُصْبِحُ ٱلْأَرْضُ مُخْضَرَّةً ۗ إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌ |
| An-Noor 24:35 (النور) | ٱللَّهُ نُورُ ٱلسَّمَـٰوَٰتِ وَٱلْأَرْضِ ۚ مَثَلُ نُورِهِۦ كَمِشْكَوٰةٍ فِيهَا مِصْبَاحٌ ۖ ٱلْمِصْبَاحُ فِى زُجَاجَةٍ ۖ ٱلزُّجَاجَةُ كَأَنَّهَا كَوْكَبٌ دُرِّىٌّ يُوقَدُ مِن شَجَرَةٍ مُّبَـٰرَكَةٍ زَيْتُونَةٍ لَّا شَرْقِيَّةٍ وَلَا غَرْبِيَّةٍ يَكَادُ زَيْتُهَا يُضِىٓءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌ ۚ نُّورٌ عَلَىٰ نُورٍ ۗ يَهْدِى ٱللَّهُ لِنُورِهِۦ مَن يَشَآءُ ۚ وَيَضْرِبُ ٱللَّهُ ٱلْأَمْثَـٰلَ لِلنَّاسِ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌ |
| Al-Furqaan 25:45 (الفرقان) | أَلَمْ تَرَ إِلَىٰ رَبِّكَ كَيْفَ مَدَّ ٱلظِّلَّ وَلَوْ شَآءَ لَجَعَلَهُۥ سَاكِنًا ثُمَّ جَعَلْنَا ٱلشَّمْسَ عَلَيْهِ دَلِيلًا |
| Ar-Room 30:22 (الروم) | وَمِنْ ءَايَـٰتِهِۦ خَلْقُ ٱلسَّمَـٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَـٰفُ أَلْسِنَتِكُمْ وَأَلْوَٰنِكُمْ ۚ إِنَّ فِى ذَٰلِكَ لَـَٔايَـٰتٍ لِّلْعَـٰلِمِينَ |
| Faatir 35:27 (فاطر) | أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءً فَأَخْرَجْنَا بِهِۦ ثَمَرَٰتٍ مُّخْتَلِفًا أَلْوَٰنُهَا ۚ وَمِنَ ٱلْجِبَالِ جُدَدٌۢ بِيضٌ وَحُمْرٌ مُّخْتَلِفٌ أَلْوَٰنُهَا وَغَرَابِيبُ سُودٌ |
| Az-Zumar 39:20 (الزمر) | لَـٰكِنِ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ لَهُمْ غُرَفٌ مِّن فَوْقِهَا غُرَفٌ مَّبْنِيَّةٌ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَـٰرُ ۖ وَعْدَ ٱللَّهِ ۖ لَا يُخْلِفُ ٱللَّهُ ٱلْمِيعَادَ |
| Muhammad 47:15 (محمد) | مَّثَلُ ٱلْجَنَّةِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۖ فِيهَآ أَنْهَـٰرٌ مِّن مَّآءٍ غَيْرِ ءَاسِنٍ وَأَنْهَـٰرٌ مِّن لَّبَنٍ لَّمْ يَتَغَيَّرْ طَعْمُهُۥ وَأَنْهَـٰرٌ مِّنْ خَمْرٍ لَّذَّةٍ لِّلشَّـٰرِبِينَ وَأَنْهَـٰرٌ مِّنْ عَسَلٍ مُّصَفًّى ۖ وَلَهُمْ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَمَغْفِرَةٌ مِّن رَّبِّهِمْ ۖ كَمَنْ هُوَ خَـٰلِدٌ فِى ٱلنَّارِ وَسُقُوا۟ مَآءً حَمِيمًا فَقَطَّعَ أَمْعَآءَهُمْ |
| Al-Fath 48:29 (الفتح) | مُّحَمَّدٌ رَّسُولُ ٱللَّهِ ۚ وَٱلَّذِينَ مَعَهُۥٓ أَشِدَّآءُ عَلَى ٱلْكُفَّارِ رُحَمَآءُ بَيْنَهُمْ ۖ تَرَىٰهُمْ رُكَّعًا سُجَّدًا يَبْتَغُونَ فَضْلًا مِّنَ ٱللَّهِ وَرِضْوَٰنًا ۖ سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ ۚ ذَٰلِكَ مَثَلُهُمْ فِى ٱلتَّوْرَىٰةِ ۚ وَمَثَلُهُمْ فِى ٱلْإِنجِيلِ كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ فَـَٔازَرَهُۥ فَٱسْتَغْلَظَ فَٱسْتَوَىٰ عَلَىٰ سُوقِهِۦ يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ ۗ وَعَدَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّـٰلِحَـٰتِ مِنْهُم مَّغْفِرَةً وَأَجْرًا عَظِيمًۢا |
| Qaaf 50:10 (ق) | وَٱلنَّخْلَ بَاسِقَـٰتٍ لَّهَا طَلْعٌ نَّضِيدٌ |
| Adh-Dhaariyat 51:1 (الذاريات) | وَٱلذَّٰرِيَـٰتِ ذَرْوًا |
| Ar-Rahmaan 55:24 (الرحمن) | وَلَهُ ٱلْجَوَارِ ٱلْمُنشَـَٔاتُ فِى ٱلْبَحْرِ كَٱلْأَعْلَـٰمِ |
| Ar-Rahmaan 55:62 (الرحمن) | وَمِن دُونِهِمَا جَنَّتَانِ |
| Ar-Rahmaan 55:64 (الرحمن) | مُدْهَآمَّتَانِ |
| Ar-Rahmaan 55:66 (الرحمن) | فِيهِمَا عَيْنَانِ نَضَّاخَتَانِ |
| Ar-Rahmaan 55:68 (الرحمن) | فِيهِمَا فَـٰكِهَةٌ وَنَخْلٌ وَرُمَّانٌ |
| Ar-Rahmaan 55:72 (الرحمن) | حُورٌ مَّقْصُورَٰتٌ فِى ٱلْخِيَامِ |
| Al-Waaqia 56:28 (الواقعة) | فِى سِدْرٍ مَّخْضُودٍ |
| Al-Waaqia 56:29 (الواقعة) | وَطَلْحٍ مَّنضُودٍ |
| Al-Waaqia 56:30 (الواقعة) | وَظِلٍّ مَّمْدُودٍ |
| Al-Mulk 67:19 (الملك) | أَوَلَمْ يَرَوْا۟ إِلَى ٱلطَّيْرِ فَوْقَهُمْ صَـٰٓفَّـٰتٍ وَيَقْبِضْنَ ۚ مَا يُمْسِكُهُنَّ إِلَّا ٱلرَّحْمَـٰنُ ۚ إِنَّهُۥ بِكُلِّ شَىْءٍۭ بَصِيرٌ |
| Al-Haaqqa 69:23 (الحاقة) | قُطُوفُهَا دَانِيَةٌ |
| Al-Insaan 76:14 (الانسان) | وَدَانِيَةً عَلَيْهِمْ ظِلَـٰلُهَا وَذُلِّلَتْ قُطُوفُهَا تَذْلِيلًا |
| At-Takwir 81:18 (التكوير) | وَٱلصُّبْحِ إِذَا تَنَفَّسَ |
| Al-A'laa 87:4 (الأعلى) | وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ |
| Al-A'laa 87:5 (الأعلى) | فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ |
| Al-Ghaashiya 88:17 (الغاشية) | أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ |
| Al-Ghaashiya 88:18 (الغاشية) | وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ |
| Al-Ghaashiya 88:19 (الغاشية) | وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ |
| Al-Ghaashiya 88:20 (الغاشية) | وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ |
| Al-Fajr 89:1 (الفجر) | وَٱلْفَجْرِ |
| Ash-Shams 91:1 (الشمس) | وَٱلشَّمْسِ وَضُحَىٰهَا |
| Ash-Shams 91:2 (الشمس) | وَٱلْقَمَرِ إِذَا تَلَىٰهَا |
| Ad-Dhuhaa 93:1 (الضحى) | وَٱلضُّحَىٰ |
| Ad-Dhuhaa 93:2 (الضحى) | وَٱلَّيْلِ إِذَا سَجَىٰ |
| At-Tin 95:1 (التين) | وَٱلتِّينِ وَٱلزَّيْتُونِ |
| Al-Alaq 96:1 (العلق) | ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ |
| Al-Alaq 96:2 (العلق) | خَلَقَ ٱلْإِنسَـٰنَ مِنْ عَلَقٍ |
| Al-Alaq 96:3 (العلق) | ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ |
| Al-Alaq 96:4 (العلق) | ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ |
| Al-Asr 103:1 (العصر) | وَٱلْعَصْرِ |
| Al-Kawthar 108:1 (الكوثر) | إِنَّآ أَعْطَيْنَـٰكَ ٱلْكَوْثَرَ |
<!--AYAHS-END-->

## 8. Sources checked on 2026-11-19

- Sahih al-Bukhari 3, the beginning of revelation in the cave of Hira — https://dorar.net/h/3hiYYDhL · https://en.tohed.com/hadith/bukhari/3/
- Sahih al-Bukhari 4084, Mount Uhud — https://hadithprophet.com/hadith-37741.html · https://surahquran.com/Hadith-3818.html
- Sahih Muslim 1385, Madinah named Taba — https://surahquran.com/Hadith-17604.html · https://hadithprophet.com/hadith-49709.html
- Sahih al-Bukhari 4986, the gathering of the Quran under Abu Bakr — https://dorar.net/h/IZ3YoOwu · https://en.tohed.com/hadith/bukhari/4986
- The hadith of Jibril and the prayer times (Abu Dawud 393, al-Tirmidhi 149) — https://dorar.net/h/yVPS80BX

The short Quranic excerpts above only point at the verse; the build checks each vowelled excerpt in «» against the
Tanzil file and stops if it is not an exact part of a cited ayah.
