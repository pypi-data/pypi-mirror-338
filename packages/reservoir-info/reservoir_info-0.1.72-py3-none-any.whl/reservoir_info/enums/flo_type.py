from mag_tools.enums.base_enum import BaseEnum


class FloType(BaseEnum):
    """
    FLO(流体流动的速率)类型枚举类
    """
    OIL = ('OIL', '油的速率')
    LIQ = ('LIQ', '液体速率')
    GAS = ('GAS', '气体速率')
    WAT = ('WAT', '水速率')
    WG = ('WG', '湿气体积速率，仅用于组分模型')
    TM = ('TM', '总摩尔速率，仅用于组分模型')