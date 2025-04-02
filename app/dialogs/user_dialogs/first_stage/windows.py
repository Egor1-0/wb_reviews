from aiogram import F
from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Column, Cancel, Back, Next
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

warning_message = Window(
    Format('Обязательные условия: ⬇\n\n'
           '‼отзывы оставлять в графе: «поделитесь впечатлениями»\n\n'
           '1. Найти товар по ключевой фразе: \n{promotion.keywords}\n\n'
           '2. Добавить товар в корзину, и пару товаров конкурентов;\n\n'
           '3.Через 3-5 минут, товар конкурентов удалить из корзины;\n\n'
           '5. Заказать наш товар. Прислать скриншот заказа, где виден ПВЗ '
           '(из раздела «Доставки» в личном кабинете Wildberries);\n\n'
           '6. Добавить магазин и товар в избранное (т.е. поставить лайк);\n\n'
           '7. Выкупить товар, т.е. забрать с ПВЗ (без возврата!);\n\n'
           '8. ❌Товар не возвращать!❌ Прислать видео как вы разрезаете 2 штрихкода (ШК от ВБ и ШК поставщика видео '
           'товара с открытой крышкой фото 📸 от 1 до 3шт со вскрытой упаковкой;);\n\n'
           '9. Прислать скриншот отзыва, далее лайкнуть чужой отзыв с 5🌟;\n\n'
           '10. Выплаты будем делать через день после публикации отзыва в карточке товара!\n\n'
           'Нажмите продолжить, если готовы начать'),
    Next(text=Const('Продолжить')),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    getter=get_selected_promotion,
    state=FirstStage.warning_message
)
find_by_keywords = Window(
    Format('Отправьте скриншот, на котором видно, что вы нашли товар по ключевым словам: "{promotion.keywords}"'),
    MessageInput(
        func=save_find_by_keywords_photo,
        content_types=[ContentType.PHOTO]
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
        content_types=[ContentType.PHOTO]
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=FirstStage.basket_with_competitors
)

basket_without_competitors = Window(
    Const('Отправьте скриншот, сделанный через 5 минут, где вы удалили товары конкурентов из корзины'),
    MessageInput(
        func=save_basket_without_competitors_photo,
        content_types=[ContentType.PHOTO]
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=FirstStage.basket_without_competitors
)

order_with_address = Window(
    Const('Отправьте скриншот, где виден заказ с адресом ПВЗ'),
    MessageInput(
        func=save_order_with_address_photo,
        content_types=[ContentType.PHOTO]
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=FirstStage.order_with_address
)

like_shop_and_product = Window(
    Const('Отправьте скриншот, где видно, что вы поставили лайк товару и магазину'),
    MessageInput(
        func=save_like_shop_and_product_photo,
        content_types=[ContentType.PHOTO]
    ),
    Back(text=Const('Назад')),
    Cancel(text=Const('Отмена')),
    state=FirstStage.like_shop_and_product
)
