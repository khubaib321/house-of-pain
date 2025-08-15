import datetime as _dt
import pydantic as _pydantic


class Persistable(_pydantic.BaseModel):
    id: int
    created_at: _dt.datetime
    updated_at: _dt.datetime
