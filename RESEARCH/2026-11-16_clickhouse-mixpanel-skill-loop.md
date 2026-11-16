# RESEARCH — AN-CH ClickHouse + AN-MIX Mixpanel skill dalgası

> ts: `2026-11-16T13:20:00Z` · Europe/Istanbul `2026-11-16T16:20:00+03:00`  
> Tür: iç doküman + web kaynak notu · **uydurma kişi yok** · tenant yok → dry-run  
> Domain: 9 skill (`AN-CH` 6 + `AN-MIX` 3)

## İç doküman (önce oku)

| Dosya | Sinyal |
|-------|--------|
| `data/skill_envanteri.json` | 696 skill / 50 domain · flag 900M RED |
| `data/skill_title_haritasi.json` | ClickHouse + Mixpanel C→WORKER title zinciri |
| `SKILLS_TALENT/TALENT_TAXONOMY.md` | ~98 yetenek iskelet |
| `ROSTER/TITLE_INVENTORY.md` | 633 holding title |
| `scripts/skill_ajans_uretim.py` | 122 slot sözleşmesi 4–12 KiB |

## Web kaynaklar (URL + ts)

| Skill | Kaynak | URL | ts |
|-------|--------|-----|-----|
| (CH genel) | ClickHouse docs index | https://clickhouse.com/docs | 2026-11-16T13:11:00Z |
| (CH genel) | OSS changelog 2026 · release 26.10 (2026-10-22) | https://clickhouse.com/docs/resources/changelogs/oss/2026 | 2026-11-16T13:11:00Z |
| chdb-datastore, chdb-sql | chDB getting started | https://clickhouse.com/docs/chdb/getting-started | 2026-11-16T13:12:00Z |
| chdb-* | chDB Python API | https://clickhouse.com/docs/chdb/api/python | 2026-11-16T13:12:00Z |
| chdb-* | chdb-io/chdb README | https://github.com/chdb-io/chdb | 2026-11-16T13:12:00Z |
| clickhouse-best-practices | Query optimization guides | https://clickhouse.com/docs/guides/clickhouse/performance-and-monitoring/query-optimization | 2026-11-16T13:15:00Z |
| clickhouse-architecture-advisor | Get started / deployment modes | https://clickhouse.com/docs/get-started/index | 2026-11-16T13:11:00Z |
| clickhouse-js-node-troubleshooting | Official JS client | https://clickhouse.com/docs/integrations/language-clients/js | 2026-11-16T13:13:00Z |
| clickhousectl-local-dev | clickhousectl reference | https://clickhouse.com/docs/concepts/features/interfaces/cli | 2026-11-16T13:14:00Z |
| clickhousectl-local-dev | Cloud CLI (OAuth read-only vs API key write) | https://clickhouse.com/docs/products/cloud/features/cli | 2026-11-16T13:14:00Z |
| manage-lexicon | Mixpanel Lexicon | https://docs.mixpanel.com/docs/data-governance/lexicon | 2026-11-16T13:12:00Z |
| manage-lexicon | Lexicon Schemas API | https://docs.mixpanel.com/reference/lexicon-schemas-api | 2026-11-16T13:12:00Z |
| tracking-implementation | Track events | https://docs.mixpanel.com/docs/overview/capture-events/track-events | 2026-11-16T13:12:00Z |
| tracking-implementation | Tracking plan | https://docs.mixpanel.com/docs/tracking-best-practices/tracking-plan | 2026-11-16T13:12:00Z |
| deep-research | (aynı Mixpanel tracking-plan + CH docs — “deep-research” skill adı Mixpanel kümesinde; ayrı üçüncü taraf rapor uydurulmadı) | https://docs.mixpanel.com/docs/tracking-best-practices/tracking-plan | 2026-11-16T13:12:00Z |
| satranç yetenek | FIDE ratings | https://ratings.fide.com/ | 2026-11-16T13:16:00Z |
| satranç yetenek | FIDE FRL download (Nov 2026 list dated 15 Nov 2026) | https://ratings.fide.com/download_lists.phtml | 2026-11-16T13:16:00Z |

## Sentez (sinyal)

- ClickHouse 26.10 (2026-10-22) changelog: analyzer-only path; `system.metric_log` bucketed schema default; optional seccomp — **ASSESS-ONLY**, exploit yok.
- chDB: in-process ClickHouse SQL; server yok; path başına tek process — holding stdlib Python runtime’da **pip/chdb kurulumu yok**; not + dry-run.
- clickhousectl: Cloud `auth login` tarayıcı **read-only**; yazma API key. Bu repo secret yazmaz (`${CLICKHOUSE_CLOUD_API_KEY}`).
- JS client: `@clickhouse/client` Node; web ayrı paket. Bu ürün `katalog/` npm **kurmaz**.
- Mixpanel: Lexicon = sözlük; Schemas API ⊂ UI; tracking plan KPI→flow→event. Credential yok → şablon.
- FIDE: Standard Top Open snapshot sayfada Carlsen 2823 — **unverified holding yayını**; ranking kopyalanmaz top-100 iddiası yok.

## Yapılmayan

- Canlı cluster / Mixpanel project / API key
- Remote CLI installer via pipe-to-shell (ethics yasak)
- 900M prompt
- FAZ6 SoA kopyası
