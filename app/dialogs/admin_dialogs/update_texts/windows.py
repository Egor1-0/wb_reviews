from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Format, Const

from dialogs.admin_dialogs.update_texts.callbacks import save_new_start_text
from dialogs.user_dialogs.menu.getters import get_start_text
from states.admin import UpdateText

update_text = Window(
    Format('{text}'),
    TextInput(
        id='get_text',
        on_success=save_new_start_text
    ),
    Cancel(text=Const('Отмена')),
    getter=get_start_text,
    state=UpdateText.get_text
)
