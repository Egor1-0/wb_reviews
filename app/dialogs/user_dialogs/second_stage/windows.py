from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput, TextInput
from aiogram_dialog.widgets.kbd import Back
from aiogram_dialog.widgets.text import Const

from dialogs.user_dialogs.second_stage.callbacks import save_photo_and_video_review, \
    save_article, save_nickname, save_phone_number, save_details_for_transfer
from states.user import SecondStage

photo_or_video_review = Window(
    Const('Отправьте фото или видео товара у вас'),
    MessageInput(
        func=save_photo_and_video_review,
        content_types=[ContentType.PHOTO, ContentType.VIDEO, ContentType.ANIMATION]
    ),
    state=SecondStage.photo_or_video_review
)

article = Window(
    Const('Отправьте артикул товара'),
    TextInput(
        id='save_art',
        on_success=save_article
    ),
    Back(text=Const('Назад')),
    state=SecondStage.article
)

nickname = Window(
    Const('Отправьте ваш никнейм на WB'),
    TextInput(
        id='save_nickname',
        on_success=save_nickname
    ),
    Back(text=Const('Назад')),
    state=SecondStage.nickname
)

phone_number = Window(
    Const('Отправьте ваш номер телефона для связи'),
    TextInput(
        id='save_phonenumber',
        on_success=save_phone_number
    ),
    Back(text=Const('Назад')),
    state=SecondStage.phone_number
)

details_for_transfer = Window(
    Const('Отправьте реквизиты для перевода вам кешбэка'),
    TextInput(
        id='save_details_for_transfer',
        on_success=save_details_for_transfer,
    ),
    Back(text=Const('Назад')),
    state=SecondStage.details_for_transfer
)
