from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.ext.asyncio import AsyncSession

from database.daos import ParticipationDao
from database.schemas.status import Status
from keyboards.datas import AcceptRejectFirstStageCallbackData
from keyboards.user import start_second_stage
from states.admin import Menu

router = Router()


@router.message(Command('admin'))
async def main_admin_menu_handler(message: Message, state: FSMContext, dialog_manager: DialogManager):
    await state.clear()
    await dialog_manager.start(state=Menu.menu, mode=StartMode.RESET_STACK)


@router.callback_query(AcceptRejectFirstStageCallbackData.filter(F.accept == True))
async def accept_first_stage(callback: CallbackQuery, callback_data: AcceptRejectFirstStageCallbackData, bot: Bot):
    await bot.send_message(callback_data.user_id, 'Вам одобрена заявка. Вы готовы приступить ко второму шагу?',
                           reply_markup=start_second_stage(callback_data.promotion_id))
    await callback.answer('Уведомление отправлено пользователю')
    await callback.message.delete_reply_markup()


@router.callback_query(AcceptRejectFirstStageCallbackData.filter(F.accept == False))
async def accept_first_stage(callback: CallbackQuery, callback_data: AcceptRejectFirstStageCallbackData, bot: Bot,
                             session: AsyncSession):
    await bot.send_message(callback_data.user_id, 'Вам отказано участие в акции')
    await ParticipationDao.update(session, {'user_id': callback_data.user_id, 'promotion_id': callback_data.promotion_id},
                                  {'status': Status.CANCELED})
    await callback.answer('Уведомление отправлено пользователю')
    await callback.message.delete_reply_markup()
