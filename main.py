import contextlib as _clib

import fastapi as _fastapi
from fastapi import responses as _responses
from fastapi.middleware import gzip as _gzip

from modules.shared import errors as _errors
from modules import settings as _settings
from modules import health as _health
from modules.users import web as _users_web
from modules import exc as _exc_handlers


settings = _settings.get_settings()


@_clib.asynccontextmanager
async def lifespan(app: _fastapi.FastAPI):
    app.state.settings = settings
    yield


app = _fastapi.FastAPI(
    lifespan=lifespan,
    title=settings.app_name,
    version=settings.app_version,
    default_response_class=_responses.JSONResponse,
)

# ── Middlewares ────────────────────────────────────────────────────
app.add_middleware(_gzip.GZipMiddleware)

# ── Exception handlers ─────────────────────────────────────────────
app.add_exception_handler(_errors.NotFoundError, _exc_handlers.not_found)

# ── Routers ────────────────────────────────────────────────────────
app.include_router(_health.router, prefix="/health")
app.include_router(_users_web.router, prefix="/users")
