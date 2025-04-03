from aiogram_dialog import Dialog

from dialogs.user_dialogs.second_stage.windows import photo_or_video_review, article, nickname, \
    details_for_transfer

router = Dialog(
    photo_or_video_review,
    article,
    nickname,
    details_for_transfer,
)
