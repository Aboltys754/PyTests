from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Полученый код состояния не равен ожидаемому"
    WRONG_ELEMENT_COUNT = "Количество элементов не равно ожидаемому"