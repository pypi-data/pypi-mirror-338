from collections import OrderedDict
from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData

from reservoir_info.bean.result.well_product_record import WellProductRecord
from reservoir_info.enums.product_column_name import ProductColumnName

@dataclass
class WellProduction(BaseData):
    well_name: str = field(default=None, metadata={'description': '井名'})
    unit_map: dict = field(default_factory=dict, metadata={'description': '列名枚举与单位的映射表'})
    product_records: list = field(default_factory=list, metadata={'description': '产品数据'})

    def get_column_names(self):
        return [key.value for key in self.unit_map.keys()]

    @classmethod
    def from_block(cls, block_lines):
        # 获取油井名
        well_name_line = block_lines[0].strip().replace("'", '')
        well_name = well_name_line.split(' ')[1] if 'WELL' in well_name_line else well_name_line

        #获取列名与单位名
        column_names = [name.strip() for name in block_lines[1].replace('\t', ' ').strip().split()]
        unit_names = [name.strip() for name in block_lines[2].replace('\t', ' ').strip()]
        # 列名枚举与单位的映射表
        unit_map = OrderedDict((ProductColumnName.of_code(column_name), unit_name) for column_name, unit_name in zip(column_names, unit_names))

        # 读取数据
        product_records = []
        for line in block_lines[3:]:
            if line:
                record = WellProductRecord.from_text(line, column_names)
                product_records.append(record)

        return cls(well_name, unit_map, product_records)

    def to_block(self):
        """
        将 WellProduction 对象转换为一个 block
        :return: 文本行的数据
        """
        block_lines = []
        # 添加油井名
        if 'FIELD_TOTAL' not in self.well_name and 'FIP_REG' not in self.well_name:
            block_lines.append(f"WELL '{self.well_name}'")
        else:
            block_lines.append(self.well_name)

        # 添加列名和单位名
        column_names = self.get_column_names()
        unit_names = [self.unit_map[ProductColumnName.of_code(name)]+'\t' for name in column_names]

        block_lines.extend(self._formatter.array_2d_to_lines([column_names, unit_names]))

        # 添加数据行
        for record in self.product_records:
            block_lines.append(record.to_line(column_names, '\t', 12, 2))

        return block_lines