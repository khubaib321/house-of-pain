import sqlalchemy.ext.asyncio as _sa_ext
from modules.users import repository as _users_repo


class RootRepository:
    def __init__(self, session: _sa_ext.AsyncSession) -> None:
        self.users = _users_repo.UsersRepository(session)
