from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Cancel, Back
from aiogram_dialog.widgets.text import Const

from states.admin import CreatePromotion
from dialogs.admin_dialogs.create_promotion.callbacks import save_name, save_keywords, save_count_and_add_to_db, \
    error_count, save_promotion_photo


get_name_promotion_window = Window(
    Const('Введите название акции'),
    TextInput(
        id='get_name',
        on_success=save_name
    ),
    Cancel(text=Const('Отмена')),
    state=CreatePromotion.get_name
)

get_keywords_window = Window(
    Const('Введите ключевые слова для поиска (они отобразятся пользователю как слова для поиска)'),
    TextInput(
        id='get_keywords',
        on_success=save_keywords
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=CreatePromotion.get_keywords
)

get_promotion_photo = Window(
    Const('Отправьте фото к акции'),
    MessageInput(
        func=save_promotion_photo,
        content_types=[ContentType.PHOTO]
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=CreatePromotion.get_photo
)


get_count_window = Window(
    Const('Введите количество требуемых отзывов'),
    TextInput(
        id='get_count',
        type_factory=int,
        on_error=error_count,
        on_success=save_count_and_add_to_db
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=CreatePromotion.get_count
)
