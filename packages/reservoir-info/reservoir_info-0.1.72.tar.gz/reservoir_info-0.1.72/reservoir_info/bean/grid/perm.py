from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.bean.dimension import Dimension

from mag_tools.utils.data.array_utils import ArrayUtils
from mag_tools.utils.data.list_utils import ListUtils

from reservoir_info.enums.perm_type import PermType


@dataclass
class Perm(BaseData):
    perm_type: PermType = field(default=None, metadata={'description': '油藏网格xyz方向渗透率，实数'})
    dimens: Optional[Dimension] = field(default=None, metadata={'description': '行数、列数和层数'})
    data: list[list[list[Optional[float]]]] = field(default_factory=list, metadata={
        'min': 0.001,
        'max': 99999,
        'description': '数据'})

    def __post_init__(self):
        self.data = [[[None for _ in range(self.dimens.ny)] for _ in range(self.dimens.nx)] for _ in range(self.dimens.nz)]

    @classmethod
    def from_block(cls, block_lines: list[str], dimens: Dimension):
        if block_lines is None or len(block_lines) == 0:
            return None

        block_lines = ListUtils.trim(block_lines)
        if len(block_lines) == 1:
            block_lines = block_lines[0].split()

        perm_type = PermType.of_code(block_lines[0])

        perm = cls(perm_type=perm_type, dimens=dimens)
        perm.data = ArrayUtils.lines_to_array_3d(block_lines[1:], dimens.nz, dimens.nx, dimens.ny, float).tolist()
        perm._formatter.group_by_layer = len(block_lines)-1 == dimens.nz
        return perm

    def to_block(self):
        if self.data is None or len(self.data) == 0 or self.perm_type is None or self.dimens is None:
            return []

        self._formatter.number_per_line = 5
        self._formatter.merge_duplicate = True
        self._formatter.pad_length = 0

        lines = [self.perm_type.code]
        data_lines = self._formatter.array_3d_to_lines(self.data, float)
        lines.extend(data_lines)

        return lines

    @classmethod
    def random_generate(cls, perm_type: PermType, dimens: Dimension):
        perm = cls(perm_type=perm_type, dimens=dimens)
        perm.set_random_array_3d('data', list(dimens.shape), max_value=999)
        return perm

