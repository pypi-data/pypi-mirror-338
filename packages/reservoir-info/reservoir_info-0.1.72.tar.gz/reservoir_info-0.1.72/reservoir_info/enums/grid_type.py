from mag_tools.enums.base_enum import BaseEnum


class GridType(BaseEnum):
    CARTESIAN = ('Cartesian grid', '笛卡尔网格')
    CPG = ('CPG', '角点网格')
    GPG = ('GPG', '广义棱柱网格')