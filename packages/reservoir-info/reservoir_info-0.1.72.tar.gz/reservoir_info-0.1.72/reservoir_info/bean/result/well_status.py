from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.array import Array, ArrayHeader
from mag_tools.bean.base_data import BaseData
from mag_tools.model.common.justify_type import JustifyType
from mag_tools.utils.data.ValueUtils import ValueUtils
from mag_tools.utils.data.list_utils import ListUtils

@dataclass
class WellStatus(BaseData):
    """
    井筒状态
    """
    well_id: Optional[str] = field(default=None, metadata={'description': '井号'})
    well_name: Optional[str] = field(default=None, metadata={'description': '井名'})
    node_number: Optional[int] = field(default=None, metadata={'description': '井节点数目'})
    product_system: Optional[str] = field(default=None, metadata={'description': '生产制度'})
    product_infos: list[Array] = field(default_factory=list, metadata={'description': '生产数据，为静态和动态数组,Array[]'})

    @classmethod
    def from_block(cls, block_lines):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 2:
            return None

        status = cls()

        # 解析井信息行
        well_items = block_lines[0].replace("'", "").split(' ')
        status.well_id = well_items[1]
        status.well_name = well_items[2]
        status.node_number = ValueUtils.to_value(well_items[3], int)
        status.product_system = f'{well_items[4]} {well_items[5]}' if len(well_items) > 5 else well_items[4]

        # 解析数据块，每行为一个数组，由若干数组组成。格式：数组名、单位和数据
        for line in block_lines[1:]:
            items = line.split()
            if items[0] in {'XCOORD', 'YCOORD', 'DEPTH'}:
                array_type = 'd'
            else:
                array_type = 'i'

            head = ArrayHeader(array_type=array_type, array_name=items[0], unit_name=items[1])
            data = [ValueUtils.to_value(value, float) if array_type == 'd' else int(value) for value in items[2:]]
            status.product_infos.append(Array(head, data))

        return status

    def to_block(self):
        self._formatter.at_header = '    '
        self._formatter.justify_type = JustifyType.RIGHT
        self._formatter.decimal_places_of_zero = 0

        block_lines = [f"WELL {self.well_id} '{self.well_name}' {self.node_number} '{self.product_system}'"]
        block_lines.extend(self._formatter.arrays_to_lines(self.product_infos))

        return block_lines

if __name__ == '__main__':
    str_ = '''
WELL 1 'INJE1' 6 'WIBHP:4000 PSIA'
    XCOORD       ft          7050          7050          7050          7050          7050          7050
    YCOORD       ft          7350          7350          7350          7350          7350          7350
     DEPTH       ft          9110      10378.16      10396.66      10415.66      10450.66      10525.66
     STAGE  integer             0             0             0             0             0             0
    OUTLET  integer            -1             0             1             2             3             4    
    '''
    status_ = WellStatus.from_block(str_.splitlines())
    print('\n'.join(status_.to_block()))


