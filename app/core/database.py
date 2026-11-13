"""Async SQLAlchemy engine and session factory.

This file is already implemented — you don't need to change it.
Use `get_db()` from `app.api.deps` to obtain a session inside your routes.
"""

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=False, pool_pre_ping=True)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
