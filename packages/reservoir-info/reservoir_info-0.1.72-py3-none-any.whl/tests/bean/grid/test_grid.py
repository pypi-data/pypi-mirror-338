import unittest

from reservoir_info.bean.grid.perm import Perm
from reservoir_info.enums.perm_type import PermType
from reservoir_info.bean.grid.fipnum import FipNum
from reservoir_info.bean.grid.grid import Grid
from reservoir_info.bean.grid.dxv import Dxv
from mag_tools.bean.dimension import Dimension


class TestGrid(unittest.TestCase):
    def test_grid(self):
        str_ = '''
        GRID
        DIMENS
        7 7 3

        DXV
        7*500

        DYV
        7*500

        DZV
        20 30 50

        TOPS
        49*8325

        PORO
        147*0.3

        PERMX
        49*500 49*50 49*200

        PERMY
        49*500 49*50 49*200

        PERMZ
         49*50 49*50 49*25
        '''
        grid_ = Grid.from_block(str_.split('\n'))
        print('\n'.join(grid_.to_block()))

    def test_dxv(self):
        str_ = '''
            DIMENS #NX=60 NY=220 NZ=85, 20ft*10ft*2ft
            60  11  65   
            '''
        dimens = Dimension.from_block(str_.splitlines())
        print('\n'.join(dimens.to_block()))

        dxv_ = Dxv.random_generate(dimens)
        print('\n'.join(dxv_.to_block()))

    def test_fipnum(self):
        _str = "FIPNUM\n201 202 203\n204 205 206"
        p = FipNum.from_block(_str.split('\n'), Dimension(2, 3, 1))
        print('\n'.join(p.to_block()))

        _str = "FIPNUM 201 202 203 204 205 206"
        p = FipNum.from_block(_str.split('\n'), Dimension(2, 3, 1))
        print('\n'.join(p.to_block()))

        _str = "FIPNUM 201 201 201 201 201 201"
        p = FipNum.from_block(_str.split('\n'), Dimension(2, 3, 1))
        print('\n'.join(p.to_block()))

        p = FipNum(Dimension(nx=5, ny=8, nz=3))
        print('\n'.join(p.to_block()))

        p = FipNum.random_generate(Dimension(2, 3, 1))
        print('\n'.join(p.to_block()))

    def test_perm(self):
        x_lines = [
            'PERMX',
            '121*1.0 121*2.0 121*3.0 121*4.0 121*5.0'
        ]
        _permx = Perm.from_block(x_lines, Dimension(11, 11, 5))
        # print('\n'.join(_permx.to_block()))

        y_lines = [
            'PERMY',
            '49.29276 162.25308 438.45926 492.32336 791.32867',
            '704.17102 752.34912 622.96875 542.24493 471.45953',
            '246.12650 82.07828 82.87408 101.65224 57.53632',
            '47.73741 55.07134 24.33975 41.06571 76.64680',
            '158.22012 84.31137 98.32045 67.18009',
            '59.36459 32.75453 48.89822 78.56290 152.85838',
            '48.61450 45.90883 49.59706 87.95659 63.36467',
            '36.76624 22.82411 12.88787 7.30505 7.74248',
            '11.78211 23.77054 123.28667 618.79059 535.32922',
            '264.58759 387.70538 682.85431 823.64056',
            '390.34323 143.02039 110.37493 66.40274 26.82064',
            '41.63234 45.19296 44.07080 37.41025 25.15281',
            '42.34485 93.56773 142.41193 71.54111 66.90506',
            '100.64468 101.82140 50.54851 68.30826 103.03153',
            '120.99303 71.92981 59.36126 38.84483',
            '82.61102 86.39167 126.21329 36.41510 18.88533',
            '12.30760 10.19921 12.95491 14.53931 111.54144',
            '302.40686 343.12231 271.43484 319.10641 428.27557',
            '438.34317 161.91951 40.33082 51.97308 35.82761',
            '18.24838 30.81277 49.74974 42.04483',
            '39.99637 55.71049 63.62318 67.26822 73.98063',
            '45.19595 42.91018 75.42314 92.84066 123.21178',
            '104.16100 131.49677 77.80956 60.96303 34.25750',
            '34.32304 70.02726 74.91326 75.89129 57.44796',
            '18.24838 30.81277 49.74974 42.04483'
        ]
        _permy = Perm.from_block(y_lines, Dimension(4, 6, 5))
        # print('\n'.join(_permy.to_block()))

        x_lines = [
            'PERMX',
            '605*1.023'
        ]
        _permx = Perm.from_block(x_lines, Dimension(11, 11, 5))
        print('\n'.join(_permx.to_block()))

        p = Perm(perm_type=PermType.PERM_X, dimens=Dimension(nx=21, ny=3, nz=5))
        print('\n'.join(p.to_block()))

        p = Perm.random_generate(PermType.PERM_X, Dimension(11, 11, 5))
        print('\n'.join(p.to_block()))