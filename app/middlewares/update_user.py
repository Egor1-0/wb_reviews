from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

from database.core import async_sessionmaker
from database.daos import UserDao


class UpdateUser(BaseMiddleware):
    def __init__(self, sessionmaker):
        self.sessiomnmaker = sessionmaker


    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user: User = data.get("event_from_user")
        async with async_sessionmaker() as session:
            user_db = await UserDao.find_by_id(session, user.id)
            if user.username != user_db.username:
                await UserDao.update(session, {'id': user.id}, {'username': user.username})

        await handler(event, data)