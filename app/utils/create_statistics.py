from sqlalchemy.ext.asyncio import AsyncSession
import pandas as pd

from database.daos import ParticipationDao
from database.models import Participation
from database.schemas.status import Status


async def create_statistics_csv(session: AsyncSession):
    participations = await ParticipationDao.get_statistics(session)

    data = []
    for p in participations:
        username = 'Отсутствует'
        if p.user.username:
            username = '@' + p.user.username

        status = None
        match p.status.value:
            case Status.FIRST_STAGE:
                status = 'Первый этап'
            case Status.SECOND_STAGE:
                status = 'Второй этап'
            case Status.COMPLETED:
                status = 'Завершено'
            case Status.CANCELED:
                status = 'Отклонено'

        data.append({
            "Дата": p.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "Название акции": p.promotion.name,
            "Колво оставшихся квот": p.promotion.count,
            "Юзернейм": username,
            "Ник на вб": p.wb_nickname,
            "Реквизиты для перевода": p.details_for_transfer,
            "Статус": status
        })

    # Создаем DataFrame
    df = pd.DataFrame(data)

    df.to_csv('statistics.csv', index=False, encoding='utf-8-sig')
