from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.array_utils import ArrayUtils

from mag_tools.bean.dimension import Dimension


@dataclass
class Dyv(BaseData):
    """
    Y方向维度数据类型
    """
    dimens: Optional[Dimension] = field(default=None, metadata={'description': '行数、列数和层数'})
    data: list[float] = field(default_factory=list, metadata={
        'min': 1,
        'max': 9999,
        'description': '数据'})

    @classmethod
    def from_block(cls, block_lines, dimens: Dimension):
        if block_lines is None or len(block_lines) < 2:
            return None

        block_lines = ListUtils.trim(block_lines)

        data = ArrayUtils.lines_to_array_1d(block_lines[1:], float).tolist()
        return cls(dimens=dimens, data=data)

    def to_block(self):
        if self.data is None or len(self.data) == 0 or self.dimens is None:
            return []

        self._formatter.number_per_line = 5
        self._formatter.pad_length = 0
        self._formatter.merge_duplicate = True

        lines = ['DYV']
        lines.extend(self._formatter.array_1d_to_lines(self.data, float))
        return lines

    @classmethod
    def random_generate(cls, dimens: Dimension):
        dxv = cls(dimens=dimens)
        dxv.set_random_array('data', dimens.size)
        return dxv