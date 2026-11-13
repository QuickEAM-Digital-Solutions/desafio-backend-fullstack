"""API v1 router aggregator (already implemented)."""

from fastapi import APIRouter

from app.api.v1.endpoints import auth, chat, tasks

router = APIRouter(prefix="/v1")
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
router.include_router(chat.router, prefix="/chat", tags=["chat"])
