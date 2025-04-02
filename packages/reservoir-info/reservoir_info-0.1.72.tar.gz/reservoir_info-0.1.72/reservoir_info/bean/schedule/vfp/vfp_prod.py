from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.string_utils import StringUtils
from mag_tools.utils.data.value_utils import ValueUtils

from reservoir_info.bean.schedule.vfp.vfp_prod_header import VfpProdHeader
from reservoir_info.bean.schedule.vfp.bhp import Bhp
from mag_tools.utils.data.list_utils import ListUtils



@dataclass
class VfpProd(BaseData):
    """
    生产井的 VFP 表
        数据由一行表头、五行自变量、若干行 BHP 数据组成，每行数据以反斜杠结尾
    """
    #表头
    header: VfpProdHeader = field(default=None, metadata={'description': '生产井VFP表头'})
    #自变量数组
    flo_values: list[float] = field(default_factory=list, metadata={'description': 'FLO数组，长度为 NFLO'})
    thp_values: list[float] = field(default_factory=list, metadata={'description': 'THP数组，长度为 NTHP'})
    wfr_values: list[float] = field(default_factory=list, metadata={'description': 'WFR数组，长度为 NWFR'})
    gfr_values: list[float] = field(default_factory=list, metadata={'description': 'GFR数组，长度为 NGFR'})
    alg_values: list[float] = field(default_factory=list, metadata={'description': 'ALG数组，长度为 NALQ'})
    #BHP数据，共有 NTHP*NWFR*NGFR*NALQ 行
    bhp: Bhp = field(default_factory=Bhp, metadata={'description': 'BHP数据'})

    @classmethod
    def from_block(cls, block_lines):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 5:
            return None
        block_lines = [StringUtils.pick_head(line, '/') for line in block_lines]

        prod = cls()
        prod.header = VfpProdHeader.from_text(block_lines[1])
        prod.flo_values = ValueUtils.to_values(block_lines[2], float)
        prod.thp_values = ValueUtils.to_values(block_lines[3], float)
        prod.wfr_values = ValueUtils.to_values(block_lines[4], float)
        prod.gfr_values = ValueUtils.to_values(block_lines[5], float)
        prod.alg_values = ValueUtils.to_values(block_lines[6], float)
        prod.bhp = Bhp.from_block(block_lines[7:])

        return prod

    def to_block(self):
        self._formatter.decimal_places = 5

        lines = ['VFPPROD', self.header.to_text()]
        self._formatter.scientific = True

        lines.extend(self._formatter.to_lines(self.flo_values))
        lines.extend(self._formatter.to_lines(self.thp_values))
        lines.extend(self._formatter.to_lines(self.wfr_values))
        lines.extend(self._formatter.to_lines(self.gfr_values))
        lines.extend(self._formatter.to_lines(self.alg_values))
        lines.extend(self.bhp.to_block())
        return lines

if __name__ == '__main__':
    str_ = '''
VFPPROD 
1 7000 LIQ WCT GOR THP * FIELD BHP / #Header 
1.00000E+01 3.00000E+02 7.00000E+02 1.00000E+03 2.00000E+03 / #5 flow vals 
2.00000E+02 1.00000E+03 / #2 THP values 
0.0 / #1 WFR value 
1.00000E+00 6.00000E+00 12.00000E+00 / #3 GFR values 
0.0 / #1 ALQ value 
#BHP data 
1 1 1 1 1.93199E+03 1.36585E+03 6.77031E+02 7.15261E+02 8.62436E+02 / 
2 1 1 1 2.73663E+03 2.73303E+03 2.75085E+03 2.77323E+03 2.90209E+03 / 
1 1 2 1 1.77471E+03 4.33035E+02 5.38422E+02 6.30479E+02 9.39472E+02 / 
2 1 2 1 2.51228E+03 2.38072E+03 2.35995E+03 2.26536E+03 2.28849E+03 / 
1 1 3 1 1.64735E+03 4.41989E+02 6.95286E+02 8.81634E+02 1.41797E+03 / 
2 1 3 1 2.46600E+03 1.78161E+03 1.80525E+03 1.85156E+03 2.04484E+03 /     
    '''
    prod_ = VfpProd.from_block(str_.splitlines())
    print('\n'.join(prod_.to_block()))