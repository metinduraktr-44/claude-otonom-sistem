/**
 * Append a row to CANVA_OPS/DESIGN_REGISTRY.csv (repo-relative).
 */
import { appendFile, access } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../../..");
const REGISTRY = path.join(ROOT, "CANVA_OPS", "DESIGN_REGISTRY.csv");

export type RegistryRow = {
  design_id: string;
  title: string;
  format: string;
  width: number | "";
  height: number | "";
  path: string;
  created_at: string;
  notes: string;
};

function csvEscape(s: string): string {
  if (/[",\n]/.test(s)) return `"${s.replace(/"/g, '""')}"`;
  return s;
}

export async function appendRegistry(row: RegistryRow): Promise<void> {
  try {
    await access(REGISTRY);
  } catch {
    await appendFile(
      REGISTRY,
      "design_id,title,format,width,height,path,created_at,notes\n",
      "utf8"
    );
  }
  const line = [
    row.design_id,
    row.title,
    row.format,
    String(row.width),
    String(row.height),
    row.path,
    row.created_at,
    row.notes,
  ]
    .map((c) => csvEscape(String(c)))
    .join(",");
  await appendFile(REGISTRY, line + "\n", "utf8");
}
