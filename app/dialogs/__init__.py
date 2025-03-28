from aiogram import Router

from . import admin_dialogs

router = Router()

router.include_routers(admin_dialogs.router)
