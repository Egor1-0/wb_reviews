from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput

from database.daos.texts_dao import TextsDao


async def save_new_start_text(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, data: str):
    await TextsDao.update(dialog_manager.middleware_data['session'], {'id': 1}, {'start_text': data})
    await message.answer('Текст обновлен!')
    await dialog_manager.done()