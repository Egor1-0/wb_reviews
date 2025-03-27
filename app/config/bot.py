from pydantic import SecretStr

from .base import BaseConfig


class BotConfig(BaseConfig):
    TOKEN: SecretStr