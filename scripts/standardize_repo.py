#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ÇOK-REPO STANDARDİZASYON MOTORU (güvenli, sadece-ekleme).
Bir repo dizinine EKSİK community-health dosyalarını ekler.
ASLA: mevcut README/kod/LICENSE'ı ezmez; sahte issue/PR/ajan üretmez.
Kullanım: python3 standardize_repo.py <repo_dir> <tip> <repo_adı> [--funding]
tip: system | webapp | app | product
"""
import os, sys, json

EMAIL = "metindurak.tr@gmail.com"

def w_if_absent(path, content):
    if os.path.exists(path):
        return f"skip (var): {os.path.relpath(path, ROOT)}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"EKLENDİ: {os.path.relpath(path, ROOT)}"

ROOT = sys.argv[1]
TYPE = sys.argv[2] if len(sys.argv) > 2 else "system"
NAME = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(ROOT.rstrip("/"))
FUNDING = "--funding" in sys.argv

TYPE_TR = {"system": "sistem/otomasyon", "webapp": "web uygulaması",
           "app": "uygulama (mobil/web)", "product": "ürün/web uygulaması"}

results = []

# ---- SECURITY.md
results.append(w_if_absent(os.path.join(ROOT, "SECURITY.md"), f"""# Security Policy — {NAME}

## Reporting a vulnerability
Please report security issues privately via GitHub Security Advisories
(Security → Advisories → Report a vulnerability) or email **{EMAIL}**.
Response target: **72 hours**. Do not open public issues for exploitable findings.

**TR:** Güvenlik bulgusunu private advisory ya da e-posta ile bildir; kamuya açık issue açma. Yanıt hedefi 72 saat.

## Scope
{NAME} ({TYPE_TR.get(TYPE, TYPE)}). Supported: default branch (`main`).
"""))

# ---- CODE_OF_CONDUCT.md (Contributor Covenant özet)
results.append(w_if_absent(os.path.join(ROOT, "CODE_OF_CONDUCT.md"), f"""# Contributor Covenant Code of Conduct

## Our Pledge
We as members, contributors, and leaders pledge to make participation in
{NAME} a harassment-free experience for everyone.

## Standards
Examples of positive behavior: empathy, respect for differing viewpoints,
graceful acceptance of constructive feedback. Unacceptable: harassment,
trolling, publishing others' private information.

## Enforcement
Report unacceptable behavior to **{EMAIL}**. Maintainers will review and
respond. This Code adapts the [Contributor Covenant](https://www.contributor-covenant.org) v2.1.

**TR:** Bu proje herkes için tacizsiz bir katılım ortamı taahhüt eder; ihlalleri {EMAIL} adresine bildir.
"""))

# ---- CONTRIBUTING.md
results.append(w_if_absent(os.path.join(ROOT, "CONTRIBUTING.md"), f"""# Contributing to {NAME}

Thanks for your interest. {NAME} is a {TYPE_TR.get(TYPE, TYPE)}.

## Workflow
1. Open an issue describing the change (use the templates).
2. Fork / branch from `main`.
3. Keep changes focused; write a clear PR description (use the PR template).
4. Ensure CI is green before requesting review.

## Standards
- Small, reviewable PRs. Conventional-style commit messages preferred.
- No secrets in code. No breaking changes without a note in the PR.
- Be respectful — see `CODE_OF_CONDUCT.md`.

**TR:** Önce issue aç, `main`'den dallan, küçük ve odaklı PR gönder, CI yeşil olsun. Gizli anahtar commit'leme.
"""))

# ---- .github/ISSUE_TEMPLATE/*.yml + config
gh = os.path.join(ROOT, ".github")
results.append(w_if_absent(os.path.join(gh, "ISSUE_TEMPLATE", "bug_report.yml"), f"""name: Bug report
description: {NAME} içinde bir hata bildir / Report a bug
labels: ["bug"]
body:
  - type: textarea
    id: what
    attributes:
      label: Ne oldu? / What happened?
      description: Beklenen vs gerçekleşen davranış.
    validations:
      required: true
  - type: textarea
    id: repro
    attributes:
      label: Yeniden üretme adımları / Steps to reproduce
    validations:
      required: true
  - type: input
    id: env
    attributes:
      label: Ortam / Environment (OS, sürüm)
"""))
results.append(w_if_absent(os.path.join(gh, "ISSUE_TEMPLATE", "feature_request.yml"), f"""name: Feature request
description: {NAME} için özellik öner / Suggest a feature
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Problem / İhtiyaç
    validations:
      required: true
  - type: textarea
    id: solution
    attributes:
      label: Önerilen çözüm / Proposed solution
    validations:
      required: true
"""))
results.append(w_if_absent(os.path.join(gh, "ISSUE_TEMPLATE", "config.yml"), f"""blank_issues_enabled: false
contact_links:
  - name: Güvenlik bulgusu / Security
    url: https://github.com/metinduraktr-44/{NAME}/security/advisories/new
    about: Zafiyetleri private advisory ile bildir (issue açma).
  - name: İletişim / Contact
    url: mailto:{EMAIL}
    about: Genel sorular ve iş birliği.
"""))

# ---- PR template
results.append(w_if_absent(os.path.join(gh, "PULL_REQUEST_TEMPLATE.md"), f"""## Neden / Why
<!-- Bu değişiklik hangi problemi çözüyor? -->

## Ne / What
<!-- Ne değişti? -->

## Test / Nasıl doğrulandı
<!-- CI + manuel test adımları -->

## Kontrol listesi / Checklist
- [ ] CI yeşil
- [ ] Gizli anahtar yok
- [ ] Gerekiyorsa doküman güncellendi
- [ ] Küçük ve odaklı PR
"""))

# ---- dependabot.yml (package.json varsa npm; workflows varsa actions)
eco = []
if os.path.exists(os.path.join(ROOT, "package.json")):
    eco.append('  - package-ecosystem: "npm"\n    directory: "/"\n    schedule: { interval: "weekly" }')
if os.path.isdir(os.path.join(ROOT, ".github", "workflows")):
    eco.append('  - package-ecosystem: "github-actions"\n    directory: "/"\n    schedule: { interval: "weekly" }')
if eco:
    results.append(w_if_absent(os.path.join(gh, "dependabot.yml"),
                               "version: 2\nupdates:\n" + "\n".join(eco) + "\n"))

# ---- FUNDING (yalnız sistem/OSS + --funding)
if FUNDING:
    results.append(w_if_absent(os.path.join(gh, "FUNDING.yml"),
                               f"github: [metinduraktr-44]\ncustom: [\"mailto:{EMAIL}\"]\n"))

for r in results:
    print(" ", r)
