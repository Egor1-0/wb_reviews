from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from states.admin import GetStatistics
from utils.create_statistics import create_statistics_by_promotion_id


async def save_statistics_by_promotion_id(callback: CallbackQuery, button: Button, dialog_manager: DialogManager, data: str):
    dialog_manager.dialog_data['promotion_id'] = data
    await create_statistics_by_promotion_id(dialog_manager.middleware_data['session'], int(data))
    await dialog_manager.switch_to(GetStatistics.get_statistics)