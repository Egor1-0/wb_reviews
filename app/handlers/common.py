from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.ext.asyncio import AsyncSession

from database.daos import UserDao, ParticipationDao
from database.models import User
from database.schemas.status import Status
from database.schemas.user import CreateUser
from keyboards.datas import StartSecondStageCallbackData
from states.user import SecondStage, UserMenu

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, session: AsyncSession, user_db: User, dialog_manager: DialogManager):
    if not user_db:
        user = CreateUser(id=message.from_user.id)
        await UserDao.create(session, obj=user)
    await dialog_manager.start(state=UserMenu.menu, mode=StartMode.RESET_STACK)


@router.callback_query(StartSecondStageCallbackData.filter())
async def start_first_stage(callback: CallbackQuery, dialog_manager: DialogManager, session: AsyncSession,
                            callback_data: StartSecondStageCallbackData):
    await ParticipationDao.update(session, {'user_id': callback.from_user.id, 'promotion_id': callback_data.promotion_id},
                                  {'status': Status.SECOND_STAGE})
    await dialog_manager.start(state=SecondStage.photo_or_video_review, mode=StartMode.RESET_STACK,
                               data={'promotion_id': callback_data.promotion_id})
