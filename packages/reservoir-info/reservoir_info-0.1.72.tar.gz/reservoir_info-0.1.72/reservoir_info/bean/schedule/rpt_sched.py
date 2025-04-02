from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.value_utils import ValueUtils

from reservoir_info.enums.wstuout_type import WstuoutType

from reservoir_info.enums.stuout_type import StuoutType


@dataclass
class RptSched(BaseData):
    """
    报告输出格式、内容控制
    """
    # 格式控制
    precs: Optional[int] = field(default=None, metadata={'description': '数据的有效位数'})
    printw: Optional[int] = field(default=None, metadata={'description': '输出文件中每行数据个数'})
    netonly: Optional[bool] = field(default=None, metadata={'description': '为true则只输出有效网格的数据'})
    rptonly: Optional[bool] = field(default=None, metadata={'description': '为true则生产输出文件中只输出汇报时间步的数据'})
    separate: Optional[int] = field(default=0, metadata={'description': '控制状态文件（stu 文件）的分离模式'})
    # 选择输出文件
    tecplot: Optional[bool] = field(default=None, metadata={'description': '当模拟器使用结构网格或GPG网格时，输出Tecplot格式的二进制文件'})
    solvd: Optional[bool] = field(default=None, metadata={'description': '当使用重力平衡法初始化时，输出油藏状态随深度变化的表格'})
    geom: Optional[bool] = field(default=None, metadata={'description': '将油藏的静态参数输出到“XXX_geom.out”或“XXX_geom.bin”文件'})
    binout: Optional[bool] = field(default=None, metadata={'description': '以二进制格式输出XXX_stu、XXX_geom文件'})
    stuout: Optional[bool] = field(default=None, metadata={'description': '以文本格式输出XXX_stu、XXX_geom文件'})
    rstbin: Optional[bool] = field(default=None, metadata={'description': '以二进制格式输出重启动文件'})
    guiout: Optional[bool] = field(default=None, metadata={'description': '采用自带的3D可视化工具输出所需的文件'})
    # 选择输出的油藏动态数据
    stuout_data: list[StuoutType] = field(default_factory=list, metadata={'description': '输出到“XXX_stu.out”或“XXX_stu.bin”中的油藏动态数据'})
    # 选择输出的井动态数据
    wstuout_data: list[WstuoutType] = field(default_factory=list, metadata={'description': '输出到“XXX_wstu.out”的井动态数据'})


    @classmethod
    def from_block(cls, block_lines: list[str]):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 2:
            return None

        rpt = cls()

        # 格式控制
        precs_line = ListUtils.pick_line_by_keyword(block_lines, 'PRECS')
        if precs_line:
            rpt.precs = ValueUtils.pick_number(precs_line)

        printw_line = ListUtils.pick_line_by_keyword(block_lines, 'PRINTW')
        if printw_line:
            rpt.printw = ValueUtils.pick_number(printw_line)

        netonly_line = ListUtils.pick_line_by_keyword(block_lines, 'NETONLY')
        rpt.netonly = netonly_line is not None

        rptonly_line = ListUtils.pick_line_by_keyword(block_lines, 'RPTONLY')
        rpt.rptonly = rptonly_line is not None

        separate_line = ListUtils.pick_line_by_keyword(block_lines, 'SEPARATE')
        if separate_line:
            num = ValueUtils.pick_number(separate_line)
            rpt.separate = num if num is not None else 0

        # 选择输出文件
        tecplot_line = ListUtils.pick_line_by_keyword(block_lines, 'TECPLOT')
        rpt.tecplot = tecplot_line is not None

        solvd_line = ListUtils.pick_line_by_keyword(block_lines, 'SOLVD')
        rpt.solvd = solvd_line is not None

        geom_line = ListUtils.pick_line_by_keyword(block_lines, 'GEOM')
        rpt.geom = geom_line is not None

        binout_line = ListUtils.pick_line_by_keyword(block_lines, 'BINOUT')
        rpt.binout = binout_line is not None

        stuout_line = ListUtils.pick_line_by_keyword(block_lines, 'STUOUT')
        rpt.stuout = stuout_line is not None

        rstbin_line = ListUtils.pick_line_by_keyword(block_lines, 'RSTBIN')
        rpt.rstbin = rstbin_line is not None

        guiout_line = ListUtils.pick_line_by_keyword(block_lines, 'GUIOUT')
        rpt.guiout = guiout_line is not None

        # 选择输出的油藏动态数据和井动态数据
        items = ' '.join(block_lines[1:]).split()
        for item in items:
            stuout_data = StuoutType.of_code(item)
            if stuout_data is not None:
                rpt.stuout_data.append(stuout_data)
            wstuout_data = WstuoutType.of_code(item)
            if wstuout_data:
                rpt.wstuout_data.append(wstuout_data)

        return rpt


    def to_block(self)->list[str]:
        items = []

        # 选择输出的油藏动态数据和井动态数据
        items.extend([data.code for data in self.stuout_data])
        items.extend([data.code for data in self.wstuout_data])

        # 格式控制
        if self.precs is not None:
            items.append(f'PRECS {self.precs}')
        if self.printw is not None:
            items.append(f'PRINTW {self.printw}')
        if self.netonly:
            items.append(f'NETONLY')
        if self.rptonly:
            items.append(f'RPTONLY')
        if self.separate is not None:
            items.append(f'SEPARATE {self.separate}')
        # 选择输出文件
        if self.tecplot:
            items.append('TECPLOT')
        if self.solvd:
            items.append('SOLVD')
        if self.geom:
            items.append('GEOM')
        if self.binout:
            items.append('BINOUT')
        if self.stuout:
            items.append('STUOUT')
        if self.rstbin:
            items.append('RSTBIN')
        if self.guiout:
            items.append('GUIOUT')

        self._formatter.number_per_line = 7
        self._formatter.at_header = ''
        data_lines = self._formatter.array_1d_to_lines(items)

        lines = ['RPTSCHED']
        lines.extend(data_lines)
        lines[-1] = f'{lines[-1]} /'

        return lines

if __name__ == '__main__':
    str_ = '''
RPTSCHED 
BASIC GUIOUT TECPLOT CFL 
POIL SGAS SOIL SWAT RS MSW::OPT 
MSW::PRES MSW::VM MSW::FRICTION /    
    '''
    rpt_ = RptSched.from_block(str_.splitlines())
    print('\n'.join(rpt_.to_block()))