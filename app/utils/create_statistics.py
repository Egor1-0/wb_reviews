import pandas as pd

from sqlalchemy.ext.asyncio import AsyncSession

from database.daos import ParticipationDao
from database.schemas.statistics import Statistics


async def create_statistics_by_promotion_id(session: AsyncSession, promotion_id: int):
    res_create, res_end = await ParticipationDao.get_statistics(session, promotion_id)
    data = dict()

    for date in res_create:
        data[date[0]] = Statistics(start=date[1])

    for date in res_end:
        if data.get(date[0]):
            data[date[0]].end = date[1]
        else:
            data[date[0]] = Statistics(end=date[1])



    date = []
    start = []
    end = []
    for k, v in data.items():
        date.append(k)
        start.append(v.start)
        end.append(v.end)

    data = {
        "Дата": date,
        "Начали участие": start,
        "Завершили участие": end
    }

    df = pd.DataFrame(data)
    df.to_csv(f"statistics_{promotion_id}", index=False, encoding='utf-8')