from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils

from mag_tools.bean.dimension import Dimension
from reservoir_info.bean.schedule.recurrent.time_control import TimeControl


@dataclass
class Recurrent(BaseData):
    """
    井和油藏参数的控制序列
    """
    time_ctls: list[TimeControl] = field(default_factory=list, metadata={'description': '时间控制序列'})

    @classmethod
    def from_block(cls, block_lines: list[str], dimens: Dimension):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 2:
            return None

        recurrent = cls()
        time_blocks = ListUtils.split_by_keyword(block_lines[1:], 'TIME ')
        for time_block in time_blocks:
            time_ctl = TimeControl.from_block(time_block, dimens)
            if time_ctl:
                recurrent.time_ctls.append(time_ctl)

        return recurrent

    def to_block(self):
        lines = ['RECURRENT']
        for time_ctl in self.time_ctls:
            lines.extend(time_ctl.to_block())
            lines.append('')

        return lines


if __name__ == '__main__':
    str_ = '''
RECURRENT 
TIME 2010-01-01 
 WELL 'W2' WIR 4 101.35 
 PERF 1 1 4 5 OPEN WI 33.0 #指定射孔 WI 
 
TIME 2010-02-01 
 WELL 'W1' WRAT 5 10.135 LIMIT WCUT 0.3 0.5 #限制 WaterCut 
 PERF 10 10 1 5 OPEN HZ DZ SKIN -0.1 #指定射孔长度、表皮 
 WELL 'W2' WIR 4 101.35 
 PERF 1 1 4 5 WI NA #将 WI 参数设置为无效 
 PERF 1 1 4 5 HZ DZ #切换为 DZ 模式，模拟器用 Peaceman 公式计算 WI 
 
TIME 2010-06-1 #无数据，延续前一步的状态 
 
TIME 2011-05-16 
 WELL 'W1' LRAT 5 10.135 LIMIT WCUT 0.3 0.0 
 WELL 'W2' WIR 4 101.35 
 
TIME 2011-12-02 #自 2011-12-02 起关闭井 
 WELL 'W1' SHUT 0 10.135 
 PERF 10 10 1 5 SHUT 
 WELL 'W2' SHUT 0 101.35 
 PERF 1 1 4 5 SHUT #自 2011-12-02 起关闭射孔 
 
TIME 2012-03-11 #2012-03-11 打开井，再计算四个时间步 
 2012-06-27 
 2012-07-27 
 2012-08-27 
 WELL 'W1' LRAT 5 10.135 LIMIT WCUT 0.3 0.0
 
 RESTART   
    '''
    recurrent_ = Recurrent.from_block(str_.splitlines(), Dimension(12, 10, 8))
    print('\n'.join(recurrent_.to_block()))
