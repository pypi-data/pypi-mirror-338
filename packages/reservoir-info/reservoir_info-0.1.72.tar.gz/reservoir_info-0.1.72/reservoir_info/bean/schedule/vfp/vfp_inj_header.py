from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.ValueUtils import ValueUtils
from mag_tools.utils.data.string_utils import StringUtils

from reservoir_info.enums.unit_system import UnitSystem
from reservoir_info.enums.flo_type import FloType


@dataclass
class VfpInjHeader(BaseData):
    """
    注入井VFP(垂直流动性能)表格的表头
    """
    number: int = field(default=None, metadata={
        'description': '表格的编号',
        'min': 1
    })
    bhp_deep: float = field(default=None, metadata={'description': 'BHP参考深度，为NA默认等于首个井节点的深度'})
    flo_type: FloType = field(default=None, metadata={'description': 'FLO(流体流动的速率)类型'})
    thp_type: str = field(default='THP', metadata={'description': 'THP(油管头压力) 的类型'})
    unit_system: UnitSystem = field(default=None, metadata={'description': '单位制'})
    vfp_type: str = field(default='BHP', metadata={'description': 'VFP(垂直流动性能)输出类型'})

    @classmethod
    def from_text(cls, text: str):
        if not text:
            return None
        text = StringUtils.pick_head(text, '#').replace('/', '')
        items = text.split()
        return cls(
            number=ValueUtils.to_value(items[0], int),
            bhp_deep=ValueUtils.to_value(items[1], float),
            flo_type=FloType.of_code(items[2]) or FloType.GAS,
            thp_type=items[3] or 'THP',
            unit_system=UnitSystem.of_code(items[4]),
            vfp_type=items[5] or 'BHP',
        )

    def to_text(self) -> str:
        """
        将 VfpHeader 对象序列化为字符串
        """
        self._formatter.decimal_places_of_zero = 0
        self._formatter.at_end = ' /'
        self._formatter.none_default = 'NA'

        items = [self.number,
                 self.bhp_deep,
                 self.flo_type.code,
                 self.thp_type if self.thp_type else 'THP',
                 self.unit_system.code,
                 self.vfp_type]

        return '\n'.join(self._formatter.to_lines(items))

if __name__ == '__main__':
    str_ = '2 99.0 WAT THP FIELD BHP /'
    header_ = VfpInjHeader.from_text(str_)
    print(header_.to_text())