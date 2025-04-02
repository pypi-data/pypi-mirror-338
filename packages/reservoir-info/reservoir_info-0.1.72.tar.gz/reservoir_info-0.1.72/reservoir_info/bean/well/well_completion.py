from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.base_data import BaseData
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.value_utils import ValueUtils

from mag_tools.bean.dimension import Dimension


@dataclass
class WellCompletion(BaseData):
    """
    完井数据
    """
    os: Optional[str] = field(default=None, metadata={'description': '射孔连接控制, OPEN/SHUT/0-7'})
    wi: Optional[float] = field(default=0, metadata={'description': '射孔的井指数'})
    tf: Optional[float] = field(default=0, metadata={'description': '射孔的传导率系数'})
    hx: Optional[float] = field(default=0, metadata={'description': 'Hx 参数'})
    hy: Optional[float] = field(default=0, metadata={'description': 'Hy 参数'})
    hz: Optional[float] = field(default=0, metadata={'description': 'Hz 参数'})
    req: Optional[float] = field(default=0, metadata={'description': '等效泄油半径'})
    kh: Optional[float] = field(default=0, metadata={'description': '地层产能系数'})
    skin: Optional[float] = field(default=0, metadata={'description': '表皮系数'})
    fcd: Optional[int] = field(default=0, metadata={'description': '限流装置编号'})
    wpimult: Optional[float] = field(default=None, metadata={'description': '井指数缩放系数'})
    icd_os: Optional[int] = field(default=None, metadata={'description': '控流装置开关'})
    #
    _dimens: Dimension = field(default=None, metadata={'description': "网络尺寸"})

    @classmethod
    def from_text(cls, text: str, dimens: Dimension):
        if not text:
            return None

        wel_comp = cls(_dimens=dimens)
        items = text.split()
        open_shut_item = ListUtils.pick_line_by_any_keyword(items, ['OPEN', 'SHUT'])
        if open_shut_item:
            wel_comp.os = open_shut_item

        os_items = ListUtils.pick_block_by_keyword(items, 'OS', 2)
        if os_items:
            wel_comp.os = os_items[1]

        wi_items = ListUtils.pick_block_by_keyword(items, 'WI', 2)
        if wi_items:
            wel_comp.wi = ValueUtils.to_value(wi_items[1], float)

        tf_items = ListUtils.pick_block_by_keyword(items, 'TF', 2)
        if tf_items:
            wel_comp.tf = ValueUtils.to_value(tf_items[1], float)

        hx_items = ListUtils.pick_block_by_keyword(items, 'HX', 2)
        if hx_items:
            wel_comp.hx = ValueUtils.to_value(hx_items[1], float) if hx_items[1] != 'DX' else dimens.nx

        hy_items = ListUtils.pick_block_by_keyword(items, 'HY', 2)
        if hy_items:
            wel_comp.hy = ValueUtils.to_value(hy_items[1], float) if hy_items[1] != 'DY' else dimens.ny

        hz_items = ListUtils.pick_block_by_keyword(items, 'HZ', 2)
        if hz_items:
            wel_comp.hz = ValueUtils.to_value(hz_items[1], float) if hz_items[1] != 'DZ' else dimens.nz

        req_items = ListUtils.pick_block_by_keyword(items, 'REQ', 2)
        if req_items:
            wel_comp.req = ValueUtils.to_value(req_items[1], float)

        kh_items = ListUtils.pick_block_by_keyword(items, 'KH', 2)
        if kh_items:
            wel_comp.kh = ValueUtils.to_value(kh_items[1], float)

        skin_items = ListUtils.pick_block_by_keyword(items, 'SKIN', 2)
        if skin_items:
            wel_comp.skin = ValueUtils.to_value(skin_items[1], float)

        wpimult_items = ListUtils.pick_block_by_keyword(items, 'WPIMULT', 2)
        if wpimult_items:
            wel_comp.wpimult = ValueUtils.to_value(wpimult_items[1], float)

        icd_os_items = ListUtils.pick_block_by_keyword(items, 'ICD_OS', 2)
        if icd_os_items:
            wel_comp.icd_os = ValueUtils.to_value(icd_os_items[1], int)

        return wel_comp

    def to_text(self) -> Optional[str]:
        items = list()
        if self.os:
            items.append(f'OS {self.os}' if self.os.isdigit() else self.os)

        if self.wi:
            items.append(f'WI {self.wi}')

        if self.tf:
            items.append(f'TF {self.tf}')

        if self.hx:
            items.append(f'HX {self.hx}' if self.hx != self._dimens.nx else 'HX DX')

        if self.hy:
            items.append(f'HY {self.hy}' if self.hy != self._dimens.ny else 'HY DY')

        if self.hz:
            items.append(f'HZ {self.hz}' if self.hz != self._dimens.nz else 'HZ DZ')

        if self.req:
            items.append(f'REQ {self.req}')

        if self.kh:
            items.append(f'KH {self.kh}')

        if self.skin:
            items.append(f'SKIN {self.skin}')

        if self.fcd:
            items.append(f'FCD {self.fcd}')

        if self.wpimult:
            items.append(f'WPIMULT {self.wpimult}')

        if self.icd_os:
            items.append(f'ICD_OD {self.icd_os}')

        return ' '.join(items) if items else None

if __name__ == '__main__':
    dim_ = Dimension(nx=3,ny=5,nz=8)
    str_ = 'OPEN HZ DZ SKIN 0.1 WPIMULT 0.5'
    wel_comp_ = WellCompletion.from_text(str_, dim_)
    print(wel_comp_.to_text())