from database.daos.base import BaseDao
from database.models import User


class UserDao(BaseDao):
    model = User
