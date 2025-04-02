from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData

from mag_tools.utils.data.value_utils import ValueUtils


@dataclass
class WellHead(BaseData):
    """
    井头文件包含井名、井头 X 坐标、井头 Y 坐标、总深（TMD）、补心海拔（KB）五列数据
    """
    well_name: Optional[str] = field(default=None, metadata={'description': '井名'})
    x_coord: Optional[float] = field(default=None, metadata={'description': '井头 X 坐标'})
    y_coord: Optional[float] = field(default=None, metadata={'description': '井头 Y 坐标'})
    tmd: Optional[float] = field(default=None, metadata={'description': '总深（TMD）'})
    kb: Optional[float] = field(default=None, metadata={'description': '补心海拔（KB）'})


    @classmethod
    def from_text(cls, text):
        head = cls()
        items = text.split()

        head.well_name = items[0]
        head.x_coord = ValueUtils.to_value(items[1], float)
        head.y_coord = ValueUtils.to_value(items[2], float)
        head.tmd = ValueUtils.to_value(items[3], float)
        head.kb = ValueUtils.to_value(items[4], float)
        return head

    def to_text(self):
        values =[self.well_name, self.x_coord, self.y_coord, self.tmd, self.kb]

        return ' '.join(self._formatter.array_1d_to_lines(values))

    def __str__(self):
        return self.to_text()

if __name__ == '__main__':
    line = 'YYH1-1 18594037.720 3282025.234 4115 421'
    wh = WellHead.from_text(line)
    print(wh.to_text())