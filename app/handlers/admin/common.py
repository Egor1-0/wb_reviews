from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from states.admin import Menu

router = Router()


@router.message(Command('admin'))
async def main_admin_menu_handler(message: Message, state: FSMContext, dialog_manager: DialogManager):
    await state.clear()
    await dialog_manager.start(state=Menu.menu, mode=StartMode.RESET_STACK)
