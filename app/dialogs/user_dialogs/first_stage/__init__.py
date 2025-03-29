from aiogram_dialog import Dialog

from dialogs.user_dialogs.first_stage.windows import select_promotion, find_by_keywords, basket_with_competitors, \
    basket_without_competitors, order_with_address, like_shop_and_product

router = Dialog(select_promotion,
                find_by_keywords,
                basket_with_competitors,
                basket_without_competitors,
                order_with_address,
                like_shop_and_product,
                )
