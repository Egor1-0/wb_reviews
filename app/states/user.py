from aiogram.fsm.state import StatesGroup, State


class FirstStage(StatesGroup):
    select_promotion = State()
    find_by_keywords = State()
    basket_with_competitors = State()
    basket_without_competitors = State()
    order_with_address = State()
    like_shop_and_product = State()


class SecondStage(StatesGroup):
    photo_or_video_review = State()
    screenshot_review = State()
    article = State()
    nickname = State()
    phone_number = State()
    details_for_transfer = State()