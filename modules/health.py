import fastapi as _fastapi
import pydantic as _pydantic

from . import settings as _settings

router = _fastapi.APIRouter(tags=["Health"])


class _AppInfo(_pydantic.BaseModel):
    name: str
    version: str


class HealthResponse(_pydantic.BaseModel):
    status: str
    app_info: _AppInfo


@router.get("/")
async def health(request: _fastapi.Request) -> HealthResponse:
    settings: _settings.Settings = request.app.state.settings

    return HealthResponse(
        status="OK",
        app_info=_AppInfo(
            name=settings.app_name,
            version=settings.app_version,
        ),
    )
