import sqlalchemy.ext.asyncio as _sa_ext


class BaseRepository:
    def __init__(self, session: _sa_ext.AsyncSession) -> None:
        self.__session__: _sa_ext.AsyncSession = session

    @property
    def _session(self) -> _sa_ext.AsyncSession:
        return self.__session__
