/**
 * Canva API client scaffold — endpoints stub
 * OAuth PKCE: TODO (see README)
 */

export interface CanvaClientConfig {
  clientId?: string;
  redirectUri?: string;
  accessToken?: string;
}

export class CanvaClient {
  private config: CanvaClientConfig;

  constructor(config: CanvaClientConfig = {}) {
    this.config = config;
  }

  /** TODO: OAuth PKCE authorization URL */
  getAuthorizationUrl(_scopes: string[] = ["design:read", "design:write"]): string {
    throw new Error("OAuth PKCE not configured — see README");
  }

  /** Stub: autofill design from brief data */
  async autofill(_designId: string, _data: Record<string, string>): Promise<{ status: "stub" }> {
    return { status: "stub" };
  }

  /** Stub: export design */
  async export(
    _designId: string,
    _format: "png" | "jpg" | "pdf" | "mp4" = "png"
  ): Promise<{ status: "stub"; path?: string }> {
    return { status: "stub" };
  }

  /** Stub: resize for channel spec */
  async resize(
    _designId: string,
    width: number,
    height: number
  ): Promise<{ status: "stub"; width: number; height: number }> {
    return { status: "stub", width, height };
  }
}

export function createClient(config?: CanvaClientConfig): CanvaClient {
  return new CanvaClient(config);
}

// CLI smoke
if (import.meta.url === `file://${process.argv[1]}`) {
  const client = createClient();
  console.log("Canva client scaffold OK", client.autofill("demo", {}));
}
