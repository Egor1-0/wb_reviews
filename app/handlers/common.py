from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.ext.asyncio import AsyncSession

from database.daos import UserDao
from database.models import User
from database.schemas.user import CreateUser
from states.user import FirstStage, SecondStage

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, session: AsyncSession, user_db: User, dialog_manager: DialogManager):
    if not user_db:
        user = CreateUser(id=message.from_user.id)
        await UserDao.create(session, obj=user)
    await dialog_manager.start(state=FirstStage.select_promotion, mode=StartMode.RESET_STACK)


@router.callback_query(F.data == 'start_second_stage')
async def start_first_stage(callback: CallbackQuery, dialog_manager: DialogManager):
    # await callback.message.delete()
    await dialog_manager.start(state=SecondStage.photo_or_video_review, mode=StartMode.RESET_STACK, data={'promotion_id': 123}) # todo
