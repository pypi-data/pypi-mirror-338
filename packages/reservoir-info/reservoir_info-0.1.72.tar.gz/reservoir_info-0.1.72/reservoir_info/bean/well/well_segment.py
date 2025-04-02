from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData

from reservoir_info.bean.well.template import Template
from reservoir_info.bean.well.well_completion import WellCompletion


@dataclass
class WellSegment(BaseData):
    #井分支
    marker: Optional[str] = field(default=None, metadata={'description': '井段命名'})
    outlet: Optional[str] = field(default=None, metadata={'description': '下游井段'})
    #网络编号
    i: Optional[int] = field(default=1, metadata={'description': '井射孔所在网格的 I 编号'})
    j: Optional[int] = field(default=1, metadata={'description': '井射孔所在网格的 J 编号'})
    k1: Optional[int] = field(default=1, metadata={'description': '井射孔所在网格的起始层号'})
    k2: Optional[int] = field(default=1, metadata={'description': '井射孔所在网格的终止层号'})
    satnum: Optional[str] = field(default=None, metadata={'description': '相渗区域'})
    wcon: Optional[str] = field(default=None, metadata={'description': '井与多重网格的连接模式'})
    #完井数据
    os: Optional[str] = field(default=None, metadata={'description': '射孔连接控制, OPEN/SHUT/0-7'})
    wi: Optional[float] = field(default=0, metadata={'description': '射孔的井指数'})
    tf: Optional[float] = field(default=0, metadata={'description': '射孔的传导率系数'})
    hx: Optional[str] = field(default=0, metadata={'description': 'Hx 参数, 实数或DX'})
    hy: Optional[str] = field(default=0, metadata={'description': 'Hy 参数, 实数或DY'})
    hz: Optional[str] = field(default=0, metadata={'description': 'Hz 参数, 实数或DZ'})
    req: Optional[float] = field(default=0, metadata={'description': '等效泄油半径'})
    kh: Optional[float] = field(default=0, metadata={'description': '地层产能系数'})
    skin: Optional[float] = field(default=0, metadata={'description': '表皮系数'})
    fcd: Optional[int] = field(default=0, metadata={'description': '限流装置编号'})
    #任何数据
    rw: Optional[float] = field(default=0.25, metadata={'description': '井半径，单位：m，feet，cm，um'})
    diam: Optional[float] = field(default=0.5, metadata={'description': '井直径，单位：m，feet，cm，um'})
    length: Optional[float] = field(default=None, metadata={'description': '井段长度，单位：m，feet，cm，um'})
    dev: Optional[float] = field(default=0, metadata={'description': '井段与垂直方向的夹角，单位：度'})
    rough: Optional[float] = field(default=0, metadata={'description': '井壁粗糙元特征长度，单位：m，feet，cm，um'})
    dcj: Optional[float] = field(default=0, metadata={'description': '射孔深度减去网格中心深度，单位：m，feet，cm，um'})
    dcn: Optional[float] = field(default=0, metadata={'description': '射孔深度减去井段中点深度，单位：m，feet，cm，um'})
    xnj: Optional[float] = field(default=0, metadata={'description': '井段中点 x 坐标减去网格中心 x 坐标，单位：m，feet，cm，um'})
    ynj: Optional[float] = field(default=0, metadata={'description': '井段中点 y 坐标减去网格中心 y 坐标，单位：m，feet，cm，um'})
    stage: Optional[int] = field(default=-1, metadata={'description': '压裂段号'})
    up: Optional[int] = field(default=0, metadata={'description': '井段上部的测深'})
    down: Optional[int] = field(default=None, metadata={'description': '井段底部的测深'})
    #控流装置
    icd_ver: Optional[int] = field(default=0, metadata={'description': '控流装置（ICD）的型号'})
    icd_os: Optional[str] = field(default=1, metadata={'description': '初始时刻控流装置启动或关闭，OPEN/1--启动，SHUT/0--关闭'})
    #
    template: Optional[Template] = field(default=None, metadata={'description': '表格列名'})
    # 未知
    satmap: Optional[str] = field(default=None, metadata={'description': '未知，占位'})

    @classmethod
    def from_text(cls, text, template):
        segment = cls()

        for index, part in enumerate(text.split()):
            name = template[index].lower()
            if part == 'NA' or part == '':
                default_value = segment.get_default_value(name)
                setattr(segment, name, default_value if default_value is not None else part)
            else:
                setattr(segment, name, part)
        segment.template = template

        return segment

    def to_text(self):
        parts = []
        for index in range(self.template.size()):
            name = self.template[index].lower()
            value = getattr(self, name, "")
            if name in ['marker', 'outlet'] and value is None:
                parts.append("NA")
            elif name in ['i', 'j', 'k1'] and value == 1:
                parts.append("NA")
            elif name in ['wi', 'req', 'xnj', 'ynj', 'dcn', 'dcj', 'rough', 'dev', 'skin', 'tf', 'hx', 'hy', 'hz', 'kh', 'up', 'icd_ver'] and value == 0:
                parts.append("NA")
            elif name == 'rw' and value == 0.25:
                parts.append("NA")
            elif name == 'diam' and value == 0.5:
                parts.append("NA")
            elif name == 'icd_os' and value == 1:
                parts.append("NA")
            else:
                parts.append(str(value))
        return " ".join(parts)

    @property
    def well_completion(self):
        return WellCompletion(os=self.os,wi=self.wi,tf=self.tf,hx=self.hx,hy=self.hy,hz=self.hz,req=self.req,kh=self.kh,skin=self.skin,fcd=self.fcd)

if __name__ == '__main__':
    temp_lines = ["TEMPLATE",
            "'MARKER' 'I' 'J' 'K1' 'K2' 'OUTLET' 'WI' 'OS' 'SATMAP' 'HX' 'HY' 'HZ' 'REQ' 'SKIN' 'LENGTH' 'RW' 'DEV' 'ROUGH' 'DCJ' 'DCN' 'XNJ' 'YNJ' /"]
    temp = Template.from_block(temp_lines)

    seg_text ="''  24  25  11  11  NA  NA  SHUT  NA  0  0  0  NA  NA  NA  0.5  NA  NA  NA  1268.16  NA  NA"
    seg_ = WellSegment.from_text(seg_text, temp)
    print(seg_.to_text())
