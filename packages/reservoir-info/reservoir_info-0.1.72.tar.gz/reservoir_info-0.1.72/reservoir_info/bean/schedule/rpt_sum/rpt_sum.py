from dataclasses import dataclass, field

from mag_tools.bean.common.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils

from reservoir_info.enums.fptfit_type import FptfitType
from reservoir_info.enums.ftp_type import FipType
from reservoir_info.enums.sum_type import SumType
from reservoir_info.bean.schedule.rpt_sum.attribute_value import AttributeValue
from reservoir_info.bean.schedule.rpt_sum.fip_sum import FipSum
from reservoir_info.bean.schedule.rpt_sum.fptfit_sum import FptfitSum
from reservoir_info.bean.schedule.rpt_sum.attribute_sum import AttributeSum


@dataclass
class RptSum(BaseData):
    """
    控制油藏统计信息的输出
    """

    # 模型FIP和分区FIP
    fip_sums: list[FipSum] = field(default_factory=list, metadata={'description': '地层单位体积内的油水气储量'})
    # 模型累计油、水、气产量和累计油、水、气注入量
    fptfit_sums: list[FptfitSum] = field(default_factory=list, metadata={'description': '整个油藏或区域的累积油水气产量和注入量'})
    # 网格动态或静态属性的统计值
    attribute_sums: list[AttributeSum] = field(default_factory=list, metadata={'description': "网格动态或静态属性的统计值"})
    # 特定网格的动态或静态属性
    attribute_values: list[AttributeValue] = field(default_factory=list, metadata={'description': '特定网格的动态或静态属性'})

    @classmethod
    def from_block(cls, block_lines):
        if block_lines is None or len(block_lines) < 2:
            return None

        rpt_sum = cls()

        fip_lines = ListUtils.pick_block_include_keywords(block_lines, FipType.codes())
        rpt_sum.fip_sums = [FipSum.from_text(line) for line in fip_lines]

        fptfit_lines = ListUtils.pick_block_include_keywords(block_lines, FptfitType.codes())
        rpt_sum.fptfit_sums = [FptfitSum.from_text(line) for line in fptfit_lines]

        attr_sum_lines = ListUtils.pick_block_include_keywords(block_lines, SumType.codes())
        rpt_sum.attribute_sums = [AttributeSum.from_text(line) for line in attr_sum_lines]

        for line in block_lines:
            attr_value = AttributeValue.from_text(line)
            if attr_value is not None:
                rpt_sum.attribute_values.append(attr_value)

        return rpt_sum

    def to_block(self):
        lines = ['RPTSUM']
        for fip_sum in self.fip_sums:
            lines.append(fip_sum.to_text())

        for fptfit_sum in self.fptfit_sums:
            lines.append(fptfit_sum.to_text())

        for attribute_sum in self.attribute_sums:
            lines.append(attribute_sum.to_text())

        for attribute_value in self.attribute_values:
            lines.append(attribute_value.to_text())

        return lines

if __name__ == '__main__':
    str_ = '''
RPTSUM 
FWIP / #油田中水的 FIP 
FGIP / #油田中气的 FIP 
FOIP / #油田中油的 FIP 
FWIP REG 1 / #区域 1 水的 FIP 
FGIP REG 1 / #区域 1 气的 FIP 
FOIP REG 1 / #区域 1 油的 FIP 
FWIP REG 2 / #区域 2 水的 FIP 
FGIP REG 2 / #区域 2 气的 FIP 
FOIP REG 2 / #区域 2 油的 FIP 
FWPT / #总累计水产量 
FGPT / #总累计气产量 
FOPT / #总累计油产量 
FWIT / #总累计水注入量 
FGIT / #总累计气注入量 
SWAT AVG / #水饱和度均值   
SWAT WAVG / #水饱和度均值，按孔隙体积加权 
SWAT MAX / #水饱和度最大值 
SWAT MIN / #水饱和度最小值 
SWAT 1 1 1 / #网格(1, 1, 1)的水饱和度 
ZMF1 13 18 5 / #网格(13,18,5)组分 1 的摩尔分数 
ZMF2 WAVG / #组分 2 摩尔分数的均值，按孔隙体积加权 
PGAS CARFIN 'FIN1' 8 5 1 / #输出加密区'FIN1'内网格(8, 5, 1)的值 
POIL CARFIN 'FIN1' MAX / #输出加密区'FIN1'的最大值 
POIL EMDF 'f1' WAVG / #输出裂缝'f1'所含网格的（孔隙体积加权）平均值 
POIL EMDF 'f1' MIN / #输出裂缝'f1'所含网格的最小值 
/ 
    '''
    sum_ = RptSum.from_block(str_.splitlines())
    print('\n'.join(sum_.to_block()))