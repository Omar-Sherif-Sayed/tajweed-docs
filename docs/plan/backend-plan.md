# Backend plan — `tajweed-backend` (tasks P0-06, P0-07, P0-14)

Written 2026-11-21 at the author's request («لو هانبدأ فيه دلوقتي هاتعمله ازاي تفصيلياً»). It is a **plan for the
author's approval** — no code is written before he answers the questions in §1 (`AGENTS.md` §1: plan, ask, then code).
It follows `AGENTS.md` §5 (architecture), §6 (data rules), §8.14 (Dorar rules), §9 (backend conventions) and the
Quran Foundation terms (§7.1).

## 1. Decisions for the author (the agent's recommendation first)

**✔ All five approved by the author on 2026-11-21** («ok for all, don't forget to document everything, also javadoc on the code everywhere, to be readable in the future»). The scaffold was built the same day; what changed while building it is in §12.

| # | Question | Recommendation | Why |
| --- | --- | --- | --- |
| B1 | Spring Boot **4.2.0** (released 2026-11-19) or **4.1.3**? | **4.2.0** | The newest line gets the longest support; a new project starts there. If a library we need does not work with it on scaffold day (springdoc is the one to watch), fall back to 4.1.3 and write why. |
| B2 | PostgreSQL **18** (18.7) or **19** (19.0, released 2026-11)? | **18** | Mature (seventh patch), supported until 2030-11; 19.0 is days old and our Flyway version must list it as supported first. Moving 18 → 19 later is a routine upgrade. |
| B3 | Calling Dorar, the Quran Foundation, mp3quran: **Spring HTTP interface clients** (`@HttpExchange` on `RestClient`) or **OpenFeign** (Spring Cloud)? | **HTTP interface clients** | The same declarative style as Feign (an interface per API), but part of Spring Framework itself — no Spring Cloud dependency and its release train to keep in step with Boot 4.2. |
| B4 | Content pipeline (P0-14 D1 / D2) | **As in §8** | Small content in reviewed Flyway migrations; large content by an import job from checksummed files; Quran Foundation and Dorar only at run time, never committed (their terms). |
| B5 | Error messages from the API in **all 22 languages**? | **Yes** | The product rule is 22 languages for every user-facing text (`AGENTS.md` §1); `messages_<code>.properties` per language, the same keys, checked by a test. |

## 2. Tools on this machine

| Tool | State | Use |
| --- | --- | --- |
| JDK 25 (25.0.5) | ✔ installed | compile and run |
| Gradle | through the **wrapper** (`gradlew`), 9.9.2 — no installation | build, tests, run |
| Docker Desktop | ✔ installed — start it before work | a local PostgreSQL (`compose.yaml`) and Testcontainers |
| Git over SSH | ✔ | push |
| An IDE | the author's choice (IntelliJ IDEA reads Gradle projects directly) | — |
| PostgreSQL client | not installed — not needed (`docker exec … psql`, or the IDE's database tool) | — |

## 3. Versions — checked 2026-11-21

Read from Maven Central metadata (`repo1.maven.org/maven2/…/maven-metadata.xml`), postgresql.org/versions.json,
Docker Hub and services.gradle.org. **Libraries that Spring Boot manages are not given a version in the build** —
the Boot BOM decides, so the set stays compatible.

| Part | Version | Managed by Boot 4.2.0? |
| --- | --- | --- |
| Spring Boot (Gradle plugin) | 4.2.0 | — (Spring Framework 7.1.0, Spring Data 2026.1.0) |
| `io.spring.dependency-management` plugin | 1.1.7 | — |
| Gradle wrapper | 9.9.2 | — |
| Java | 25 (toolchain) | — |
| Hibernate ORM | 7.4.15.Final | ✔ |
| Flyway | 12.11.0 (13.13.0 exists; we keep Boot's) | ✔ |
| PostgreSQL JDBC driver | 42.7.14 | ✔ |
| Jackson | 3.1.8 | ✔ |
| Lombok | 1.18.48 | ✔ |
| Caffeine (in-memory cache) | 3.3.1 | ✔ |
| JUnit Jupiter / AssertJ / Mockito | 6.1.3 / 3.27.7 / 5.24.0 | ✔ |
| Testcontainers | 2.0.5 | ✔ |
| springdoc-openapi (`starter-webmvc-ui`) | 3.2.1 (2026-11-20) | ✘ pinned — ☐ prove it works with Boot 4.2 on scaffold day |
| ShedLock (`shedlock-spring`, JDBC provider) | 7.11.0 | ✘ pinned |
| Bucket4j (`bucket4j_jdk17-core`) | 8.22.0 | ✘ pinned |
| WireMock (`wiremock-standalone`) | 3.13.2 (4.x is still beta) | ✘ pinned |
| ArchUnit (`archunit-junit5`) | 1.5.1 | ✘ pinned |
| JaCoCo | 0.8.16 | Gradle plugin |
| PostgreSQL server (Docker `postgres:18`) | 18.7 | — |
| Runtime image | `eclipse-temurin:25-jre` | — |

## 4. Dependencies — what and why

```groovy
plugins {
    id 'java'
    id 'org.springframework.boot' version '4.2.0'
    id 'io.spring.dependency-management' version '1.1.7'
    id 'jacoco'
}
// group 'io.github.omarsherifsayed', Java toolchain 25

dependencies {
    // web API: controllers, validation, JSON (Jackson 3), health
    implementation 'org.springframework.boot:spring-boot-starter-webmvc'
    implementation 'org.springframework.boot:spring-boot-starter-validation'
    implementation 'org.springframework.boot:spring-boot-starter-actuator'      // /actuator/health only
    // database
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
    implementation 'org.springframework.boot:spring-boot-starter-flyway'
    runtimeOnly    'org.flywaydb:flyway-database-postgresql'
    runtimeOnly    'org.postgresql:postgresql'
    // calling Dorar, the Quran Foundation, mp3quran (HTTP interface clients)
    implementation 'org.springframework.boot:spring-boot-starter-restclient'
    // caching (Dorar ≤ 24 h, HTTP responses) and rate limiting (public API, Dorar's 60 / minute)
    implementation 'org.springframework.boot:spring-boot-starter-cache'
    implementation 'com.github.ben-manes.caffeine:caffeine'
    implementation 'com.bucket4j:bucket4j_jdk17-core:8.22.0'
    // schedulers that run once even with two instances (radio health checks, Content Sync)
    implementation 'net.javacrumbs.shedlock:shedlock-spring:7.11.0'
    implementation 'net.javacrumbs.shedlock:shedlock-provider-jdbc-template:7.11.0'
    // OpenAPI contract for the three clients (docs/api/openapi.yaml)
    implementation 'org.springdoc:springdoc-openapi-starter-webmvc-ui:3.2.1'
    // less boilerplate
    compileOnly 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'
    // local run: starts compose.yaml's PostgreSQL by itself
    developmentOnly 'org.springframework.boot:spring-boot-docker-compose'
    // tests
    testImplementation 'org.springframework.boot:spring-boot-starter-test'           // JUnit, AssertJ, Mockito
    testImplementation 'org.springframework.boot:spring-boot-starter-webmvc-test'    // MockMvc slices
    testImplementation 'org.springframework.boot:spring-boot-starter-data-jpa-test'  // repository slices
    testImplementation 'org.springframework.boot:spring-boot-testcontainers'
    testImplementation 'org.testcontainers:testcontainers-postgresql'
    testImplementation 'org.wiremock:wiremock-standalone:3.13.2'
    testImplementation 'com.tngtech.archunit:archunit-junit5:1.5.1'
}
```

**Not included, on purpose:** Spring Security (no login, no accounts — CORS and security headers are set by a small
filter instead); any analytics, crash or tracking library (`AGENTS.md` §5); Redis (one instance; Caffeine is enough);
MapStruct (mappers are `final` classes with static methods — `AGENTS.md` §9); Spring Cloud.

## 5. Project structure

```
tajweed-backend/
  build.gradle  settings.gradle  gradlew  gradlew.bat  gradle/wrapper/
  compose.yaml                       PostgreSQL 18 for local runs (and nothing else)
  Dockerfile                         two stages: build with JDK 25, run on eclipse-temurin:25-jre, non-root user
  .github/workflows/ci.yml           build · unit tests · integration tests · JaCoCo report · OpenAPI file check
  AGENTS.md  README.md  LICENSE  .gitignore  .gitattributes
  docs/  README.md  api/openapi.yaml  data-sources/  deployment/  quality/
  content/                           untouched source files (Tanzil text, metadata) + SHA256SUMS — never edited
  src/main/java/io/github/omarsherifsayed/tajweed/
    TajweedApplication.java
    general/
      config/        CorsConfig, CacheConfig, RateLimitFilter, SecurityHeadersFilter, OpenApiConfig, ClockConfig,
                     HttpClientsConfig (the @HttpExchange clients, timeouts), SchedulingConfig (ShedLock)
      exception/     ErrorCode (enum: NOT_FOUND_*, INVALID_*, UPSTREAM_*, RATE_LIMITED …), BaseException,
                     GlobalExceptionHandler (→ BaseResponse with the message in the request's language)
      schema/        BaseResponse<T> (success, code, message, data, timestamp), PageResponse<T>
      audit/         AbstractAuditingEntity (created / updated time)
      i18n/          LocaleConfig (Accept-Language → one of the 22 codes, Arabic by default), MessageService
      util/          ChecksumUtil, ArabicDigits …
    business/
      appinfo/       controller/AppInfoRetrievalController   GET /v1/app-info
                     service/AppInfoRetrievalService + impl/  schema/response/DtoAppInfo   mapper/AppInfoMapper
      (phase 1)      quran/  reciter/    (later) tafsir/ hadith/ radio/ dorar/ qf/ …  — one package per module of §9
  src/main/resources/
    application.properties           every value from an environment variable, with a safe local default
    application-local.properties     local run (compose.yaml)
    db/migration/V1_0_0__baseline.sql   then V<MAJOR>_<MINOR>_<PATCH>__<what>.sql
    i18n/messages.properties (Arabic) · messages_en.properties · … one file per language (22)
  src/test/java/…                    mirrors main; <Module>TestData fixtures; ArchitectureTest (ArchUnit)
```

Inside every module the order is fixed (`AGENTS.md` §9): `controller → service (interface) → service/impl →
repository (+ specs) → entity`, with `schema/request` (`Req*`), `schema/response` (`Dto*`), `mapper` (`final`,
static methods), `enums` (with `nameAr` / `nameEn` and the other languages through i18n keys), `constant`,
`scheduler`. **ArchUnit** checks these rules on every build: controllers never touch repositories, entities never
leave the service layer, nothing imports another module's `impl`.

## 6. Configuration

| Setting | Environment variable | Local default |
| --- | --- | --- |
| Database URL / user / password | `DB_URL`, `DB_USER`, `DB_PASSWORD` | the compose database |
| Allowed web origins (CORS) | `CORS_ORIGINS` | `http://localhost:4200` |
| Public rate limit | `RATE_LIMIT_PER_MINUTE` | 120 per IP |
| Dorar key | `DORAR_API_KEY` | empty → the Dorar module is off |
| Quran Foundation | `QF_CLIENT_ID`, `QF_CLIENT_SECRET`, `QF_ENV` (`prelive` / `production`) | empty → off |

**Secrets are never in a file in the repository** (all four repositories are public): locally in the IDE's run
configuration or a `.env` file listed in `.gitignore`; in CI as GitHub Actions secrets (only where a test needs them —
none at scaffold time); on the server as environment variables. A leaked Dorar key is reported within 24 hours
(§8.14), a Quran Foundation breach likewise (§7.1).

## 7. Cross-cutting behaviour

- **Responses:** every endpoint returns `BaseResponse<T>`; errors carry an `ErrorCode` and a message in the
  `Accept-Language` language (22 files, one key set; a test fails when a file misses a key).
- **HTTP caching:** `ETag` + `Cache-Control` on content endpoints (content changes only with a migration or an
  import), and `GET /v1/content-version` so the apps know when to refresh.
- **Rate limiting:** Bucket4j per IP on the public API; a separate global bucket of 60 / minute in front of Dorar.
- **CORS:** only the web application's origins.
- **Security headers:** `X-Content-Type-Options`, `Referrer-Policy`, `Content-Security-Policy` for the Swagger page.
- **Logging:** identifiers and timings, never payloads or secrets; no IP addresses kept beyond the rate limiter's memory.
- **Actuator:** only `health` is exposed.
- **OpenAPI:** generated from the code; the build writes `docs/api/openapi.yaml`, and CI fails when the committed file
  differs — the three clients read it as the contract.
- **Time:** a `Clock` bean (tests fix it); the backend never calculates prayer times (they are calculated on the
  device — §8.5).

## 8. Content pipeline — proposal for P0-14 (D1, D2)

| Content | How it enters | Checks |
| --- | --- | --- |
| Quran text (Tanzil Uthmani), metadata, surah names | the untouched files in `content/` + `SHA256SUMS`; a **Flyway Java migration** reads them, verifies the checksum, inserts byte for byte | a test recomputes the checksum and counts 114 surahs and 6,236 ayahs; a word-for-word comparison with the source |
| Search text (Tanzil Simple / Clean) | the same way, a second table, never displayed | the same 6,236 ayahs in the same order (§8.1) |
| Small catalogues (reciters, radio stations, books list, scholars list) | reviewed SQL migrations | constraints and tests |
| Large licensed content (hadith, books) — only after permission | an import job from versioned, checksummed data files | checksum, counts, spot checks against the edition |
| **Quran Foundation** (tafsirs …) | **never committed** — synced at run time through Content Sync, at least every 7 days | their terms (§7.1): a public repository is redistribution |
| **Dorar** | **never stored** — live through the backend, cached ≤ 24 h | §8.14 |
| The phones' bundled database (D1) | the same import code writes the SQLite file the apps ship, with a manifest of checksums | the apps verify the manifest |

## 9. Tests

| Kind | Tool | Runs with |
| --- | --- | --- |
| Unit (services, mappers, validation, i18n keys, checksums) | JUnit Jupiter + AssertJ + Mockito | `./gradlew test` — no database, no network |
| Web slices (controllers, `BaseResponse`, error codes, languages) | `@WebMvcTest` + MockMvc | `./gradlew test` |
| HTTP clients (Dorar, Quran Foundation, mp3quran) | WireMock | `./gradlew test` |
| Database and migrations | Testcontainers PostgreSQL 18, tagged `integration` | `./gradlew integrationTest` (Docker needed) |
| Architecture rules | ArchUnit | `./gradlew test` |
| Coverage | JaCoCo — report only, no minimum (`build/reports/jacoco`) | `./gradlew jacocoTestReport` |

Style: class Javadoc + `@DisplayName`, given / when / then, `<Module>TestData` fixtures (`AGENTS.md` §9).

## 10. Order of work (P0-06 → P0-07), each step checked before the next

1. **P0-06** — on the day: re-read the versions of §3, write them into `tajweed-backend/AGENTS.md` and `AGENTS.md` §4.1.
2. Generate the project with Spring Initializr (Gradle Groovy, Java 25, the starters of §4), base package
   `io.github.omarsherifsayed.tajweed` (R3, final); add the pinned libraries.
3. `compose.yaml` (postgres:18) and `V1_0_0__baseline.sql`; `ddl-auto=validate`; the app starts locally.
4. `general/`: `BaseResponse`, `ErrorCode`, `BaseException`, `GlobalExceptionHandler`, i18n (22 files), CORS,
   headers, rate limit, cache, OpenAPI.
5. `business/appinfo`: `GET /v1/app-info` (name in the request's language, author «Omar Sherif — عمر شريف», the
   LinkedIn link, API version) — the model every later endpoint copies.
6. Tests of §9; ArchUnit rules.
7. `Dockerfile`; CI on GitHub Actions (Temurin 25, Gradle cache, unit + integration + JaCoCo + OpenAPI check).
8. `AGENTS.md` (versions, structure, conventions with examples from the real code, how to run), `README.md` (build,
   test, run — step by step), `docs/README.md`. Commit as the author, push.

**Done when:** `./gradlew build` and `integrationTest` are green on this machine and in CI; `GET /v1/app-info` answers
inside `BaseResponse` in Arabic, English and the other 20 languages; a wrong path answers with an `ErrorCode` body in
the requested language; `docs/api/openapi.yaml` is generated.

**Then phase 1** (`P1-B1 …`): the `quran` module — before any migration, the exact tables and columns are listed for
the author's approval (`AGENTS.md` §1).

## 11. Risks to watch on scaffold day

- Spring Boot 4.2.0 is two days old: if springdoc 3.2.1 or ShedLock fails with it, B1 falls back to 4.1.3.
- Flyway 12.11 must list PostgreSQL 18 as supported (it warns otherwise).
- The machine's certificate store (§1): Maven Central and Gradle's services answered today; Docker Hub must answer
  for `postgres:18` — if any host fails, it is reported, never worked around by disabling certificate checks.

## 12. As built (2026-11-21) — what differs from the plan above

- **Javadoc everywhere** (the author's new rule): Checkstyle 14.4.0 with Javadoc rules only (`config/checkstyle/checkstyle.xml`) and the Javadoc tool with `-Xdoclint:all,-missing -Werror` fail the build on a missing or broken comment; every package has a `package-info.java`.
- **Added with their first use, not now:** ShedLock (first scheduler), WireMock and the HTTP interface clients (first external API). Nothing unused is in the build.
- **Database settings:** Spring's standard `SPRING_DATASOURCE_URL / _USERNAME / _PASSWORD` instead of `DB_*`; locally nothing is set — `spring-boot-docker-compose` starts `compose.yaml` and connects.
- **Mockito's agent** is given to the test JVM up front (`-javaagent`), as JDK 21+ deprecates loading it at run time.
- **The OpenAPI document stays on in production** (`API_DOCS_ENABLED`, default `true`): it is the public contract.
- **CI actions** at their latest major tags of the day: checkout v7, setup-java v6, gradle/actions v6, upload-artifact v7.
- Result: 42 tests (39 unit, 3 integration on PostgreSQL 18); `bootRun` checked; the backend's own `AGENTS.md` holds the versions, structure and conventions with examples.

## 13. The `reciter` module (P1-D4, P1-B3, P1-B6) — proposal of 2026-11-22, waiting for the author

The author: «Yes, reciters next» (2026-11-22). Nothing is built before his answers to the questions at the end.

### 13.1 What the sources hold today (read 2026-11-22)

mp3quran.net API v3 (`/reciters`, `/moshaf`, `/riwayat`, `/ayat_timing/reads`, `/ayat_timing?surah=&read=`) and
EveryAyah's own list (`everyayah.com/data/recitations.js`). A "moshaf" is one recitation: a reciter, a riwayah, a
style, a folder of surah files `NNN.mp3` and the list of surahs it holds. mp3quran's timings are given per moshaf
(`read` = the moshaf id), in milliseconds, one row per ayah plus a row «ayah 0» for what is recited before ayah 1
(the isti'adha and basmala).

| Reciter (§7.3) | mp3quran moshaf (id · surahs) | mp3quran timings | EveryAyah (one file per ayah) |
| --- | --- | --- | --- |
| محمد صديق المنشاوي | مرتل 112 · 114 · مجود 113 · 114 · معلم 114 · 114 · (a 1967 recording 10924 · 110) | **مرتل only** | Murattal 128 · Mujawwad 64 / 192 |
| محمود خليل الحصري | مرتل 118 · 114 · مجود 119 · 114 · (Warsh 120, al-Duri 269, Qalun 270) | مرتل, مجود (and the three other riwayat) | 64 / 128 · Mujawwad 64 / 128 · **Muallim 128** |
| عبد الباسط عبد الصمد | مرتل 53 · 114 · مجود 51 · 114 · (Warsh 52) | مرتل, مجود | Murattal 64 / 192 · Mujawwad 128 |
| محمد محمود الطبلاوي | مرتل 106 · 114 · مجود 10912 · 114 | **مرتل only** | 64 / 128 |
| ماهر المعيقلي | مرتل 102 · 114 · مجود 133 · 114 · معلم 103 · **38** | **مجود only** | 64 / 128 |
| ياسر الدوسري | مرتل 92 · 114 | ✔ | 128 |
| عبد الرحمن السديس | مرتل 54 · 114 | ✔ | 64 / 192 |
| سعود الشريم | مرتل 31 · 114 | ✔ | 64 / 128 |
| نورين محمد صديق | الدوري عن أبي عمرو 138 · 114 | — | — |
| فارس عباد | مرتل 81 · 114 | ✔ | 64 |
| سعد الغامدي | مرتل 30 · 114 | ✔ | 40 |
| علي بن عبد الرحمن الحذيفي | حفص 74 · 114 · (Qalun 75, Shu'bah 305) | حفص (and the other two) | 32 / 64 / 128 |
| أيمن رشدي سويد | معلم 10925 · 114 (on `server15`, not the CDN) | — | 64 |

Two corrections to §7.3 of the parent `AGENTS.md`, from these lists: mp3quran's timings exist for some styles only
(Minshawi and al-Tablawi: murattal only; al-Muaiqli: mujawwad only); Ayman Suwayd has no timings. An audio file
answered `200 audio/mpeg` from both hosts (checked on one file each).

### 13.2 Proposed tables (migration 1.3.0, written into `tajweed-backend/docs/database/README.md` first)

| Table | Columns |
| --- | --- |
| `reciter` | `pk_id` smallint · `name_ar` · `name_en` (mp3quran's own names) · `mp3quran_id` (unique) · audit |
| `recitation` | `pk_id` · `reciter_id` → `reciter` · `style` (`MURATTAL` / `MUJAWWAD` / `MUALLIM`) · `riwayah` (`HAFS_AN_ASIM`, `AL_DURI_AN_ABI_AMR`, …) · `listening_only` (true when the riwayah is not Hafs: never shown over the Hafs text, §6.7, R5) · `mp3quran_moshaf_id` (unique) · `surah_count` · audit |
| `recitation_surah` | `pk_id` · `recitation_id` · `surah_id` → `surah` (unique together) — which surahs a recitation has (al-Muaiqli's muallim: 38) |
| `audio_source` | `pk_id` · `recitation_id` · `priority` (1, 2, … — the order the players try, F11) · `kind` (`SURAH_FILE` / `AYAH_FILE`) · `provider` (`MP3QURAN` / `EVERYAYAH`) · `url_template` (e.g. `…/r1/{surah:3}.mp3`, `…/{surah:3}{ayah:3}.mp3`) · `bitrate_kbps` · `download_allowed` (F28: false until the source allows it in writing) · `status` (`OK` / `FAILING`) · `last_checked_at` · `consecutive_failures` · audit |
| `ayah_timing` | `pk_id` · `recitation_id` · `surah_id` · `ayah_number` (0 = before ayah 1) · `start_ms` · `end_ms` (unique: recitation, surah, ayah) — about 6,350 rows per timed recitation |
| `shedlock` | ShedLock's own table, so that the health check runs once even with two instances |

### 13.3 How the data enters (§8 of this plan)

- The catalogue (reciters, recitations, surah lists, sources) is a **reviewed data file** in `content/mp3quran/`
  (the two API answers as received, checksummed) plus our own selection file (which moshafs, which EveryAyah folders,
  in which order) — imported by a Java migration that checks every count (114 surahs where complete, the surah list
  equal to `surah_total`).
- The timings: the raw answers of `/ayat_timing` kept as received (about 1.3 MB per recitation; about 17 MB for the
  thirteen timed Hafs recitations), checksummed; the import checks that every surah has one row per ayah of the Tanzil
  count (plus ayah 0), that times only increase, and that no gap or overlap exceeds a set limit.
- **A verification script** (P1-D4) requests every surah file of every recitation once (`HEAD`, about 2,300
  requests to mp3quran's CDN) and the first and last ayah of every surah on EveryAyah; a recitation with a missing
  file is not published. The result and the date go into `docs/data-sources/`.
- Audio is never copied: the apps stream from the sources (§5).

### 13.4 Endpoints and the health check

`GET /v1/reciters` (with their recitations) · `GET /v1/reciters/{id}` · `GET /v1/recitations/{id}` (surahs, sources in
order with their status) · `GET /v1/recitations/{id}/surahs/{n}/timings`. The health check (ShedLock 7.11.0, checked
2026-11-21) sends one `HEAD` a day to a sample file of every source and marks it `FAILING` after three failures in a
row; the clients try the sources in order anyway (F11), so a wrong mark never stops playback.

### 13.5 The author's answers (2026-11-22)

| Question | Answer |
| --- | --- |
| Download from mp3quran and keep the files in `tajweed-backend` | **Yes, all of it**: the catalogue, the ayah timings of the 13 timed Hafs recitations, and one check of every surah file. |
| EveryAyah, which has not answered its letter yet | **Include it now, streaming only** (downloads off, credited); **what depends on their answer continues after it** — downloading (F28) and anything their terms may limit. Recorded in `docs/permissions/README.md`. |
| The other riwayat of the requested reciters (al-Husary: Warsh, Qalun, al-Duri; Ali al-Hudhaifi: Qalun, Shu'bah; Abdul Basit: Warsh) | **Include them all**, and with every recitation **say clearly which riwayah it is**, Hafs or another. They are listening only (§6.7): the text the application shows is Hafs. |
| The incomplete Hafs recitations (al-Muaiqli's muallim, 38 surahs; al-Minshawi's 1967 recording, 110 surahs) | **Both**, each showing which surahs it has. |

What follows from the answers: 27 mp3quran recitations of 13 reciters; EveryAyah's Hafs folders of the same reciters
(its Warsh folder of Abdul Basit is left out — EveryAyah lists it with 47 files missing, and its numbering would not be
the Hafs one). A riwayah is shown with its full name as mp3quran writes it («ورش عن نافع»), its rawi and its qari taken
from that name, and «للاستماع فقط — النص المعروض برواية حفص عن عاصم» when it is not Hafs; ☐ a longer description of each
riwayah only from a named book. Timings are imported for the Hafs recitations only — another riwayah counts the
ayahs differently, so its timings would not match the Hafs ayah numbers.

### 13.6 As built (2026-11-22)

- **37 recitations**: the 27 mp3quran moshafs of the answers, and 10 EveryAyah folders as their own recitations,
  labelled «(ملف لكل آية)». Five EveryAyah folders are not separate recitations but **fallbacks** after an mp3quran
  file, because a measurement showed they are the same recording (the method and the figures:
  `tajweed-backend/docs/data-sources/README.md`). «Hudhaify» on EveryAyah is left out: its identity cannot be
  measured, since Ali al-Hudhaifi's mp3quran timings cannot be trusted.
- **Timings**: 12 of the 13 timed Hafs moshafs, 74,977 rows. Left out with their reasons
  (`content/reviewed/timing-exclusions.csv`): Ali al-Hudhaifi's whole set (112 of 114 surahs miss their last ayah)
  and 7 single surahs. The rule: ayahs 1 to the Tanzil count, «ayah 0» optional (only some recitations have it).
- **Audio check**: 8,926 `HEAD` requests (every mp3quran surah file; the first and last ayah of every surah of 25
  EveryAyah folders) — all `200 audio/mpeg`. A Python thread pool was used: Git Bash cannot fork that many processes.
- Changes from §13.2: `recitation.provider` added; the health state is a separate table `audio_source_check` (the
  content tables stay read-only); `download_allowed` is false everywhere until an owner allows downloads in writing.
- **Size**: the timing files are 19.9 MB (1,482 files) — more than the 17 MB estimated.
