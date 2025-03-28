from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button


async def save_name(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, data: str):
    dialog_manager.dialog_data['name'] = data
    await dialog_manager.next()


async def save_keywords(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, data: str):
    dialog_manager.dialog_data['keywords'] = data
    await dialog_manager.next()


async def save_count_and_add_to_db(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, data: str):
    count = data
    keywords = dialog_manager.dialog_data['keywords']
    name = dialog_manager.dialog_data['name']

    ... # todo save to db

    await message.answer('Акция создана')
    await dialog_manager.done()


async def error_count(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, error: ValueError):
    await message.answer('Введите число!')