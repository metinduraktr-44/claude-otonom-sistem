/**
 * Canva OAuth PKCE skeleton — Creative Agency OS
 * Default mode: CANVA:BRIEF-ONLY (no OAuth required)
 */

export interface CanvaConfig {
  clientId: string;
  redirectUri: string;
  scopes?: string[];
}

export interface TokenPair {
  accessToken: string;
  refreshToken: string;
  expiresAt: number;
}

const CANVA_AUTH = "https://www.canva.com/api/oauth/authorize";
const CANVA_TOKEN = "https://api.canva.com/rest/v1/oauth/token";

export function generatePkceVerifier(): string {
  const bytes = crypto.getRandomValues(new Uint8Array(32));
  return btoa(String.fromCharCode(...bytes))
    .replace(/\+/g, "-")
    .replace(/\//g, "_")
    .replace(/=+$/, "");
}

export async function pkceChallenge(verifier: string): Promise<string> {
  const data = new TextEncoder().encode(verifier);
  const digest = await crypto.subtle.digest("SHA-256", data);
  return btoa(String.fromCharCode(...new Uint8Array(digest)))
    .replace(/\+/g, "-")
    .replace(/\//g, "_")
    .replace(/=+$/, "");
}

export async function buildAuthorizeUrl(config: CanvaConfig, state: string, verifier: string): Promise<string> {
  const challenge = await pkceChallenge(verifier);
  const params = new URLSearchParams({
    client_id: config.clientId,
    redirect_uri: config.redirectUri,
    response_type: "code",
    code_challenge: challenge,
    code_challenge_method: "S256",
    state,
    scope: (config.scopes ?? ["design:content:read", "design:content:write"]).join(" "),
  });
  return `${CANVA_AUTH}?${params}`;
}

/** Stub: exchange auth code for tokens */
export async function exchangeCode(_code: string, _verifier: string, _config: CanvaConfig): Promise<TokenPair> {
  throw new Error("OAuth exchange not implemented — configure CANVA_CLIENT_ID/SECRET in Cursor Secrets");
}

/** Stub: refresh access token */
export async function refreshToken(_refreshToken: string, _config: CanvaConfig): Promise<TokenPair> {
  throw new Error("Token refresh not implemented");
}

/** Stub: poll async Canva job (autofill, resize, export) */
export async function pollJob<T>(_jobId: string, _tokens: TokenPair): Promise<T> {
  throw new Error("Job polling not implemented");
}

export interface DesignRegistryRow {
  design_id: string;
  brief_id: string;
  channel: string;
  format: string;
  status: string;
}

/** Append row to CANVA_OPS/DESIGN_REGISTRY.csv */
export function formatRegistryRow(row: DesignRegistryRow): string {
  return [row.design_id, row.brief_id, row.channel, row.format, row.status].join(",");
}
