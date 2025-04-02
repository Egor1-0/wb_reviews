from aiogram import F
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, ScrollingGroup, Select, Column
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Case, Format

from dialogs.admin_dialogs.get_statistics.callbacks import save_statistics_by_promotion_id
from dialogs.admin_dialogs.get_statistics.getters import get_promotions, get_path_file
from states.admin import GetStatistics

select_widget = Select(
    Format("{item.name}"),
    id="select_promotion",
    item_id_getter=lambda item: item.id,
    items="promotions",
    on_click=save_statistics_by_promotion_id,
    when='exists'
)

select_promotion_to_get_statistics = Window(
    Case(
        texts={
            True: Const('Выберите акцию для статистики'),
            False: Const('Вы еще не добавили акции')
        },
        selector='exists'
    ),
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
    state=GetStatistics.select_promotion
)

get_statistics_promotion = Window(
    DynamicMedia('file'),
    Format('Статистика отправлена'),
    Cancel(text=Const('В меню')),
    getter=get_path_file,
    state=GetStatistics.get_statistics
)
