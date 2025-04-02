from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.value_utils import ValueUtils


@dataclass
class Pvdo(BaseData):
    p: float = field(default=None, metadata={'description': '压力,单位：bar(米制)，psi(英制)，atm(lab)，Pa(MESO)'})
    bo: float = field(default=None, metadata={'description': '油的体积系数,单位：rm3/sm3(米制)，rb/stb(英制)，cm3/cm3(lab)，um3/um3(MESO)'})
    visc: float = field(default=None, metadata={'description': '油的粘度,单位：cP'})

    @classmethod
    def from_text(cls, text, titles: list[str]):
        items = text.split()
        values = {title.lower().strip(): ValueUtils.to_value(items[index], float) for index, title in enumerate(titles)}
        return cls(**values)

    def to_list(self, titles: list[str]) -> list[float]:
        return [getattr(self, title.lower()) for title in titles]

@dataclass
class PvdoSet(BaseData):
    """
    油水共存时关于 Sw 的饱和度函数函数，用于黑油模型、油水模型和组分模型
    """
    titles: list[str] = field(default_factory=list, metadata={'description': '表格标题'})
    data: list[Pvdo] = field(default_factory=list, metadata={'description': 'PVDO列表'})

    @classmethod
    def from_block(cls, block_lines):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 2:
            return None
        pvdos = cls()

        #解析标题行
        title_line = ListUtils.pick_line_by_keyword(block_lines, 'P(psi)')
        if title_line is None:
            title_line = '# P(psi) BO(rb/stb) VISC(cP)'
        titles_text = title_line.replace('#', '').replace('(psi)', '').replace('(rb/stb)', '').replace('(cP)', '').replace('(um)', '')
        pvdos.titles = titles_text.split()

        block_lines = ListUtils.remove_by_header(block_lines, '#')
        for line in block_lines[1:]:
            pvdo = Pvdo.from_text(line, pvdos.titles)
            pvdos.data.append(pvdo)

        return pvdos

    def to_block(self):
        self._formatter.pad_length = 0
        self._formatter.at_header = '  '
        values = [['P(psi)', 'BO(rb/stb)', 'VISC(cP)']]

        for pvdo in self.data:
            values.append(pvdo.to_list(self.titles))

        lines = ['PVDO']
        lines.extend(self._formatter.array_2d_to_lines(values))
        lines[1] = '#' + lines[1][1:]
        return lines

if __name__ == '__main__':
    str_ = '''
PVDO 
# P(psi) BO(rb/stb) VISC(cP) 
 14 1.03 1.2 
 1014.7 1.0106 1.2 
 2014.7 0.9916 1.2 
 3014.7 0.9729 1.200166 
 4014.7 0.9546 1.200222 
 5014.7 0.9367 1.200277 
 6014.7 0.9190 1.200333 
 7014.7 0.9017 1.200388     
    '''
    pvdo_ = PvdoSet.from_block(str_.splitlines())
    print('\n'.join(pvdo_.to_block()))