from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Next, Back
from aiogram_dialog.widgets.text import Const

from states.admin import CreatePromotion

get_name_promotion_window = Window(
    Const('Введите название акции'),
    TextInput(
        id='get_name',
        on_success=Next(on_click=...)
    ),
    Cancel(text=Const('Отмена')),
    state=CreatePromotion.get_name
)

get_keywords_window = Window(
    Const('Введите ключевые слова для поиска (они отобразятся пользователю как слова для поиска)'),
    TextInput(
        id='get_keywords',
        on_success=Next(on_click=...)
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=CreatePromotion.get_keywords
)

get_count_window = Window(
    Const('Введите количество требуемых отзывов'),
    TextInput(
        id='get_keywords',
        type_factory=int,
        on_error=...,
        on_success=Next(on_click=...)
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=CreatePromotion.get_count
)
