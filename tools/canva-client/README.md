# Canva Client — OAuth PKCE TODO

TypeScript scaffold for Canva Connect API integration.

## Status
- **Faz 0:** Endpoint stubs (autofill, export, resize)
- **Faz 4:** OAuth PKCE flow

## OAuth PKCE (TODO)
1. Register app at [Canva Developer Portal](https://www.canva.com/developers/)
2. Set redirect URI (local: `http://127.0.0.1:3000/callback`)
3. Store in Cursor Secrets:
   - `CANVA_CLIENT_ID`
   - `CANVA_CLIENT_SECRET` (if required)
4. Implement PKCE: code_verifier + code_challenge (S256)
5. Token refresh → `accessToken` in client config

## MCP alternative
Cursor MCP: `.cursor/mcp.json` → `https://mcp.canva.com/mcp`  
Prefer MCP when CANVA:ON in Cursor; use this client for batch/script automation.

## Build
```bash
cd tools/canva-client
npm install
npm run build
npm start
```

## Registry
Design tracking: `CANVA_OPS/DESIGN_REGISTRY.csv`

## Endpoints (stub)
| Method | Purpose |
|--------|---------|
| `autofill()` | Brief data → design fields |
| `export()` | PNG/JPG/PDF/MP4 export |
| `resize()` | Channel spec dimensions |
