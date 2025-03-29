from aiogram import F
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Column, Cancel, Back
from aiogram_dialog.widgets.text import Const, Format

from dialogs.user_dialogs.first_stage.callbacks import save_promotion_id, save_find_by_keywords_photo, \
    save_find_by_keywords_photo, save_basket_with_competitors_photo, save_basket_without_competitors_photo, \
    save_order_with_address_photo, save_like_shop_and_product_photo
from dialogs.user_dialogs.first_stage.getters import get_promotions, get_selected_promotion
from states.user import FirstStage

select_widget = Select(
    Format("{item.name}"),
    id="select_promotion",
    item_id_getter=lambda item: item.id,
    items="promotions",
    on_click=save_promotion_id,
    when='exists'
)

select_promotion = Window(
    Const('Выберите акцию из доступных'),
    ScrollingGroup(
        select_widget,
        when=F['promotions'].len() > 7,
        height=7,
        width=1,
        id="group_accs_to_del",
    ),
    Column(
        select_widget,
        when=F['promotions'].len() <= 7
    ),
    Cancel(text=Const('Отмена')),
    getter=get_promotions,
    state=FirstStage.select_promotion
)

find_by_keywords = Window(
    Format('Отправьте скриншот, на котором видно, что вы нашли товар по ключевым словам: "{promotion.keywords}"'),
    MessageInput(
        func=save_find_by_keywords_photo,
        filter=F.photo
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    getter=get_selected_promotion,
    state=FirstStage.find_by_keywords
)

basket_with_competitors = Window(
    Const('Отправьте скриншот, на котором виден наш товар и товар конкурентов в корзине'),
    MessageInput(
        func=save_basket_with_competitors_photo,
        filter=F.photo
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=FirstStage.basket_with_competitors
)

basket_without_competitors = Window(
    Const('Отправьте скриншот, сделанный через 5 минут, где вы удалили товары конкурентов из корзины'),
    MessageInput(
        func=save_basket_without_competitors_photo,
        filter=F.photo
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=FirstStage.basket_without_competitors
)

order_with_address = Window(
    Const('Отправьте скриншот, где виден заказ с адресом ПВЗ'),
    MessageInput(
        func=save_order_with_address_photo,
        filter=F.photo
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=FirstStage.order_with_address
)

like_shop_and_product = Window(
    Const('Отправьте скриншот, где видно, что вы поставили лайк товару и магазину'),
    MessageInput(
        func=save_like_shop_and_product_photo,
        filter=F.photo
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=FirstStage.like_shop_and_product
)
