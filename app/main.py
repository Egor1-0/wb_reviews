import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import DefaultKeyBuilder, RedisStorage
from aiogram.enums.parse_mode import ParseMode
from aiogram_dialog import setup_dialogs
from redis.asyncio.client import Redis

import handlers
import dialogs
from database.core import async_sessionmaker
from middlewares.dependencies import DependenciesMiddleware
from utils.setup_logging import setup_logging
from config import config


async def main():
    redis = Redis(
        host=config.redis.REDIS_HOST,
        port=config.redis.REDIS_PORT
    )
    storage = RedisStorage(redis=redis,
                           key_builder=DefaultKeyBuilder(with_destiny=True))
    logging.info(await redis.ping())  # тест, что редис запустился и работает

    bot = Bot(token=config.bot.TOKEN.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=storage)

    dp.include_routers(handlers.router, dialogs.router)
    dp.update.middleware(DependenciesMiddleware(sessionmaker=async_sessionmaker))

    await bot.delete_webhook(drop_pending_updates=True)

    setup_dialogs(dp)  # настройка диалогов
    await dp.start_polling(bot)


if __name__ == '__main__':
    setup_logging()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
