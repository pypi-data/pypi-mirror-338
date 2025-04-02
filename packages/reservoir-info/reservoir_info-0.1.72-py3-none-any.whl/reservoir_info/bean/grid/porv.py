from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData

from mag_tools.utils.data.array_utils import ArrayUtils
from mag_tools.utils.data.list_utils import ListUtils


@dataclass
class Porv(BaseData):
    """
    指定参考压力下网格的孔隙体积
    """
    nx: int = field(default=None, metadata={"description": "行数"})
    ny: int = field(default=None, metadata={"description": "列数"})
    nz: int = field(default=None, metadata={"description": "层数"})
    data: list[list[list[Optional[float]]]] = field(default_factory=list, metadata={"description": "数据"})

    def __post_init__(self):
        self.data = [[[None for _ in range(self.ny)] for _ in range(self.nx)] for _ in range(self.nz)]

    @classmethod
    def from_block(cls, block_lines, nx, ny, nz):
        """
        从一个文本块中生成 Porv
        :param nx: 网络的行数
        :param ny: 网络的列数
        :param nz: 网络的层数
        :param block_lines: 文本块，每行为一层的数值列表，如：600*0.087
        :return:
        """
        if block_lines is None or len(block_lines) == 0:
            return None

        block_lines = ListUtils.trim(block_lines)
        if len(block_lines) == 1:
            block_lines = block_lines[0].split()

        porv = cls(nx=nx, ny=ny, nz=nz)
        porv.data = ArrayUtils.lines_to_array_3d(block_lines[1:], nz, nx, ny, float).tolist()
        porv._formatter.group_by_layer = len(block_lines)-1 == nz
        return porv

    def to_block(self):
        if self.data is None or len(self.data) == 0 or self.nx is None or self.ny is None or self.nz is None:
            return []

        self._formatter.number_per_line = 5
        self._formatter.merge_duplicate = True
        self._formatter.none_default = 'NA'

        lines = ['PORV']
        lines.extend(self._formatter.array_3d_to_lines(self.data, float))
        return lines

if __name__ == '__main__':
    _str = "PORV\n605*100.0"
    p = Porv.from_block(_str.split('\n'), 11,11, 5)
    print('\n'.join(p.to_block()))

    _str = "PORV 605*100.0"
    p = Porv.from_block(_str.split('\n'), 11,11, 5)
    print('\n'.join(p.to_block()))

    _str = "PORV\n121*100.0\n121*100.0\n121*100.0\n121*100.0\n121*100.0"
    p = Porv.from_block(_str.split('\n'), 11, 11, 5)
    print('\n'.join(p.to_block()))

    p = Porv(nx=3, ny=5, nz=7)
    print('\n'.join(p.to_block()))