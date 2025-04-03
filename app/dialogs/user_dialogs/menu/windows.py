from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const, Format

from dialogs.user_dialogs.menu.getters import get_start_text
from states.user import UserMenu, FirstStage, GetUserStatistics

main_menu = Window(
    Format('{text}'),
    Start(text=Const('Мои активные акции'),
          id='my_active_promotions',
          state=GetUserStatistics.get_statistics),
    Start(text=Const('Учавствовать в акции'),
          id='go_promotion',
          state=FirstStage.select_promotion),
    getter=get_start_text,
    state=UserMenu.menu
)
