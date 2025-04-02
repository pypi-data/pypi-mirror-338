
from mag_tools.enums.base_enum import BaseEnum


class RelPermeateType(BaseEnum):
    """
    相对渗透率类型枚举
    枚举值为相对渗透率模型的名称，如：RelPermeateType.STONEI
    """
    STONEI = ('STONEI', 'STONE II 模型')
    STONEII = ('STONEII', 'STONE I 模型')
    SEGR = ('SEGR', '分离模型')

