from aiogram.enums import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment

from utils.create_statistics import create_statistics_csv


async def get_path_file(dialog_manager: DialogManager, **kwargs):
    await create_statistics_csv(dialog_manager.middleware_data['session'])

    file = MediaAttachment(type=ContentType.DOCUMENT, path=f'statistics.csv')
    return {"file": file}
