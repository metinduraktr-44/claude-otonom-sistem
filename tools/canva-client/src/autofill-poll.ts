/**
 * Autofill job create + poll (Enterprise gate).
 * Poll every 2–5s with jitter; fail soft after maxAttempts.
 */
export type AutofillJob = {
  jobId: string;
  status: "in_progress" | "success" | "failed" | "dry_run";
  designId?: string;
};

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

export async function createAutofillJob(_payload: unknown): Promise<AutofillJob> {
  if (!process.env.CANVA_CLIENT_ID) {
    return { jobId: "dry-run", status: "dry_run" };
  }
  // TODO: Enterprise Autofill API — requires Enterprise plan
  throw new Error("TODO: Enterprise autofill create — plan gate");
}

export async function pollAutofill(
  jobId: string,
  opts: { maxAttempts?: number; minMs?: number; maxMs?: number } = {}
): Promise<AutofillJob> {
  if (jobId === "dry-run") return { jobId, status: "dry_run" };
  const maxAttempts = opts.maxAttempts ?? 60;
  const minMs = opts.minMs ?? 2000;
  const maxMs = opts.maxMs ?? 5000;
  for (let i = 0; i < maxAttempts; i++) {
    // TODO: GET job status
    const jitter = minMs + Math.floor(Math.random() * (maxMs - minMs));
    await sleep(jitter);
  }
  return { jobId, status: "failed" };
}
