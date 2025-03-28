from aiogram import Router

from . import create_promotion, menu, get_statistics

router = Router()

router.include_routers(
    create_promotion.router,
    menu.router,
    get_statistics.router
)