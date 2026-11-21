# Backend plan — `tajweed-backend` (tasks P0-06, P0-07, P0-14)

Written 2026-11-21 at the author's request («لو هانبدأ فيه دلوقتي هاتعمله ازاي تفصيلياً»). It is a **plan for the
author's approval** — no code is written before he answers the questions in §1 (`AGENTS.md` §1: plan, ask, then code).
It follows `AGENTS.md` §5 (architecture), §6 (data rules), §8.14 (Dorar rules), §9 (backend conventions) and the
Quran Foundation terms (§7.1).

## 1. Decisions for the author (the agent's recommendation first)

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
