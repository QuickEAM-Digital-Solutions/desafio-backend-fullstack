"""JWT and password hashing utilities.

This file is already implemented — you don't need to change it.

- `hash_password` / `verify_password`: use when creating users and on login.
- `create_access_token`: use in `POST /v1/auth/login` to issue the token.
- `decode_access_token`: use in `get_current_user` (app/api/deps.py) to
  read the user id from the token. It raises `jwt.InvalidTokenError` when the
  token is invalid or expired — convert it into an HTTP 401 response.
"""

from datetime import UTC, datetime, timedelta
from typing import Any

import bcrypt
import jwt

from app.config import settings


def hash_password(password: str) -> str:
    """Hash a plain-text password using bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plain-text password against its bcrypt hash."""
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())


def create_access_token(subject: str) -> str:
    """Create a signed JWT whose `sub` claim is the given subject (user id)."""
    expire = datetime.now(UTC) + timedelta(minutes=settings.JWT_EXPIRATION_MINUTES)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )


def decode_access_token(token: str) -> dict[str, Any]:
    """Decode and validate a JWT.

    Raises:
        jwt.InvalidTokenError: if the token is malformed, tampered or expired.
    """
    return jwt.decode(
        token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
    )
