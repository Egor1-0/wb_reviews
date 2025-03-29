from aiogram.filters.callback_data import CallbackData


class AcceptRejectCallbackData(CallbackData, prefix='acrejfirst'):
    user_id: int
    accept: bool