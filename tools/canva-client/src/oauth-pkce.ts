/**
 * OAuth 2.0 PKCE helpers (scaffold).
 * Wire to Canva Connect docs: https://www.canva.dev/docs/connect/
 * Without CLIENT_ID → dry-run only.
 */
import { createHash, randomBytes } from "node:crypto";

export function generateCodeVerifier(bytes = 32): string {
  return randomBytes(bytes).toString("base64url");
}

export function challengeS256(verifier: string): string {
  return createHash("sha256").update(verifier).digest("base64url");
}

export type TokenSet = {
  access_token: string;
  refresh_token?: string;
  expires_at?: number;
};

export function authUrl(opts: {
  clientId: string;
  redirectUri: string;
  challenge: string;
  scopes: string[];
  state: string;
}): string {
  const u = new URL("https://www.canva.com/api/oauth/authorize");
  u.searchParams.set("response_type", "code");
  u.searchParams.set("client_id", opts.clientId);
  u.searchParams.set("redirect_uri", opts.redirectUri);
  u.searchParams.set("code_challenge", opts.challenge);
  u.searchParams.set("code_challenge_method", "S256");
  u.searchParams.set("scope", opts.scopes.join(" "));
  u.searchParams.set("state", opts.state);
  return u.toString();
}

/** Exchange authorization code — STUB: returns null if env missing. */
export async function exchangeCode(_code: string, _verifier: string): Promise<TokenSet | null> {
  if (!process.env.CANVA_CLIENT_ID) {
    console.warn("[canva-client] CANVA_CLIENT_ID missing → dry-run");
    return null;
  }
  // TODO: POST token endpoint per Canva Connect OAuth docs
  throw new Error("TODO: implement token exchange (Enterprise/Pro app credentials)");
}
