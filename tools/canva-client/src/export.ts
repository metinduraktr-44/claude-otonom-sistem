/** Export design bytes / URLs — queue politely; do not unbounded parallelize. */
export type ExportResult = {
  designId: string;
  format: "png" | "pdf" | "jpg";
  url?: string;
  dryRun: boolean;
};

export async function exportDesign(
  designId: string,
  format: ExportResult["format"] = "png"
): Promise<ExportResult> {
  if (!process.env.CANVA_CLIENT_ID) {
    return { designId, format, dryRun: true };
  }
  // TODO: export endpoints + download with rate limit
  throw new Error("TODO: export API");
}
