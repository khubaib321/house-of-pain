from typing import Self
import sqlalchemy as _sa
import sqlalchemy.orm as _sa_orm
from modules.users import enums as _enums
from modules.shared import model as _model
from modules.users import domain as _domain


class User(_model.BaseModel):
    __tablename__ = "users"

    email: _sa_orm.Mapped[str] = _sa_orm.mapped_column(
        _sa.String(length=255), unique=True, nullable=False
    )
    password: _sa_orm.Mapped[str] = _sa_orm.mapped_column(
        _sa.String(length=255), nullable=False
    )

    first_name: _sa_orm.Mapped[str] = _sa_orm.mapped_column(
        _sa.String(length=255), nullable=True
    )
    middle_name: _sa_orm.Mapped[str] = _sa_orm.mapped_column(
        _sa.String(length=255), nullable=True
    )
    last_name: _sa_orm.Mapped[str] = _sa_orm.mapped_column(
        _sa.String(length=255), nullable=False
    )

    status: _sa_orm.Mapped[_sa.Enum] = _sa_orm.mapped_column(
        _sa.String(length=255), nullable=False
    )

    def to_domain(self) -> _domain.User:
        return _domain.User(
            id=self.id,
            email=self.email,
            status=self.status,
            first_name=self.first_name,
            middle_name=self.middle_name,
            last_name=self.last_name,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def from_domain(cls, domain: _domain.BaseUserWithPassword) -> Self:
        return cls(
            email=domain.email,
            status=domain.status,
            password=domain.password,
            last_name=domain.last_name,
            first_name=domain.first_name,
            middle_name=domain.middle_name,
        )
