from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.value_utils import ValueUtils


@dataclass
class Density(BaseData):
    """
    地面标况下油、水、气的密度
    """
    oil: Optional[float] = field(default=None, metadata={'description': '油密度'})
    water: Optional[float] = field(default=None, metadata={'description': '水密度'})
    gas: Optional[float] = field(default=None, metadata={'description': '气密度'})

    @classmethod
    def from_block(cls, block_lines: list[str]) -> 'Density' or None:
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 2:
            return None

        title_line = ListUtils.pick_line_by_keyword(block_lines, 'Oil')
        if title_line is None:
            title_line = '# Oil Water Gas'
        titles = title_line.replace('#', '').split()

        block_lines = ListUtils.remove_by_header(block_lines, '#')

        values = block_lines[1].split()
        values = {title.lower().strip(): ValueUtils.to_value(values[index], float) for index, title in enumerate(titles)}

        return cls(**values)

    def to_block(self) -> list[str]:
        self._formatter.pad_length = 0
        self._formatter.at_header = '  '

        titles = ['Oil', 'Water', 'Gas']
        values = [getattr(self, title.lower().strip()) for title in titles]

        lines = ['DENSITY']
        lines.extend(self._formatter.array_2d_to_lines([titles, values]))
        lines[1] = '#' + lines[1][1:]

        return lines

if __name__ == '__main__':
    _lines = ['DENSITY',
              '# Oil Water Gas',
              '44.98 63.01 0.0702']

    density_set = Density.from_block(_lines)
    print('\n'.join(density_set.to_block()))
