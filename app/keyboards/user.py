from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.datas import StartSecondStageCallbackData


def start_second_stage(promotion_id: int):
    kb = InlineKeyboardBuilder()
    kb.button(text='Приступить', callback_data=StartSecondStageCallbackData(promotion_id=promotion_id))
    kb.adjust(1)

    return kb.as_markup(resize_keyboard=True)
