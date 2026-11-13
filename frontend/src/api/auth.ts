import { tokenStorage } from './client'

/**
 * TODO: call POST /v1/auth/login with apiFetch<TokenResponse>() and save
 * the token with tokenStorage.set(access_token).
 *
 * If your backend uses OAuth2PasswordRequestForm (form data), send:
 *   body: new URLSearchParams({ username: email, password })
 * If it uses a JSON body, send:
 *   body: JSON.stringify({ email, password })
 */
export async function login(email: string, password: string): Promise<void> {
  void email
  void password
  throw new Error('login() not implemented yet')
}

export function logout(): void {
  tokenStorage.clear()
}

export function isAuthenticated(): boolean {
  return tokenStorage.get() !== null
}
