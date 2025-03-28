from database.daos.base import BaseDao
from database.models import Participation


class ParticipationDao(BaseDao):
    model = Participation
