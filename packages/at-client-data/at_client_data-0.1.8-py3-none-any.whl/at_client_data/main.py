# app/main.py
from logging.config import dictConfig
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.exceptions import (
    handle_unhandled_exception
)
from app.api.core import candlestick as core_candlestick, entry as core_entry, news as core_news, quote as core_quote
from app.api.core.stock import analyst as core_analyst, calendar as core_calendar, company as core_company, financial as core_financial
from app.api.external.nasdaqtrader import entry as external_nasdaqtrader_entry
from app.api.external.finnhub import entry as external_finnhub_entry
from app.api.utils.middleware import setup_middleware

# Configure logging
dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr"
        }
    },
    "loggers": {
        "app": {  # This will catch all loggers under the 'app' namespace
            "handlers": ["default"],
            "level": "INFO",
            "propagate": False
        }
    },
    "root": {  # This is the root logger configuration
        "handlers": ["default"],
        "level": "INFO"
    }
})

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup custom middleware
setup_middleware(app)

# Add exception handlers
app.add_exception_handler(Exception, handle_unhandled_exception)

# Include routers
app.include_router(core_entry.router, prefix=f"/core/entry", tags=["core entry"])
app.include_router(core_news.router, prefix=f"/core/news", tags=["core news"])
app.include_router(core_quote.router, prefix=f"/core/quote", tags=["core quote"])
app.include_router(core_candlestick.router, prefix=f"/core/candlestick", tags=["core candlestick"])
app.include_router(core_analyst.router, prefix=f"/core/stock/analyst", tags=["core stock analyst"])
app.include_router(core_calendar.router, prefix=f"/core/stock/calendar", tags=["core stock calendar"])
app.include_router(core_company.router, prefix=f"/core/stock/company", tags=["core stock company"])
app.include_router(core_financial.router, prefix=f"/core/stock/financial", tags=["core stock financial"])
app.include_router(external_nasdaqtrader_entry.router, prefix=f"/external/nasdaqtrader/entry", tags=["external nasdaqtrader entry"])
app.include_router(external_finnhub_entry.router, prefix=f"/external/finnhub/entry", tags=["external finnhub entry"])