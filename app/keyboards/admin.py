from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Создать акцию', callback_data='create_promotion')],
    [InlineKeyboardButton(text='Получить данные по акции', callback_data='get_promotion_info')],
], resize_keyboard=True
)
