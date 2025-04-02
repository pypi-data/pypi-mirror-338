from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.common.string_utils import StringUtils
from mag_tools.utils.data.list_utils import ListUtils


@dataclass
class Group(BaseData):
    """
    单个井组
    """
    name: str = field(default=None, metadata={'description': '井组名'})
    well_names: list[str] = field(default_factory=list, metadata={'description': '井名清单'})

    @classmethod
    def from_text(cls, text: str):
        if not text:
            return None

        text = StringUtils.pick_head(text, '#').replace('/', '').replace("'", "")
        items = text.split()
        return cls(name=items[1], well_names=items[2:])

    def to_text(self) -> str:
        items = ['GROUP', f"'{self.name}'"]
        items.extend([f"'{name}'" for name in self.well_names])
        items.append('/')
        return ' '.join(items)

@dataclass
class GroupWell(BaseData):
    """
    井组信息
    """
    groups: list[Group] = field(default_factory=list, metadata={'description': '井组名列表'})

    @classmethod
    def from_block(cls, block_lines):
        block_lines = ListUtils.trim(block_lines)
        if block_lines is None or len(block_lines) < 2:
            return None

        gw = cls()
        for line in block_lines[1:]:
            gw.groups.append(Group.from_text(line))
        return gw

    def to_block(self) -> list[str]:
        lines = ['GROUPWELL']
        lines.extend([group.to_text() for group in self.groups])
        return lines

if __name__ == '__main__':
    str_ = '''
GROUPWELL 
GROUP 'GPROD' 'PROD1' 'PROD2' 'PROD3' 'PROD4' / 
GROUP 'GINJ' 'INJ*' / #用到了通配符    
    '''
    gw_ = GroupWell.from_block(str_.splitlines())
    print('\n'.join(gw_.to_block()))