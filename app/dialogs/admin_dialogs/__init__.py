from aiogram import Router

from . import create_promotion

router = Router()

router.include_routers(
    create_promotion.router
)