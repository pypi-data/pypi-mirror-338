from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.value_utils import ValueUtils

from reservoir_info.enums.perforation_type import PerforationType
from mag_tools.bean.dimension import Dimension
from reservoir_info.bean.schedule.perforate_well import PerforateWell
from reservoir_info.bean.schedule.recurrent.stream_well import StreamWell
from reservoir_info.enums.well_control_type import WellControlType
from reservoir_info.enums.well_group_model import WellGroupModel
from reservoir_info.enums.well_tatio_limit_type import WellRatioLimitType


@dataclass
class WellControl(BaseData):
    """
    井控制数据
    """
    well_name: str = field(default=None, metadata={'description': '井名称'})
    #井控制
    control_type: Optional[WellControlType] = field(default=None, metadata={'description': '控制类型'})
    control_target: Optional[float] = field(default=None, metadata={'description': '控制目标值'})
    bhp_limit: Optional[float] = field(default=None, metadata={'description': '井底压力限制'})
    #井产液比例限制
    limit_type: Optional[WellRatioLimitType] = field(default=None, metadata={'description': '比例限制类型'})
    limit_threshold: Optional[float] = field(default=None, metadata={'description': '比例限制阈值'})
    multiplier: Optional[float] = field(default=None, metadata={
        'description': '井口流量乘数',
        "min": 0.0,
        "max": 1.0
    })
    #
    wefac: Optional[float] = field(default=None, metadata={
        'description': '有效工作时间比',
        "min": 0.0,
        "max": 1.0
    })
    bhp_min: Optional[float] = field(default=1.0135, metadata={'description': 'BHP 下限'})
    bhp_max: Optional[float] = field(default=1013.5, metadata={'description': 'BHP 上限'})
    thp_min: Optional[float] = field(default=None, metadata={'description': 'THP 下限'})
    thp_max: Optional[float] = field(default=None, metadata={'description': 'THP 上限'})
    vfp: Optional[str] = field(default=None, metadata={'description': 'VFP 表编号'})
    separator: Optional[str] = field(default=None, metadata={'description': '分离器'})
    welldraw: Optional[float] = field(default=None, metadata={'description': '生产压差上限'})
    group_control_model: Optional[WellGroupModel] = field(default=None, metadata={'description': '井组控制模式'})
    #完井数据
    perf_wells: list[PerforateWell] = field(default_factory=list, metadata={'description': '完井的射孔信息'})
    #注气井气体组分
    stream: Optional[StreamWell] = field(default=None, metadata={'description': '组分模型注气井气体的组分'})
    #
    _dimens: Dimension = field(default=None, metadata={'description': "网络尺寸"})

    @classmethod
    def from_block(cls, block_lines: list[str], dimens: Dimension):
        """
        从文本解析参数并创建 WellControl 对象

        :param dimens: 网络尺寸
        :param block_lines: 包含参数的文本块
        """
        block_lines = ListUtils.trim(block_lines)
        if not block_lines:
            return None

        wel_ctl = cls(_dimens=dimens)

        # 井控制数据
        well_line = ListUtils.pick_line_by_keyword(block_lines, 'WELL')
        if not well_line:
            raise ValueError('井数据不能为空')

        well_items = [item.strip() for item in well_line.split()]
        wel_ctl.well_name = well_items[1].strip("'")

        wel_ctl.control_type = WellControlType.of_name(well_items[2])
        if wel_ctl.control_type:
            wel_ctl.control_target = ValueUtils.to_value(well_items[3], float)
            wel_ctl.bhp_limit = ValueUtils.to_value(well_items[4], float)

        limit_items = ListUtils.pick_block_by_keyword(well_items, 'LIMIT', 4)
        if limit_items:
            wel_ctl.limit_type = WellRatioLimitType.of_code(limit_items[1])
            wel_ctl.limit_threshold = ValueUtils.to_value(limit_items[2], float)
            wel_ctl.multiplier = ValueUtils.to_value(limit_items[3], float)

        wefac_items = ListUtils.pick_block_by_keyword(well_items, 'WEFAC', 2)
        if wefac_items:
            wel_ctl.wefac = ValueUtils.to_value(wefac_items[1], float)

        bhp_items = ListUtils.pick_block_by_keyword(well_items, 'BHP', 3)
        if bhp_items:
            wel_ctl.bhp_min = ValueUtils.to_value(bhp_items[1], float)
            wel_ctl.bhp_max = ValueUtils.to_value(bhp_items[2], float)

        thp_items = ListUtils.pick_block_by_keyword(well_items, 'THP', 3)
        if thp_items:
            wel_ctl.thp_min = ValueUtils.to_value(thp_items[1], float)
            wel_ctl.thp_max = ValueUtils.to_value(thp_items[1], float)

        vfp_items = ListUtils.pick_block_by_keyword(well_items, 'VFP', 2)
        if vfp_items:
            wel_ctl.vfp = vfp_items[1]

        separator_items = ListUtils.pick_block_by_keyword(well_items, 'SEP', 2)
        if separator_items:
            wel_ctl.separator = separator_items[1]

        weldraw_items = ListUtils.pick_block_by_keyword(well_items, 'WELDRAW', 2)
        if weldraw_items:
            wel_ctl.weldraw = ValueUtils.to_value(weldraw_items[1], float)

        control_model_item = ListUtils.pick_line_by_any_keyword(well_items, ['GRUPP','GRUPI','FIXED'])
        if control_model_item:
            wel_ctl.group_control_model = WellGroupModel.of_code(control_model_item)

        #井射孔信息
        perf_well_lines = ListUtils.pick_block_include_keywords(block_lines, PerforationType.codes())
        for perf_well_line in perf_well_lines:
            perf_well = PerforateWell.from_text(perf_well_line, dimens)
            if perf_well:
                wel_ctl.perf_wells.append(perf_well)

        #注入气体的组分
        stream_line = ListUtils.pick_line_by_keyword(block_lines, 'STREAM')
        if stream_line:
            wel_ctl.stream = StreamWell.from_text(stream_line)

        # 未设置模式的井，根据井控制自动设置
        if wel_ctl.group_control_model is None:
            wel_ctl.group_control_model = WellGroupModel.GROUPP if wel_ctl.control_type and wel_ctl.control_type.is_product() else WellGroupModel.GROUPI

        return wel_ctl

    def to_block(self) -> list[str]:
        """
        将 WellControl 对象转换为文本

        :return: 包含参数的文本
        """
        # 井控制数据
        well_items = ["WELL", f"'{self.well_name}'"]
        if self.control_type:
            well_items.append(self.control_type.name)
        if self.control_target:
            well_items.append(self.control_target)
        if self.bhp_limit is not None:
            well_items.append(self.bhp_limit)
        # 井产液比例限制
        if self.limit_type is not None:
            well_items.extend(["LIMIT", self.limit_type.name, self.limit_threshold, self.multiplier])
        #
        if self.wefac is not None:
            well_items.extend(["WEFAC", self.wefac])
        if (self.bhp_min is not None and self.bhp_min != 1.0135) or (self.bhp_max is not None and self.bhp_max != 1013.5):
            well_items.extend(["BHP", self.bhp_min, self.bhp_max])
        if self.thp_min is not None or self.thp_max is not None:
            well_items.extend(["THP", self.thp_min, self.thp_max])
        if self.vfp is not None:
            well_items.extend(["VFP", self.vfp])
        if self.separator is not None:
            well_items.extend(["SEP", self.separator])
        if self.welldraw is not None:
            well_items.extend(["WELDRAW", self.welldraw])
        if self.group_control_model is not None:
            well_items.append(self.group_control_model.name)

        self._formatter.at_header = '  '
        lines = self._formatter.array_1d_to_lines(well_items)

        # 完井数据
        self._formatter.at_header = '    '
        self._formatter.none_default = 'NA'
        self._formatter.merge_duplicate = False
        for perf_well in self.perf_wells:
            lines.extend(self._formatter.array_1d_to_lines(perf_well.to_list()))

        if self.stream:
            lines.append(self.stream.to_text())

        return lines

if __name__ == '__main__':
    # 示例数据
    text3 = """
 WELL 'INJECT*' GRUPI BHP 420 1234
 PERF 10 10 1 5 OPEN WPIMULT 0.5
 PERF 1 1 4 5 WI NA
 STAGE 1 2 OS 4"""
    dim_ = Dimension(nx=3, ny=5, nz=8)
    well_control3 = WellControl.from_block(text3.split('\n'), dim_)
    print('\n'.join(well_control3.to_block()))