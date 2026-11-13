"""FastAPI application entrypoint."""

from fastapi import FastAPI

from app.api.v1.router import router as api_v1_router
from app.config import settings

# TODO: call setup_logging() from app/core/logging.py here

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# TODO: add CORSMiddleware so the React frontend can call this API.
# Allowed origins are available in `settings.cors_origins_list`.
# Docs: https://fastapi.tiangolo.com/tutorial/cors/

app.include_router(api_v1_router)


@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    """Liveness probe."""
    return {"status": "ok"}
