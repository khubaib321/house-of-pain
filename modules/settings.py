import pathlib as _pl
import functools as _ft

import pydantic_settings as _ps


class Settings(_ps.BaseSettings):
    model_config = _ps.SettingsConfigDict(
        env_file=_pl.Path(__file__).parent.parent / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    env: str = "dev"
    app_name: str = "hop"
    app_version: str = "0.0.1"
    database_url: str = "localhost"


@_ft.lru_cache
def get_settings() -> Settings:
    return Settings()
