from mag_tools.enums.base_enum import BaseEnum


class GfrType(BaseEnum):
    """
    GFR(气体流速或气体流量)类型枚举类
    """
    GOR = ('GOR', '气-油比')
    GLR = ('GLR', '气-液比')
    OGR = ('OGR', '油-气比')