from enum import Enum


class Status(str, Enum):
    FIRST_STAGE = 'FIRST_STAGE'
    SECOND_STAGE = 'SECOND_STAGE'
    CANCELED = 'CANCELED'
    COMPLETED = 'COMPLETED'
