import pydantic as _pydantic
from modules.users import enums as _enums
from modules.shared import domain as _domain


class BaseUser(_pydantic.BaseModel):
    email: str = _pydantic.EmailStr
    status: _enums.UserStatus = _enums.UserStatus.ACTIVE

    last_name: str
    first_name: str | None
    middle_name: str | None

    @property
    def full_name(self) -> str:
        return " ".join(
            filter(lambda n: n, [self.first_name, self.middle_name, self.last_name])
        )


class BaseUserWithPassword(BaseUser):
    password: str = _pydantic.Field(max_length=255)


class User(BaseUser, _domain.Persistable):
    pass
