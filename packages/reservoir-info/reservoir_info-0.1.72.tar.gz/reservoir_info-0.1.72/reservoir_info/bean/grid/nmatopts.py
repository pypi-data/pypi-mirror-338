from dataclasses import dataclass,field

import numpy as np
from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.array_utils import ArrayUtils
from mag_tools.utils.data.list_utils import ListUtils

from reservoir_info.enums.nmatopts_type import NmatoptsType


@dataclass
class Nmatopts(BaseData):
    nmatopts_type: NmatoptsType = field(default=NmatoptsType.GEOMETRIC, metadata={"description": "体积比例类型"})
    proportions: list[float] = field(default_factory=list, metadata={"description": "各层基质的体积比例"})

    @classmethod
    def from_block(cls, block_lines):
        if block_lines is None or len(block_lines) == 0:
            return None

        block_lines = ListUtils.trim(block_lines)

        nmatopts_type = NmatoptsType.of_code(block_lines[1], NmatoptsType.DESIGNATED)
        proportions = ArrayUtils.text_to_array_1d(block_lines[1], float).tolist()

        return cls(nmatopts_type=nmatopts_type, proportions=proportions)

    def to_block(self):
        lines = ['NMATOPTS']
        if self.nmatopts_type == NmatoptsType.DESIGNATED:
            data_str = ArrayUtils.array_1d_to_text(np.array(self.proportions))
            self._formatter.number_per_line = 5

            lines.extend(data_str.splitlines())
        else:
            lines.append(self.nmatopts_type.code)
        return lines

if __name__ == '__main__':
    value_str = '''
NMATOPTS
UNIFORM
'''
    data_ = Nmatopts.from_block(value_str.split('\n'))
    print('\n'.join(data_.to_block()))

    value_str = '''
NMATOPTS
0.2 0.3 0.5
    '''
    data_ = Nmatopts.from_block(value_str.split('\n'))
    print('\n'.join(data_.to_block()))
