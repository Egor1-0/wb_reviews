from aiogram.fsm.state import StatesGroup, State


class FirstStage(StatesGroup):
    select_promotion = State()
    warning_message = State()
    find_by_keywords = State()
    basket_with_competitors = State()
    basket_without_competitors = State()
    order_with_address = State()
    like_shop_and_product = State()


class SecondStage(StatesGroup):
    photo_or_video_review = State()
    article = State()
    nickname = State()
    details_for_transfer = State()


class UserMenu(StatesGroup):
    menu = State()

class GetUserStatistics(StatesGroup):
    get_statistics = State()