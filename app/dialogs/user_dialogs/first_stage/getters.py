import logging
import os
from pathlib import Path

from aiogram.enums import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment

from database.daos import PromotionDao


async def get_promotions(dialog_manager: DialogManager, **kwargs):
    promotions = await PromotionDao.find_active_promotions(dialog_manager.middleware_data['session'])
    return {'promotions': promotions,
            'exists': bool(promotions)}


async def get_selected_promotion(dialog_manager: DialogManager, **kwargs):
    promotion_id = dialog_manager.dialog_data.get('promotion_id')
    if not promotion_id:
        promotion_id = dialog_manager.start_data['promotion_id']
        dialog_manager.dialog_data['promotion_id'] = dialog_manager.start_data['promotion_id']
    promotion = await PromotionDao.find_by_id(dialog_manager.middleware_data['session'],
                                              int(promotion_id))

    photo = MediaAttachment(ContentType.PHOTO, path=os.path.join(Path(__file__).resolve().parents[4], 'images',
                                                                 f'promotion_{promotion.id}.jpg'))

    return {'promotion': promotion,
            'photo': photo}
