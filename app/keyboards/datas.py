from aiogram.filters.callback_data import CallbackData


class AcceptRejectFirstStageCallbackData(CallbackData, prefix='acrejfirst'):
    user_id: int
    accept: bool

class AcceptRejectSecondStageCallbackData(CallbackData, prefix='acrejsecond'):
    user_id: int
    accept: bool
