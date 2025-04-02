
from mag_tools.enums.base_enum import BaseEnum


class WellRatioLimitType(BaseEnum):
    """
    井比率限制类型枚举
    枚举值为井比率限制类型的名称，如：WellRatioLimitType.WCUT
    """
    WCUT = ('WCUT', '含水率')  # 含水率
    GOR = ('GOR', '气-油比')  # 气-油比
    GLR = ('GLR', '气-液比')  # 气-液比
    WGR = ('WGR', '水-气比')  # 水-气比