from aiogram import Router

from . import first_stage

router = Router()

router.include_routers(
    first_stage.router
)