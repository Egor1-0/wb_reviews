from aiogram_dialog import DialogManager

from database.daos import PromotionDao, ParticipationDao


async def get_active_promotions(dialog_manager: DialogManager, **kwargs):
    promotions = await ParticipationDao.find_active_promotions(dialog_manager.middleware_data['session'],
                                                               dialog_manager.middleware_data['event_from_user'].id)
    return {'promotions': promotions,
            'exists': bool(promotions)}