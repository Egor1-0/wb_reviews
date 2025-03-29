from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.datas import AcceptRejectCallbackData

start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Создать акцию', callback_data='create_promotion')],
    [InlineKeyboardButton(text='Получить данные по акции', callback_data='get_promotion_info')],
], resize_keyboard=True
)


def get_accept_reject_keyboard(user_id: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='Принять', callback_data=AcceptRejectCallbackData(accept=True, user_id=user_id))
    kb.button(text='отказать', callback_data=AcceptRejectCallbackData(accept=False, user_id=user_id))
    kb.adjust(1)

    return kb.as_markup(resize_keyboard=True)