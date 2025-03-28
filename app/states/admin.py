from aiogram.fsm.state import StatesGroup, State


class Menu(StatesGroup):
    menu = State()


class CreatePromotion(StatesGroup):
    get_name = State()
    get_keywords = State()
    get_count = State()


class GetStatistics(StatesGroup):
    select_promotion = State()
    get_statistics = State()
