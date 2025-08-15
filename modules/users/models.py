from typing import Self
import sqlalchemy as _sa
import sqlalchemy.orm as _sa_orm
from modules.shared import model as _model
from modules.users import domain as _domain


class User(_model.BaseModel):
    __tablename__ = "users"

    email: _sa_orm.Mapped[str] = _sa_orm.mapped_column(
        _sa.String(length=255), unique=True, nullable=False
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

    is_active: _sa_orm.Mapped[bool] = _sa_orm.mapped_column(_sa.Boolean, default=True)

    def to_domain(self) -> _domain.User:
        return _domain.User(
            id=self.id,
            email=self.email,
            f_name=self.first_name,
            m_name=self.middle_name,
            l_name=self.last_name,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def from_domain(cls, domain: _domain.BaseUser) -> Self:
        return cls(
            email=domain.email,
            is_active=domain.is_active,
            last_name=domain.last_name,
            first_name=domain.first_name,
            middle_name=domain.middle_name,
        )
