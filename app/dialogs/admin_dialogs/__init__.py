from aiogram import Router

from . import create_promotion, menu, get_statistics
from config import config

router = Router()

router.callback_query.filter(lambda x: x.from_user.id == config.bot.ADMINISTRATION)

router.include_routers(
    create_promotion.router,
    menu.router,
    get_statistics.router
)