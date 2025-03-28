from aiogram_dialog import Dialog

from dialogs.admin_dialogs.create_promotion.windows import get_name_promotion_window, get_keywords_window, \
    get_count_window

router = Dialog(get_name_promotion_window, get_keywords_window, get_count_window)
