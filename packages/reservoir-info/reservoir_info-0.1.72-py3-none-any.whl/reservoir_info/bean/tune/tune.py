from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from mag_tools.bean.base_data import BaseData


@dataclass
class Tune(BaseData):
    """
    时间步控制，求解器选择，收敛判据
        格式：字符串+数据，参数没有先后顺序
    """
    tstart: Optional[datetime] = field(default=None, metadata={'description': '开始时间'})
    tend: Optional[datetime] = field(default=None, metadata={'description': '结束时间'})
    maxitr: Optional[int] = field(default=10, metadata={'description': '最大迭代次数'})
    stepcut: Optional[float] = field(default=1.0, metadata={'description': '步长缩减的乘数'})
    mindt: Optional[float] = field(default=0.1, metadata={'description': '最小时间步长'})
    maxdt: Optional[float] = field(default=50.0, metadata={'description': '最大时间步长'})
    dtinc: Optional[float] = field(default=2.0, metadata={'description': '时间步长增加'})
    dtcut: Optional[float] = field(default=0.5, metadata={'description': '时间步长减少'})
    checkdx: Optional[bool] = field(default=False, metadata={'description': '是否检查 dx'})
    maxdp: Optional[float] = field(default=0.0, metadata={'description': '最大 dp'})
    maxds: Optional[float] = field(default=0.5, metadata={
        'description': '最大 ds',
        'min': 0.2,
        'max': 0.5})
    maxdc: Optional[float] = field(default=0.0, metadata={'description': '最大 dc'})
    mbepc: Optional[float] = field(default=1e-3, metadata={'description': '最大误差百分比'})
    mbeavg: Optional[float] = field(default=1e-7, metadata={'description': '平均误差'})
    solver: Optional[int] = field(default=1034, metadata={'description': '求解器'})
    inistol: Optional[int] = field(default=None, metadata={'description': '初始容差'})
    amgset: Optional[int] = field(default=1, metadata={'description': 'AMG 设置'})
    wsol: Optional[int] =field(default=0, metadata={'description': 'Wsol 设置'})

    @classmethod
    def from_block(cls, block_lines: list[str]):
        """
        从块字符串中解析参数并创建 Tune 对象

        :param block_lines: 包含参数的块字符串
        :return: Tune 对象
        """
        if block_lines is None or len(block_lines) == 0:
            return None

        items = ' '.join(block_lines).split()
        kwargs = {}
        i = 0
        while i < len(items):
            if items[i] == 'TSTART':
                kwargs['tstart'] = datetime.strptime(items[i+1], '%Y-%m-%d')
                i += 2
            elif items[i] in ['MINDT', 'MAXDT', 'DTINC', 'DTCUT', 'MAXDP', 'MAXDS', 'MAXDC', 'MBEPC', 'MBEAVG']:
                kwargs[items[i].lower()] = float(items[i+1])
                i += 2
            elif items[i] == 'CHECKDX':
                kwargs['checkdx'] = True
                i += 1
            elif items[i] == 'NCHECHDX':
                kwargs['checkdx'] = False
                i += 1
            elif items[i] == 'SOLVER':
                kwargs['solver'] = int(items[i+1])
                i += 2
            else:
                i += 1
        return cls(**kwargs)

    def to_block(self) -> list[str]:
        """
        将 Tune 对象转换为块字符串列表

        :return: 包含参数的块字符串列表
        """
        block_lines = [
            "TUNE",
            f"TSTART {self.tstart.strftime('%Y-%m-%d') if self.tstart else ''}",
            f"MINDT {self.mindt} MAXDT {self.maxdt} DTINC {self.dtinc} DTCUT {self.dtcut} {'CHECKDX' if self.checkdx else 'NCHECHDX'}",
            f"MAXDP {self.maxdp} MAXDS {self.maxds} MAXDC {self.maxdc} MBEPC {self.mbepc} MBEAVG {self.mbeavg}",
            f"SOLVER {self.solver}"
        ]
        return block_lines

    def __str__(self):
        return '\n'.join(self.to_block())

if __name__ == '__main__':
    # 示例数据
    _block_lines = """
    TUNE
    TSTART  1990-01-01 
    MINDT  0.1  MAXDT  31  DTINC  2.0  DTCUT  0.5  NCHECKDX  
    MAXDP  200  MAXDS  0  MAXDC  0  MBEPC  1E-4  MBEAVG  1E-6   
    SOLVER  1034
    """
    _tune = Tune.from_block(_block_lines.split('\n'))

    print(_tune)
