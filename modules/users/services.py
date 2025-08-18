from typing import Self
import datetime as _dt
import pydantic as _pydantic
from modules.users import domain as _domain
from modules.base.repository import root as _repo


class UserRead(_pydantic.BaseModel):
    id: int
    email: str
    full_name: str
    created_at: _dt.datetime
    updated_at: _dt.datetime

    @classmethod
    def from_domain(cls, user: _domain.User) -> Self:
        return cls(
            id=user.id,
            email=user.email,
            full_name=user.full_name,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )


async def get_users(repo: _repo.RootRepository) -> list[UserRead]:
    return [UserRead.from_domain(user) for user in await repo.users.get_users()]


async def get_user_by_id(repo: _repo.RootRepository, user_id: int) -> UserRead:
    return await repo.users.get_user_by_id(user_id=user_id)


async def get_user_by_email(repo: _repo.RootRepository, email: str) -> UserRead:
    return await repo.users.get_user_by_email(email=email)


async def email_exists(repo: _repo.RootRepository, email: str) -> bool:
    return await repo.users.email_exists(email=email)


async def search_user_by_name(repo: _repo.RootRepository, name: str) -> list[UserRead]:
    return await repo.users.search_by_name(name=name)
