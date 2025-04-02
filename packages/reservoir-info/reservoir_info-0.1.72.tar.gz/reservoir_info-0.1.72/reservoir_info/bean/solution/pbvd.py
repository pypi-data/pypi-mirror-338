from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.value_utils import ValueUtils


@dataclass
class DeepPressure(BaseData):
    d: float = field(default=None, metadata={'description': '深度，单位：m(米制)，feet(英制)，cm(lab)，um(MESO)'})
    p_bub: float = field(default=None, metadata={'description': '泡点压力，单位：bar(米制)，psi(英制)，atm(lab)，Pa(MESO)'})

    @classmethod
    def from_text(cls, text: str):
        numbers = ValueUtils.pick_numbers(text)
        return cls(d=float(numbers[0]), p_bub=float(numbers[1]))

    def to_text(self):
        return f'{self.d} {self.p_bub}'

@dataclass
class Pbvd(BaseData):
    """
    深度-泡点压力曲线
    """
    data: list[DeepPressure] = field(default_factory=list, metadata={'description': '深度-泡点压力列表'})

    @classmethod
    def from_block(cls, block_lines):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 2:
            return None

        block_lines.pop(0)
        dps = []
        for line in block_lines:
            dp = DeepPressure.from_text(line)
            dps.append(dp)

        return cls(data=dps)

    def to_block(self) -> list[str]:
        lines = ['PBVD']
        for dp in self.data:
            lines.append(f'  {dp.to_text()}')

        return lines

if __name__ == '__main__':
    src_ = '''
PBVD
   5000        3600
   9000        3600    
    '''
    pbvd_ = Pbvd.from_block(src_.splitlines())
    print('\n'.join(pbvd_.to_block()))