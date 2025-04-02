from dataclasses import dataclass, field
from typing import Any, Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.value_utils import ValueUtils


@dataclass
class Pvto(BaseData):
    """
    活油(live oil)的 PVT 属性
    """
    rssat: Optional[float] = field(default=None, metadata={'description': '溶解气油比'})
    pres: Optional[float] = field(default=None, metadata={'description': '压力'})
    bo: Optional[float] = field(default=None, metadata={'description': '体积系数'})
    vis: Optional[float] = field(default=None, metadata={'description': '粘度'})

    @classmethod
    def from_text(cls, text: str, titles: list[str]):
        items = text.replace('/', '').split()
        if len(items) != len(titles):
            raise ValueError(f"Data length {len(items)} does not match titles length {len(titles)}")

        values = {title.lower().strip(): ValueUtils.to_value(items[index], float) for index, title in enumerate(titles)}
        return cls(**values)

    def to_list(self, titles: list[str]) -> list[Any]:
        return [getattr(self, title.lower().strip()) for title in titles]

@dataclass
class PvtoBlock(BaseData):
    pvto_blocks: list[Pvto] = field(default_factory=list, metadata={'description': 'PVTO子表格，包含一或多条PVTO数据'})

    @classmethod
    def from_block(cls, block_lines: list[str], titles: list[str]):
        if block_lines is None or len(block_lines) < 1:
            return None

        block_lines = ListUtils.trim(block_lines)

        blocks = cls()
        pvto_0 = Pvto.from_text(block_lines[0], titles)
        blocks.pvto_blocks.append(pvto_0)

        for line in block_lines[1:]:
            pvto = Pvto.from_text(f'{pvto_0.rssat} {line}', titles)
            blocks.pvto_blocks.append(pvto)
        return blocks

    def to_list(self,  titles: list[str]) -> list[list[Any]]:
        blocks = [block.to_list(titles) for block in self.pvto_blocks]
        for block in blocks[1:]:
            block[0] = ''

        return blocks

@dataclass
class PvtoSet(BaseData):
    """
    活油(live oil)的 PVT 属性
    """
    titles: list[str] = field(default_factory=list, metadata={'description': '列名数组'})
    pvtos: list[PvtoBlock] = field(default_factory=list, metadata={'description': 'PVTO二维数组'})

    @classmethod
    def from_block(cls, block_lines: list[str]):
        block_lines = ListUtils.trim(block_lines)

        pvto_set = cls()

        # 处理标题行，为空则设置缺省值
        title_line = ListUtils.pick_line_by_keyword(block_lines, 'Rssat')
        title_line = title_line.replace('#', '').strip() if title_line else 'Rssat Pres Bo Vis'
        pvto_set.titles = title_line.split()

        block_lines = ListUtils.remove_by_keyword(block_lines[1:], '#')
        pvto_table_blocks = ListUtils.split_by_keyword(block_lines, '/', at_head=False)
        pvto_table_blocks.pop(-1)
        for table_block in pvto_table_blocks:
            block = PvtoBlock.from_block(table_block, titles=pvto_set.titles)
            if block:
                pvto_set.pvtos.append(block)

        return pvto_set

    def to_block(self) -> list[str]:
        self._formatter.pad_length = 0
        self._formatter.at_header = '  '

        lines = ['PVTO']

        titles = ['Rssat', 'Pres', 'Bo', 'Vis']
        values = [titles]

        for pvto_blk in self.pvtos:
            blk_lines = pvto_blk.to_list(titles)
            blk_lines[-1][-1] = ValueUtils.to_string(blk_lines[-1][-1]) + ' /'
            values.extend(blk_lines)

        lines.extend(self._formatter.array_2d_to_lines(values))
        lines[1] = '#' + lines[1][1:]

        lines.append('/')

        return lines

if __name__ == '__main__':
    _lines = [
        'PVTO',
        '# Rssat Pres Bo Vis',
        '0.165 400 1.012 1.17 /',
        '0.335 800 1.0255 1.14 /',
        '0.5 1200 1.038 1.11 /',
        '0.665 1600 1.051 1.08 /',
        '0.828 2000 1.063 1.06 /',
        '0.985 2400 1.075 1.03 /',
        '1.13 2800 1.087 1.00 /',
        '1.270 4014.7 1.695 0.51',
        '      5014.7 1.671 0.549',
        '      9014.7 1.579 0.74 /',
        '1.618 5014.7 1.827 0.449',
        '      9014.7 1.726 0.605 /',
        '/'
    ]

    _pvto_set = PvtoSet.from_block(_lines)
    print('\n'.join(_pvto_set.to_block()))
