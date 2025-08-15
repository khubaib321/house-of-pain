import contextlib as _clib

import fastapi as _fastapi
from fastapi.middleware import gzip as _gzip

from modules import settings as _settings
from modules import health as _health
from modules.users import web as _users_web


settings = _settings.get_settings()


@_clib.asynccontextmanager
async def lifespan(app: _fastapi.FastAPI):
    app.state.settings = settings
    yield


app = _fastapi.FastAPI(
    lifespan=lifespan,
    title=settings.app_name,
    version=settings.app_version,
    default_response_class=_fastapi.responses.JSONResponse,
)

# ── Middlewares ────────────────────────────────────────────────────
app.add_middleware(_gzip.GZipMiddleware)

# ── Routers ────────────────────────────────────────────────────────
app.include_router(_health.router, prefix="/health")
app.include_router(_users_web.router, prefix="/users")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8192, reload=True)
