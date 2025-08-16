import fastapi as _fastapi
from modules.shared import errors as _errors


async def not_found(request: _fastapi.Request, exc: _errors.NotFoundError):
    return _fastapi.responses.JSONResponse(
        status_code=404,
        content=str(exc),
    )
