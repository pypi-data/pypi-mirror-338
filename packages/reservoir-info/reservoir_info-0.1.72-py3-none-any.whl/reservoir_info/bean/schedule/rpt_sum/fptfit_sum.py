from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.string_utils import StringUtils

from reservoir_info.enums.fptfit_type import FptfitType


@dataclass
class FptfitSum(BaseData):
    fptfit_type: FptfitType = field(default=None, metadata={'description': '模型累计产量和累计注入量的类别'})
    reg: Optional[int] = field(default=None, metadata={'description': '区域编号'})

    @classmethod
    def from_text(cls, text: str):
        if not text:
            return None
        text = StringUtils.pick_head(text, '#').replace('/', '').replace("'", "").strip()

        fptfit_sum = cls()
        fptfit_sum.fptfit_type = FptfitType.of_code(next((code for code in FptfitType.codes() if code in text), None))

        items = text.split()
        fptfit_sum.attribute_name = items[0]

        idx = ListUtils.find(items, 'REG')
        if idx is not None:
            fptfit_sum.reg = int(items[idx+1])

        return fptfit_sum

    def to_text(self):
        items = [self.fptfit_type.code]
        if self.reg:
            items.append(f'REG {self.reg}')

        return ' '.join(items) + ' /'

if __name__ == '__main__':
    sum_ = FptfitSum.from_text("FGIT REG 1")
    print(sum_.to_text())

    sum_ = FptfitSum.from_text("FWPT /")
    print(sum_.to_text())

    sum_ = FptfitSum.from_text("FWIT /")
    print(sum_.to_text())