#!/usr/bin/env python3
"""FAZ 6: ISO/IEC 27001:2022 SoA skeleton + 10 catalog CTRLs (ASSESS-ONLY).

Does not copy ISO standard body text — Annex A IDs + public short titles only.
Idempotent. Defense-only. No secrets, no exploit content.

Usage:
  python3 scripts/giga_security_faz6_soa.py
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUARD = (
    "> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. "
    "No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. "
    "ATT&CK only for detection/D3FEND mapping. "
    "Secrets: ${VAR}|vault://|op://|<REDACTED> only."
)
BANNER = "# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok"

# Public Annex A short titles (ID labels used in SoA practice; not standard prose).
ISO_ANNEX: list[tuple[str, str, str]] = [
    ("A.5.1", "Organizational", "Policies for information security"),
    ("A.5.2", "Organizational", "Information security roles and responsibilities"),
    ("A.5.3", "Organizational", "Segregation of duties"),
    ("A.5.4", "Organizational", "Management responsibilities"),
    ("A.5.5", "Organizational", "Contact with authorities"),
    ("A.5.6", "Organizational", "Contact with special interest groups"),
    ("A.5.7", "Organizational", "Threat intelligence"),
    ("A.5.8", "Organizational", "Information security in project management"),
    ("A.5.9", "Organizational", "Inventory of information and other associated assets"),
    ("A.5.10", "Organizational", "Acceptable use of information and other associated assets"),
    ("A.5.11", "Organizational", "Return of assets"),
    ("A.5.12", "Organizational", "Classification of information"),
    ("A.5.13", "Organizational", "Labelling of information"),
    ("A.5.14", "Organizational", "Information transfer"),
    ("A.5.15", "Organizational", "Access control"),
    ("A.5.16", "Organizational", "Identity management"),
    ("A.5.17", "Organizational", "Authentication information"),
    ("A.5.18", "Organizational", "Access rights"),
    ("A.5.19", "Organizational", "Information security in supplier relationships"),
    ("A.5.20", "Organizational", "Addressing information security within supplier agreements"),
    ("A.5.21", "Organizational", "Managing information security in the ICT supply chain"),
    ("A.5.22", "Organizational", "Monitoring, review and change management of supplier services"),
    ("A.5.23", "Organizational", "Information security for use of cloud services"),
    ("A.5.24", "Organizational", "Information security incident management planning and preparation"),
    ("A.5.25", "Organizational", "Assessment and decision on information security events"),
    ("A.5.26", "Organizational", "Response to information security incidents"),
    ("A.5.27", "Organizational", "Learning from information security incidents"),
    ("A.5.28", "Organizational", "Collection of evidence"),
    ("A.5.29", "Organizational", "Information security during disruption"),
    ("A.5.30", "Organizational", "ICT readiness for business continuity"),
    ("A.5.31", "Organizational", "Legal, statutory, regulatory and contractual requirements"),
    ("A.5.32", "Organizational", "Intellectual property rights"),
    ("A.5.33", "Organizational", "Protection of records"),
    ("A.5.34", "Organizational", "Privacy and protection of PII"),
    ("A.5.35", "Organizational", "Independent review of information security"),
    ("A.5.36", "Organizational", "Compliance with policies, rules and standards for information security"),
    ("A.5.37", "Organizational", "Documented operating procedures"),
    ("A.6.1", "People", "Screening"),
    ("A.6.2", "People", "Terms and conditions of employment"),
    ("A.6.3", "People", "Information security awareness, education and training"),
    ("A.6.4", "People", "Disciplinary process"),
    ("A.6.5", "People", "Responsibilities after termination or change of employment"),
    ("A.6.6", "People", "Confidentiality or non-disclosure agreements"),
    ("A.6.7", "People", "Remote working"),
    ("A.6.8", "People", "Information security event reporting"),
    ("A.7.1", "Physical", "Physical security perimeters"),
    ("A.7.2", "Physical", "Physical entry"),
    ("A.7.3", "Physical", "Securing offices, rooms and facilities"),
    ("A.7.4", "Physical", "Physical security monitoring"),
    ("A.7.5", "Physical", "Protecting against physical and environmental threats"),
    ("A.7.6", "Physical", "Working in secure areas"),
    ("A.7.7", "Physical", "Clear desk and clear screen"),
    ("A.7.8", "Physical", "Equipment siting and protection"),
    ("A.7.9", "Physical", "Security of assets off-premises"),
    ("A.7.10", "Physical", "Storage media"),
    ("A.7.11", "Physical", "Supporting utilities"),
    ("A.7.12", "Physical", "Cabling security"),
    ("A.7.13", "Physical", "Equipment maintenance"),
    ("A.7.14", "Physical", "Secure disposal or re-use of equipment"),
    ("A.8.1", "Technological", "User endpoint devices"),
    ("A.8.2", "Technological", "Privileged access rights"),
    ("A.8.3", "Technological", "Information access restriction"),
    ("A.8.4", "Technological", "Access to source code"),
    ("A.8.5", "Technological", "Secure authentication"),
    ("A.8.6", "Technological", "Capacity management"),
    ("A.8.7", "Technological", "Protection against malware"),
    ("A.8.8", "Technological", "Management of technical vulnerabilities"),
    ("A.8.9", "Technological", "Configuration management"),
    ("A.8.10", "Technological", "Information deletion"),
    ("A.8.11", "Technological", "Data masking"),
    ("A.8.12", "Technological", "Data leakage prevention"),
    ("A.8.13", "Technological", "Information backup"),
    ("A.8.14", "Technological", "Redundancy of information processing facilities"),
    ("A.8.15", "Technological", "Logging"),
    ("A.8.16", "Technological", "Monitoring activities"),
    ("A.8.17", "Technological", "Clock synchronization"),
    ("A.8.18", "Technological", "Use of privileged utility programs"),
    ("A.8.19", "Technological", "Installation of software on operational systems"),
    ("A.8.20", "Technological", "Networks security"),
    ("A.8.21", "Technological", "Security of network services"),
    ("A.8.22", "Technological", "Segregation of networks"),
    ("A.8.23", "Technological", "Web filtering"),
    ("A.8.24", "Technological", "Use of cryptography"),
    ("A.8.25", "Technological", "Secure development life cycle"),
    ("A.8.26", "Technological", "Application security requirements"),
    ("A.8.27", "Technological", "Secure system architecture and engineering principles"),
    ("A.8.28", "Technological", "Secure coding"),
    ("A.8.29", "Technological", "Security testing in development and acceptance"),
    ("A.8.30", "Technological", "Outsourced development"),
    ("A.8.31", "Technological", "Separation of development, test and production environments"),
    ("A.8.32", "Technological", "Change management"),
    ("A.8.33", "Technological", "Test information"),
    ("A.8.34", "Technological", "Protection of information systems during audit testing"),
]

N_A_PHYSICAL = {f"A.7.{i}" for i in range(1, 15)}
N_A_HR = {"A.6.1", "A.6.2", "A.6.4", "A.6.5"}

EXTRA_CONTROLS: list[dict] = [
    {
        "folder": "LAYERS",
        "id": "CTRL-L-016",
        "ad": "Kimlik katmanı — iş yükü ve insan kimlik envanteri",
        "aciklama": "Repo OS kapsamında GitHub org üyeliği, GITHUB_ACTOR ve yerel agent kimliği envanteri; yerel IAM store yok.",
        "nist_csf": ["Protect", "Govern"],
        "n80053": ["IA-2", "AC-2"],
        "iso": ["A.5.16", "A.5.18"],
        "cis": ["CIS-5", "CIS-6"],
        "owasp": ["A07:2021"],
        "dogrulama": "ORG/ROLES + inventory.md kimlik satırları; GHA actor koşulları ASSESS.",
        "gerekce": "Kimliksiz erişim ve sahte bot hesabı yüzeyini daraltır.",
    },
    {
        "folder": "LAYERS",
        "id": "CTRL-L-017",
        "ad": "Kimlik doğrulama bilgisi — secret placeholder standardı",
        "aciklama": "Parola/token/API anahtarı yalnızca ${VAR}|vault://|op://|<REDACTED>; gerçek değer commit ve sohbet yasağı.",
        "nist_csf": ["Protect"],
        "n80053": ["IA-5"],
        "iso": ["A.5.17", "A.8.5"],
        "cis": ["CIS-5"],
        "owasp": ["A07:2021"],
        "dogrulama": "python3 scripts/secret_scan.py; docs/SECRETS-DRYRUN-MATRISI.md.",
        "gerekce": "Kimlik doğrulama sırrının sızması diğer kontrolleri geçersiz kılar.",
    },
    {
        "folder": "FIREWALLS",
        "id": "CTRL-FW-013",
        "ad": "Bulut hizmeti kullanım envanteri (GitHub/GHA/LLM)",
        "aciklama": "Holding OS ‘cloud’ yüzeyi: GitHub, Actions, isteğe bağlı Gemini/OpenRouter; müşteri SaaS yok varsayımı.",
        "nist_csf": ["Identify", "Protect"],
        "n80053": ["SA-9", "CA-3"],
        "iso": ["A.5.23"],
        "cis": ["CIS-15"],
        "owasp": [],
        "dogrulama": "SECURITY_CONTEXT/inventory.md + trust-boundaries.md cloud satırları.",
        "gerekce": "Paylaşılan sorumluluk ve üçüncü taraf işlemci sınırı netleşir.",
    },
    {
        "folder": "FIREWALLS",
        "id": "CTRL-FW-014",
        "ad": "Doküman/agent URL hijyeni (web filtering analog)",
        "aciklama": "Agent fetch ve araştırma URL’leri resmi standart/docs allowlist kültürü; rastgele paste/kurulum yasağı.",
        "nist_csf": ["Protect"],
        "n80053": ["SI-3", "SC-7"],
        "iso": ["A.8.23", "A.5.7"],
        "cis": ["CIS-7", "CIS-9"],
        "owasp": ["A10:2021"],
        "dogrulama": "SECURITY_RESEARCH kaynak URL’leri + ethics_check tehlikeli-indir pattern.",
        "gerekce": "Sosyal-medya ‘setup’ ve rastgele script yüzeyi bu OS’te birincil web riski.",
    },
    {
        "folder": "ENCRYPTION",
        "id": "CTRL-ENC-013",
        "ad": "Çıktı sızıntı önleme — log/rapor redaksiyonu",
        "aciklama": "AUDIT_LOG, REPORTS, gunluk md: secret değer yok; konum+tip. LLM çıktısı redakte.",
        "nist_csf": ["Protect", "Detect"],
        "n80053": ["SI-12", "AU-9"],
        "iso": ["A.8.12", "A.8.11"],
        "cis": ["CIS-3", "CIS-8"],
        "owasp": ["A02:2021"],
        "dogrulama": "secret_scan REPORTS; holding_report dry-run; chat secret yasağı.",
        "gerekce": "DLP analogu bu runtime’da log ve agent dökümü.",
    },
    {
        "folder": "CHANGE",
        "id": "CTRL-CH-013",
        "ad": "Kaynak koda erişim — branch/CODEOWNERS ASSESS",
        "aciklama": "Kaynak (scripts/, .github/, SECURITY_*) değişikliği PR ile; fork secret izolasyonu hedefi.",
        "nist_csf": ["Protect"],
        "n80053": ["AC-3", "CM-5"],
        "iso": ["A.8.4", "A.8.3"],
        "cis": ["CIS-6", "CIS-16"],
        "owasp": ["A01:2021"],
        "dogrulama": "CODEOWNERS varlığı ASSESS; branch protection insan teyidi (gh api).",
        "gerekce": "Kaynak bütünlüğü tedarik zinciri ve yetkisiz değişiklik riskini keser.",
    },
    {
        "folder": "CHANGE",
        "id": "CTRL-CH-014",
        "ad": "Ortam ayrımı — local agent vs CI vs yok-prod",
        "aciklama": "Üretim uygulama sunucusu yok; ayrım: geliştirici workspace / GHA runner / main branch artefaktı.",
        "nist_csf": ["Protect"],
        "n80053": ["CM-2", "SC-2"],
        "iso": ["A.8.31"],
        "cis": ["CIS-4", "CIS-16"],
        "owasp": [],
        "dogrulama": "inventory.md ‘uygulama sunucusu yok’ + workflow job sınırları.",
        "gerekce": "Yanlışlıkla runner’da canlı secret veya prod mutasyonu önlenir.",
    },
    {
        "folder": "TRANSPARENT_CODE",
        "id": "CTRL-TC-013",
        "ad": "Teknik zafiyet yönetimi — scanner + Dependabot ASSESS",
        "aciklama": "Zafiyet süreci: secret_scan, ethics_check, Dependabot Actions; exploit PoC yok.",
        "nist_csf": ["Identify", "Detect"],
        "n80053": ["RA-5", "SI-2"],
        "iso": ["A.8.8"],
        "cis": ["CIS-7"],
        "owasp": ["A06:2021"],
        "dogrulama": ".github/dependabot.yml; python3 scripts/secret_scan.py; ethics_check.py.",
        "gerekce": "Tespit ve yama hipotezi; silahlandırılmış repro yasak.",
    },
    {
        "folder": "TRANSPARENT_CODE",
        "id": "CTRL-TC-014",
        "ad": "Geliştirme güvenlik testi — validate/ethics/secret kapısı",
        "aciklama": "Kabul testi analogu: validate.py GECTI, ethics failClosed, secret warn/redact.",
        "nist_csf": ["Protect", "Detect"],
        "n80053": ["SA-11", "SI-10"],
        "iso": ["A.8.29", "A.8.28"],
        "cis": ["CIS-16"],
        "owasp": ["A04:2021"],
        "dogrulama": "python3 scripts/validate.py; ethics_check; spec_validate --self-test.",
        "gerekce": "Kod kabulünde savunma kapısı olmazsa SoA kâğıtta kalır.",
    },
    {
        "folder": "CONDITIONAL",
        "id": "CTRL-CD-016",
        "ad": "Koşullu: yasal/sözleşmesel kapsam (repo OS)",
        "aciklama": "Bu depo kişisel veri işlemcisi iddiası yok; lisans MIT vendored + holding içeriği. KVKK/GDPR pack ayrı tur.",
        "nist_csf": ["Govern"],
        "n80053": ["PL-1", "AU-1"],
        "iso": ["A.5.31", "A.5.34"],
        "cis": ["CIS-3"],
        "owasp": [],
        "dogrulama": "SECURITY.md raporlama yolu; LICENSE; COMPLIANCE SoA N/A gerekçeleri.",
        "gerekce": "Kapsam dışı iddia denetimde şişirme ve sahte sertifika riskini önler.",
    },
]


def render_control(c: dict) -> str:
    y = [
        f"id: {c['id']}",
        f"ad: {c['ad']}",
        f"açıklama: {c['aciklama']}",
        f"NIST_CSF: {c['nist_csf']}",
        f"800-53: {c['n80053']}",
        f"ISO27001: {c['iso']}",
        f"CIS: {c['cis']}",
        f"OWASP: {c['owasp']}",
        "status: assess",
        "mode: ASSESS-ONLY",
        f"doğrulama_yöntemi: {c['dogrulama']}",
        f"savunma_gerekçesi: {c['gerekce']}",
    ]
    return "\n".join(
        [
            f"# {c['id']} — {c['ad']}",
            "",
            "```yaml",
            *y,
            "```",
            "",
            "## Açıklama",
            c["aciklama"],
            "",
            "## Doğrulama (ASSESS-ONLY)",
            f"- {c['dogrulama']}",
            "",
            "## Savunma gerekçesi",
            c["gerekce"],
            "",
            GUARD,
            "",
        ]
    )


def write_extra_controls() -> list[str]:
    ids = []
    for c in EXTRA_CONTROLS:
        d = ROOT / c["folder"]
        d.mkdir(parents=True, exist_ok=True)
        path = d / f"{c['id']}.md"
        path.write_text(render_control(c), encoding="utf-8")
        ids.append(c["id"])
    return ids


def parse_ctrl_iso(text: str) -> list[str]:
    m = re.search(r"^ISO27001:\s*\[([^\]]*)\]", text, re.M)
    if not m:
        return []
    return re.findall(r"A\.\d+\.\d+", m.group(1))


def collect_catalog_iso() -> dict[str, list[str]]:
    idx: dict[str, list[str]] = defaultdict(list)
    for folder in (
        "LAYERS",
        "FIREWALLS",
        "ENCRYPTION",
        "CHANGE",
        "TRANSPARENT_CODE",
        "CONDITIONAL",
    ):
        d = ROOT / folder
        if not d.is_dir():
            continue
        for path in sorted(d.glob("CTRL-*.md")):
            ids = parse_ctrl_iso(path.read_text(encoding="utf-8", errors="replace"))
            cid = path.stem
            for iso in ids:
                if cid not in idx[iso]:
                    idx[iso].append(cid)
    return idx


def applicability(iso_id: str, mapped: list[str]) -> tuple[str, str, str]:
    """Return (applicable, status, note)."""
    if mapped:
        return ("Evet", "ASSESS / kısmi", "Katalog CTRL eşlemesi var; implement/verify değil.")
    if iso_id in N_A_PHYSICAL:
        return (
            "Hayır (N/A)",
            "N/A",
            "Fiziksel tesis bu repo OS kapsamı dışında; endpoint → A.8.1 ASSESS ayrı.",
        )
    if iso_id in N_A_HR:
        return (
            "Hayır (N/A)",
            "N/A",
            "İK/işe alım süreci holding HR’da; bu depo otomasyon OS’i.",
        )
    if iso_id == "A.8.7":
        return (
            "Kısmi",
            "GAP",
            "Malware runtime yok (stdlib script); runner/OS antimalware holding IT ASSESS.",
        )
    if iso_id in {"A.6.3", "A.6.6", "A.6.7", "A.6.8"}:
        return (
            "Kısmi",
            "GAP",
            "Awareness analogu ethics-guardrail/AGENTS.md; resmi eğitim kaydı yok.",
        )
    return ("Evet (hedef)", "GAP", "Kapsamda; katalog CTRL henüz yok — sonraki /kontrol-uret.")


def write_soa(idx: dict[str, list[str]]) -> dict[str, int]:
    counts = {"assess": 0, "gap": 0, "na": 0}
    lines = [
        "# ISO/IEC 27001:2022 — Statement of Applicability (iskelet)",
        "",
        BANNER,
        "",
        "**MODE:** `ASSESS-ONLY` · **ts_utc:** 2026-11-03T11:50:00Z · **tz:** Europe/Istanbul",
        "",
        "Bu SoA **sertifika iddiası değildir**. Annex A 93 kontrol için uygulanabilirlik + mevcut `CTRL-*` eşlemesi.",
        "ISO standart gövde metni kopyalanmaz (üyelik/telif). Kısa başlık + ID + kanıt yolu.",
        "Kaynak teyidi: `SECURITY_RESEARCH/standards-currency.md` · CSF/800-53 çapraz: `SECURITY_MATRIX/matrix.md`.",
        "",
        "## Kapsam (Holding Security OS)",
        "- **İçinde:** `scripts/` stdlib, GitHub Actions, doküman OS, agent/hooks, LLM istemcileri (anahtar `${VAR}`).",
        "- **Dışında:** fiziksel ofis, İK tarama, müşteri üretim SaaS, Canva live API (BRIEF-ONLY).",
        "- **Durum sözlüğü:** `ASSESS / kısmi` = doküman+scanner; `GAP` = uygulanır ama kart/kanıt yok; `N/A` = kapsam dışı.",
        "",
        "## Özet",
        "",
        "| Tema | Annex | SoA satırı |",
        "|------|-------|------------|",
        "| Organizational | A.5 | 37 |",
        "| People | A.6 | 8 |",
        "| Physical | A.7 | 14 (çoğu N/A) |",
        "| Technological | A.8 | 34 |",
        "| **Toplam** | | **93** |",
        "",
        "## SoA tablosu",
        "",
        "| ID | Tema | Kısa başlık | Uygulanır | Durum | CTRL katalog |",
        "|----|------|-------------|-----------|-------|--------------|",
    ]
    for iso_id, theme, title in ISO_ANNEX:
        mapped = idx.get(iso_id, [])
        appl, status, _note = applicability(iso_id, mapped)
        if status.startswith("ASSESS"):
            counts["assess"] += 1
        elif status == "N/A":
            counts["na"] += 1
        else:
            counts["gap"] += 1
        ctrl = ", ".join(f"`{x}`" for x in mapped) if mapped else "—"
        lines.append(
            f"| {iso_id} | {theme} | {title} | {appl} | {status} | {ctrl} |"
        )
    lines.extend(
        [
            "",
            f"**Sayaç (dürüst):** ASSESS/kısmi={counts['assess']} · GAP={counts['gap']} · N/A={counts['na']} · toplam=93",
            "",
            "## Kanıt indeksi (minimum)",
            "| Kanıt | Yol |",
            "|-------|-----|",
            "| Envanter | `SECURITY_CONTEXT/inventory.md` |",
            "| Trust boundary | `SECURITY_CONTEXT/attack-surface.md` / `trust-boundaries.md` |",
            "| Secret hygiene | `docs/SECRETS-DRYRUN-MATRISI.md` · `scripts/secret_scan.py` |",
            "| Ethics | `scripts/ethics_check.py` |",
            "| Matrix crosswalk | `SECURITY_MATRIX/matrix.md` |",
            "| IR stub | `.cursor/skills/incident-response/` |",
            "| Bu SoA üretici | `python3 scripts/giga_security_faz6_soa.py` |",
            "",
            "## Bilinçli boşluklar (sonraki DEVAM)",
            "- NIST CSF / CIS IG1 / SOC2 CC pack: ID listesi seed var, SoA yok.",
            "- 600 kontrol hedefi: katalog hâlâ 88/600 bandı (sample hariç sayım script çıktısı).",
            "- Bağımsız iç denetim (A.5.35) insan kapısı.",
            "",
            GUARD,
            "",
        ]
    )
    out = ROOT / "COMPLIANCE" / "ISO27001-2022-SOA.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    return counts


def write_pack(counts: dict[str, int], extra_ids: list[str], catalog_n: int) -> None:
    body = f"""# ISO/IEC 27001:2022 — uyumluluk paketi (ASSESS-ONLY)

{BANNER}

**Komut:** `/compliance-paket` · **üretici:** `python3 scripts/giga_security_faz6_soa.py`

## Ne bu?
Holding Security OS için **SoA iskeleti**. Sertifika, denetçi imzası veya “27001 uyumluyuz” iddiası **yok**.

## Teslim
| Dosya | Rol |
|-------|-----|
| `COMPLIANCE/ISO27001-2022-SOA.md` | 93 satır uygulanabilirlik + CTRL map |
| `COMPLIANCE/gap-evidence.md` | GAP/N/A gerekçeleri |
| `SECURITY_MATRIX/coverage.md` | Katalog vs matris 120 satır dürüst fark |

## Sayaç
- SoA: ASSESS/kısmi={counts['assess']} · GAP={counts['gap']} · N/A={counts['na']}
- Bu tur ek CTRL: {', '.join(f'`{i}`' for i in extra_ids)}
- Katalog dosya sayısı (CTRL-*.md): {catalog_n}

## Diğer çerçeveler
- NIST CSF 2.0 / 800-53 / CIS / ASVS: kolonlar `SECURITY_MATRIX/matrix.md` (120 satır tranche).
- SOC2 CC: **backlog** (compliance-mapper TODO).

{GUARD}
"""
    (ROOT / "COMPLIANCE" / "ISO27001-2022-pack.md").write_text(body, encoding="utf-8")


def write_gap(idx: dict[str, list[str]]) -> None:
    rows = [
        "# COMPLIANCE — GAP / N/A kanıt listesi",
        "",
        BANNER,
        "",
        "SoA ile üretilir. Secret yok. Exploit yok.",
        "",
        "| ID | Durum | Gerekçe |",
        "|----|-------|---------|",
    ]
    for iso_id, _theme, _title in ISO_ANNEX:
        mapped = idx.get(iso_id, [])
        _appl, status, note = applicability(iso_id, mapped)
        if status.startswith("ASSESS"):
            continue
        rows.append(f"| {iso_id} | {status} | {note} |")
    rows.extend(["", GUARD, ""])
    (ROOT / "COMPLIANCE" / "gap-evidence.md").write_text("\n".join(rows), encoding="utf-8")


def catalog_count() -> int:
    n = 0
    for folder in (
        "LAYERS",
        "FIREWALLS",
        "ENCRYPTION",
        "CHANGE",
        "TRANSPARENT_CODE",
        "CONDITIONAL",
    ):
        n += len(list((ROOT / folder).glob("CTRL-*.md")))
    return n


def main() -> int:
    extra = write_extra_controls()
    idx = collect_catalog_iso()
    counts = write_soa(idx)
    n = catalog_count()
    write_pack(counts, extra, n)
    write_gap(idx)
    print(
        f"OK soa assess={counts['assess']} gap={counts['gap']} na={counts['na']} "
        f"catalogs={n} extra={len(extra)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
