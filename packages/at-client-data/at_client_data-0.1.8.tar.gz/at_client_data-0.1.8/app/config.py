# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Application Metadata
    APP_NAME: str
    APP_VERSION: str
    
    # Security & CORS
    ALLOWED_ORIGINS: list[str]

    # FMP Settings
    FMP_API_KEY: str
    FMP_REQUEST_TIMEOUT: int
    FMP_REQUEST_RETRIES: int
    FMP_RATE_LIMIT_PER_SEC: int
    FMP_API_URL: str

    # NASDAQTRADER Settings
    NASDAQTRADER_RATE_LIMIT_PER_SEC: int
    NASDAQTRADER_API_URL: str
    NASDAQTRADER_REQUEST_RETRIES: int

    # FINNHUB Settings
    FINNHUB_API_TOKEN: str
    FINNHUB_REQUEST_TIMEOUT: int
    FINNHUB_REQUEST_RETRIES: int
    FINNHUB_RATE_LIMIT_PER_SEC: int
    FINNHUB_API_URL: str

    model_config = {
        "env_file": ".env"
    }

settings = Settings()