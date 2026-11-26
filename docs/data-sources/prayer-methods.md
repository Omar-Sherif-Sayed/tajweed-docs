# The default prayer-time method of each country (`P2-D1`) — first batch, 2026-11-22

The author (2026-11-17): every country gets the default method of its own official body, each with a named source; a
country without a verified source falls back to the Muslim World League's method **and the screen says so**
(`AGENTS.md` §8.5). The author (2026-11-22): «اعملهم».

## How a method is verified — from the official timetable itself

A method copied from a website about methods is not a source. What an official body publishes is its **timetable**,
so the method is read from that timetable: for every published day, the sun's position is computed at the published
minutes (the NOAA solar-position formulas — [`tools/infer_prayer_method.py`](tools/infer_prayer_method.py)), and the
result shows what the body uses:

- Fajr and Isha: the sun's depression below the horizon at the published minute. A method by angle gives the **same
  angle every day**; a method by interval gives the same **Isha − Maghrib** every day.
- Maghrib, sunrise and Dhuhr: how many minutes after the computed sunset, sunrise and solar noon — the body's own
  added minutes (ihtiyat / temkin).
- Asr: the shadow factor (1 = the majority's, 2 = the Hanafi school's).

Times are published to the minute, so one day is good to about ±0.25°; a year of days gives the method to a few
hundredths. The coordinates are the city's centre; a body that times a zone from another point shows a small constant
offset, reported as it is.

## Verified

| Country | Official body — source | Days read | What its timetable shows | Default in the apps (Adhan) |
| --- | --- | --- | --- | --- |
| **Saudi Arabia** | Umm al-Qura Calendar (KACST) — [ummulqura.org.sa/en/prayer-times](https://www.ummulqura.org.sa/en/prayer-times), Makkah, read 2026-11-23 | 1 | Fajr 18.40° (18.5° within the minute's rounding); **Isha = Maghrib + 90 min**; Maghrib +0.6 min; Asr factor 1 | `UmmAlQura` (Fajr 18.5°, Isha 90 min — 120 min in Ramadan by the method's definition, ☐ to be read in Ramadan's table) |
| **Egypt** | the Egyptian General Authority of Survey, as published by Dar al-Ifta — [dar-alifta.org/ar/prayer-times](https://www.dar-alifta.org/ar/prayer-times), Cairo, 2026-11-22; Dar al-Ifta's fatwas 3012 (2015) and 4021 (2017) make the Authority's timetable the reference and give Fajr at 19.5° | 1 | Fajr 19.54°; Isha 17.42°; Maghrib, sunrise, Dhuhr within 0.2 min of the computed; Asr factor 1.00 | `Egyptian` (Fajr 19.5°, Isha 17.5°) |
| **Türkiye** | Diyanet İşleri Başkanlığı — [namazvakitleri.diyanet.gov.tr](https://namazvakitleri.diyanet.gov.tr/tr-TR/9541/istanbul-icin-namaz-vakti), İstanbul, all of 2026 | 365 | Fajr (imsak) **17.99°** (sd 0.05); Isha (yatsı) **17.01°**; Maghrib +7.0 min, sunrise −7.0 min, Dhuhr +5.0 min, Asr factor 1.06 (≈ +4 min) | `Turkey` (18° / 17°, with sunrise −7, Dhuhr +5, Asr +4, Maghrib +7) |
| **Malaysia** | JAKIM — e-Solat, [e-solat.gov.my](https://www.e-solat.gov.my) (its yearly table, zone WLY01 Kuala Lumpur), all of 2026 | 365 | Fajr **17.55°**, Isha **18.47°**, Maghrib +1.9 min, Dhuhr +2.8 min, Asr factor 1 — i.e. **18° for both**, each published about two minutes after the 18° moment (ihtiyat) | 18° / 18° with JAKIM's minutes. ⚠ **Not** the library's `Singapore` preset (20°): Malaysia changed Subuh from 20° to 18° (National Muzakarah Committee, 116th meeting, 2019); the 20° preset gives Fajr about 8 minutes too early |
| **Singapore** | MUIS — its timetable on [data.gov.sg](https://data.gov.sg/datasets/d_e81ea2337599b674c4f645c1af93e0dc/view), all of 2025 | 365 | Fajr **19.85°**, Isha **18.16°**, Maghrib +0.7 min, Dhuhr +1.7 min, Asr factor 1 | `Singapore` (20° / 18°, Dhuhr +1) |

The exact minutes each body adds are fixed when the clients' prayer screens are built (`P2-W/A/I-1`): the test there
compares the apps' times with these timetables, day by day, within one minute.

## Not verified yet — the fallback (Muslim World League, Fajr 18°, Isha 17°) until each is read

| Country | The official body to read | Note |
| --- | --- | --- |
| **Japan** (named by the author) | — no national Islamic authority that publishes a timetable was found | MWL, and the screen says so. ☐ Whether a body (e.g. the Japan Muslim Association, Tokyo Camii) publishes one. |
| United Arab Emirates | the General Authority of Islamic Affairs, Endowments and Zakat — awqaf.gov.ae | its page builds the table with scripts; read it in the browser. Secondary sites say 18.2° / 18.2°. |
| Indonesia | Kemenag, Bimas Islam — bimasislam.kemenag.go.id/jadwalshalat | statements of its officials give Subuh −20°; Isya −18° only in secondary sources. |
| Kuwait, Qatar, Bahrain, Oman, Jordan, Iraq, Syria, Lebanon, Palestine, Yemen | their ministries of awqaf | |
| Morocco, Algeria, Tunisia, Libya, Sudan, Mauritania | their ministries of religious affairs (Morocco: habous.gov.ma) | |
| Pakistan, Bangladesh, India, Afghanistan, Iran | — | Pakistan has no single national timetable; Iran's Institute of Geophysics (Tehran) publishes one. |
| Brunei | the Ministry of Religious Affairs | |
| Russia, the Central Asian states, the Balkans | their muftiates | |
| Europe, the Americas, Africa south of the Sahara, East Asia | — usually no single national body | MWL, and the screen says so. |

Every country not in the first table uses MWL and the screen names it. Each one is added to the first table only when
its official timetable has been read and the method computed from it, as above.

## The shared data file

[`prayer-methods.json`](prayer-methods.json) (2026-11-26) holds the table above as data: each method's angles,
interval and minutes, the country → method table, and the time zones that suggest a country on a device. The clients
build each method from these values — not from the Adhan library's presets, which add a minute to Dhuhr for MWL and
Egypt that the timetables do not show. Malaysia's minutes are the measured ones rounded (Fajr and Isha +2, Dhuhr +3,
Maghrib +2). The web copies the file with `tools/sync-design.mjs`.

## Rules this sets for the clients (`P2-W/A/I-1`)

- The default method follows the country of the device's location (or the chosen city); the user can change it, and
  the screen always names the method in use and its source.
- The method's parameters live in one data file shared by the three clients (the country → method table above), not
  in code; adding a country is a data change.
- Times can differ by a minute or two from a mosque's own calendar — the screen says so (`AGENTS.md` §8.5).
