from aiogram import F
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, ScrollingGroup, Column, Select
from aiogram_dialog.widgets.text import Format, Const, Case, List, Jinja

from dialogs.user_dialogs.promotions_stats.callbacks import continue_task
from dialogs.user_dialogs.promotions_stats.getters import get_active_promotions
from states.user import GetUserStatistics

select_widget = Select(
    Format("{item.promotion.name}"),
    id="select_promotion",
    on_click=continue_task,
    item_id_getter=lambda item: item.id,
    items="promotions",
    when='exists'
)

get_statistics_promotion = Window(
    Case(
        texts={
            True: Format('Ваши активные акции (вы можете нажать на акцию, чтобы вернуться к ней):\n\n') +
                  List(Jinja('{{item.promotion.name}} - {{ "первый этап" if item.status == "FIRST_STAGE" else "второй этап" }}')
                       , id='text_promotions', items='promotions'),
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
    Cancel(text=Const('В меню')),
    getter=get_active_promotions,
    state=GetUserStatistics.get_statistics
)
