# tools/canva-client — Canva Connect API scaffold (Enterprise/Pro aware)

TypeScript stub for **server-side** Canva Connect flows that MCP does not cover well
(bulk autofill, polled jobs, registry CSV writer).

## Gates
| Capability | Plan |
|------------|------|
| MCP interactive edit (Cursor) | Canva account + OAuth MCP |
| Autofill / Brand templates bulk | **Enterprise** |
| Resize API bulk | **Pro or Enterprise** (confirm current Canva docs) |
| Export | Connected apps; rate-limit politely |

Without credentials or plan: stay in **dry-run** / `CANVA:BRIEF-ONLY`.

## Rate limits (document assumptions — verify against Canva developer docs)
- Prefer ≤1 mutating request / second for autofill create.
- Job poll interval: **2–5 seconds** with jitter; max ~60 polls then fail soft.
- Export: queue; do not fan-out unbounded parallel downloads.

## Setup
```bash
cd tools/canva-client
cp .env.example .env   # never commit secrets
npm install            # when you actually run TS (optional for Holding HQ)
```

OAuth PKCE: see `src/oauth-pkce.ts`. Set `CANVA_CLIENT_ID` / redirect URI in Canva developer portal.

## Scripts (intended)
- `npm run dry-run` — print planned jobs from `../../CANVA_OPS/QUEUE.md`
- Registry writer appends to `../../CANVA_OPS/DESIGN_REGISTRY.csv`

## Relation to MCP
Cursor Agent prefers **Canva MCP** (`https://mcp.canva.com/mcp`) for interactive work.
This client is for batch/Enterprise automation.
