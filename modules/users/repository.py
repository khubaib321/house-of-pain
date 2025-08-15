import sqlalchemy as _sa
from modules.users import models as _models
from modules.users import domain as _domain
from modules.shared import errors as _errors
from modules.shared.repository import base as _base_repo


class UsersRepository(_base_repo.BaseRepository):
    async def get_users(self) -> list[_domain.User]:
        query = await self._session.execute(
            _sa.select(_models.User).where(_models.User.is_active.is_(True))
        )

        return [user.to_domain() for user in query.scalars()]

    async def get_user_by_id(self, user_id: int) -> _domain.User:
        query = await self._session.execute(
            _sa.select(_models.User).where(_models.User.id == user_id)
        )

        if result := query.scalar_one_or_none():
            return result.to_domain()

        raise _errors.UserNotFoundError("User not found")

    async def get_user_by_email(self, email: str) -> _domain.User:
        query = await self._session.execute(
            _sa.select(_models.User).where(_models.User.email == email)
        )

        if result := query.scalar_one_or_none():
            return result.to_domain()

        raise _errors.UserNotFoundError("User not found")

    async def email_exists(self, email: str) -> bool:
        query = await self._session.execute(
            _sa.select(_models.User).where(_models.User.email == email)
        )

        return bool(query.scalar_one_or_none())

    async def search_by_name(self, name: str) -> list[_domain.User]:
        query = await self._session.execute(
            _sa.select(_models.User).where(
                _sa.or_(
                    _models.User.first_name.like(f"%{name}%"),
                    _models.User.middle_name.like(f"%{name}%"),
                    _models.User.last_name.like(f"%{name}%"),
                )
            )
        )

        return [user.to_domain() for user in query.scalars()]
