import datetime as _dt
import sqlalchemy as _sa
import sqlalchemy.orm as _sa_orm


class BaseModel(_sa_orm.DeclarativeBase):
    id: _sa_orm.Mapped[int] = _sa_orm.mapped_column(_sa.BigInteger, primary_key=True)

    created_at: _sa_orm.Mapped[_dt.datetime] = _sa_orm.mapped_column(
        _sa.DateTime,
        nullable=False,
        server_default=_sa.func.timezone("utc", _sa.func.now()),
    )
    updated_at: _sa_orm.Mapped[_dt.datetime] = _sa_orm.mapped_column(
        _sa.DateTime,
        nullable=False,
        onupdate=_sa.func.timezone("utc", _sa.func.now()),
        server_default=_sa.func.timezone("utc", _sa.func.now()),
    )
