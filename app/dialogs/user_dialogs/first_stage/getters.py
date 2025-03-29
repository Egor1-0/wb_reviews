from aiogram_dialog import DialogManager

from database.daos import PromotionDao


async def get_promotions(dialog_manager: DialogManager, **kwargs):
    promotions = await PromotionDao.find_all(dialog_manager.middleware_data['session'])
    return {'promotions': promotions,
            'exists': bool(promotions)}


async def get_selected_promotion(dialog_manager: DialogManager, **kwargs):
    promotion = await PromotionDao.find_by_id(dialog_manager.middleware_data['session'],
                                              int(dialog_manager.dialog_data['promotion_id']))
    return {'promotion': promotion}