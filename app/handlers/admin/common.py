from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import keyboards.admin as kb
from states.admin import CreatePromotion

router = Router()


@router.message(Command('admin'))
async def main_admin_menu_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Вы в админ-панели', reply_markup=kb.start_menu)
