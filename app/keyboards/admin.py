from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.datas import AcceptRejectFirstStageCallbackData, AcceptRejectSecondStageCallbackData

start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Создать акцию', callback_data='create_promotion')],
    [InlineKeyboardButton(text='Получить данные по акции', callback_data='get_promotion_info')],
], resize_keyboard=True
)


def get_accept_reject_first_stage_keyboard(user_id: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='Принять', callback_data=AcceptRejectFirstStageCallbackData(accept=True, user_id=user_id))
    kb.button(text='Отказать', callback_data=AcceptRejectFirstStageCallbackData(accept=False, user_id=user_id))
    kb.adjust(1)

    return kb.as_markup(resize_keyboard=True)


def get_accept_reject_second_stage_keyboard(user_id: int):
    kb = InlineKeyboardBuilder()
    kb.button(text='Подтвердить перевод', callback_data=AcceptRejectSecondStageCallbackData(accept=True, user_id=user_id))
    kb.button(text='Отказать', callback_data=AcceptRejectSecondStageCallbackData(accept=False, user_id=user_id))
    kb.adjust(1)

    return kb.as_markup(resize_keyboard=True)