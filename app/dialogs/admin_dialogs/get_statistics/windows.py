from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

from dialogs.admin_dialogs.get_statistics.getters import get_path_file
from states.admin import GetStatistics


get_statistics_promotion = Window(
    DynamicMedia('file'),
    Format('Статистика отправлена'),
    Cancel(text=Const('В меню')),
    getter=get_path_file,
    state=GetStatistics.get_statistics
)
