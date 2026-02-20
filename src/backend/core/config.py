from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseModel):
    pass


class DatabaseConfig(BaseModel):
    port: int = 5432
    host: str


class Settings(BaseSettings):
    app: AppConfig = AppConfig()
    db: DatabaseConfig = DatabaseConfig()

    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
    )
