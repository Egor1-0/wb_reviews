from pydantic import BaseModel

from .bot import BotConfig
from .database import DatabaseConfig
from .redis import RedisConfig


class AppConfig(BaseModel):
    bot: BotConfig = BotConfig()
    database: DatabaseConfig = DatabaseConfig()
    redis: RedisConfig = RedisConfig()

config = AppConfig()