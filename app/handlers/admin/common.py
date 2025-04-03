from datetime import datetime

from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.ext.asyncio import AsyncSession

from config import config
from database.daos import ParticipationDao, PromotionDao
from database.schemas.status import Status
from keyboards.datas import AcceptRejectFirstStageCallbackData, AcceptRejectSecondStageCallbackData
from keyboards.user import start_second_stage
from states.admin import Menu

router = Router()

router.message.filter(F.from_user.id == config.bot.ADMINISTRATION)
router.callback_query.filter(F.from_user.id == config.bot.ADMINISTRATION)


@router.message(Command('admin'))
async def main_admin_menu_handler(message: Message, state: FSMContext, dialog_manager: DialogManager):
    await state.clear()
    await dialog_manager.start(state=Menu.menu, mode=StartMode.RESET_STACK)


# first stage


@router.callback_query(AcceptRejectFirstStageCallbackData.filter(F.accept == True))
async def accept_first_stage(callback: CallbackQuery, callback_data: AcceptRejectFirstStageCallbackData,
                             bot: Bot, session: AsyncSession):
    await ParticipationDao.update(session,
                                  {'user_id': callback_data.user_id, 'promotion_id': callback_data.promotion_id},
                                  {'status': Status.SECOND_STAGE})
    await bot.send_message(callback_data.user_id, 'Вам одобрена заявка. Вы готовы приступить ко второму шагу?',
                           reply_markup=start_second_stage(callback_data.promotion_id))
    await callback.message.answer('Уведомление отправлено пользователю')
    await callback.message.delete_reply_markup()


@router.callback_query(AcceptRejectFirstStageCallbackData.filter(F.accept == False))
async def reject_first_stage(callback: CallbackQuery, callback_data: AcceptRejectFirstStageCallbackData, bot: Bot,
                             session: AsyncSession):
    promotion = await PromotionDao.find_by_id(session, callback_data.promotion_id)
    await bot.send_message(callback_data.user_id, f'Вам отказано участие в акции {promotion.name}')
    await ParticipationDao.update(session,
                                  {'user_id': callback_data.user_id, 'promotion_id': callback_data.promotion_id},
                                  {'status': Status.CANCELED})
    await callback.message.answer('Уведомление отправлено пользователю')
    await callback.message.delete_reply_markup()


# second stage


@router.callback_query(AcceptRejectSecondStageCallbackData.filter(F.accept == True))
async def accept_second_stage(callback: CallbackQuery, callback_data: AcceptRejectSecondStageCallbackData, bot: Bot,
                              session: AsyncSession):
    promotion = await PromotionDao.find_by_id(session, callback_data.promotion_id)
    await PromotionDao.update(session, {'id': promotion.id}, {'count': promotion.count - 1})
    await bot.send_message(callback_data.user_id,
                           f'Вам перевели кешбэк за товар {promotion.name} по указанным реквизитам')
    await ParticipationDao.update(session,
                                  {'user_id': callback_data.user_id, 'promotion_id': callback_data.promotion_id},
                                  {'status': Status.COMPLETED, "ended_at": datetime.now()})
    await callback.message.answer('Уведомление отправлено пользователю')
    await callback.message.delete_reply_markup()


@router.callback_query(AcceptRejectSecondStageCallbackData.filter(F.accept == False))
async def reject_second_stage(callback: CallbackQuery, callback_data: AcceptRejectFirstStageCallbackData, bot: Bot,
                              session: AsyncSession):
    promotion = await PromotionDao.find_by_id(session, callback_data.promotion_id)
    await bot.send_message(callback_data.user_id, f'Вам отказано участие в акции {promotion.name}')
    await ParticipationDao.update(session,
                                  {'user_id': callback_data.user_id, 'promotion_id': callback_data.promotion_id},
                                  {'status': Status.CANCELED})
    await callback.message.answer('Уведомление отправлено пользователю')
    await callback.message.delete_reply_markup()
