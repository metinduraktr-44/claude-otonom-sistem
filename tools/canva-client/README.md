# Canva Client — OAuth PKCE Scaffold

> Creative Agency OS · `tools/canva-client/`  
> **Varsayılan mod:** `CANVA:BRIEF-ONLY` — OAuth gerekmez

## Durum

| Bileşen | Durum |
|---------|-------|
| PKCE verifier/challenge | ✅ skeleton |
| Authorize URL builder | ✅ skeleton |
| Token exchange | ⏳ TODO |
| Token refresh | ⏳ TODO |
| Job polling (autofill/resize/export) | ⏳ TODO |
| DESIGN_REGISTRY integration | ✅ format helper |

## Kurulum (CANVA:ON için)

```bash
cd tools/canva-client
npm install
npm run build
```

## Environment (Cursor Secrets / .env)

```
CANVA_CLIENT_ID=
CANVA_CLIENT_SECRET=
CANVA_REDIRECT_URI=http://localhost:3000/callback
```

## MCP alternatifi

Canva MCP (`https://mcp.canva.com/mcp`) — `.cursor/mcp.json`  
OAuth gerektirmeden MCP üzerinden design ops mümkün olabilir; PKCE yine de export pipeline için önerilir.

## Registry

Export sonrası satır: `CANVA_OPS/DESIGN_REGISTRY.csv`  
Helper: `formatRegistryRow()` in `src/index.ts`

## Referans

- Rule: `.cursor/rules/40-canva-ops.mdc`
- Skills: `.cursor/skills/canva-*`
- MCP doc: `CANVA_OPS/MCP_TOOLS.md`
