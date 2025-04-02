from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.value_utils import ValueUtils
from mag_tools.utils.data.list_utils import ListUtils


@dataclass
class Swof(BaseData):
    """
    Sw 的饱和度函数函数
    """
    sw: Optional[float] = field(default=None, metadata={'description': '水饱和度'})
    krw: Optional[float] = field(default=None, metadata={'description': '水的相对渗透率'})
    krow: Optional[float] = field(default=None, metadata={'description': '油在水中的相对渗透率'})
    pcow: Optional[float] = field(default=None, metadata={'description': '毛管力 Pcow(=Po-Pw)'})

    @classmethod
    def from_text(cls, text: str, titles: list[str]):
        items = text.split()
        values = {title.lower().replace('(=po-pw)', '').strip(): ValueUtils.to_value(items[index], float) for index, title in enumerate(titles)}
        return cls(**values)

@dataclass
class SwofSet(BaseData):
    """
    油水共存时关于 Sw 的饱和度函数函数，用于黑油模型、油水模型和组分模型
    """
    titles: list[str] = field(default_factory=list, metadata={'description': '表格标题'})
    data: list[Swof] = field(default_factory=list, metadata={'description': 'SWOF列表'})

    @classmethod
    def from_block(cls, block_lines):
        if block_lines is None or len(block_lines) == 0:
            return None

        # 处理标题行，为空则设置缺省值
        block_lines = ListUtils.trim(block_lines)
        if 'Sw' not in block_lines[1]:
            titles_text = 'Sw Krw Krow Pcow(=Po-Pw)'
        else:
            titles_text = block_lines[1].replace('#', '')
            if '(' not in titles_text:
                titles_text = titles_text.replace('Pc', 'Pcow(=Po-Pw)')
        titles = titles_text.split()

        data = []
        for line in block_lines[2:]:
            if line.strip() != '/':
                swof = Swof.from_text(line, titles)
                data.append(swof)

        return cls(titles=titles, data=data)

    def to_block(self):
        self._formatter.at_header = '  '
        self._formatter.decimal_places = 5
        self._formatter.decimal_places_of_zero = 0
        self._formatter.pad_length = 0

        values = [['Sw', 'Krw', 'Krow', 'Pcow(=Po-Pw)']]
        values.extend([list(vars(swof).values()) for swof in self.data])

        lines = ['SWOF']
        lines.extend(self._formatter.array_2d_to_lines(values))
        lines[1] = '#' + lines[1][1:]
        return lines

if __name__ == '__main__':
    _lines = ['SWOF',
'#           Sw         Krw       Krow       Pcow(=Po-Pw)',
       '0.15109           0           1         400',
       '0.15123           0     0.99997      359.19',
       '0.15174           0     0.99993      257.92',
       '0.15246           0     0.99991      186.31',
       '0.15647           0     0.99951       79.06',
       '0.16585           0     0.99629       40.01',
       '0.17835           0     0.99159       27.93',
       '0.20335      1e-005     0.97883        20.4']
    _swof_set = SwofSet.from_block(_lines)
    print('\n'.join(_swof_set.to_block()))
