"""
Authentication Endpoints
========================
You should implement here:

- POST /v1/auth/register: creates a new user (email, full_name, password).
  Store the password hashed (`hash_password`). Return 409 if the email is taken.
- POST /v1/auth/login: validates credentials and returns a JWT
  (`create_access_token(str(user.id))`). Return 401 on invalid credentials.
- GET /v1/auth/me: returns the authenticated user (uses `get_current_user`).

Security helpers are ready in app/core/security.py.

Tip: if you accept the login as form data (`OAuth2PasswordRequestForm`),
the "Authorize" button in Swagger UI works out of the box. If you prefer a
JSON body (`LoginRequest` schema), that is fine too — just document it.
"""

from fastapi import APIRouter

router = APIRouter()
