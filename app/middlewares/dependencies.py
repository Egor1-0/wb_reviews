from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from sqlalchemy.ext.asyncio import AsyncSession

from database.daos import UserDao


class DependenciesMiddleware(BaseMiddleware):
    def __init__(self, sessionmaker):
        self.sessionmaker = sessionmaker

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user: User = data.get("event_from_user")
        async with self.sessionmaker() as session: # type: AsyncSession
            user_db = await UserDao.find_by_id(session, model_id=user.id)
            data['user_db'] = user_db
            data['session'] = session
            return await handler(event, data)
