from aiogram.enums import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment

from database.daos import PromotionDao


async def get_promotions(dialog_manager: DialogManager, **kwargs):
    promotions = await PromotionDao.find_all(dialog_manager.middleware_data['session'])
    return {'promotions': promotions,
            'exists': bool(promotions)}


async def get_path_file(dialog_manager: DialogManager, **kwargs):
    promotion_id = dialog_manager.dialog_data['promotion_id']
    file = MediaAttachment(type=ContentType.DOCUMENT, path=f'statistics_{promotion_id}.csv')
    return {"file": file}
