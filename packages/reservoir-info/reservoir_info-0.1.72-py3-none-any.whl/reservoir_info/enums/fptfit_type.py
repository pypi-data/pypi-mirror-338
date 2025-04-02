from mag_tools.enums.base_enum import BaseEnum


class FptfitType(BaseEnum):
    FOPT = ('FOPT', '整个油藏或区域的累积油产量')
    FWPT = ('FWPT', '整个油藏或区域的累积水产量')
    FGPT = ('FGPT', '整个油藏或区域的累积气产量')
    FOIT = ('FOIT', '整个油藏或区域的累积注水量')
    FWIT = ('FWIT', '整个油藏或区域的累积注水量')
    FGIT = ('FGIT', '整个油藏或区域的累积注气量')