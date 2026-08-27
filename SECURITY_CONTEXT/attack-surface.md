# Attack Surface — Defense Perspective (Faz 0)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**Amaç:** Saldırı tarifi değil; **tespit & sertleştirme önceliği** için yüzey haritası.

## Yüzey sınıfları

### 1) Secret / credential handling
- **Risk:** Env key sızıntısı chat/commit/log
- **Kontrol adayları:** secret_scan hook, `.gitignore`, dry-run matris, vault placeholder
- **D3FEND:** Credential hardening / secret storage hygiene
- **Öncelik:** P0

### 2) LLM client outbound
- **Risk:** API key env; prompt injection via ingested markdown (katalog/uretim)
- **Kontrol:** key yoksa dry-run; çıktı denetimi; untrusted content isolation
- **Öncelik:** P1

### 3) GitHub Actions
- **Risk:** Workflow permission creep; secret exposure in logs
- **Kontrol:** least privilege `permissions:`; secret mask; pin actions SHA (Faz 1 research)
- **Öncelik:** P1

### 4) Terraform / observability
- **Risk:** Sensitive variable misuse in state/tfvars commit
- **Kontrol:** `*.tfvars` gitignore (örnek hariç); remote state encryption (ASSESS)
- **Öncelik:** P1

### 5) Vendored katalog
- **Risk:** Üçüncü parti şablonlarda güvensiz script örnekleri
- **Kontrol:** katalog’u runtime dep sayma; ethics_check kapsamı; pin/upstream-sync gözlemi
- **Öncelik:** P2

### 6) Holding otomasyon yazımı
- **Risk:** Generator’ların `AUDIT_LOG` / dokümanlara yanlışlıkla secret basması
- **Kontrol:** secret_scan afterFileEdit; redaksiyon politikası
- **Öncelik:** P1

### 7) MCP yüzey (opsiyonel)
- **Risk:** Token’lı MCP açılması
- **Kontrol:** security MCP default OFF (`mcp.security.example.json`); Canva ayrı track
- **Öncelik:** P2

## Bilinçli kapsam dışı (şimdilik)
- Canlı penetrasyon / exploit doğrulama
- Production cloud hesap tarama (credential yok → dry-run)

## Sonraki (Faz 1)
- GHA permissions matrisi
- Action pin / Scorecard ASSESS
- Threat model (STRIDE) holding otomasyonuna
