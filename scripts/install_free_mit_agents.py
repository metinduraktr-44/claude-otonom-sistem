#!/usr/bin/env python3
"""MIT ücretsiz Status Agents paketi — katalog/ → .claude/katalog-mit/

Kaynak: davila7/claude-code-templates (katalog/LICENSE-UPSTREAM, MIT).
Amaç: ücretli API anahtarı olmadan Claude Code/Cursor'un kullanacağı
ürün-ilgili ajanları .claude altına "işe almak" (kopya + atıf + manifest).

Kural 2 (CILT): oto-vendorlama yok — bu script yerel/CI'da açıkça çalıştırılır;
katalog içeriğini upstream'den çekmez, yalnızca mevcut MIT kopyadan seçer.

Ücretsiz Nightly: LLM anahtarı yokken scripts/nightly.sh zaten damga+validate
modunda çalışır. Bu paket ajan tanımlarını hazır tutar; kredi harcamaz.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KAT = ROOT / "katalog" / "agents"
OUT = ROOT / ".claude" / "katalog-mit"
MANIFEST = ROOT / "data" / "mit_free_agents_manifest.json"
LICENSE = ROOT / "katalog" / "LICENSE-UPSTREAM"

# Ürün-odaklı kürasyon (holding HQ + araştırma + otomasyon + güvenlik).
# Tam katalog katalog/ altında kalır; burası "Status Agents" ücretsiz çekirdek.
CURATED: list[tuple[str, str]] = [
    # Deep research swarm
    ("deep-research-team", "research-orchestrator"),
    ("deep-research-team", "research-coordinator"),
    ("deep-research-team", "research-analyst"),
    ("deep-research-team", "research-synthesizer"),
    ("deep-research-team", "fact-checker"),
    ("deep-research-team", "search-specialist"),
    ("deep-research-team", "competitive-intelligence-analyst"),
    ("deep-research-team", "report-generator"),
    # AI / prompt
    ("ai-specialists", "prompt-engineer"),
    ("ai-specialists", "llm-architect"),
    ("ai-specialists", "task-decomposition-expert"),
    ("ai-specialists", "ai-ethics-advisor"),
    # Expert advisors / orchestration
    ("expert-advisors", "multi-agent-coordinator"),
    ("expert-advisors", "workflow-orchestrator"),
    ("expert-advisors", "knowledge-synthesizer"),
    ("expert-advisors", "planner"),
    ("expert-advisors", "critical-thinking"),
    ("expert-advisors", "agent-organizer"),
    # Business / marketing (holding dikeyi)
    ("business-marketing", "market-researcher"),
    ("business-marketing", "competitive-analyst"),
    ("business-marketing", "content-marketer"),
    ("business-marketing", "product-strategist"),
    ("business-marketing", "seo-specialist"),
    # DevEx / CI
    ("development-tools", "code-reviewer"),
    ("development-tools", "debugger"),
    ("development-tools", "qa-expert"),
    ("git", "commit-guardian"),
    ("git", "git-workflow-manager"),
    # Security / docs
    ("security", "security-auditor"),
    ("security", "compliance-auditor"),
    ("documentation", "technical-writer"),
    ("mcp-dev-team", "mcp-security-auditor"),
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def find_agent_file(category: str, name: str) -> Path | None:
    base = KAT / category
    if not base.is_dir():
        return None
    candidates = [
        base / f"{name}.md",
        base / name / "agent.md",
        base / name / f"{name}.md",
        base / name / "SKILL.md",
    ]
    for c in candidates:
        if c.is_file():
            return c
    # fuzzy: first md under name dir
    d = base / name
    if d.is_dir():
        mds = sorted(d.glob("*.md"))
        if mds:
            return mds[0]
    return None


def install(dry_run: bool = False) -> dict:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    installed: list[dict] = []
    missing: list[dict] = []

    if not dry_run:
        OUT.mkdir(parents=True, exist_ok=True)
        # MIT atıf
        if LICENSE.is_file():
            shutil.copy2(LICENSE, OUT / "LICENSE-UPSTREAM")
        readme = OUT / "README.md"
        readme.write_text(
            "# .claude/katalog-mit — MIT ücretsiz Status Agents çekirdeği\n\n"
            "Kaynak: `katalog/agents/` (davila7/claude-code-templates, MIT).\n"
            "Üretici: `python3 scripts/install_free_mit_agents.py`\n\n"
            "Nightly ücretsiz mod: LLM secret yoksa `scripts/nightly.sh` yalnızca "
            "damga+validate çalıştırır; bu ajanlar Claude Code/Cursor oturumunda "
            "kullanılır, Actions'a ekstra ücret bağlanmaz.\n",
            encoding="utf-8",
        )

    for category, name in CURATED:
        src = find_agent_file(category, name)
        if src is None:
            missing.append({"category": category, "name": name})
            continue
        rel = f"{category}/{name}.md"
        dest = OUT / category / f"{name}.md"
        entry = {
            "category": category,
            "name": name,
            "source": str(src.relative_to(ROOT)),
            "dest": str(dest.relative_to(ROOT)),
            "sha256": sha256_file(src),
        }
        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            body = src.read_text(encoding="utf-8", errors="replace")
            footer = (
                f"\n\n<!-- MIT: katalog/LICENSE-UPSTREAM · kurulum {ts} · "
                f"kaynak {src.relative_to(ROOT)} -->\n"
            )
            if "<!-- MIT:" not in body:
                dest.write_text(body.rstrip() + footer, encoding="utf-8")
            else:
                dest.write_text(body, encoding="utf-8")
        installed.append(entry)

    manifest = {
        "ts": ts,
        "lisans": "MIT",
        "license_path": "katalog/LICENSE-UPSTREAM",
        "upstream": "github.com/davila7/claude-code-templates",
        "ucretsiz": True,
        "nightly_ucretsiz_mod": (
            "OPENROUTER_API_KEY ve ANTHROPIC_API_KEY yoksa nightly damga+validate; "
            "ajan dosyalari ucretsiz kullanilir"
        ),
        "adet_hedef": len(CURATED),
        "adet_kurulu": len(installed),
        "adet_eksik": len(missing),
        "installed": installed,
        "missing": missing,
    }
    if not dry_run:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return manifest


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    m = install(dry_run=args.dry_run)
    if args.json:
        print(json.dumps(m, ensure_ascii=False, indent=2))
    else:
        print(
            f"[mit-free] ts={m['ts']} kurulu={m['adet_kurulu']}/{m['adet_hedef']} "
            f"eksik={m['adet_eksik']} out={OUT.relative_to(ROOT)}"
        )
        for x in m["missing"]:
            print(f"  MISSING {x['category']}/{x['name']}")
    return 0 if m["adet_eksik"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
