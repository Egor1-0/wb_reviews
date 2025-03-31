from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from database.daos import ParticipationDao
from states.user import FirstStage

from database.schemas.status import Status
from states.user import SecondStage


async def continue_task(callback: CallbackQuery, button: Button, dialog_manager: DialogManager, data: str):
    participation = await ParticipationDao.find_by_id_with_promotion(dialog_manager.middleware_data['session'], int(data))
    if participation.status == Status.FIRST_STAGE:
        await dialog_manager.start(FirstStage.find_by_keywords, data={'promotion_id': participation.promotion.id})
    elif participation.status == Status.SECOND_STAGE:
        await dialog_manager.start(SecondStage.photo_or_video_review, data={'promotion_id': participation.promotion.id})