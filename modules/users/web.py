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


@router.get("/search/")
async def get_user_by_email(
    name: str = _fastapi.Query(default=None),
    repo: _root.RootRepository = _fastapi.Depends(_db.get_repo),
) -> list[_services.UserRead]:
    return await _services.search_user_by_name(repo=repo, name=name)


@router.get("/email-available/")
async def email_available(
    email: str = _fastapi.Query(),
    repo: _root.RootRepository = _fastapi.Depends(_db.get_repo),
) -> bool:
    return not await _services.email_exists(repo=repo, email=email)


@router.get("/{user_id}/")
async def get_user_by_email(
    user_id: int = _fastapi.Path(),
    repo: _root.RootRepository = _fastapi.Depends(_db.get_repo),
) -> _services.UserRead:
    return await _services.get_user_by_id(repo=repo, user_id=user_id)


@router.get("/{email}/")
async def get_user_by_email(
    email: str = _fastapi.Path(),
    repo: _root.RootRepository = _fastapi.Depends(_db.get_repo),
) -> _services.UserRead:
    return await _services.get_user_by_email(repo=repo, email=email)
