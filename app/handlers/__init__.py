from aiogram import Router

from . import common

router = Router()


router.include_routers(
    common.router
)