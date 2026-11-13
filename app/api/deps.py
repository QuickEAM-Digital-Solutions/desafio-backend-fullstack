"""
Shared Dependencies (Dependency Injection)
==========================================
FastAPI dependencies used across routes via `Depends(...)`.

`get_db()` is already implemented. You must implement `get_current_user()`.
"""

from collections.abc import AsyncGenerator

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import async_session_maker

# Tells FastAPI/Swagger where the token comes from. Thanks to this, the
# "Authorize" button in Swagger UI (/docs) works with your login endpoint.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Yield an async database session and close it at the end of the request."""
    async with async_session_maker() as session:
        yield session


# TODO: implement get_current_user
#
# async def get_current_user(
#     token: str = Depends(oauth2_scheme),
#     db: AsyncSession = Depends(get_db),
# ) -> User:
#     1. Decode the token with `decode_access_token` (app/core/security.py)
#     2. If the token is invalid/expired -> raise HTTPException(401)
#     3. Load the user from the database using the `sub` claim (user id)
#     4. If the user does not exist or is inactive -> raise HTTPException(401)
#     5. Return the user
#
# Usage in a route:
#     @router.get("/")
#     async def list_tasks(current_user: User = Depends(get_current_user)): ...
