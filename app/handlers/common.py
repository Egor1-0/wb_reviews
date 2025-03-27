import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message): #, dialog_manager: DialogManager):
    # await dialog_manager.start(state=MainWindow.start, mode=StartMode.RESET_STACK)
    await message.answer('hello world')