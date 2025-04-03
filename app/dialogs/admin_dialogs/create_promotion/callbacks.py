import os
from pathlib import Path

import aiofiles
from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.api.internal import MediaWidget
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput

from database.daos import PromotionDao
from database.schemas.promotion import CreatePromotion


async def save_name(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, data: str):
    dialog_manager.dialog_data['name'] = data
    await dialog_manager.next()


async def save_keywords(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, data: str):
    dialog_manager.dialog_data['keywords'] = data
    await dialog_manager.next()


async def save_promotion_photo(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    dialog_manager.dialog_data['photo_id'] = message.photo[-1].file_id
    await dialog_manager.next()



async def save_count_and_add_to_db(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                                   data: str):
    count = int(data)
    keywords = dialog_manager.dialog_data['keywords']
    photo_id = dialog_manager.dialog_data['photo_id']
    name = dialog_manager.dialog_data['name']

    promotion = CreatePromotion(name=name, keywords=keywords, count=count)
    promotion = await PromotionDao.create(dialog_manager.middleware_data['session'], promotion)

    file = await message.bot.get_file(photo_id)

    await message.bot.download_file(file.file_path, os.path.join(Path(__file__).resolve().parents[4], 'images',
                                                                 f'promotion_{promotion.id}.jpg'))

    await message.answer('Акция создана')
    await dialog_manager.done()


async def error_count(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, error: ValueError):
    await message.answer('Введите число!')
