# tools/security-scanners

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

Savunma amaçlı tarayıcı iskeleti. **Exploit scanner yok.**

## Modüller (stub)
| Modül | Durum | Giriş |
|-------|-------|-------|
| `secret_scan` | canlı: `scripts/secret_scan.py` | pattern warn/redact log |
| `ethics_check` | canlı: `scripts/ethics_check.py` | offensive pattern block |
| `control_validate` | stub | kontrol dosyası şema doğrulama (Faz 3) |

## Kullanım
```bash
python3 scripts/secret_scan.py SECURITY_CONTEXT .cursor
python3 scripts/ethics_check.py .cursor LAYERS
python3 -m tools.security_scanners.control_validate --help  # stub
```

Secret değer basılmaz. MODE=ASSESS-ONLY.
