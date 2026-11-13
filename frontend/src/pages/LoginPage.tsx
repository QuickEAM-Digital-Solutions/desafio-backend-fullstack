import { useState, type FormEvent } from 'react'
import { login } from '../api/auth'

interface LoginPageProps {
  onLogin: () => void
}

/**
 * TODO:
 * - Call login(email, password) on submit
 * - Show a loading state while the request is in progress
 * - Show an error message on invalid credentials (ApiError with status 401)
 * - Call onLogin() on success
 */
export default function LoginPage({ onLogin }: LoginPageProps) {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState<string | null>(null)

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    try {
      await login(email, password)
      onLogin()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unexpected error')
    }
  }

  return (
    <main className="container narrow">
      <h1>Entrar</h1>
      <form onSubmit={handleSubmit} className="stack">
        <input
          type="email"
          placeholder="E-mail"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Senha"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        {error && <p className="error">{error}</p>}
        <button type="submit">Entrar</button>
      </form>
    </main>
  )
}
