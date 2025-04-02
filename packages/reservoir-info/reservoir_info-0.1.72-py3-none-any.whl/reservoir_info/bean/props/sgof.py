from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from typing import Optional

from mag_tools.utils.data.value_utils import ValueUtils


@dataclass
class Sgof(BaseData):
    sg: Optional[float] = field(default=None, metadata={'description': '气体饱和度'})
    krg: Optional[float] = field(default=None, metadata={'description': '气体的相对渗透率'})
    krog: Optional[float] = field(default=None, metadata={'description': '油在气中的相对渗透率'})
    pcgo: Optional[float] = field(default=None, metadata={'description': '毛管力 Pcgo(=Pg-Po)'})

    @classmethod
    def from_text(cls, text: str, titles: list[str]):
        items = text.split()
        values = {title.lower().replace('(=pg-po)', '').strip(): ValueUtils.to_value(items[index], float) for index, title in enumerate(titles)}
        return cls(**values)

    def to_list(self, titles: list[str]) -> list[float]:
        return [getattr(self, title.lower().replace('(=pg-po)', '').strip()) for title in titles]

@dataclass
class SgofSet(BaseData):
    """
    油，气，不动水共存时关于 Sg 的饱和度函数，用于黑油模型和组分模型
    """
    titles: list[str] = field(default_factory=list, metadata={'description': '表格标题'})
    data: list[Sgof] = field(default_factory=list, metadata={'description': 'SGOF列表'})

    @classmethod
    def from_block(cls, block_lines: list[str]):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 2:
            return None

        sgofs = cls()

        # 处理标题行，为空则设置缺省值
        title_line = ListUtils.pick_line_by_keyword(block_lines, '#')
        if title_line is None:
            title_line = '# Sg Krg Krog Pcgo(=Pg-Po)'
        sgofs.titles = title_line.replace('#', '').split()

        block_lines = ListUtils.remove_by_header(block_lines, '#')
        for line in block_lines[1:]:
            if line.strip() != '/':
                sgof = Sgof.from_text(line, sgofs.titles)
                sgofs.data.append(sgof)

        return sgofs

    def to_block(self) -> list[str]:
        self._formatter.pad_length = 0
        self._formatter.at_header = '  '

        values = [['Sg', 'Krg', 'Krog', 'Pcgo(=Pg-Po)']]

        for sgof in self.data:
            values.append(sgof.to_list(self.titles))

        lines = ['SGOF']
        lines.extend(self._formatter.array_2d_to_lines(values))
        lines.append('/')
        lines[1] = '#' + lines[1][1:]

        return lines

if __name__ == '__main__':
    _lines = ['#           Sg         Krg       Krog       Pcgo(=Pg-Po)',
    '0.0500000 0.000000 0.593292 0.0523257',
    '0.111111 0.000823045 0.292653 0.0696509',
    '0.172222 0.00658436 0.131341 0.0845766',
    '0.355556 0.102881 0.00457271 0.129908']

    _sgof_set = SgofSet.from_block(_lines)
    print('\n'.join(_sgof_set.to_block()))
