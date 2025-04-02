from mag_tools.enums.base_enum import BaseEnum


class WfrType(BaseEnum):
    """
    WFR(水流速或水流量)类型枚举类
    """
    WOR = ('WOR', '水-油比')
    WCT = ('WCT', '含水率')
    WGR = ('WGR', '水-气比')
    WWR = ('WWR', '水-湿气比')
    WTF = ('WTF', '水摩尔比')