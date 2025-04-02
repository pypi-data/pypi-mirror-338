from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.common.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.string_utils import StringUtils

from reservoir_info.enums.sum_type import SumType


@dataclass
class AttributeSum(BaseData):
    attribute_name: str = field(default=None, metadata={'description': '属性关键字'})
    sum_type: SumType = field(default=None, metadata={'description': '统计类型'})
    # 区域信息
    reg: Optional[int] = field(default=None, metadata={'description': '区域编号'})
    carfin: Optional[str] = field(default=None, metadata={'description': '加密区名'})
    emdf: Optional[str] = field(default=None, metadata={'description': "裂缝名"})

    @classmethod
    def from_text(cls, text: str):
        if not text:
            return None
        text = StringUtils.pick_head(text, '#').replace('/', '').replace("'", "").strip()

        attr_sum = cls()
        attr_sum.sum_type = SumType.of_code(next((code for code in SumType.codes() if code in text), None))

        items = text.split()
        attr_sum.attribute_name = items[0]

        idx = ListUtils.find(items, 'REG')
        if idx is not None:
            attr_sum.reg = int(items[idx+1])

        idx = ListUtils.find(items, 'CARFIN')
        if idx is not None:
            attr_sum.carfin = items[idx+1].strip()

        idx = ListUtils.find(items, 'EMDF')
        if idx is not None:
            attr_sum.emdf = items[idx+1].strip()

        return attr_sum

    def to_text(self):
        items = [self.attribute_name, self.sum_type.code]
        if self.reg:
            items.append(f'REG {self.reg}')
        if self.carfin:
            items.append(f"CARFIN '{self.carfin}'")
        if self.emdf:
            items.append(f'EMDF {self.emdf}')

        return ' '.join(items) + ' /'

if __name__ == '__main__':
    sum_ = AttributeSum.from_text("SWAT WAVG / #水饱和度均值，按孔隙体积加权")
    print(sum_.to_text())

    sum_ = AttributeSum.from_text("POIL CARFIN 'FIN1' MAX /")
    print(sum_.to_text())

    sum_ = AttributeSum.from_text("SWAT MIN /")
    print(sum_.to_text())

    sum_ = AttributeSum.from_text("POIL EMDF 'f1' WAVG /")
    print(sum_.to_text())






