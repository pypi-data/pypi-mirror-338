from dataclasses import dataclass, field
from typing import Any, Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.value_utils import ValueUtils

from mag_tools.bean.dimension import Dimension
from reservoir_info.bean.well.well_completion import WellCompletion
from reservoir_info.enums.perforation_type import PerforationType


@dataclass
class PerforateWell(BaseData):
    """
    完井数据的射孔信息
    """
    perf_type: PerforationType = field(default=None, metadata={'description': '射孔类型'})
    i: int = field(default=None, metadata={'description': "I；对SEG为起始井段编号；对STAGE为起始stage编号"})
    j: int = field(default=None, metadata={'description': "J；对SEG为终止井段编号；对STAGE为终止stage编号"})
    k1: Optional[int] = field(default=None, metadata={'description': "K1"})
    k2: Optional[int] = field(default=None, metadata={'description': "K2"})
    row1: Optional[int] = field(default=None, metadata={'description': "ROW1"})
    row2: Optional[int] = field(default=None, metadata={'description': "ROW2"})
    well_completion: WellCompletion = field(default=None, metadata={'description': '完井数据'})
    #
    _dimens: Dimension = field(default=None, metadata={'description': "网络尺寸"})

    @classmethod
    def from_text(cls, text: str, dimens: Dimension):
        if not text:
            return None

        pw = cls(_dimens=dimens)

        items = text.split()

        # 选择射孔
        pw.perf_type = PerforationType.of_code(items[0])

        well_complete_idx = 3
        pw.i = ValueUtils.to_value(items[1], int)
        pw.j = ValueUtils.to_value(items[2], int)
        if pw.perf_type == PerforationType.PERF:
            well_complete_idx = 5
            pw.k1 = ValueUtils.to_value(items[3], int)
            pw.k2 = ValueUtils.to_value(items[4], int)
            if len(items) > 6 and items[5].isdigit() and items[6].isdigit():
                well_complete_idx = 7
                pw.row1 = ValueUtils.to_value(items[5], int)
                pw.row2 = ValueUtils.to_value(items[6], int)

        well_complete_items = items[well_complete_idx:]
        pw.well_completion = WellCompletion.from_text(' '.join(well_complete_items), dimens)

        return pw

    def to_list(self) -> list[Any]:
        items = [self.perf_type.code, self.i, self.j]
        if self.perf_type == PerforationType.PERF:
            items.append(self.k1)
            items.append(self.k2)
            if self.row1 and self.row2:
                items.append(self.row1)
                items.append(self.row2)

        items.append(self.well_completion.to_text())
        return items

if __name__ == '__main__':
    dim_ = Dimension(nx=3, ny=5, nz=8)
    str_ = 'PERF 10 10 1 5 OPEN HZ DZ SKIN 0.1 WPIMULT 0.5'
    perf_well_ = PerforateWell.from_text(str_, dim_)
    print(perf_well_.to_list())

    str_ = 'PERF NA NA NA NA OPEN HZ DZ SKIN 0.1 WPIMULT 0.5'
    perf_well_ = PerforateWell.from_text(str_, dim_)
    print(perf_well_.to_list())


