import { useState } from 'react'
import { isAuthenticated, logout } from './api/auth'
import LoginPage from './pages/LoginPage'
import TasksPage from './pages/TasksPage'

// Root component — already implemented.
// Shows the login page or the tasks page depending on the stored token.
// (Using a router library such as react-router is optional.)
export default function App() {
  const [loggedIn, setLoggedIn] = useState(isAuthenticated())

  function handleLogout() {
    logout()
    setLoggedIn(false)
  }

  if (!loggedIn) {
    return <LoginPage onLogin={() => setLoggedIn(true)} />
  }

  return <TasksPage onLogout={handleLogout} />
}
