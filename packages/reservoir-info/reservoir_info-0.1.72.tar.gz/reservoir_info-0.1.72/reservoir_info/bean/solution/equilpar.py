from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.ValueUtils import ValueUtils
from mag_tools.utils.data.list_utils import ListUtils


@dataclass
class Equilpar(BaseData):
    """
    平衡法初始化的参数
    """
    ref_dep: float = field(default=None, metadata={"description": "参考深度 Dref，单位：m, feet, cm, ms"})
    ref_p: float = field(default=None, metadata={"description": "参考深度的压力 pref，单位：bar, psi, atm, Pa"})
    gwc_owc: float = field(default=None, metadata={"description": "油水界面深度 OWC 或气水界面深度 GWC，单位：m, feet, cm, um"})
    gwcpc_owcpc: float = field(default=None, metadata={"description": "油水界面或气水界面的毛管力 pcowc/pcgwc，单位：bar, psi, atm, Pa"})
    dh: float = field(default=None, metadata={"description": "初始化深度步长 dh，单位：m, feet, cm, um"})
    goc: Optional[float] = field(default=None, metadata={"description": "油气界面深度 GOC，单位：m, feet, cm, um"})
    goc_pc: Optional[float] = field(default=None, metadata={"description": "油气界面的毛管力 pcgoc，单位：bar, psi, atm, Pa"})

    @classmethod
    def from_block(cls, block_lines):
        """
        从块数据创建 Equilpar 实例。

        :param block_lines: 包含 EQUILPAR 数据块的行列表。
        :return: 创建的 Equilpar 实例。
        """
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 2:
            return None

        block_lines.pop(0)
        # 如数据分行，则合并
        if len(block_lines) >= 4 and block_lines[2].startswith('#'):
            block_lines = [f'{block_lines[0]} {block_lines[2]}', f'{block_lines[1]} {block_lines[3]}']
        elif len(block_lines) == 1:
            block_lines.insert(0, '# Ref_dep    Ref_p    GWC/OWC  GWC_pc/OWC_pc   dh')

        title_line = block_lines[0].replace('#', '').strip()
        titles = title_line.split()
        values = block_lines[1].split()
        data_dict = dict(zip(titles, values))

        return cls(
            ref_dep=ValueUtils.to_value(data_dict.get("Ref_dep", '0.0'), float),
            ref_p=ValueUtils.to_value(data_dict.get("Ref_p", '0.0'), float),
            gwc_owc=ValueUtils.to_value(data_dict.get("GWC/OWC", '0.0'), float),
            gwcpc_owcpc=ValueUtils.to_value(data_dict.get("GWC_pc/OWC_pc", '0.0'), float),
            dh=ValueUtils.to_value(data_dict.get("dh", '0.0'),float),
            goc=ValueUtils.to_value(data_dict.get("GOC", '0.0'),float),
            goc_pc=ValueUtils.to_value(data_dict.get("GOC_pc", '0.0'),float)
        )

    def to_block(self):
        """
        将 Equilpar 实例转换为块数据。

        :return: 包含 EQUILPAR 数据块的行列表。
        """
        self._formatter.number_per_line = 5
        self._formatter.pad_length = 0
        self._formatter.group_by_layer = True
        self._formatter.merge_duplicate = False
        self._formatter.decimal_places_of_zero = 1
        self._formatter.at_header = '# '

        title_1 = ["Ref_dep", "Ref_p", "GWC/OWC", "GWC_pc/OWC_pc", "dh"]
        title_2 = ["GOC", "GOC_pc", '', '', '']
        values_1 = [self.ref_dep, self.ref_p, self.gwc_owc, self.gwcpc_owcpc, self.dh]
        values_2 = [self.goc, self.goc_pc, '', '', '']

        lines = ['EQUILPAR', ]
        lines.extend(self._formatter.array_2d_to_lines([title_1, values_1, title_2, values_2]))
        lines[2] = lines[2].replace('#', ' ')
        lines[4] = lines[4].replace('#', ' ')
        return lines

if __name__ == "__main__":
    txt = """
    EQUILPAR
# Ref_dep    Ref_p    GWC/OWC  GWC_pc/OWC_pc   dh
  9035       3600      9950        0.0         2
# GOC       GOC_pc
  8800        0.0 
    """
    _eq = Equilpar.from_block(txt.split("\n"))
    print('\n'.join(_eq.to_block()))