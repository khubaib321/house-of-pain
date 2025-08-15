import fastapi as _fastapi
from modules import db as _db
from modules.users import services as _services
from modules.shared.repository import root as _root


router = _fastapi.APIRouter(
    tags=["Users"],
)


@router.get("/")
async def get_users(
    repo: _root.RootRepository = _fastapi.Depends(_db.get_repo),
) -> list[_services.UserRead]:
    return await _services.get_users(repo=repo)
