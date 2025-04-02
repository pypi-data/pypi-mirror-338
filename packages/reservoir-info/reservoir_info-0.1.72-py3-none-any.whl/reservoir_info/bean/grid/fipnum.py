from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.array_utils import ArrayUtils
from mag_tools.utils.data.list_utils import ListUtils

from mag_tools.bean.dimension import Dimension


@dataclass
class FipNum(BaseData):
    """
    指定 FIP 区域编号
    """
    dimens: Optional[Dimension] = field(default=None, metadata={'description': '行数、列数和层数'})
    data: list[list[list[Optional[int]]]] = field(default_factory=list, metadata={
        'min': 1,
        'max': 99999,
        'description': '三维数据'})

    def __post_init__(self):
        self.data = [[[None for _ in range(self.dimens.ny)] for _ in range(self.dimens.nx)] for _ in range(self.dimens.nz)]

    @classmethod
    def from_block(cls, block_lines: list[str], dimens: Dimension):
        """
        从一个文本块中生成 FipNum
        :param dimens: 网络的行数、列数、层数
        :param block_lines: 文本块
        :return:
        """
        if block_lines is None or len(block_lines) == 0:
            return None
        block_lines = ListUtils.trim(block_lines)

        block_lines = ListUtils.trim(block_lines)
        if len(block_lines) == 1:
            block_lines = block_lines[0].split()

        fipnum = cls(dimens)
        fipnum.data = ArrayUtils.lines_to_array_3d(block_lines[1:], dimens.nz, dimens.nx, dimens.ny, int).tolist()
        fipnum._formatter.group_by_layer = len(block_lines)-1 == dimens.nz
        return fipnum

    def to_block(self):
        if self.data is None or len(self.data) == 0 or self.dimens is None:
            return []

        self._formatter.none_default = 'NA'

        lines = ['FIPNUM']
        lines.extend(self._formatter.array_3d_to_lines(self.data, float))
        return lines

    @classmethod
    def random_generate(cls, dimens: Dimension):
        fip = cls(dimens=dimens)
        fip.set_random_array_3d('data', list(dimens.shape), max_value=999)
        return fip