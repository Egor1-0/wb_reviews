from aiogram import Router

from . import common
from . import admin

router = Router()


router.include_routers(
    common.router,
    admin.router
)