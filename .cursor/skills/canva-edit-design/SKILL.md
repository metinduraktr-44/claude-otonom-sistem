---
name: canva-edit-design
description: Edit an existing Canva design via MCP editing transaction (CANVA:ON + OAuth)
---

# canva-edit-design

Prereq: `CANVA:ON` + Canva MCP authorized.

1. `search-designs` / `get-design` → design_id
2. `start-editing-transaction` → apply ops → show user preview
3. Explicit approval → `commit-editing-transaction` (never silent commit)
4. On abort → `cancel-editing-transaction`

BRIEF-ONLY: write edit plan to `CANVA_OPS/QUEUE.md` only.

