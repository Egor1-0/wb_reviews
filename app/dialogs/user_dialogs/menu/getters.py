from aiogram_dialog import DialogManager

from database.daos.texts_dao import TextsDao


async def get_start_text(dialog_manager: DialogManager, **kwargs):
    texts = await TextsDao.find_by_id(dialog_manager.middleware_data['session'], 1)
    return {
        'text': texts.start_text
    }