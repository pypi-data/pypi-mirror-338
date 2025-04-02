from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.model.justify_type import JustifyType
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.value_utils import ValueUtils

from reservoir_info.bean.simulate.process_step import ProcessStep
from reservoir_info.enums.simulate_type import SimulateType


@dataclass
class Stage(BaseData):
    # 公共
    uuid: Optional[str] = field(default=None, metadata={"description": "模拟标识"})
    simulate_type: Optional[SimulateType] = field(default=None, metadata={"description": "模拟方式"})
    percent: float = field(init=False, default=0, metadata={'description': '当前阶段的完成率'})
    time: float = field(init=False, default=0, metadata={'description': '当前阶段的时间，单位：天'})
    timestep: float = field(init=False, default=0, metadata={'description': '时间步长，单位：天'})
    nr_step_num: int = field(init=False, default=0, metadata={'description': '本阶段牛顿迭代步数'})
    # 组分模型参数
    timestep_sn: int = field(init=False, default=0, metadata={'description': '时间步序号'})
    dp: float = field(init=False, default=0, metadata={'description': '时间步目标压力变化'})
    ds: float = field(init=False, default=0, metadata={'description': '时间步目标饱和度变化量'})
    dc: float = field(init=False, default=0, metadata={'description': '时间步目标溶解气油比、挥发油气比'})
    cfl: float = field(init=False, default=0, metadata={'description': '时间步收敛难易度'})
    titles: list[str] = field(init=False, default_factory=lambda: [], metadata={'description': '阶段列名'})
    process_steps: list[ProcessStep] = field(init=False, default_factory=list, metadata={'description': '当前阶段的迭代步骤'})
    max_mbe_of_stage: float = field(init=False, default=0, metadata={'description': '当前阶段的最大均方误差'})
    avg_mbe_of_stage: float = field(init=False, default=0, metadata={'description': '当前阶段的平均均方误差'})
    msw_mbe_of_stage: float = field(init=False, default=0, metadata={'description': '当前阶段的MSW均方误差'})
    stab_test_of_stage: int = field(init=False, default=0, metadata={'description': '当前阶段的稳定性测试'})
    flash_of_stage: int = field(init=False, default=0, metadata={'description': '当前阶段的闪蒸'})

    # 黑油模型参数
    oil: float = field(default=None, metadata={"description": "油压"})
    water: float = field(default=None, metadata={"description": "水压"})
    gas: float = field(default=None, metadata={"description": "气压"})

    @classmethod
    def from_block(cls, block_lines):
        if ListUtils.find(block_lines, 'Percent ') is not None:
            simulate_type = SimulateType.COMP
            return cls.__from_block_comp(block_lines, simulate_type)
        elif ListUtils.find(block_lines, '---  TIME ') is not None:
            simulate_type = SimulateType.BLK
            return cls.__from_block_blk(block_lines, simulate_type)
        return None

    def to_block(self)->list[str]:
        if self.simulate_type == SimulateType.COMP:
            return self.__to_block_comp()
        elif self.simulate_type == SimulateType.BLK:
            return self.__to_block_blk()
        return []

    @classmethod
    def __from_block_blk(cls, block_lines: list[str], simulate_type: SimulateType):
        block_lines = ListUtils.trim(block_lines)

        stage = cls(simulate_type=simulate_type)
        time_line = ListUtils.pick_line_by_keyword(block_lines, 'TIME =')
        stage.time = ValueUtils.pick_number(time_line)

        timestep_line = ListUtils.pick_line_by_keyword(block_lines, 'TIMESTEP =')
        numbers = ValueUtils.pick_numbers(timestep_line)
        stage.timestep = numbers[0]
        stage.nr_step_num = numbers[1]

        balance_line = ListUtils.pick_line_by_keyword(block_lines, 'MATERIAL BALANCE')
        numbers = ValueUtils.pick_numbers(balance_line)
        stage.oil = numbers[0]
        stage.water = numbers[1]
        stage.gas = numbers[2]

        return stage

    def __to_block_blk(self) -> list[str]:
        lines = list()
        lines.append(f'---  TIME =      {self.time} DAYS')
        lines.append(f'      TIMESTEP =      {self.timestep} DAYS           {self.nr_step_num} NEWTON ITERATIONS')
        lines.append(f'      MATERIAL BALANCES : OIL  {self.oil}  WATER  {self.water}  GAS  {self.gas}')

        return lines

    @classmethod
    def __from_block_comp(cls, block_lines: list[str], simulate_type: SimulateType):
        stage = cls(simulate_type=simulate_type)

        if len(block_lines) >= 4:
            # 清除出错信息行
            block_lines = ListUtils.trim(block_lines)
            block_lines = ListUtils.remove_by_keyword(block_lines, 'shifts to BHP control')
            block_lines = ListUtils.remove_by_keyword(block_lines, 'exceeds BHP boundary')
            block_lines = ListUtils.remove_by_keyword(block_lines, 'got unphysical BHP')
            block_lines = ListUtils.remove_by_keyword(block_lines, 'Roll back')

            # 进度信息
            percent_line = ListUtils.pick_line_by_keyword(block_lines, 'Percent ')
            percent_values = ValueUtils.pick_numbers(percent_line)
            stage.percent = percent_values[0]/100
            stage.time = percent_values[1]
            stage.timestep = percent_values[2]
            stage.timestep_sn = percent_values[3]

            # 步骤数据标题
            title_line = ListUtils.pick_line_by_keyword(block_lines, 'NRStep').strip()
            stage.titles = [title.strip() for title in title_line.split()]

            # 压力、饱和度等
            dp_ds_line = ListUtils.pick_line_by_keyword(block_lines, 'DP=')
            if dp_ds_line:
                end_map = {k: v for k, v in (item.split('=') for item in dp_ds_line.strip().split(' '))}
                stage.dp = ValueUtils.to_value(end_map['DP'], float)
                stage.ds = ValueUtils.to_value(end_map['DS'], float)
                stage.dc = ValueUtils.to_value(end_map['DC'], float)
                stage.cfl = ValueUtils.to_value(end_map['CFL'], float)

            # 解析步骤行和精细误差行
            mbe_line = None
            step_lines = []
            for line in block_lines[2:]:
                if len(line.split()) == len(stage.titles) - 2:
                    mbe_line = line.strip()
                    break
                step_lines.append(line)

            # 解析精细就差
            if mbe_line:
                mbe_list = [item.strip() for item in mbe_line.split(' ') if item.strip() != '']
                stage.max_mbe_of_stage = ValueUtils.to_value(mbe_list[0], float)
                stage.avg_mbe_of_stage = ValueUtils.to_value(mbe_list[1], float)
                stage.msw_mbe_of_stage = ValueUtils.to_value(mbe_list[2], float)
                if len(mbe_list) > 3:
                    txt = mbe_list[3].split('/')
                    stage.stab_test_of_stage = ValueUtils.to_value(txt[0], int)
                    stage.flash_of_stage = ValueUtils.to_value(txt[1], int)

            # 解析牛顿迭代步骤信息
            for line in step_lines:
                step = ProcessStep.from_text(line, stage.titles)
                stage.process_steps.append(step)
            stage.nr_step_num = len(stage.process_steps)

        return stage

    def __to_block_comp(self)->list[str]:
        self._formatter.pad_length = 0
        self._formatter.justify_type = JustifyType.RIGHT

        values = [self.titles]
        steps = [step.to_list(self.titles) for step in self.process_steps]
        values.extend(steps)

        avg_values = ['', self.max_mbe_of_stage, self.avg_mbe_of_stage, self.msw_mbe_of_stage,
                      f'{self.stab_test_of_stage}/{self.flash_of_stage}', '']
        values.append(avg_values)

        lines = [f' Percent   {self.percent * 100}%  Time {self.time} DAY  DT {self.timestep} DAY  TStep {self.timestep_sn}']
        lines.extend(self._formatter.array_2d_to_lines(values))
        lines.append(f' DP={self.dp} DS={self.ds} DC={self.dc} CFL={self.cfl}')

        return lines

if __name__ == '__main__':
    stage_comp = '''
 Percent   0.14%  Time 3.5 DAY  DT 1.5 DAY  TStep 3
 NRStep        MAXMBE        AVGMBE        MSWMBE    StabTest/Flash   Lin_itr
      9      0.217422    0.00150504   1.73028e-05         1761/1670         4
     10     0.0208898   0.000121658    0.00660303            0/1650         4
     11    0.00557685   4.86559e-06   0.000899253            3/1643         3
          2.06412e-06   8.30442e-09   1.16966e-05            0/1643
 DP=7.82919 DS=0.00818025 DC=0.264462 CFL=0   
'''

    stage_ = Stage.from_block(stage_comp.split('\n'))
    print('以下是组分模型：')
    print('\n'.join(stage_.to_block()))

    stage_blk = """
---  TIME =      2.000 DAYS
  TIMESTEP =      1.000 DAYS           2 NEWTON ITERATIONS
  MATERIAL BALANCES : OIL  1.00  WATER 10.00  GAS  1.00"""

    stage_ = Stage.from_block(stage_blk.split('\n'))
    print('\n以下是黑油模型：')
    print('\n'.join(stage_.to_block()))