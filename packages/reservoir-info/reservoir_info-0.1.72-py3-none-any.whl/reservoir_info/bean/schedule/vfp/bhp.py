from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.common.string_utils import StringUtils
from mag_tools.utils.data.list_utils import ListUtils


@dataclass
class BhpValue(BaseData):
    thp_no: int = field(default=None, metadata={'description': 'THP编号'})
    wfr_no: int = field(default=None, metadata={'description': 'WFR编号'})
    gfr_no: int = field(default=None, metadata={'description': 'GFR编号'})
    alg_no: int = field(default=None, metadata={'description': 'ALG编号'})
    data: list[float] = field(default_factory=list, metadata={'description': '数据'})

    @classmethod
    def from_text(cls, text: str):
        if not text:
            return None
        text = StringUtils.pick_head(text, '#').replace('/', '')
        items = text.split()
        value = cls()
        value.thp_no = items[0]
        value.wfr_no = items[1]
        value.gfr_no = items[2]
        value.alg_no = items[3]

        value.data = list(map(float, items[4:]))
        return value

    def to_list(self):
        items = [self.thp_no, self.wfr_no, self.gfr_no, self.alg_no]
        items.extend(self.data)
        return items

@dataclass
class Bhp(BaseData):
    data: list[BhpValue] = field(default_factory=list, metadata={'description': 'BHP数据'})

    @classmethod
    def from_block(cls, block_lines):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 2:
            return None

        block_lines = ListUtils.remove_by_keyword(block_lines, '#BHP')

        data = [BhpValue.from_text(line) for line in block_lines]
        return cls(data)

    def to_block(self):
        self._formatter.at_end = ' /'
        self._formatter.scientific = True

        values = [bhp_value.to_list() for bhp_value in self.data]

        lines = ['#BHP data']
        lines.extend(self._formatter.to_blocks(values))
        return lines

if __name__ == '__main__':
    str_ = '''
#BHP data 
1 1 1 1 1.93199E+03 1.36585E+03 6.77031E+02 7.15261E+02 8.62436E+02 / 
2 1 1 1 2.73663E+03 2.73303E+03 2.75085E+03 2.77323E+03 2.90209E+03 / 
1 1 2 1 1.77471E+03 4.33035E+02 5.38422E+02 6.30479E+02 9.39472E+02 / 
2 1 2 1 2.51228E+03 2.38072E+03 2.35995E+03 2.26536E+03 2.28849E+03 / 
1 1 3 1 1.64735E+03 4.41989E+02 6.95286E+02 8.81634E+02 1.41797E+03 / 
2 1 3 1 2.46600E+03 1.78161E+03 1.80525E+03 1.85156E+03 2.04484E+03 /     
    '''
    value_ = Bhp.from_block(str_.splitlines())
    print('\n'.join(value_.to_block()))