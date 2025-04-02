from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.common.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.string_utils import StringUtils

from mag_tools.bean.dimension import Dimension


@dataclass
class AttributeValue(BaseData):
    attribute_name: str = field(default=None, metadata={'description': '属性关键字'})
    # 区域信息
    dimens: Optional[Dimension] = field(default=None, metadata={'description': '网格编号'})
    carfin: Optional[str] = field(default=None, metadata={'description': '加密区名'})

    @classmethod
    def from_text(cls, text: str):
        if not text or len(text.strip()) < 2:
            return None
        text = StringUtils.pick_head(text, '#').replace('/', '').replace("'", "").strip()

        attr_value = cls()

        items = [item.strip() for item in text.split()]
        attr_value.attribute_name = items[0]

        idx = ListUtils.find(items, 'CARFIN')
        if idx is not None:
            attr_value.carfin = items[idx+1].strip()
            attr_value.dimens = Dimension.from_block(items[idx+2:])
        else:
            attr_value.dimens = Dimension.from_block(items[1:])

        if attr_value.dimens is None or attr_value.dimens.nx is None:
            attr_value = None

        return attr_value

    def to_text(self):
        items = [self.attribute_name]
        if self.carfin:
            items.append(f"CARFIN '{self.carfin}'")

        items.extend(self.dimens.to_block())

        return ' '.join(items) + ' /'

if __name__ == '__main__':
    sum_ = AttributeValue.from_text("SWAT 1 1 1 /")
    print(sum_.to_text())

    sum_ = AttributeValue.from_text("ZMF1 13 18 5 /")
    print(sum_.to_text())

    sum_ = AttributeValue.from_text("PGAS CARFIN 'FIN1' 8 5 1 /")
    print(sum_.to_text())

    # 不正确
    sum_ = AttributeValue.from_text("ZMF1 /")
    print(sum_)






