import pydantic as _pydantic
from modules.shared import domain as _domain


class BaseUser(_pydantic.BaseModel):
    email: str
    last_name: str
    first_name: str | None = None
    middle_name: str | None = None
    is_active: bool

    @property
    def full_name(self) -> str:
        return " ".join(
            filter(lambda n: n, [self.first_name, self.middle_name, self.last_name])
        )


class User(BaseUser, _domain.Persistable):
    pass
