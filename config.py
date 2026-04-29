from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Customer Success Copilot"
    app_version: str = "2026.1"
    openai_api_key: str | None = None
    llm_provider: str = "rules"  # rules or openai

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
