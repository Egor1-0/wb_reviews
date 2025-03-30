from aiogram import Router

from . import first_stage, second_stage

router = Router()

router.include_routers(
    first_stage.router,
    second_stage.router
)