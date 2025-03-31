from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from states.user import UserMenu, FirstStage, GetUserStatistics

main_menu = Window(
    Const('Выберите пункт меню'),
    Start(text=Const('Мои активные акции'),
          id='my_active_promotions',
          state=GetUserStatistics.get_statistics),
    Start(text=Const('Учавствовать в акции'),
          id='go_promotion',
          state=FirstStage.select_promotion),
    state=UserMenu.menu
)
