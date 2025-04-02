from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.string_utils import StringUtils

from enums.ftp_type import FipType


@dataclass
class FipSum(BaseData):
    fip_type: FipType = field(default=None, metadata={'description': 'Fip类型'})
    reg: Optional[int] = field(default=None, metadata={'description': '区域编号'})

    @classmethod
    def from_text(cls, text: str):
        if not text:
            return None
        text = StringUtils.pick_head(text, '#').replace('/', '').replace("'", "").strip()

        fip_sum = cls()
        fip_sum.fip_type = FipType.of_code(next((code for code in FipType.codes() if code in text), None))

        items = text.split()
        fip_sum.attribute_name = items[0]

        idx = ListUtils.find(items, 'REG')
        if idx is not None:
            fip_sum.reg = int(items[idx+1])

        return fip_sum

    def to_text(self):
        items = [self.fip_type.code]
        if self.reg:
            items.append(f'REG {self.reg}')

        return ' '.join(items) + ' /'

if __name__ == '__main__':
    sum_ = FipSum.from_text("FWIP REG 1")
    print(sum_.to_text())

    sum_ = FipSum.from_text("FGIP /")
    print(sum_.to_text())

    sum_ = FipSum.from_text("FWIP REG 2 /")
    print(sum_.to_text())
