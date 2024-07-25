from functools import lru_cache

from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env")

    secret_key: SecretStr = Field(init=False)
    debug: bool = Field(init=False)
    allowed_hosts: list[str] = Field(init=False)


class Settings(BaseModel):
    app: AppSettings = Field(default_factory=AppSettings)


@lru_cache(1)
def get_settings() -> Settings:
    return Settings()
