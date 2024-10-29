from pydantic import SecretStr

from .base import EnvSettings


class TelegramConfig(EnvSettings, env_prefix="TELEGRAM_"):
    bot_token: SecretStr
    support_url: str
    gpt_token: SecretStr
    proxy: str
    admins: list[int]
    channel_id: SecretStr
    channel_url: str
