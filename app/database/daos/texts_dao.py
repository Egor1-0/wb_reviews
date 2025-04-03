from database.daos.base import BaseDao
from database.models import Texts


class TextsDao(BaseDao):
    model = Texts
