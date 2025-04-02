from dataclasses import dataclass, field

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.value_utils import ValueUtils


@dataclass
class StreamWell(BaseData):
    molar_fractions: list[float] = field(default_factory=list, metadata={'description': '注入气各组分的摩尔分数'})

    @classmethod
    def from_text(cls, text: str):
        if not text:
            return None

        text = text.strip().replace('STREAM', '')
        fractions = [ValueUtils.to_value(item, float) for item in text.split()]
        return cls(molar_fractions=fractions)

    def to_text(self):
        items = ['STREAM']
        items.extend([str(f) for f in self.molar_fractions])
        return ' '.join(items)

if __name__ == '__main__':
    str_ = 'STREAM 12.6 232.0 32.1'
    stream_ = StreamWell.from_text(str_)
    print(stream_.to_text())