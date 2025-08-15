from typing import AsyncGenerator
import logging as _logging
import sqlalchemy as _sa
import sqlalchemy.orm as _sa_orm
import sqlalchemy.ext.asyncio as _sa_ext
from modules import settings as _settings
from modules.shared.repository import root as _root

_logger = _logging.getLogger(__name__)

_engine = _sa_ext.create_async_engine(
    _settings.get_settings().database_url, echo=False, future=True
)
_engine_sync = _sa.create_engine(
    _settings.get_settings().database_url_sync, echo=False, future=True
)

SessionMaker: _sa_ext.async_sessionmaker[_sa_ext.AsyncSession] = (
    _sa_ext.async_sessionmaker(_engine, expire_on_commit=False)
)
SessionMakerSync: _sa_orm.Session = _sa_orm.sessionmaker(
    bind=_engine_sync, expire_on_commit=False
)


async def get_session() -> AsyncGenerator[_sa_ext.AsyncSession, None]:
    async with SessionMaker() as session:
        try:
            yield session
            session.commit()

        except Exception:
            _logger.exception("Pain detected; transaction rolled back.")
            raise


async def get_repo() -> AsyncGenerator[_root.RootRepository, None]:
    async with SessionMaker() as session:
        try:
            async with session.begin():
                yield _root.RootRepository(session)

        except Exception:
            _logger.exception("Pain detected; transaction rolled back.")
            raise
