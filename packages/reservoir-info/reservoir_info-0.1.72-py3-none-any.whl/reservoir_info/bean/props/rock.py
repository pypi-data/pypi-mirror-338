from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData
from typing import Optional

from mag_tools.utils.data.value_utils import ValueUtils


@dataclass
class Rock(BaseData):
    """
    ROCK 岩石的压缩属性
    """
    pref: Optional[float] = field(default=None, metadata={'description': '参考压力'})
    compressibility: Optional[float] = field(default=None, metadata={'description': '压缩系数'})

    @classmethod
    def from_block(cls, block_lines: list[str]):
        if not block_lines:
            return None

        items = block_lines[1].split()
        values = {
            'pref': ValueUtils.to_value(items[0], float),
            'compressibility': ValueUtils.to_value(items[1], float)
        }
        return cls(**values)

    def to_block(self) -> list[str]:
        self._formatter.decimal_places = 1

        title_items = ['Pref', 'Compressibility']
        value_items = [getattr(self, title.lower().strip()) for title in title_items]

        lines = ['ROCK']
        lines.extend(self._formatter.array_1d_to_lines(value_items))
        return lines

if __name__ == '__main__':
    _lines = ['ROCK',
              '3600.0 1.0E-6']

    rock = Rock.from_block(_lines)
    print('\n'.join(rock.to_block()))
