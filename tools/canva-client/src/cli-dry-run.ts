/** Dry-run CLI — no network. Reads QUEUE.md existence and prints plan. */
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../../..");

const queuePath = path.join(ROOT, "CANVA_OPS", "QUEUE.md");
const text = await readFile(queuePath, "utf8").catch(() => "(missing QUEUE.md)");
console.log("[canva-client dry-run] flag default CANVA:BRIEF-ONLY");
console.log("[canva-client dry-run] QUEUE.md preview:\n");
console.log(text.slice(0, 800));
console.log("\n[canva-client dry-run] OK — no API calls");
