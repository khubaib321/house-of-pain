from typing import Self
import datetime as _dt
import pydantic as _pydantic
from modules.users import domain as _domain
from modules.shared.repository import root as _repo


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
