from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils

from reservoir_info.enums.product_column_name import ProductColumnName


@dataclass
class WellProductRecord(BaseData):
    """
    井生产数据类，包含了井的生产和注入数据。
    """
    report_time: Optional[str] = field(default=None, metadata={'description': '报告时间，格式为 "YYYY-MM-DD HH:MM"'})
    work_time: Optional[float] = field(default=None, metadata={'description': '工作时长，单位为 DAYS'})
    water_product_rate: Optional[float] = field(default=None, metadata={'description': '水生产速率，单位为 STB/DAY'})
    gas_product_rate: Optional[float] = field(default=None, metadata={'description': '气生产速率，单位为 Mscf/DAY'})
    oil_product_rate: Optional[float] = field(default=None, metadata={'description': '油生产速率，单位为 STB/DAY'})
    water_inject_rate: Optional[float] = field(default=None, metadata={'description': '水注入速率，单位为 STB/DAY'})
    gas_inject_rate: Optional[float] = field(default=None, metadata={'description': '气注入速率，单位为 Mscf/DAY'})
    water_product_total: Optional[float] = field(default=None, metadata={'description': '累计水生产量，单位为 STB'})
    gas_product_total: Optional[float] = field(default=None, metadata={'description': '累计气生产量，单位为 Mscf'})
    oil_product_total: Optional[float] = field(default=None, metadata={'description': '累计油生产量，单位为 STB'})
    water_inject_total: Optional[float] = field(default=None, metadata={'description': '累计水注入量，单位为 STB'})
    gas_inject_total: Optional[float] = field(default=None, metadata={'description': '累计气注入量，单位为 Mscf'})
    bottom_hole_pressure: Optional[float] = field(default=None, metadata={'description': '井底压力，单位为 PSIA'})
    tubing_head_pressure: Optional[float] = field(default=None, metadata={'description': '油管头压力，单位为 PSIA'})
    liquid_product_rate: Optional[float] = field(default=None, metadata={'description': '液体生产速率，单位为 STB/DAY'})
    liquid_product_total: Optional[float] = field(default=None, metadata={'description': '液体生产总量，单位为 STB'})
    water_cut: Optional[float] = field(default=None, metadata={'description': '生产液体中水的比例，单位为 STB/STB'})
    water_gas_ratio: Optional[float] = field(default=None, metadata={'description': '水汽比，单位为 STB/Mscf'})
    gas_oil_ratio: Optional[float] = field(default=None, metadata={'description': '气油比，单位为 STB/Mscf'})
    increase_time: Optional[float] = field(default=None, metadata={'description': '递增时间，单位为 DAY'})
    molar_flow_rate: Optional[float] = field(default=None, metadata={'description': '摩尔流速，单位为 mol/s'})

    @classmethod
    def from_text(cls, text: str, column_names: list[str]):
        """
        从一行文本中解析数据并创建 WellProduction 对象。
        参数：
        :param column_names: 列名列表
        :param text: 生产数据
        :return: WellProduction
        """
        if text is None:
            return None

        column_names = ListUtils.trim(column_names)

        value_line = text.replace('\t', ' ')
        values = [value.strip() for value in value_line.split()]
        values = [float(value) if isinstance(value, float) else value for value in values]

        data = {name: value for name, value in zip(column_names, values)}

        try:
            return cls(report_time=data[ProductColumnName.REPORT_TIME.code],
                       work_time=float(data[ProductColumnName.WORK_TIME.code]),
                       water_product_rate=float(data[ProductColumnName.WATER_PRODUCT_RATE.code]),
                       gas_product_rate=float(data[ProductColumnName.GAS_PRODUCT_RATE.code]),
                       oil_product_rate=float(data[ProductColumnName.OIL_PRODUCT_RATE.code]),
                       water_inject_rate=float(data[ProductColumnName.WATER_INJECT_RATE.code]),
                       gas_inject_rate=float(data[ProductColumnName.GAS_INJECT_RATE.code]),
                       water_product_total=float(data[ProductColumnName.WATER_PRODUCT_TOTAL.code]),
                       gas_product_total=float(data[ProductColumnName.GAS_PRODUCT_TOTAL.code]),
                       oil_product_total=float(data[ProductColumnName.OIL_PRODUCT_TOTAL.code]),
                       water_inject_total=float(data[ProductColumnName.WATER_INJECT_TOTAL.code]),
                       gas_inject_total=float(data[ProductColumnName.GAS_INJECT_TOTAL.code]),
                       bottom_hole_pressure=float(data[ProductColumnName.BOTTOM_HOLE_PRESSURE.code]),
                       tubing_head_pressure=float(data[ProductColumnName.TUBING_HEAD_PRESSURE.code]),
                       liquid_product_rate=float(data[ProductColumnName.LIQUID_PRODUCT_RATE.code]),
                       liquid_product_total=float(data[ProductColumnName.LIQUID_PRODUCT_TOTAL.code]),
                       water_cut=float(data[ProductColumnName.WATER_CUT.code]),
                       water_gas_ratio=float(data[ProductColumnName.WATER_GAS_RATIO.code]),
                       gas_oil_ratio=float(data[ProductColumnName.GAS_OIL_RATIO.code]),
                       increase_time=float(data[ProductColumnName.INCREASE_TIME.code]),
                       molar_flow_rate=None)
        except (KeyError, ValueError, TypeError, Exception) as e:
            print(f"{data}: {str(e)}")

    def to_text(self, column_names: list[str]) -> str:
        """
        将 WellProductRecord 对象转换为以 分隔符分隔的字符串。
        :return: 以 sep 分隔的字符串
        """
        self._formatter.decimal_places = 5

        data = {ProductColumnName.REPORT_TIME.code: self.report_time,
                ProductColumnName.WORK_TIME.code: self.work_time,
                ProductColumnName.WATER_PRODUCT_RATE.code: self.water_product_rate,
                ProductColumnName.GAS_PRODUCT_RATE.code: self.gas_product_rate,
                ProductColumnName.OIL_PRODUCT_RATE.code: self.oil_product_rate,
                ProductColumnName.WATER_INJECT_RATE.code: self.water_inject_rate,
                ProductColumnName.GAS_INJECT_RATE.code: self.gas_inject_rate,
                ProductColumnName.WATER_PRODUCT_TOTAL.code: self.water_product_total,
                ProductColumnName.GAS_PRODUCT_TOTAL.code: self.gas_product_total,
                ProductColumnName.OIL_PRODUCT_TOTAL.code: self.oil_product_total,
                ProductColumnName.WATER_INJECT_TOTAL.code: self.water_inject_total,
                ProductColumnName.GAS_INJECT_TOTAL.code: self.gas_inject_total,
                ProductColumnName.BOTTOM_HOLE_PRESSURE.code: self.bottom_hole_pressure,
                ProductColumnName.TUBING_HEAD_PRESSURE.code: self.tubing_head_pressure,
                ProductColumnName.LIQUID_PRODUCT_RATE.code: self.liquid_product_rate,
                ProductColumnName.LIQUID_PRODUCT_TOTAL.code: self.liquid_product_total,
                ProductColumnName.WATER_CUT.code: self.water_cut,
                ProductColumnName.WATER_GAS_RATIO.code: self.water_gas_ratio,
                ProductColumnName.GAS_OIL_RATIO.code: self.gas_oil_ratio,
                ProductColumnName.INCREASE_TIME.code: self.increase_time,
                ProductColumnName.MOLAR_FLOW_RATE.code: self.molar_flow_rate}

        values = [data[column_name] for column_name in column_names]
        return self._formatter.array_1d_to_lines(values)

if __name__ == '__main__':
    title_str = '''
    Time	    WorkTime	 WatProdRate	 GasProdRate	 OilProdRate	  WatInjRate	  GasInjRate	WatProdTotal	GasProdTotal	OilProdTotal	 WatInjTotal	 GasInjTotal	         BHP	         THP	 LiqProdRate	LiqProdTotal	    WaterCut	 WatGasRatio	 GasOilRatio	    IncrTime
    '''
    value_str = '''
    0.02	        0.01	     27.5575	           0	     16130.5	        5000	           0	    0.576931	           0	     387.606	         100	           0	     6021.85	           0	       16158	     388.183	   0.0017055	         INF	           0	        0.02
           '''
    column_names_ = title_str.replace('\n', '').split('\t')
    column_names_ = [name.strip() for name in column_names_]
    record = WellProductRecord.from_text(value_str, column_names_)

    _lines = record.to_text(column_names_)
    for line in _lines:
        print(line)
