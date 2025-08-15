import sqlalchemy as _sa
from modules.users import models as _models
from modules.users import domain as _domain
from modules.shared.repository import base as _base_repo


class UsersRepository(_base_repo.BaseRepository):
    async def get_users(self) -> list[_domain.User]:
        result = await self._session.execute(
            _sa.select(_models.User).where(_models.User.is_active.is_(True))
        )

        return [user.to_domain() for user in result.all()]
