from aiogram import Router

from . import first_stage, second_stage, menu, promotions_stats

router = Router()

router.include_routers(
    first_stage.router,
    second_stage.router,
    menu.router,
    promotions_stats.router
)