from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_second_stage = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Приступить', callback_data='start_second_stage')]
], resize_keyboard=True)