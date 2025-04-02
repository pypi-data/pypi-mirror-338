from dataclasses import dataclass, field

import numpy as np
from mag_tools.utils.data.array_utils import ArrayUtils

@dataclass
class CopyGrid:
    source_name: str = field(metadata={"description": "源数组名"})
    target_name: str = field(metadata={"description": "目标数组名"})
    i1: int = field(metadata={'description': '数组1的行数'})
    i2: int = field(metadata={'description': '数组2的行数'})
    j1: int = field(metadata={'description': '数组1的列数'})
    j2: int = field(metadata={'description': '数组2的列数'})
    k1: int = field(metadata={'description': '数组1的层数'})
    k2: int = field(metadata={'description': '数组2的层数'})
    min_val: float = field(default=float('-inf'), metadata={'description': '最小值'})
    max_val: float = field(default=float('inf'), metadata={'description': '最大值'})
    c: float = field(default=1.0, metadata={'description': '缩放因子'})
    d: float = field(default=0.0, metadata={'description': '增加值'})

    @classmethod
    def from_text(cls, text):
        items = text.split()
        source = items[1]
        target = items[2]
        i1 = int(items[3])
        i2 = int(items[4])
        j1 = int(items[5])
        j2 = int(items[6])
        k1 = int(items[7])
        k2 = int(items[8])
        min_val = float(items[9]) if len(items) > 9 and items[9] != 'NA' else float('-inf')
        max_val = float(items[10]) if len(items) > 10 and items[10] != 'NA' else float('inf')
        c = float(items[11]) if len(items) > 11 else 1.0
        d = float(items[12]) if len(items) > 12 else 0.0

        return cls(source_name=source,
                   target_name=target,
                   i1=i1, i2=i2, j1=j1, j2=j2, k1=k1, k2=k2, min_val=min_val, max_val=max_val, c=c, d=d)

    def to_text(self):
        min_val_str = 'NA' if self.min_val == float('-inf') else str(self.min_val)
        max_val_str = 'NA' if self.max_val == float('inf') else str(self.max_val)

        line = f"COPY {self.source_name} {self.target_name} {self.i1} {self.i2} {self.j1} {self.j2} {self.k1} {self.k2}"
        if self.min_val != float('-inf') or self.max_val != float('inf') or self.c != 1.0 or self.d != 0.0:
            line += f" {min_val_str} {max_val_str} {self.c} {self.d}"

        return line

    def calculate(self, source_array: list, target_array: list) -> list:
        """
        复制数组指定数据到目标数据
        :param source_array: 源数组
        :param target_array: 目标数组
        :return: 计算结果
        """
        source = np.array(source_array)
        target = np.array(target_array)
        ArrayUtils.copy_array_3d(source, target, self.k1-1, self.k2-1, self.i1-1, self.i2-1, self.j1-1, self.j2-1)
        return target.tolist()