from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils

from reservoir_info.bean.tune.tune import Tune
from reservoir_info.bean.general.general import General
from reservoir_info.bean.grid.grid import Grid
from reservoir_info.bean.well.well_group import WellGroup
from reservoir_info.bean.solution.solution import Solution
from reservoir_info.bean.props.props import Props

@dataclass
class ModelParams(BaseData):
    uuid: Optional[str] = field(default=None, metadata={"description": "模拟标识"})
    general: Optional[General] = field(default=None, metadata={"description": "通用信息"})
    grid: Optional[Grid] = field(default=None, metadata={"description": "油藏地质模型"})
    well: Optional[WellGroup] = field(default=None, metadata={"description": "井定义信息"})
    props: Optional[Props] = field(default=None, metadata={'description': '组分数量'})
    solution: Optional[Solution] = field(default=None, metadata={'description': '解决方案'})
    tune: Optional[Tune] = field(default=None, metadata={"description": "计算控制信息"})

    @classmethod
    def from_block(cls, block_lines):
        # 通用信息
        general_lines = ListUtils.pick_block(block_lines, 'FIELD', 'GRID')
        general_lines.pop(-1)
        general_lines[1] = f'{general_lines[1]} {general_lines[2]}'
        general = General.from_block(general_lines)

        # 油藏地质模型
        grid_lines = ListUtils.pick_block(block_lines, 'GRID', 'WELL')
        grid_lines.pop(-1)
        grid = Grid.from_block(grid_lines)

        # 井定义信息
        well_lines = ListUtils.pick_block(block_lines, 'WELL', 'PROPS')
        well_lines.pop(-1)
        well = WellGroup.from_block(well_lines)

        # 岩石、流体物性
        props_lines = ListUtils.pick_block(block_lines, 'PROPS', 'SOLUTION')
        props_lines.pop(-1)
        props = Props.from_block(props_lines)

        # 初始化信息
        solution_lines = ListUtils.pick_block(block_lines, 'SOLUTION', 'TUNE')
        solution_lines.pop(-1)
        solution = Solution.from_block(solution_lines)

        # 计算控制信息
        computing_lines = ListUtils.pick_block(block_lines, 'TUNE', '')
        computing_lines.pop(-1)
        tune = Tune.from_block(computing_lines)

        return cls(general=general, grid=grid, well=well, props=props, solution= solution, tune=tune)

    def to_block(self):
        lines = []
        lines.extend(self.general.to_block())
        lines.append('')

        lines.extend(self.grid.to_block())
        lines.append('')

        lines.extend(self.well.to_block())
        lines.append('')

        lines.extend(self.props.to_block())
        lines.append('')

        lines.extend(self.solution.to_block())
        lines.append('')

        lines.extend(self.tune.to_block())
        lines.append('')

        return lines

if __name__ == '__main__':
    src_ = '''
FIELD
MODELTYPE
OILWATER
GRID
DIMENS
60 220 85 
INCLUDE
spe_phi
 Reading included file "D:\AUCK\Cishi\Codes\Python\collection\data\case\Comp\spe10\spe_phi.dat"
INCLUDE
spe_permxy
 Reading included file "D:\AUCK\Cishi\Codes\Python\collection\data\case\Comp\spe10\spe_permxy.dat"
INCLUDE
spe_permz
 Reading included file "D:\AUCK\Cishi\Codes\Python\collection\data\case\Comp\spe10\spe_permz.dat"
TOPS
13200*12000 
DXV
60*20.0 
DYV
220*10.0 
DZV
85*2.00 
WELL
 Warning: file "SPE10_EMDF.inc" does not exist
TEMPLATE
MARKER I J K1 K2 OUTLET WI OS SATMAP HX HY HZ REQ SKIN LENGTH RW DEV ROUGH DCJ DCN 
XNJ YNJ 
WELSPECS
NAME W1 
'' 1 1 1 85 NA NA OPEN NA 0 0 DZ NA 0 NA 0.5 NA 0 NA NA NA NA 
NAME W2 
'' 60 1 1 85 NA NA OPEN NA 0 0 DZ NA 0 NA 0.5 NA 0 NA NA NA NA 
NAME W3 
'' 60 220 1 85 NA NA OPEN NA 0 0 DZ NA 0 NA 0.5 NA 0 NA NA NA NA 
NAME W4 
'' 1 220 1 85 NA NA OPEN NA 0 0 DZ NA 0 NA 0.5 NA 0 NA NA NA NA 
NAME W5 
'' 30 110 1 85 NA NA OPEN NA 0 0 DZ NA 0 NA 0.5 NA 0 NA NA NA NA 
PROPS 
 Message: generated grid blocks (259.789 ms); type = "CARTESIAN"
SWOF
0.200 0.0000 1.0000 0.0000 
0.250 0.0069 0.8403 0.0000 
0.300 0.0278 0.6944 0.0000 
0.350 0.0625 0.5625 0.0000 
0.400 0.1111 0.4444 0.0000 
0.450 0.1736 0.3403 0.0000 
0.500 0.2500 0.2500 0.0000 
0.550 0.3403 0.1736 0.0000 
0.600 0.4444 0.1111 0.0000 
0.650 0.5625 0.0625 0.0000 
0.700 0.6944 0.0278 0.0000 
0.750 0.8403 0.0069 0.0000 
0.800 1.0000 0.0000 0.0000 
PVDO
300 1.05 2.85 
800 1.02 2.99 
8000 1.01 3.00 
PVTW
6000 1.01 3.1E-6 0.3 0.0 
DENSITY
53 64 53 
ROCK
6000 1.0E-6 
SOLUTION
EQUILPAR
12000 6000 12200 0.0 0.5 
TUNE
TSTART 0 STEPCUT 1.0 MINDT 0.01 MAXDT 50 
DTINC 3.0 DTCUT 0.5 NCHECKDX MAXDP 0 MAXDS 
0.15 MAXDC 0 MBEPC 1E-3 MBEAVG 1E-6 SOLVER 
3064 INISTOL 1E-3 SCHEDULE 
RECURRENT
TIME 20*100.0 
WELL W1 BHP 4000 100.0 
WELL W2 BHP 4000 100.0 
WELL W3 BHP 4000 100.0 
WELL W4 BHP 4000 100.0 
WELL W5 WIR 5000 10000 
RPTSCHED 
BASIC TECPLOT 
RPTSUM
FWIP 
FOIP     
'''
    params_ = ModelParams.from_block(src_.splitlines())
    print('\n'.join(params_.to_block()))