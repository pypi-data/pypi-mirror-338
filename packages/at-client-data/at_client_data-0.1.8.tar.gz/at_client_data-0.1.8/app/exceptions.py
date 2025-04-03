from fastapi import Request, status
from app.constants import ErrorCode
from fastapi.responses import JSONResponse
import logging
from app.api.utils.errors import APIError

logger = logging.getLogger(__name__)

async def handle_unhandled_exception(request: Request, exc: Exception):
    """
    Handle exceptions that are not caught by our custom error handlers.
    This is registered as a global exception handler in the FastAPI app.
    """
    # If it's our custom APIError, use its properties
    if isinstance(exc, APIError):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.detail,
                "code": exc.error_code
            }
        )
    
    # Otherwise, log the unhandled exception and return a generic error
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "An unexpected error occurred",
            "code": ErrorCode.SRV_UNKNOWN_ERROR
        }
    )