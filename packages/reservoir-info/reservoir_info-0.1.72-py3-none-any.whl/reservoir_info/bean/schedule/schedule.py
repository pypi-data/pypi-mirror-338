from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils

from reservoir_info.bean.schedule.rpt_sched import RptSched
from reservoir_info.bean.schedule.rpt_sum.rpt_sum import RptSum
from mag_tools.bean.dimension import Dimension
from reservoir_info.bean.schedule.vfp.vfp_inj import VfpInj
from reservoir_info.bean.schedule.recurrent.recurrent import Recurrent
from reservoir_info.bean.schedule.vfp.vfp_prod import VfpProd
from reservoir_info.bean.schedule.group_well import GroupWell
from reservoir_info.enums.user_time_type import UserTimeType


@dataclass
class Schedule(BaseData):
    """
    井口控制与生产动态信息，包括：井口控制，井产率限制，井射孔控制，油藏参数随时间变化，以及文件输出控制
    """
    use_time_type: UserTimeType = field(default=UserTimeType.USEENDTIME, metadata={'description': '时间类型'})
    group_well: Optional[GroupWell] = field(default=None, metadata={'description': "井组信息"})
    vfp_prod: Optional[VfpProd] = field(default=None, metadata={'description': '生产井的 VFP 表'})
    vfp_inj: Optional[VfpInj] = field(default=None, metadata={'description': '注入井的 VFP 表'})
    recurrent: Optional[Recurrent] = field(default=None, metadata={'description': '井和油藏参数的控制序列'})
    rpt_sched: Optional[RptSched] = field(default=None, metadata={'description': '报告输出格式、内容控制'})
    rpt_sum: Optional[RptSum] = field(default=None, metadata={'description': '控制油藏统计信息的输出'})

    @classmethod
    def from_block(cls, block_lines: list[str],  dimens: Dimension):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 2:
            return None
        block_lines = ListUtils.remove_by_header(block_lines, '###')

        scheduler = cls()
        time_type_line = ListUtils.pick_line_by_keyword(block_lines, 'USESTARTTIME')
        scheduler.time_type = UserTimeType.USESTARTTIME if time_type_line else UserTimeType.USEENDTIME

        group_well_lines = ListUtils.pick_block(block_lines, 'GROUPWELL', '')
        scheduler.group_well = GroupWell.from_block(group_well_lines)

        vfp_prod_lines = ListUtils.pick_block(block_lines, 'VFPPROD', '')
        scheduler.vfp_prod = VfpProd.from_block(vfp_prod_lines)

        vfp_inj_lines = ListUtils.pick_block(block_lines, 'VFPINJ', '')
        scheduler.vfp_inj = VfpProd.from_block(vfp_inj_lines)

        recurrent_lines = ListUtils.pick_block(block_lines, 'RECURRENT', 'RPTSCHED')
        if recurrent_lines is not None:
            recurrent_lines.pop(-1)
            scheduler.recurrent = Recurrent.from_block(recurrent_lines, dimens)

        rpt_sched_lines = ListUtils.pick_block(block_lines, 'RPTSCHED', '')
        scheduler.rpt_sched = RptSched.from_block(rpt_sched_lines)

        rpt_sum_lines = ListUtils.pick_block(block_lines, 'RPTSUM', '')
        scheduler.rpt_sum = RptSum.from_block(rpt_sum_lines)

        return scheduler

    def to_block(self):
        lines = list()
        lines.append('SCHEDULE')

        if self.use_time_type:
            lines.append(self.use_time_type.code)

        if self.recurrent:
            lines.extend(self.recurrent.to_block())

        if self.group_well:
            lines.extend(self.group_well.to_block())
            lines.append('')

        if self.vfp_prod:
            lines.extend(self.vfp_prod.to_block())
            lines.append('')

        if self.vfp_inj:
            lines.extend(self.vfp_inj.to_block())
            lines.append('')

        if self.rpt_sched:
            lines.extend(self.rpt_sched.to_block())
            lines.append('')

        if self.rpt_sum:
            lines.extend(self.rpt_sum.to_block())
            lines.append('')

        return lines

if __name__ == '__main__':
#     str_ = '''
# SCHEDULE
# RECURRENT
# TIME 20*100.0
#  WELL  'W1'     BHP     4000     100.0
#  WELL  'W2'     BHP     4000     100.0
#  WELL  'W3'     BHP     4000     100.0
#  WELL  'W4'     BHP     4000     100.0
#  WELL  'W5'     WIR     5000     10000
#
# RPTSCHED
#  BASIC TECPLOT  /
#
# RPTSUM
#  FWIP /
#  FOIP /
#  /
#     '''
    # sec_ = Schedule.from_block(str_.splitlines(), Dimension(2,5,8))
    # print('\n'.join(sec_.to_block()))

    str_ = '''
SCHEDULE
USESTARTTIME  # All date is the start time of the operation
RECURRENT
TIME  1990-01-01
# WellID.    Ctrl  Val  BHP bd  		
  WELL  'INJE1'  WIR   5000   4000  	  
  WELL  'PROD2'  ORAT  1500   1000
  WELL  'PROD3'  ORAT  1500   1000  
  WELL  'PROD9'  ORAT  1500   1000  
  WELL  'PROD10'  ORAT  1500   1000  
  WELL  'PROD11'  ORAT  1500   1000  
  WELL  'PROD12'  ORAT  1500   1000  
  WELL  'PROD13'  ORAT  1500   1000  

TIME  1990-01-02

TIME  1990-07-20

TIME  1990-10-28
# WellID.    Ctrl  Val  BHP bd  		
  WELL  'INJE1'  WIR   5000  4000 
  WELL  'PROD2'  ORAT  100   1000  
  WELL  'PROD10'  ORAT  100   1000  
  WELL  'PROD17'  ORAT  100   1000      
	    
TIME  1990-12-27
# WellID.    Ctrl  Val  BHP bd  		
  WELL  'INJE1'  WIR   5000   4000
  WELL  'PROD2'  ORAT  1500   1000  
  WELL  'PROD3'  ORAT  1500   1000      

TIME  1991-02-25

TIME  1991-03-26

RESTART

RPTSCHED
BINOUT SEPARATE NETONLY GEOM RPTONLY RSTBIN SOLVD 
POIL SOIL SGAS SWAT RS NOSTU  TECPLOT 
 /

RPTSUM
POIL 1 2 1 /
POIL AVG Reg 2 /
/    
    '''
    sec_ = Schedule.from_block(str_.splitlines(), Dimension(2,5,8))
    print('\n'.join(sec_.to_block()))



        
