from aiogram import Router

from . import admin_dialogs, user_dialogs

router = Router()

router.include_routers(admin_dialogs.router, user_dialogs.router)
