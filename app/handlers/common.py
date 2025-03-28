from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.ext.asyncio import AsyncSession

from database.daos import UserDao
from database.models import User
from database.schemas.user import CreateUser

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, session: AsyncSession, user_db: User): #, dialog_manager: DialogManager):
    if not user_db:
        user = CreateUser(id=message.from_user.id)
        await UserDao.create(session, obj=user)
    # await dialog_manager.start(state=MainWindow.start, mode=StartMode.RESET_STACK)
    await message.answer('hello world')