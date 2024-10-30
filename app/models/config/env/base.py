from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

_CONFIG_PATH = Path(__file__).parent.parent.parent.parent.parent / "config.env"


class EnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=_CONFIG_PATH,
        env_file_encoding="utf-8",
    )
