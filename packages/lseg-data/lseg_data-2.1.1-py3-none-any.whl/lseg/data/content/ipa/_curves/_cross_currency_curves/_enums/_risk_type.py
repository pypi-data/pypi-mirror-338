from enum import unique
from ......_base_enum import StrEnum


@unique
class RiskType(StrEnum):
    CROSS_CURRENCY = "CrossCurrency"
