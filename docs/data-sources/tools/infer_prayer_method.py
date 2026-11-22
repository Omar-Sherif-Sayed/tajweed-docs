"""Infers the method of an official prayer timetable from its own times.

For every day: the sun's depression below the horizon at the published Fajr and Isha minutes (NOAA solar position
algorithm), Isha - Maghrib in minutes, Maghrib - sunset, Dhuhr - solar noon, and the Asr shadow factor. A method by
angle shows a constant angle; a method by interval shows a constant interval. Times are published to the minute, so a
single day's angle is only good to about +-0.25 degrees; the mean over many days is what counts.
"""
import math, statistics, datetime as dt


def jd(y, m, d):
    if m <= 2:
        y -= 1; m += 12
    a = y // 100; b = 2 - a + a // 4
    return math.floor(365.25 * (y + 4716)) + math.floor(30.6001 * (m + 1)) + d + b - 1524.5


def sun(jdn):
    """Declination (deg) and equation of time (min) for a Julian day (NOAA)."""
    t = (jdn - 2451545.0) / 36525.0
    l0 = (280.46646 + t * (36000.76983 + 0.0003032 * t)) % 360
    m = 357.52911 + t * (35999.05029 - 0.0001537 * t)
    e = 0.016708634 - t * (0.000042037 + 0.0000001267 * t)
    mr = math.radians(m)
    c = (math.sin(mr) * (1.914602 - t * (0.004817 + 0.000014 * t)) + math.sin(2 * mr) * (0.019993 - 0.000101 * t)
         + math.sin(3 * mr) * 0.000289)
    true_long = l0 + c
    omega = 125.04 - 1934.136 * t
    app_long = true_long - 0.00569 - 0.00478 * math.sin(math.radians(omega))
    eps0 = 23 + (26 + (21.448 - t * (46.815 + t * (0.00059 - t * 0.001813))) / 60) / 60
    eps = eps0 + 0.00256 * math.cos(math.radians(omega))
    decl = math.degrees(math.asin(math.sin(math.radians(eps)) * math.sin(math.radians(app_long))))
    y = math.tan(math.radians(eps / 2)) ** 2
    l0r = math.radians(l0)
    eqt = 4 * math.degrees(y * math.sin(2 * l0r) - 2 * e * math.sin(mr) + 4 * e * y * math.sin(mr) * math.cos(2 * l0r)
                           - 0.5 * y * y * math.sin(4 * l0r) - 1.25 * e * e * math.sin(2 * mr))
    return decl, eqt


def altitude(date, minutes_local, lat, lon, tz):
    """Sun altitude (deg) at a local clock time (minutes after midnight)."""
    ut_min = minutes_local - tz * 60
    jdn = jd(date.year, date.month, date.day) + ut_min / 1440.0
    decl, eqt = sun(jdn)
    tst = ut_min + eqt + 4 * lon  # true solar time, minutes
    ha = tst / 4 - 180
    lr, dr, hr = map(math.radians, (lat, decl, ha))
    cosz = math.sin(lr) * math.sin(dr) + math.cos(lr) * math.cos(dr) * math.cos(hr)
    return 90 - math.degrees(math.acos(max(-1, min(1, cosz))))


def noon(date, lon, tz):
    _, eqt = sun(jd(date.year, date.month, date.day) + 0.5 - tz / 24)
    return 720 - 4 * lon - eqt + tz * 60


def time_at(date, lat, lon, tz, target_alt, morning):
    """Clock minutes when the sun is at target_alt (bisection), morning or evening."""
    n = noon(date, lon, tz)
    lo, hi = (n - 720, n) if morning else (n, n + 720)
    for _ in range(60):
        mid = (lo + hi) / 2
        a = altitude(date, mid, lat, lon, tz)
        if morning:
            lo, hi = (mid, hi) if a < target_alt else (lo, mid)
        else:
            lo, hi = (mid, hi) if a > target_alt else (lo, mid)
    return (lo + hi) / 2


def asr_factor(date, minutes, lat, lon, tz):
    """The shadow factor k such that shadow = k * object + noon shadow, at the published Asr."""
    decl, _ = sun(jd(date.year, date.month, date.day) + 0.5 - tz / 24)
    a = altitude(date, minutes, lat, lon, tz)
    noon_shadow = math.tan(math.radians(abs(lat - decl)))
    return 1 / math.tan(math.radians(a)) - noon_shadow


def hm(s, pm=False):
    h, m = map(int, s.split(':')[:2])
    if pm and h < 12:
        h += 12
    return h * 60 + m


def report(name, rows, lat, lon, tz, elevation_note=""):
    """rows: (date, fajr, sunrise, dhuhr, asr, maghrib, isha) in clock minutes."""
    fa, ia, iv, ms, dn, sr, af = [], [], [], [], [], [], []
    for d, f, s, z, a, m, i in rows:
        fa.append(-altitude(d, f, lat, lon, tz))
        ia.append(-altitude(d, i, lat, lon, tz))
        iv.append(i - m)
        sset = time_at(d, lat, lon, tz, -0.833, False)
        srise = time_at(d, lat, lon, tz, -0.833, True)
        ms.append(m - sset)
        sr.append(s - srise)
        dn.append(z - noon(d, lon, tz))
        af.append(asr_factor(d, a, lat, lon, tz))
    def st(x):
        return f"mean {statistics.mean(x):6.2f}  sd {statistics.pstdev(x):5.2f}  min {min(x):6.2f}  max {max(x):6.2f}"
    out = [f"## {name}  ({len(rows)} days, {lat}, {lon}, UTC{tz:+g}) {elevation_note}",
           f"Fajr depression (deg)   {st(fa)}",
           f"Isha depression (deg)   {st(ia)}",
           f"Isha - Maghrib (min)    {st(iv)}",
           f"Maghrib - sunset (min)  {st(ms)}",
           f"Sunrise - calc (min)    {st(sr)}",
           f"Dhuhr - noon (min)      {st(dn)}",
           f"Asr shadow factor       {st(af)}"]
    return "\n".join(out)
