from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData

from mag_tools.utils.data.list_utils import ListUtils
from typing import Optional

from mag_tools.utils.data.value_utils import ValueUtils


@dataclass
class Pvtw(BaseData):
    """
    水的 PVT 属性
    """
    pref: Optional[float] = field(default=None, metadata={'description': '参考压力'})
    refbw: Optional[float] = field(default=None, metadata={'description': '参考体积系数'})
    cw: Optional[float] = field(default=None, metadata={'description': '压缩系数'})
    refvisw: Optional[float] = field(default=None, metadata={'description': '参考粘度'})
    cvisw: Optional[float] = field(default=None, metadata={'description': '粘度系数'})

    @classmethod
    def from_block(cls, block_lines: list[str]):
        if not block_lines:
            return None

        # 处理标题行，为空则设置缺省值
        title_line = ListUtils.pick_line_by_keyword(block_lines, 'Pref')
        if title_line is None:
            title_line = '# Pref refBw Cw refVisw Cvisw'
        titles = title_line.replace('#', '').split()

        block_lines = ListUtils.remove_by_header(block_lines, '#')

        items = block_lines[1].split()
        values = {title.lower().strip(): ValueUtils.to_value(items[index], float) for index, title in enumerate(titles)}

        return cls(**values)

    def to_block(self) -> list[str]:
        self._formatter.pad_length = 0
        self._formatter.at_header = '  '

        titles = ['Pref', 'refBw', 'Cw', 'refVisw', 'Cvisw']
        values = [getattr(self, title.lower().strip()) for title in titles]

        lines = ['PVTW']
        lines.extend(self._formatter.array_2d_to_lines([titles, values]))
        lines[1] = '#' + lines[1][1:]

        return lines


if __name__ == '__main__':
    _lines = ['PVTW',
              '# Pref refBw Cw refVisw Cvisw',
              '3600 1.0034 1e-006 0.96 0']

    pvtw_set = Pvtw.from_block(_lines)
    print('\n'.join(pvtw_set.to_block()))
