from aiogram_dialog import DialogManager

from database.daos import PromotionDao


async def get_promotions(dialog_manager: DialogManager, **kwargs):
    promotions = await PromotionDao.find_all(dialog_manager.middleware_data['session'])
    return {'promotions': promotions,
            'exists': bool(promotions)}