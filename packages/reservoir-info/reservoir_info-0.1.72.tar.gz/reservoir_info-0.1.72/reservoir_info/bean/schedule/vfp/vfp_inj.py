from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.value_utils import ValueUtils

from reservoir_info.bean.schedule.vfp.vfp_inj_header import VfpInjHeader
from reservoir_info.bean.schedule.vfp.bhp import Bhp
from mag_tools.utils.data.list_utils import ListUtils


@dataclass
class VfpInj(BaseData):
    """
    注入井的 VFP 表
        数据由一行表头、五行自变量、若干行 BHP 数据组成，每行数据以反斜杠结尾
    """
    #表头
    header: VfpInjHeader = field(default=None, metadata={'description': '注入井VFP表头'})
    #自变量数组
    flo_values: list[float] = field(default_factory=list, metadata={'description': 'FLO数组，长度为 NFLO'})
    thp_values: list[float] = field(default_factory=list, metadata={'description': 'THP数组，长度为 NTHP'})
    #BHP数据，共有 NTHP*NWFR*NGFR*NALQ 行
    bhp: Bhp = field(default_factory=Bhp, metadata={'description': 'BHP数据'})

    @classmethod
    def from_block(cls, block_lines):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 5:
            return None

        prod = cls()
        prod.header = VfpInjHeader.from_text(block_lines[1])
        prod.flo_values = ValueUtils.pick_numbers(block_lines[2])
        prod.thp_values = ValueUtils.pick_numbers(block_lines[3])
        prod.bhp = Bhp.from_block(block_lines[4:])

        return prod

    def to_block(self):
        self._formatter.decimal_places = 5

        lines = ['VFPINJ', self.header.to_text()]
        self._formatter.scientific = True

        lines.extend(self._formatter.to_lines(self.flo_values))
        lines.extend(self._formatter.to_lines(self.thp_values))
        lines.extend(self.bhp.to_block())
        return lines

if __name__ == '__main__':
    str_ = '''
VFPINJ 
2 9110 WAT THP FIELD BHP / 
1.00000E+00 3.00000E+02 7.00000E+02 1.00000E+03 2.00000E+03 / #5 flow values 
1.00000E+03 2.00000E+03 3.00000E+03 / #3 THP values 
#BHP values 
1 1.32484E+03 1.32300E+03 1.31556E+03 1.30626E+03 1.25098E+03 / 
2 2.74881E+03 2.74801E+03 2.74490E+03 2.74110E+03 2.71934E+03 / 
3 3.94062E+03 3.94000E+03 3.93761E+03 3.93471E+03 3.91830E+03 /    
    '''
    prod_ = VfpInj.from_block(str_.splitlines())
    print('\n'.join(prod_.to_block()))