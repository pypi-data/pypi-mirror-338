from mag_tools.enums.base_enum import BaseEnum


class SumType(BaseEnum):
    WAVG = ('WAVG', '加权平均值')
    AVG = ('AVG', '平均值')
    MAX = ('MAX', '最大值')
    MIN = ('MIN', '最小值')