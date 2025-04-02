from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils

from reservoir_info.bean.grid.dyv import Dyv
from reservoir_info.bean.grid.dxv import Dxv
from reservoir_info.bean.grid.dzv import Dzv
from enums.mult_type import MultType
from reservoir_info.bean.common.box import Box
from reservoir_info.bean.common.copy_grid import CopyGrid
from mag_tools.bean.dimension import Dimension
from reservoir_info.bean.grid.fipnum import FipNum
from reservoir_info.bean.grid.mult import Mult
from reservoir_info.bean.grid.multiporo import Multiporo
from reservoir_info.bean.grid.nmatopts import Nmatopts
from reservoir_info.bean.grid.perm import Perm
from reservoir_info.bean.grid.poro import Poro
from reservoir_info.bean.grid.porv import Porv
from reservoir_info.bean.grid.tops import Tops
from reservoir_info.enums.nmatopts_type import NmatoptsType
from reservoir_info.enums.perm_type import PermType


@dataclass
class Grid(BaseData):
    dimens: Optional[Dimension] = field(default=None, metadata={"description": "油藏网格数"})
    multiporo: Optional[Multiporo] = field(default=None, metadata={"description": "多重网格"})
    nmatopts: Optional[Nmatopts] = field(default=NmatoptsType.GEOMETRIC, metadata={"description": "各层基质的体积比例"})
    fipnum: Optional[FipNum] = field(default=None, metadata={"description": "区域编号"})
    permx: Optional[Perm] = field(default=None, metadata={"description": "油藏网格 x 方向渗透率"})
    permy: Optional[Perm] = field(default=None, metadata={"description": "油藏网格 y 方向渗透率"})
    permz: Optional[Perm] = field(default=None, metadata={"description": "油藏网格 z 方向渗透率"})
    multx: Optional[Mult] = field(default=None, metadata={"description": "油藏网格 x 方向传导率乘数"})
    multy: Optional[Mult] = field(default=None, metadata={"description": "油藏网格 y 方向传导率乘数"})
    multz: Optional[Mult] = field(default=None, metadata={"description": "油藏网格 z 方向传导率乘数"})
    poro: Optional[Poro] = field(default=None, metadata={"description": "指定参考压力下地层的孔隙度"})
    porv: Optional[Porv] = field(default=None, metadata={"description": "指定参考压力下网格的孔隙体积"})
    dxv: Optional[Dxv] = field(default=None, metadata={"description": "指定网格 x 方向的长度"})
    dyv: Optional[Dyv] = field(default=None, metadata={"description": "指定网格 y 方向的长度"})
    dzv: Optional[Dzv] = field(default=None, metadata={"description": "指定网格 z 方向的长度"})
    tops: Optional[Tops] = field(default=None, metadata={"description": "顶面深度"})

    @classmethod
    def from_block(cls, block_lines):
        if block_lines is None or len(block_lines) == 0:
            return None

        grid = cls()
        dimens_lines = ListUtils.pick_block_by_keyword(block_lines, 'DIMENS', 2)
        grid.dimens = Dimension.from_block(dimens_lines)

        multiporo_lines = ListUtils.pick_block_by_keyword(block_lines, 'MULTIPORO', 2)
        grid.multiporo = Multiporo.from_block(multiporo_lines) if multiporo_lines else None

        nmatopts_line = ListUtils.pick_line_by_keyword(block_lines, 'NMATOPTS')
        grid.nmatopts = Nmatopts.from_block(nmatopts_line) if nmatopts_line else None

        # 根据网络数初始化fip_num和permx/permy/permz
        grid.fip_num = FipNum(grid.dimens)
        grid.permx = Perm(perm_type=PermType.PERM_X, dimens=grid.dimens)
        grid.permy = Perm(perm_type=PermType.PERM_Y, dimens=grid.dimens)
        grid.permz = Perm(perm_type=PermType.PERM_Z, dimens=grid.dimens)
        grid.multx = Mult(mult_type=MultType.MULT_X, m=grid.dimens.ny, n=grid.dimens.nz)
        grid.multy = Mult(mult_type=MultType.MULT_Y, m=grid.dimens.nx, n=grid.dimens.nz)
        grid.multz = Mult(mult_type=MultType.MULT_Z, m=grid.dimens.nx, n=grid.dimens.ny)
        grid.poro = Poro(nx=grid.dimens.nx, ny=grid.dimens.ny, nz=grid.dimens.nz)
        grid.porv = Porv(nx=grid.dimens.nx, ny=grid.dimens.ny, nz=grid.dimens.nz)
        grid.dxv = Dxv(dimens=grid.dimens)
        grid.dyv = Dyv(dimens=grid.dimens)
        grid.dzv = Dzv(dimens=grid.dimens)
        grid.tops = Tops(grid.dimens.nx, grid.dimens.ny)

        # FIP 区域编号
        fipnum_lines = ListUtils.pick_block(block_lines, 'FIPNUM', '')
        if fipnum_lines and 'BOX' not in fipnum_lines[0] and 'COPY' not in fipnum_lines[0]:
            grid.fipnum = FipNum.from_block(fipnum_lines, grid.dimens)

        # 渗透率
        permx_lines = ListUtils.pick_block(block_lines, 'PERMX', '')
        if permx_lines and 'BOX' not in permx_lines[0] and 'COPY' not in permx_lines[0]:
            grid.permx = Perm.from_block(permx_lines, grid.dimens)

        permy_lines = ListUtils.pick_block(block_lines, 'PERMY', '')
        if permy_lines and 'BOX' not in permy_lines[0] and 'COPY' not in permy_lines[0]:
            grid.permy = Perm.from_block(permy_lines, grid.dimens)

        permz_lines = ListUtils.pick_block(block_lines, 'PERMZ', '')
        if permz_lines and 'BOX' not in permz_lines[0] and 'COPY' not in permz_lines[0]:
            grid.permz = Perm.from_block(permz_lines, grid.dimens)

        # 传导率乘数
        multx_lines = ListUtils.pick_block(block_lines, 'MULTX', '')
        if multx_lines and 'BOX' not in multx_lines[0] and 'COPY' not in multx_lines[0]:
            grid.multx = Mult.from_block(multx_lines, grid.dimens.ny, grid.dimens.nz)

        multy_lines = ListUtils.pick_block(block_lines, 'MULTY', '')
        if multy_lines and 'BOX' not in multy_lines[0] and 'COPY' not in multy_lines[0]:
            grid.multy = Mult.from_block(multy_lines, grid.dimens.nx, grid.dimens.nz)

        multz_lines = ListUtils.pick_block(block_lines, 'MULTZ', '')
        if multz_lines and 'BOX' not in multz_lines[0] and 'COPY' not in multz_lines[0]:
            grid.multz = Mult.from_block(multz_lines, grid.dimens.nx, grid.dimens.ny)

        # 孔隙度
        poro_lines = ListUtils.pick_block(block_lines, 'PORO', '')
        if poro_lines and 'BOX' not in poro_lines[0] and 'COPY' not in poro_lines[0]:
            grid.poro = Poro.from_block(poro_lines, grid.dimens.nx, grid.dimens.ny, grid.dimens.nz)

        # 孔隙体积
        porv_lines = ListUtils.pick_block(block_lines, 'PORV', '')
        if porv_lines and 'BOX' not in porv_lines[0] and 'COPY' not in porv_lines[0]:
            grid.porv = Porv.from_block(porv_lines, grid.dimens.nx, grid.dimens.ny, grid.dimens.nz)

        # xyz方向的长度
        dxv_lines = ListUtils.pick_block(block_lines, 'DXV', '')
        grid.dxv = Dxv.from_block(dxv_lines, grid.dimens)

        dyv_lines = ListUtils.pick_block(block_lines, 'DYV', '')
        grid.dyv = Dyv.from_block(dyv_lines, grid.dimens)

        dzv_lines = ListUtils.pick_block(block_lines, 'DZV', '')
        grid.dzv = Dzv.from_block(dzv_lines, grid.dimens)

        # 顶面深度
        tops_lines = ListUtils.pick_block(block_lines, 'TOPS', '')
        grid.tops = Tops.from_block(tops_lines, grid.dimens.nx, grid.dimens.ny)

        for line in block_lines:
            if line.startswith('BOX'):
                box = Box.from_text(line)
                array = grid.get_array(box.var_name)
                if array is not None:
                    grid.set_array(box.var_name, box.calculate(array))
            elif line.startswith('COPY'):
                copy = CopyGrid.from_text(line)
                source_array = grid.get_array(copy.source_name)
                target_array = grid.get_array(copy.target_name)
                if source_array is not None and target_array is not None:
                    grid.set_array(copy.target_name, copy.calculate(source_array, target_array))
        return grid

    def to_block(self) -> list[str]:
        lines = ['GRID','##################################################']
        lines.extend(self.dimens.to_block())
        lines.append("")

        if self.multiporo is not None:
            lines.extend(self.multiporo.to_block())
            lines.append("")

        if self.nmatopts is not None:
            lines.extend(self.nmatopts.to_block())
            lines.append("")

        if self.fipnum is not None and len(self.fipnum.data) > 0:
            lines.extend(self.fipnum.to_block())
            lines.append("")

        if self.multx is not None and len(self.multx.data) > 0:
            lines.extend(self.multx.to_block())
            lines.append("")
        if self.multy is not None and len(self.multy.data) > 0:
            lines.extend(self.multy.to_block())
            lines.append("")
        if self.multz is not None and len(self.multz.data) > 0:
            lines.extend(self.multz.to_block())
            lines.append("")

        if self.permx is not None and len(self.permx.data) > 0:
            lines.extend(self.permx.to_block())
            lines.append("")
        if self.permy is not None :
            lines.extend(self.permy.to_block())
            lines.append("")
        if self.permz is not None and len(self.permz.data) > 0:
            lines.extend(self.permz.to_block())
            lines.append("")

        if self.poro is not None and len(self.poro.data) > 0:
            lines.extend(self.poro.to_block())
            lines.append("")

        if self.porv is not None and len(self.porv.data) > 0:
            lines.extend(self.porv.to_block())
            lines.append("")

        if self.dxv is not None and len(self.dxv.data) > 0:
            lines.extend(self.dxv.to_block())
            lines.append("")

        if self.dyv is not None and len(self.dyv.data) > 0:
            lines.extend(self.dyv.to_block())
            lines.append("")

        if self.dzv is not None and len(self.dzv.data) > 0:
            lines.extend(self.dzv.to_block())
            lines.append("")

        if self.tops is not None and len(self.tops.data) > 0:
            lines.extend(self.tops.to_block())
            lines.append("")

        lines.append('#GRID END#########################################')
        return lines

    def get_array(self, var_type)->Optional[np.array]:
        _var = None
        if var_type == 'PERMX':
            _var = np.array(self.permx.data) if self.permx else None
        elif var_type == 'PERMY':
            _var = np.array(self.permy.data) if self.permy else None
        elif var_type == 'PERMZ':
            _var = np.array(self.permz.data) if self.permz else None
        elif var_type == 'FIPNUM':
            _var = np.array(self.fipnum.data) if self.fipnum else None
        elif var_type == 'TOPS':
            _var = np.array(self.tops.data) if self.tops else None
        return _var

    def set_array(self, var_type, value: list[float]):
        if var_type == 'PERMX':
            self.permx.data = value
        elif var_type == 'PERMY':
            self.permy.data = value
        elif var_type == 'PERMZ':
            self.permz.data = value
        elif var_type == 'FIPNUM':
            self.fipnum.data = value
        elif var_type == 'TOPS':
            self.tops.data = value