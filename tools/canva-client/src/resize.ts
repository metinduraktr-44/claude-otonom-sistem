/** Resize design for social presets. Pro/Enterprise gate — verify current Canva docs. */
export const PRESETS: Record<string, { width: number; height: number }> = {
  ig_square: { width: 1080, height: 1080 },
  ig_story: { width: 1080, height: 1920 },
  x_post: { width: 1600, height: 900 },
  linkedin: { width: 1200, height: 627 },
};

export async function resizeDesign(
  _designId: string,
  preset: keyof typeof PRESETS
): Promise<{ designId: string; dryRun: boolean }> {
  if (!PRESETS[preset]) throw new Error(`unknown preset: ${String(preset)}`);
  if (!process.env.CANVA_CLIENT_ID) {
    return { designId: "dry-run", dryRun: true };
  }
  // TODO: Connect resize API (plan-gated)
  throw new Error("TODO: resize API — Pro/Enterprise gate");
}
