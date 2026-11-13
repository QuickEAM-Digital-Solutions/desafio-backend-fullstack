"""Application settings loaded from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed application settings (read from the environment and `.env`)."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_NAME: str = "desafio-backend-python-ai"
    APP_ENV: str = "development"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://app:app@db:5432/desafio"

    # JWT
    JWT_SECRET_KEY: str = "dev-secret-key-not-for-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 60

    # CORS (comma-separated list of allowed frontend origins)
    CORS_ORIGINS: str = "http://localhost:5173,http://localhost:3000"

    # AI Agent
    # Any model string supported by PydanticAI, e.g.:
    #   "test"                    -> fake model, no API key needed (great for dev/tests)
    #   "ollama:llama3.2"         -> local Ollama (requires OLLAMA_BASE_URL)
    #   "google:gemini-3.8-flash" -> Gemini (requires GOOGLE_API_KEY, has a free tier)
    #   "openai:<model-name>"     -> OpenAI (requires OPENAI_API_KEY)
    # Provider API keys are read directly from the environment by PydanticAI.
    LLM_MODEL: str = "test"

    @property
    def cors_origins_list(self) -> list[str]:
        """Return CORS_ORIGINS as a list."""
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin]


settings = Settings()
