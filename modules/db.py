from typing import AsyncGenerator
import logging as _logging
import sqlalchemy.ext.asyncio as _sa_ext
from modules import settings as _settings
from modules.shared.repository import root as _root

_logger = _logging.getLogger(__name__)

DATABASE_URL = _settings.get_settings().database_url

engine = _sa_ext.create_async_engine(DATABASE_URL, echo=False, future=True)

SessionMaker: _sa_ext.async_sessionmaker[_sa_ext.AsyncSession] = (
    _sa_ext.async_sessionmaker(engine, expire_on_commit=False)
)


async def get_repo() -> AsyncGenerator[_root.RootRepository, None]:
    async with SessionMaker() as session:
        try:
            async with session.begin():
                yield _root.RootRepository(session)

        except Exception:
            _logger.exception("Pain detected; transaction rolled back.")
            raise
