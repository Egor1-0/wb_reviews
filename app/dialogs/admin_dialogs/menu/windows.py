from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from states.admin import CreatePromotion, Menu, GetStatistics, UpdateText

main_menu = Window(
    Const('Выберите пункт меню'),
    Start(text=Const('Создать новую акцию'),
          id='create_promotion',
          state=CreatePromotion.get_name),
    Start(text=Const('Получить статистику по акции'),
          id='get_stats',
          state=GetStatistics.get_statistics),
    Start(text=Const('Обновить стартовый текст'),
          id='upd_text',
          state=UpdateText.get_text),
    state=Menu.menu
)
