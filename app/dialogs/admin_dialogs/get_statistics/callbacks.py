from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from states.admin import GetStatistics


async def save_promotion_id(callback: CallbackQuery, button: Button, dialog_manager: DialogManager, data: str):
    dialog_manager.dialog_data['promotion_id'] = data
    await dialog_manager.switch_to(GetStatistics.get_statistics)