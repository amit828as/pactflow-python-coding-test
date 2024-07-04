"""
Base routes for the API.

The routes in this module serve a very basic purpose, such as health checks and
version information.
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from pypacter.language_detector import detect_programming_language
from pypacter_api import get_version

router = APIRouter()


@router.post("/detect-language", tags=["language"])
async def detect_code_language(code_snippet: str) -> JSONResponse:
    """

    Detects the most likely programming language for a given code snippet.

    **Parameters:**
        - code_snippet (str): The input code snippet (required).

    **Returns:**
        A JSON response containing the  programming language name or an error message.

    **Raises:**
        HTTPException: If the code snippet is missing or language detection fails.
    """
    # Validate input (ensure code_snippet is provided)
    if not code_snippet:
        raise HTTPException(status_code=400, detail="Missing code snippet")

    try:
        detected_language = detect_programming_language(code_snippet)
        return JSONResponse(content={"detected_language": detected_language.lower()})
    except KeyError:
        # Handle any potential errors during language detection
        raise HTTPException(
            status_code=500, detail="Failed to detect language"
        ) from None


@router.get("/health", tags=["health"])
async def health() -> JSONResponse:
    """
    Health check.

    Returns:
        A JSON response indicating the health of the API.
    """
    return JSONResponse(content={"status": "ok"})


@router.get("/version", tags=["version"])
async def version() -> JSONResponse:
    """
    Get the version of the API.

    Returns:
        A JSON response containing the version of the API.
    """
    return JSONResponse(content={"version": get_version()})
