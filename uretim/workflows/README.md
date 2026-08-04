# uretim/workflows/ — Kişisel & grup workflow'ları (CILT10 §4)

Her ünvan (kişisel) ve her ekip/departman (grup) 6 eksende workflow taşır: **eğitim · to-do · roadmap · toplantı · üst iletişim · yan/alt iletişim**.

```
uretim/workflows/
├── kisisel/{UNVAN}.md      # ünvan-özel workflow (rol kartına bağlı)
└── grup/{DEPT}-departman.md# departman/ekip workflow'u
```

- **7/24 canlı akış:** üst iş listesi → task → roadmap → deadline → rapor/özet → yan senkron → geri-okuma zinciriyle tekrar (follow-the-sun, 3 vardiya).
- **Seed:** `kisisel/MKT-PRF-LEAD.md` + `grup/MKT-PRF-departman.md`. Gerisi org.json'dan jeneratörle çoğaltılır (CILT10 §7).
- Kaynak sözleşme: her ajanın okuduğu `CLAUDE.md` (ortak sözleşme); rol kartı `.claude/agents/{DEPT}/{dept}-lead.md`.
