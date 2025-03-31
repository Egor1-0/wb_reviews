from aiogram_dialog import Dialog

from dialogs.user_dialogs.promotions_stats.windows import get_statistics_promotion

router = Dialog(get_statistics_promotion)
