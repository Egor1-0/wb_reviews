from database.daos.base import BaseDao
from database.models import Promotion


class PromotionDao(BaseDao):
    model = Promotion
