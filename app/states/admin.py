from aiogram.fsm.state import StatesGroup, State


class CreatePromotion(StatesGroup):
    get_name = State()
    get_keywords = State()
    get_count = State()