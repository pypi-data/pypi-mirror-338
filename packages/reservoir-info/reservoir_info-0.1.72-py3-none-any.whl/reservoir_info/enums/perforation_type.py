from mag_tools.enums.base_enum import BaseEnum

class PerforationType(BaseEnum):
    """
    穿孔类型枚举
    枚举值为不包含前缀的穿孔类型名，如：PerforationType.PERF
    """
    PERF = ('PERF', '穿孔')
    SEG = ('SEG', '分段')
    STAGE = ('STAGE', '阶段')