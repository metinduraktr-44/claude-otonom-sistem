#!/usr/bin/env python3
"""Idempotent GIGA Security OS bootstrap — creates skeleton + deep samples.
Defense-only. No secrets. Run from repo root: python3 scripts/giga_security_bootstrap.py
"""
from __future__ import annotations

import os
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TS = "2026-08-27T12:40:00Z"

GUARDRAIL = (
    "DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. "
    "No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. "
    "ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only."
)

SKILLS = [
    "layers-engine",
    "firewall-engine",
    "encryption-engine",
    "change-protocol-engine",
    "transparent-code-engine",
    "conditional-policy-engine",
    "security-expert-engine",  # creative expert-engine preserved; security twin
    "threat-modeling",
    "compliance-mapper",
    "incident-response",
    "secret-hygiene",
    "zero-trust-architect",
    "crypto-agility",
    "sbom-provenance",
    "iam-hardening",
    "cloud-security-posture",
    "detection-engineering",
    "vulnerability-management",
    "privacy-engineering",
    "security-qa",
]

# High-priority engines get one deep reference sample
DEEP_REFS = {
    "threat-modeling": (
        "stride-dread.md",
        "# STRIDE / DREAD (defense)\n\n"
        "Use STRIDE for design review; DREAD for prioritization of *findings* "
        "already in scope for remediation — not for attack recipes.\n\n"
        "| STRIDE | Control focus |\n|--------|---------------|\n"
        "| Spoofing | AuthN, MFA, mTLS |\n"
        "| Tampering | Integrity, signing, WORM logs |\n"
        "| Repudiation | Audit trails, non-repudiation |\n"
        "| Info disclosure | Encryption, least privilege |\n"
        "| DoS | Rate limits, capacity, circuit breakers |\n"
        "| Elevation | RBAC/ABAC, privilege boundaries |\n\n"
        "Map findings → NIST CSF / D3FEND. MODE=ASSESS-ONLY by default.\n"
        f"\n> {GUARDRAIL}\n",
    ),
    "compliance-mapper": (
        "nist-csf-control-fields.md",
        "# NIST CSF control field contract\n\n"
        "Every control card under `LAYERS/` or `SECURITY_MATRIX/` MUST include:\n\n"
        "```yaml\n"
        "id: CTRL-XXX\n"
        "title: <short>\n"
        "nist_csf: [Identify|Protect|Detect|Respond|Recover]\n"
        "nist_800_53: []  # optional\n"
        "iso27001: []     # optional\n"
        "d3fend: []       # defensive techniques only\n"
        "attack_detect: []  # ATT&CK IDs for DETECTION mapping only\n"
        "owner: <role>\n"
        "status: planned|assess|implement|verify\n"
        "evidence: []\n"
        "```\n\n"
        f"> {GUARDRAIL}\n",
    ),
    "secret-hygiene": (
        "patterns.md",
        "# Secret hygiene patterns\n\n"
        "- Never commit real or fake-looking secrets.\n"
        "- Placeholders only: `${VAR}`, `vault://path`, `op://vault/item`, `<REDACTED>`.\n"
        "- Scanner: `python3 scripts/secret_scan.py`\n"
        "- AWS-like key pattern `AKIA[0-9A-Z]{16}` → flag + redact in reports; do not store match.\n"
        "- Pre-commit / afterFileEdit hook fail-open if script missing; intent failClosed in IDE.\n\n"
        f"> {GUARDRAIL}\n",
    ),
    "incident-response": (
        "playbook-skeleton.md",
        "# IR playbook skeleton (defense)\n\n"
        "1. Detect → triage severity\n"
        "2. Contain (isolate, revoke tokens via vault)\n"
        "3. Eradicate (patch, rotate `${SECRETS}`)\n"
        "4. Recover + lessons → `REPORTS/` + `ARCHIVE/`\n"
        "5. Never include exploit steps; point to vendor advisories.\n\n"
        f"> {GUARDRAIL}\n",
    ),
    "layers-engine": (
        "defense-in-depth.md",
        "# Defense-in-depth layers\n\n"
        "L0 Policy · L1 Identity · L2 Network · L3 Host · L4 App · L5 Data · L6 Detect/Respond\n\n"
        "Each layer: objective, controls, gaps, NIST map. Fill under `LAYERS/`.\n\n"
        f"> {GUARDRAIL}\n",
    ),
    "detection-engineering": (
        "sigma-d3fend.md",
        "# Detection engineering notes\n\n"
        "Prefer Sigma/YARA for *detection* content. Map to D3FEND.\n"
        "ATT&CK technique IDs OK only as detection coverage labels.\n"
        "Do not ship offensive payloads. MODE=ASSESS-ONLY default.\n\n"
        f"> {GUARDRAIL}\n",
    ),
}


def write(path: Path, content: str, *, force: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return
    path.write_text(content if content.endswith("\n") else content + "\n", encoding="utf-8")


def ensure_readme(path: Path, title: str, body: str = "") -> None:
    write(
        path / "README.md",
        f"# {title}\n\n{body}\n\nMODE=`ASSESS-ONLY` default.\n\n> {GUARDRAIL}\n",
    )


def skill_md(name: str) -> str:
    desc = {
        "layers-engine": "Defense-in-depth layer cards + NIST mapping",
        "firewall-engine": "Network/policy firewall design (hardening, not bypass)",
        "encryption-engine": "Crypto at rest/in transit; agility; no break-crypto",
        "change-protocol-engine": "Secure change / CAB / rollback protocols",
        "transparent-code-engine": "Transparent, auditable code & SBOM-friendly diffs",
        "conditional-policy-engine": "Conditional access / policy-as-code (deny-by-default)",
        "security-expert-engine": "Security EXPERTS seed cards; no fabricated rankings",
        "threat-modeling": "STRIDE/DREAD threat modeling for remediation",
        "compliance-mapper": "Map controls to NIST/ISO/SOC2/D3FEND",
        "incident-response": "IR playbooks — contain/eradicate/recover",
        "secret-hygiene": "Secret detection hygiene; placeholders only",
        "zero-trust-architect": "Zero Trust architecture patterns",
        "crypto-agility": "Algorithm agility and migration plans",
        "sbom-provenance": "SBOM, provenance, supply-chain attestations",
        "iam-hardening": "IAM least-privilege hardening",
        "cloud-security-posture": "CSPM posture assessment (read/assess)",
        "detection-engineering": "Detection rules ↔ D3FEND/ATT&CK detect map",
        "vulnerability-management": "Vuln triage, SLAs, patch evidence",
        "privacy-engineering": "Privacy-by-design / DPIA stubs",
        "security-qa": "Security QA checklists for ASSESS-ONLY reviews",
    }.get(name, f"Security skill {name}")
    refs = "references/TODO.md"
    extra = ""
    if name in DEEP_REFS:
        extra = f"\nDeep sample: `references/{DEEP_REFS[name][0]}`\n"
    return (
        f"---\nname: {name}\ndescription: {desc}. {GUARDRAIL[:80]}…\n---\n\n"
        f"# {name}\n\n"
        f"{desc}.\n\n"
        f"**Mode:** `ASSESS-ONLY` unless user sets `MODE=IMPLEMENT` with explicit scope.\n\n"
        f"**Guardrail:** {GUARDRAIL}\n\n"
        f"## Expansion (FAZ 3)\n"
        f"Full ~20k char depth is **continuous expansion**, not this PR. "
        f"Fill `{refs}` stubs iteratively; keep PRs reviewable.\n"
        f"{extra}\n"
        f"## Inputs / Outputs\n"
        f"- In: SECURITY_CONTEXT/, SECURITY_MATRIX/, TASKS/\n"
        f"- Out: control cards, assessments, REPORTS/ (no secrets)\n"
    )


def main() -> None:
    os.chdir(ROOT)

    # --- directories ---
    dirs = [
        "SECURITY_CONTEXT",
        "SECURITY_RESEARCH",
        "LAYERS",
        "FIREWALLS",
        "ENCRYPTION",
        "CHANGE",
        "TRANSPARENT_CODE",
        "CONDITIONAL",
        "SECURITY_MATRIX",
        "IMPLEMENTATION",
        "ASSESSMENTS",
        "COMPLIANCE",
        "CALENDAR",
        "MEMORY",
        "REPORTS",
        "SECURITY",
        "ORG/ROLES",
        "ARCHIVE",
        "QA",
        "TASKS",
        "EXPERTS",
        "tools/security-scanners",
        ".cursor/hooks",
        ".cursor/plans",
        ".cursor/agents",
        ".cursor/commands",
        ".cursor/rules",
        ".cursor/skills",
    ]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)

    ensure_readme(Path("SECURITY_CONTEXT"), "SECURITY_CONTEXT", "Org threat profile, assets, data classes, trust boundaries.")
    ensure_readme(Path("SECURITY_RESEARCH"), "SECURITY_RESEARCH", "Sourced research notes only (URLs + archive ts).")
    ensure_readme(Path("LAYERS"), "LAYERS", "Defense-in-depth layer cards.")
    ensure_readme(Path("FIREWALLS"), "FIREWALLS", "Firewall / network policy designs (allowlists).")
    ensure_readme(Path("ENCRYPTION"), "ENCRYPTION", "Encryption standards, key mgmt via vault:// refs.")
    ensure_readme(Path("CHANGE"), "CHANGE", "Secure change protocol artifacts.")
    ensure_readme(Path("TRANSPARENT_CODE"), "TRANSPARENT_CODE", "Auditability / review contracts.")
    ensure_readme(Path("CONDITIONAL"), "CONDITIONAL", "Conditional access policy drafts.")
    ensure_readme(Path("SECURITY_MATRIX"), "SECURITY_MATRIX", "Control matrix + gap analysis.")
    ensure_readme(Path("IMPLEMENTATION"), "IMPLEMENTATION", "Hardening implementation notes (defense).")
    ensure_readme(Path("ASSESSMENTS"), "ASSESSMENTS", "ASSESS-ONLY findings.")
    ensure_readme(Path("COMPLIANCE"), "COMPLIANCE", "Compliance packages (NIST/ISO/SOC2 stubs).")
    ensure_readme(Path("CALENDAR"), "CALENDAR", "Monthly security review calendar.")
    ensure_readme(Path("MEMORY"), "MEMORY", "Durable lessons (no secrets).")
    ensure_readme(Path("REPORTS"), "REPORTS", "Phase / compliance / IR reports.")
    ensure_readme(Path("SECURITY"), "SECURITY", "Security OS hub. State: `SECURITY/STATE.md`.")
    ensure_readme(Path("ORG/ROLES"), "ORG/ROLES", "Security RACI / role cards.")

    write(
        Path("SECURITY/STATE.md"),
        textwrap.dedent(
            f"""\
            # SECURITY STATE

            ```yaml
            faz: 0
            mode: ASSESS-ONLY
            son_komut: bootstrap
            ts: {TS}
            ethics: GECTI
            secret_scan: pending
            notlar: "GIGA Security bootstrap. /baslat-security ile doğrula."
            ```
            """
        ),
        force=True,
    )

    # Sample NIST control template
    write(
        Path("LAYERS/CTRL-SAMPLE-ACCESS.md"),
        textwrap.dedent(
            f"""\
            # CTRL-SAMPLE-ACCESS — Least privilege access

            ```yaml
            id: CTRL-SAMPLE-ACCESS
            title: Least privilege access
            nist_csf: [Protect]
            nist_800_53: [AC-2, AC-3, AC-6]
            iso27001: [A.5.15, A.8.2]
            d3fend: [D3-LRA, D3-UAP]
            attack_detect: [T1078]  # detection coverage label only
            owner: IAM Lead
            status: assess
            evidence: []
            secrets: []  # use ${{VAR}} / vault:// only if referencing
            ```

            ## Objective
            Enforce least privilege for human and workload identities.

            ## Assessment checklist (ASSESS-ONLY)
            - [ ] Inventory of roles documented
            - [ ] Break-glass procedure exists (vault://)
            - [ ] MFA required for privileged paths
            - [ ] Periodic access review scheduled (`CALENDAR/`)

            > {GUARDRAIL}
            """
        ),
        force=True,
    )

    write(
        Path("SECURITY_MATRIX/GAP-TEMPLATE.md"),
        textwrap.dedent(
            f"""\
            # Gap analysis template

            | Control | Framework | Current | Target | Gap | Owner | Due |
            |---------|-----------|---------|--------|-----|-------|-----|
            | CTRL-… | NIST CSF Protect | assess | verify | TBD | … | … |

            MODE=`ASSESS-ONLY` until explicit IMPLEMENT scope.

            > {GUARDRAIL}
            """
        ),
        force=True,
    )

    # EXPERTS security seed (separate file; creative SEED.md preserved)
    write(
        Path("EXPERTS/_SEED.md"),
        textwrap.dedent(
            f"""\
            # EXPERTS — Security seed (kaynaklı; sıralama uydurma YASAK)

            > Domain: security / cryptography / IR / privacy.
            > `status` + `sources` zorunlu. Ölenler `deceased`. Ranking claim yok.

            | name | domain | status | sources | archived_at |
            |------|--------|--------|---------|-------------|
            | Bruce Schneier | cryptography/policy | living | https://www.schneier.com/ | {TS} |
            | Dan Kaminsky | DNS/security research | deceased | https://en.wikipedia.org/wiki/Dan_Kaminsky | {TS} |
            | Katie Moussouris | vuln disclosure | living | https://en.wikipedia.org/wiki/Katie_Moussouris | {TS} |
            | Tanya Janca | AppSec | living | https://shehackspurple.dev/ | {TS} |
            | Troy Hunt | breach awareness | living | https://www.troyhunt.com/ | {TS} |
            | Adam Shostack | threat modeling | living | https://shostack.org/ | {TS} |
            | Kelly Shortridge | resilience/security | living | https://kellyshortridge.com/ | {TS} |
            | Parisa Tabriz | browser security | living | https://en.wikipedia.org/wiki/Parisa_Tabriz | {TS} |
            | Eva Galperin | privacy/security | living | https://en.wikipedia.org/wiki/Eva_Galperin | {TS} |
            | Wendy Nather | CISO/advisory | living | https://www.linkedin.com/in/wendynather/ | {TS} |
            | Matt Blaze | crypto/systems | living | https://www.mattblaze.org/ | {TS} |
            | Gene Spafford | infosec academia | living | https://spaf.cerias.purdue.edu/ | {TS} |
            | Tarah Wheeler | cyber policy | living | https://tarah.org/ | {TS} |
            | Chris Wysopal | AppSec | living | https://en.wikipedia.org/wiki/Chris_Wysopal | {TS} |
            | Whitfield Diffie | public-key crypto | living | https://en.wikipedia.org/wiki/Whitfield_Diffie | {TS} |

            Historical note: **Dan Kaminsky** — deceased; cite historically; do not invent quotes.
            """
        ),
        force=True,
    )

    # Skills
    for name in SKILLS:
        base = Path(".cursor/skills") / name
        write(base / "SKILL.md", skill_md(name), force=True)
        write(
            base / "references" / "TODO.md",
            f"# TODO — {name} expansion (FAZ 3)\n\n"
            f"- [ ] Expand to depth (~sections for patterns, checklists, anti-patterns)\n"
            f"- [ ] Add framework maps (NIST/ISO/D3FEND)\n"
            f"- [ ] Keep SIGNAL > LENGTH; no filler to hit 20k\n"
            f"- [ ] Full 20k/skill = continuous FAZ 3, not one-shot\n\n"
            f"> {GUARDRAIL}\n",
            force=True,
        )
        if name in DEEP_REFS:
            fn, body = DEEP_REFS[name]
            write(base / "references" / fn, body, force=True)

    # Rules (non-colliding IDs)
    write(
        Path(".cursor/rules/00-security-core.mdc"),
        textwrap.dedent(
            f"""\
            ---
            description: Security OS core — ASSESS-ONLY default, defense-only, phased files
            alwaysApply: true
            ---

            # Security Core (GIGA)

            Orchestrate modular **AI Security Architecture & Governance OS**. SIGNAL > LENGTH.
            Default **MODE=ASSESS-ONLY**. IMPLEMENT only on explicit user scope.

            {GUARDRAIL}

            Preserve Holding HQ + Creative Agency (Canva) sections. Security paths:
            SECURITY_*/LAYERS/FIREWALLS/… + `.cursor/skills/*` security engines.

            🚩 ≥900B single prompt = RED → multi-file FAZ 0–8.
            Commands: baslat-security, kontrol-uret, gap-analizi, compliance-paket, etik-denetim.
            """
        ),
        force=True,
    )
    write(
        Path(".cursor/rules/05-ethics-guardrail.mdc"),
        textwrap.dedent(
            f"""\
            ---
            description: Ethics guardrail — refuse offensive cyber / dual-use weaponization
            alwaysApply: true
            ---

            # Ethics Guardrail

            Refuse: exploits, phishing kits, malware, C2, ransomware, credential stuffing,
            auth bypass how-to, weaponized PoCs. ATT&CK = detection/D3FEND map only.

            On refuse: short Turkish+EN reason; offer defense alternative (harden/detect/IR).

            {GUARDRAIL}
            """
        ),
        force=True,
    )
    write(
        Path(".cursor/rules/10-secret-hygiene.mdc"),
        textwrap.dedent(
            """\
            ---
            description: Secret hygiene — placeholders only; never real or fake-looking secrets
            alwaysApply: true
            ---

            # Secret Hygiene

            Allowed placeholders only: `${VAR}`, `vault://…`, `op://…`, `<REDACTED>`.
            Never invent AKIA…/Bearer/JWT samples. Scan: `python3 scripts/secret_scan.py`.
            """
        ),
        force=True,
    )
    write(
        Path(".cursor/rules/20-control-mapping.mdc"),
        textwrap.dedent(
            """\
            ---
            description: Control cards must carry NIST CSF (+ optional 800-53/ISO/D3FEND) fields
            alwaysApply: true
            ---

            # Control Mapping

            New controls → template `LAYERS/CTRL-SAMPLE-ACCESS.md` fields.
            ATT&CK IDs only under `attack_detect` (detection coverage), never as attack steps.
            """
        ),
        force=True,
    )
    write(
        Path(".cursor/rules/31-security-file-structure.mdc"),
        textwrap.dedent(
            """\
            ---
            description: Security OS directory contract (additive to creative 30-file-structure)
            alwaysApply: true
            ---

            # Security File Structure

            | Dir | Role |
            |-----|------|
            | SECURITY_CONTEXT/ | Assets, trust boundaries |
            | SECURITY_RESEARCH/ | Sourced notes |
            | LAYERS/ FIREWALLS/ ENCRYPTION/ | Control domains |
            | CHANGE/ TRANSPARENT_CODE/ CONDITIONAL/ | Process engines |
            | SECURITY_MATRIX/ ASSESSMENTS/ COMPLIANCE/ | Gaps & packs |
            | IMPLEMENTATION/ REPORTS/ MEMORY/ CALENDAR/ | Exec + archive inputs |
            | SECURITY/STATE.md | Security faz/mode |
            | EXPERTS/_SEED.md | Security experts seed |
            | tools/security-scanners/ | Defense scanners only |

            Do not dump controls into repo root. Creative dirs (CONTEXT/, CANVA_OPS/) untouched.
            """
        ),
        force=True,
    )
    write(
        Path(".cursor/rules/40-secops.mdc"),
        textwrap.dedent(
            """\
            ---
            description: SecOps playbooks — IR, detection engineering, vuln mgmt (Agent Requested; no globs)
            ---

            # SecOps (on request)

            Load when user asks IR, detection, vuln triage, CSPM assess.
            Prefer skills: incident-response, detection-engineering, vulnerability-management,
            cloud-security-posture. Stay ASSESS-ONLY unless scoped. No attack tooling.
            """
        ),
        force=True,
    )

    # Commands (security-prefixed where shared names exist)
    cmds = {
        "baslat-security.md": (
            "Security OS bootstrap doğrula; SECURITY/STATE READY; MODE=ASSESS-ONLY",
            "# /baslat-security\n\n"
            "1. Doğrula: security rules/skills, SECURITY_*/LAYERS, scripts/secret_scan.py + ethics_check.py.\n"
            "2. `SECURITY/STATE.md`: faz=0, mode=ASSESS-ONLY.\n"
            "3. Çalıştır: `python3 scripts/secret_scan.py --self-test` · `ethics_check.py --self-test`.\n"
            "4. Çıktı: FAZ 0–8 tablosu + `/devam` veya `/gap-analizi`.\n",
        ),
        "kontrol-uret.md": (
            "Yeni kontrol kartı üret (NIST alanları zorunlu)",
            "# /kontrol-uret\n\n"
            "1. Şablon: `LAYERS/CTRL-SAMPLE-ACCESS.md`.\n"
            "2. Doldur: nist_csf, d3fend, attack_detect (detect-only).\n"
            "3. Secret yok. MODE=ASSESS-ONLY.\n",
        ),
        "gap-analizi.md": (
            "SECURITY_MATRIX gap analizi",
            "# /gap-analizi\n\n"
            "1. Oku SECURITY_MATRIX + LAYERS.\n"
            "2. `SECURITY_MATRIX/GAP-TEMPLATE.md` doldur.\n"
            "3. Öncelik: risk × impact; IMPLEMENT yoksa sadece assess.\n",
        ),
        "compliance-paket.md": (
            "Compliance paket stub (NIST/ISO/SOC2)",
            "# /compliance-paket\n\n"
            "1. Hedef çerçeve sor (NIST CSF varsayılan).\n"
            "2. `COMPLIANCE/{framework}/` paket iskeleti.\n"
            "3. Evidence placeholders; canlı Semgrep/Snyk iddiası credential yoksa YASAK.\n",
        ),
        "etik-denetim.md": (
            "Ethics + secret hygiene denetimi",
            "# /etik-denetim\n\n"
            "```bash\npython3 scripts/ethics_check.py\npython3 scripts/secret_scan.py\n```\n"
            "KALDI → düzelt; secrets REDACTED raporda saklanır, ham secret yazılmaz.\n",
        ),
    }
    for fn, (desc, body) in cmds.items():
        write(
            Path(".cursor/commands") / fn,
            f"---\ndescription: {desc}\n---\n\n{body}",
            force=True,
        )

    # Merge notes into shared commands (append section if missing)
    for shared, blurb in [
        (
            "devam.md",
            "\n## Security OS\n"
            "If `SECURITY/STATE.md` active: advance security faz per "
            "`.cursor/plans/security-master-plan.md`. Keep MODE=ASSESS-ONLY unless scoped.\n",
        ),
        (
            "resume.md",
            "\n## Security OS\n"
            "Also read `SECURITY/STATE.md` + last `REPORTS/` / `ARCHIVE/` security snapshot.\n",
        ),
        (
            "faz-raporu.md",
            "\n## Security OS\n"
            "Include FAZ 0–8 from `docs/IS-LISTESI-GIGA-SECURITY.md` + `SECURITY/STATE.md`.\n",
        ),
        (
            "aylik-dongu.md",
            "\n## Security experts\n"
            "Refresh `EXPERTS/_SEED.md` sources; mark deceased; no fabricated rankings.\n",
        ),
        (
            "uzman-guncelle.md",
            "\n## Security\n"
            "Update `EXPERTS/_SEED.md` (security) separately from creative `EXPERTS/SEED.md`.\n",
        ),
        (
            "arsivle.md",
            "\n## Security\n"
            "Snapshot SECURITY_MATRIX/REPORTS into `ARCHIVE/{YYYY-MM}/security/`.\n",
        ),
    ]:
        p = Path(".cursor/commands") / shared
        if p.exists():
            txt = p.read_text(encoding="utf-8")
            if "Security OS" not in txt and "## Security" not in txt:
                p.write_text(txt.rstrip() + "\n" + blurb, encoding="utf-8")

    # Agents
    for name, desc in [
        ("security-reviewer", "Read-only security architecture review (defense)"),
        ("compliance-auditor", "Read-only compliance mapping audit"),
        ("ethics-checker", "Read-only ethics / dual-use refusal audit"),
    ]:
        write(
            Path(".cursor/agents") / f"{name}.md",
            f"---\nname: {name}\ndescription: {desc}\nreadonly: true\n---\n\n"
            f"# {name}\n\n{desc}.\n\n{GUARDRAIL}\n\n"
            f"Output: findings table + severity + remediation *direction* (no exploit steps).\n",
            force=True,
        )

    # Plan
    write(
        Path(".cursor/plans/security-master-plan.md"),
        textwrap.dedent(
            f"""\
            # Security Master Plan — FAZ 0–8

            Default **MODE=ASSESS-ONLY**.

            | Faz | Ad | Çıktı |
            |-----|-----|-------|
            | 0 | BOOTSTRAP | rules/commands/skills/hooks + SECURITY/STATE |
            | 1 | CONTEXT | SECURITY_CONTEXT/ assets & boundaries |
            | 2 | RESEARCH | SECURITY_RESEARCH/ sourced |
            | 3 | ORG+EXPERTS | ORG/ROLES + EXPERTS/_SEED |
            | 4 | ENGINES | layers/firewall/encryption/… cards |
            | 5 | MATRIX | SECURITY_MATRIX + gap |
            | 6 | COMPLIANCE | COMPLIANCE/ paket |
            | 7 | QA+IR | QA + incident-response stubs |
            | 8 | ARCHIVE | ARCHIVE + CALENDAR monthly |

            FAZ 3 continuous: deepen skill `references/` (not one-shot 20k×20).

            > {GUARDRAIL}
            """
        ),
        force=True,
    )

    # Hooks merge
    hooks = Path(".cursor/hooks.json")
    hooks.write_text(
        textwrap.dedent(
            """\
            {
              "version": 1,
              "hooks": {
                "afterFileEdit": [
                  {
                    "command": "python3 scripts/spec_validate.py --hook",
                    "description": "Canva/spec validate (fail-open). Creative Agency."
                  },
                  {
                    "command": "bash .cursor/hooks/secret-scan.sh",
                    "description": "Secret hygiene scan (fail-open if script missing; intent failClosed in IDE)."
                  },
                  {
                    "command": "bash .cursor/hooks/ethics-check.sh",
                    "description": "Ethics pattern check (fail-open if missing)."
                  }
                ],
                "beforeShellExecution": [
                  {
                    "command": "bash .cursor/hooks/dangerous-shell-block.sh",
                    "description": "Block clearly dangerous shell patterns; fail-open on script errors."
                  }
                ]
              }
            }
            """
        ),
        encoding="utf-8",
    )

    write(
        Path(".cursor/hooks/secret-scan.sh"),
        "#!/usr/bin/env bash\n"
        "# fail-open wrapper — missing script must not break CI/agents\n"
        "set +e\n"
        "if [[ -f scripts/secret_scan.py ]]; then\n"
        "  python3 scripts/secret_scan.py --hook \"$@\" || true\n"
        "fi\n"
        "exit 0\n",
        force=True,
    )
    write(
        Path(".cursor/hooks/ethics-check.sh"),
        "#!/usr/bin/env bash\n"
        "set +e\n"
        "if [[ -f scripts/ethics_check.py ]]; then\n"
        "  python3 scripts/ethics_check.py --hook \"$@\" || true\n"
        "fi\n"
        "exit 0\n",
        force=True,
    )
    write(
        Path(".cursor/hooks/dangerous-shell-block.sh"),
        "#!/usr/bin/env bash\n"
        "# Intent: failClosed on dangerous patterns when Cursor provides command via stdin/env.\n"
        "# Missing input → fail-open (exit 0) so CI/agents are not bricked.\n"
        "set +e\n"
        "CMD=\"${CURSOR_SHELL_COMMAND:-${1:-}}\"\n"
        "if [[ -z \"$CMD\" ]] && [[ ! -t 0 ]]; then\n"
        "  CMD=$(cat 2>/dev/null || true)\n"
        "fi\n"
        "if [[ -z \"$CMD\" ]]; then exit 0; fi\n"
        "if echo \"$CMD\" | grep -Eiq "
        "'rm[[:space:]]+-rf[[:space:]]+/|"
        "curl[^\\n]*\\|[[:space:]]*sh|"
        "wget[^\\n]*\\|[[:space:]]*sh|"
        "base64[[:space:]]+-d[^\\n]*\\|[[:space:]]*sh|"
        "mkfs\\.|dd[[:space:]]+if=.*of=/dev/'; then\n"
        "  echo \"[dangerous-shell-block] RED: refused dangerous pattern\" >&2\n"
        "  exit 2\n"
        "fi\n"
        "exit 0\n",
        force=True,
    )

    # MCP merge — keep canva; add security stubs OFF by default (commented in README)
    write(
        Path(".cursor/mcp.json"),
        textwrap.dedent(
            """\
            {
              "mcpServers": {
                "canva": {
                  "url": "https://mcp.canva.com/mcp",
                  "description": "Canva remote MCP — OAuth via Cursor Settings. Without auth: BRIEF-ONLY."
                }
              },
              "_securityStubsDisabledByDefault": {
                "comment": "User enable only. Placeholders ${VAR} — no real secrets. Do not claim live scanners without credentials.",
                "semgrep": {
                  "command": "npx",
                  "args": ["-y", "semgrep", "mcp"],
                  "env": { "SEMGREP_APP_TOKEN": "${SEMGREP_APP_TOKEN}" },
                  "disabled": true
                },
                "snyk": {
                  "command": "npx",
                  "args": ["-y", "snyk-mcp"],
                  "env": { "SNYK_TOKEN": "${SNYK_TOKEN}" },
                  "disabled": true
                }
              }
            }
            """
        ),
        force=True,
    )

    # tools/security-scanners
    write(
        Path("tools/security-scanners/README.md"),
        textwrap.dedent(
            f"""\
            # tools/security-scanners — defense only

            Wrappers around repo `scripts/secret_scan.py` + `scripts/ethics_check.py`.
            **No attack tools.** Optional Semgrep/Snyk require user credentials — do not claim live without them.

            ```bash
            python3 tools/security-scanners/run_secret_scan.py
            python3 tools/security-scanners/run_ethics_check.py
            ```

            > {GUARDRAIL}
            """
        ),
        force=True,
    )
    write(
        Path("tools/security-scanners/run_secret_scan.py"),
        "#!/usr/bin/env python3\n"
        "import runpy, sys\n"
        "from pathlib import Path\n"
        "sys.argv = [\"secret_scan.py\"] + sys.argv[1:]\n"
        "runpy.run_path(str(Path(__file__).resolve().parents[2] / \"scripts\" / \"secret_scan.py\"), run_name=\"__main__\")\n",
        force=True,
    )
    write(
        Path("tools/security-scanners/run_ethics_check.py"),
        "#!/usr/bin/env python3\n"
        "import runpy, sys\n"
        "from pathlib import Path\n"
        "sys.argv = [\"ethics_check.py\"] + sys.argv[1:]\n"
        "runpy.run_path(str(Path(__file__).resolve().parents[2] / \"scripts\" / \"ethics_check.py\"), run_name=\"__main__\")\n",
        force=True,
    )

    print("BOOTSTRAP: OK")


if __name__ == "__main__":
    main()
