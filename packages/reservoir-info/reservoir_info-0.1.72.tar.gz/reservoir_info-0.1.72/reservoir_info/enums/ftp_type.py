from mag_tools.enums.base_enum import BaseEnum


class FipType(BaseEnum):
    FWIP = ('FWIP', '地层单位体积内的水储量')
    FGIP = ('FGIP', '地层单位体积内的气储量')
    FOIP = ('FOIP', '地层单位体积内的油储量')
    FSGIP = ('FSGIP', '吸附气总量')