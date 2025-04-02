from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils

from reservoir_info.bean.solution.equilpar import Equilpar
from reservoir_info.bean.solution.pbvd import Pbvd


@dataclass
class Solution(BaseData):
    equilpar: Optional[Equilpar] = field(default=None, metadata={'description': '平衡法初始化的参数'})
    pbvd: Optional[Pbvd] = field(default=None, metadata={'description': '深度-泡点压力曲线'})

    @classmethod
    def from_block(cls, block_lines):
        equilpar_lines = ListUtils.pick_tail(block_lines, 'EQUILPAR')
        equilpar = Equilpar.from_block(equilpar_lines)

        pbvd_lines = ListUtils.pick_block(block_lines, 'PBVD', '')
        pbvd = Pbvd.from_block(pbvd_lines)

        return cls(equilpar=equilpar, pbvd=pbvd)

    def to_block(self) -> list[str]:
        lines = ['SOLUTION', '##################################################', '']
        if self.equilpar:
            lines.extend(self.equilpar.to_block())

        if self.pbvd:
            lines.extend(self.pbvd.to_block())
            lines.append('')

        lines.append('#SOLUTION END######################################')
        return lines

if __name__ == '__main__':
    src_ = '''
 EQUILPAR
# Ref_dep    Ref_p    GWC/OWC  GWC_pc/OWC_pc   dh
  9035       3600      9950        0.0         2
# GOC       GOC_pc
  8800        0.0    
PBVD
   5000        3600
   9000        3600   
    '''
    sol = Solution.from_block(src_.splitlines())
    print('\n'.join(sol.to_block()))