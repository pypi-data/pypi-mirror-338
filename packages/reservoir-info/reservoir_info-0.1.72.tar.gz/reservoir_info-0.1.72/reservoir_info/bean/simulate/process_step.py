from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.ValueUtils import ValueUtils


@dataclass
class ProcessStep(BaseData):
    nr_step: Optional[int] = field(init=False, default=0, metadata={'description': '迭代步数序号'})
    max_mbe: float = field(init=False, default=0, metadata={'description': '最大均方误差'})
    avg_mbe: float = field(init=False, default=0, metadata={'description': '平均均方误差'})
    msw_mbe: float = field(init=False, default=0, metadata={'description': 'MSW均方误差'})
    stab_test: int = field(init=False, default=0, metadata={'description': '稳定性测试'})
    flash: int = field(init=False, default=0, metadata={'description': '闪蒸计算'})
    lin_itr: Optional[int] = field(init=False, default=0, metadata={'description': '线性求解次数'})

    @classmethod
    def from_text(cls, text: str, titles: list[str]):
        step = cls()
        values = text.split()

        if 'NRStep' in titles:
            step.nr_step = int(values[titles.index('NRStep')])
        if 'MAXMBE' in titles:
            step.max_mbe = float(values[titles.index('MAXMBE')])
        if 'AVGMBE' in titles:
            step.avg_mbe = float(values[titles.index('AVGMBE')])
        if 'MSWMBE' in titles:
            step.msw_mbe = float(values[titles.index('MSWMBE')])
        if 'StabTest/Flash' in titles:
            stab_test, flash = map(int, values[titles.index('StabTest/Flash')].split('/'))
            step.stab_test = stab_test
            step.flash = flash
        if 'Lin_itr' in titles:
            step.lin_itr = int(values[titles.index('Lin_itr')])
        return step

    def to_list(self, titles: list[str]) -> list[Optional[str]]:
        result = []
        for title in titles:
            if 'NRStep' in title:
                result.append(ValueUtils.to_string(self.nr_step))
            elif 'MAXMBE' in title:
                result.append(ValueUtils.to_string(self.max_mbe))
            elif 'AVGMBE' in title:
                result.append(ValueUtils.to_string(self.avg_mbe))
            elif 'MSWMBE' in title:
                result.append(ValueUtils.to_string(self.msw_mbe))
            elif 'StabTest/Flash' in title:
                result.append(f'{ValueUtils.to_string(self.stab_test)}/{ValueUtils.to_string(self.flash)}')
            elif 'Lin_itr' in title:
                result.append(ValueUtils.to_string(self.lin_itr))

        return result