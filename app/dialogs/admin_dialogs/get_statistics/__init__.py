from aiogram_dialog import Dialog

from .windows import select_promotion_to_get_statistics, get_statistics_promotion

router = Dialog(select_promotion_to_get_statistics, get_statistics_promotion)
