from dataclasses import dataclass, field
from datetime import date
from typing import Optional

import numpy as np
from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.array_utils import ArrayUtils
from mag_tools.utils.data.date_utils import DateUtils
from mag_tools.utils.data.list_utils import ListUtils

from mag_tools.bean.dimension import Dimension
from reservoir_info.bean.schedule.recurrent.well_control import WellControl

@dataclass
class TimeControl(BaseData):
    ctl_date: list[date or float] = field(default_factory=list, metadata={'description': '%Y-%m-%d 格式的日期'})
    well_controls: list[WellControl] = field(default_factory=lambda: [], metadata={'description': '井控数据'})
    restart: Optional[bool] = field(default=None, metadata={'description': '标识输出重启动文件的时间点'})
    #
    _dimens: Dimension = field(default=None, metadata={'description': "网络尺寸"})

    @classmethod
    def from_block(cls, block_lines, dimens: Dimension):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) == 0:
            return None

        time_blk = cls(_dimens=dimens)

        #时间头
        time_lines = ListUtils.pick_block(block_lines, 'TIME ', 'WELL ')
        if time_lines and len(time_lines) > 1:
            if 'WELL' in time_lines[-1]:
                time_lines.pop(-1)
        else:
            time_lines = ListUtils.pick_block(block_lines, 'TIME ', 'RESTART')
            if time_lines is None or len(time_lines) == 0:
                time_lines = block_lines

        time_lines = ListUtils.trim(time_lines)


        if len(time_lines) == 1 and '*' in time_lines[0]:
            items = time_lines[0].split()
            for item in items[1:]:
                time_blk.ctl_date.extend(ArrayUtils.text_to_array_1d(item, float).tolist())
        else:
            for time_line in time_lines:
                dt = DateUtils.pick_datetime(time_line)
                if dt:
                    time_blk.ctl_date.append(dt)

        #井控数据
        wel_ctrl_lines = ListUtils.pick_tail(block_lines, 'WELL')
        wel_ctrl_blocks = ListUtils.split_by_keyword(wel_ctrl_lines, 'WELL ')
        for wel_ctrl_block in wel_ctrl_blocks:
            wel_ctrl = WellControl.from_block(wel_ctrl_block, dimens)
            time_blk.well_controls.append(wel_ctrl)

        #输出重启动文件的时间点
        restart_line = ListUtils.pick_line_by_keyword(block_lines, 'RESTART')
        time_blk.restart = restart_line is not None

        return time_blk

    def to_block(self) ->list[str]:
        self._formatter.at_header = '     '

        if len(self.ctl_date) > 0 and isinstance(self.ctl_date[0], float):
            text = ArrayUtils.array_1d_to_text(np.array(self.ctl_date))
            lines = self._formatter.array_2d_to_lines([[d] for d in text.split()])
        else:
            lines = self._formatter.array_2d_to_lines([[DateUtils.to_string(d, '%Y-%m-%d')] for d in self.ctl_date])

        lines[0]= lines[0].replace('    ', 'TIME')

        for wel_ctrl in self.well_controls:
            lines.extend(wel_ctrl.to_block())

        return lines

if __name__ == '__main__':
    str_ = '''
TIME 2010-02-01
 WELL 'W1' WRAT 5 10.135 LIMIT WCUT 0.3 0.5 #限制 WaterCut
 PERF 10 10 1 5 OPEN HZ DZ SKIN -0.1 #指定射孔长度、表皮
 WELL 'W2' WIR 4 101.35
 PERF 1 1 4 5 WI NA #将 WI 参数设置为无效
 PERF 1 1 4 5 HZ DZ #切换为 DZ 模式，模拟器用 Peaceman 公式计算 WI
#     '''
    dim_ = Dimension(nx=3, ny=5, nz=8)
    blk_ = TimeControl.from_block(str_.splitlines(), dim_)
    print('\n'.join(blk_.to_block()))


    str_ = '''
TIME 2012-03-11 #2012-03-11 打开井，再计算四个时间步 
 2012-06-27 
 2012-07-27 
 2012-08-27 
 WELL 'W1' LRAT 5 10.135 LIMIT WCUT 0.3 0.0     
 WELL 'W2' WIR 4 101.35
    '''
    blk_ = TimeControl.from_block(str_.splitlines(), dim_)
    print('\n'.join(blk_.to_block()))

    str_ = '''
TIME 20*100.0
 WELL  'W1'     BHP     4000     100.0
 WELL  'W2'     BHP     4000     100.0
 WELL  'W3'     BHP     4000     100.0
 WELL  'W4'     BHP     4000     100.0
 WELL  'W5'     WIR     5000     10000       
    '''
    blk_ = TimeControl.from_block(str_.splitlines(), dim_)
    print('\n'.join(blk_.to_block()))