from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData

from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.value_utils import ValueUtils


@dataclass
class Pvdg(BaseData):
    """
    PVDG 干气(dry gas)的 PVT 属性
    """
    pres: Optional[float] = field(default=None, metadata={'description': '压力'})
    bg: Optional[float] = field(default=None, metadata={'description': '气体体积系数'})
    vis: Optional[float] = field(default=None, metadata={'description': '粘度'})

    @classmethod
    def from_text(cls, text: str, titles: list[str]):
        items = text.split()
        values = {title.lower().strip(): ValueUtils.to_value(items[index], float) for index, title in enumerate(titles)}
        return cls(**values)

    def to_list(self, titles: list[str]) -> list[float]:
        return [getattr(self, title.lower().strip()) for title in titles]

@dataclass
class PvdgSet(BaseData):
    """
    油，气，不动水共存时关于 Sg 的饱和度函数，用于黑油模型和组分模型
    """
    titles: list[str] = field(default_factory=list, metadata={'description': '列名数组'})
    pvdgs: list[Pvdg] = field(default_factory=list, metadata={'description': 'PVDG数组'})

    @classmethod
    def from_block(cls, block_lines: list[str]):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 2:
            return None

        pvdg_set = cls()

        # 处理标题行，为空则设置缺省值
        title_line = ListUtils.pick_line_by_keyword(block_lines, 'Pres')
        if title_line is None:
            title_line = '# Pres Bg Vis'
        titles_text = title_line.replace('#', '').strip()
        pvdg_set.titles = titles_text.split()

        block_lines = ListUtils.remove_by_header(block_lines, '#')
        for line in block_lines[1:]:
            if line != '/':
                pvdg = Pvdg.from_text(line, pvdg_set.titles)
                pvdg_set.pvdgs.append(pvdg)
        return pvdg_set

    def to_block(self) -> [str]:
        self._formatter.pad_length = 0
        self._formatter.at_header = '  '

        values = [self.titles]
        for pvdg in self.pvdgs:
            values.append(pvdg.to_list(self.titles))

        lines = ['PVDG']
        lines.extend(self._formatter.array_2d_to_lines(values))
        lines[1] = '#' + lines[1][1:]
        return lines

    def __str__(self):
        return '\n'.join(self.to_block())


if __name__ == '__main__':
    _lines = ['PVDG',
              '# Pres Bg Vis',
    '400 5.4777 0.013',
    '800 2.7392 0.0135',
    '1200 1.8198 0.014',
    '1600 1.3648 0.0145',
    '2000 1.0957 0.015',
    '2400 0.9099 0.0155']

    _pvdg_set = PvdgSet.from_block(_lines)
    print(_pvdg_set)
