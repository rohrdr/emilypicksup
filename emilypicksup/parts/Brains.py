import numpy as np
from scipy import interpolate 

x_default = np.array([
[88,	2260],[20,	2220],[252,	2336],[76,	2228],[316,	2284],[288,	2264],[120,	2148],[328,	2224],
[196,	2120],[456,	2240],[312,	2124],[572,	2264],[468,	2156],[712,	2340],[632,	2228],[512,	2076],
[324,	1820],[804,	2332],[748,	2232],[660,	2080],[516,	1832],[220,	1376],[800,	2124],[855,	2222],
[756,	1976],[1052,	2260],[1040,	2144],[1040,	1976],[1268,	648], [1248,	1100],[1232,	1400],[1220,	1688],
[1216,	1824],[1208,	1988],[1208,	2072],[1184,	2172],[1180,	2228],[1176,	2300],[1172,	2336],[1716,	1404],
[1552,	1828],[1460,	2072],[1392,	2228],[1352,	2336],[1428,	2244],[1440,	2220],[1516,	2268],[1560,	2200],
[1592,	2148],[2436,	1440],[2056,	1848],[1848,	2084],[1712,	2240],[1624,	2344],[1696,	2264],[1736,	2224],
[1812,	2160],[1928,	2220],[2064,	2132],[1964,	2268],[2140,	2156],[2480,	2088],[2232,	2240],[2064,	2348],
[2180,	2248],[2340,	2156],[2404,	2200],[2356,	2208],[2240,	2252],[2204,	2292],]).astype(np.float64)

zy_default = np.array([
[58],[54],[60],[50],[60],[58],[48],[54],
[46],[56],[46],[58],[48],[60],[50],[40],
[30],[60],[50],[40],[30],[20],[46],[54],
[38],[58],[48],[38],[0],[16],[20],[26],
[30],[36],[40],[46],[50],[56],[60],[20],
[30],[40],[50],[60],[56],[54],[58],[52],
[48],[20],[30],[40],[50],[60],[58],[54],
[48],[54],[46],[58],[48],[40],[50],[60],
[56],[48],[48],[52],[58],[60]
]).astype(np.float64)

zx_default = np.array([
[-22],[-22],[-20],[-20],[-18],[-18],[-18],[-16],
[-16],[-14],[-14],[-12],[-12],[-10],[-10],[-10],
[-10],[-8],[-8],[-8],[-8],[-8],[-6],[-6],
[-6],[-4],[-4],[-4],[0],[0],[0],[0],
[0],[0],[0],[0],[0],[0],[0],[4],
[4],[4],[4],[4],[6],[6],[8],[8],
[8],[10],[10],[10],[10],[10],[12],[12],
[12],[16],[16],[18],[18],[20],[20],[20],
[22],[22],[24],[24],[24],[24]
]).astype(np.float64)


class Brains:

    def __init__(self, **kwargs):
        # need to initialize some stuff

        try:
            x = kwargs['x']
            zx = kwargs['zx']
            zy = kwargs['zy']
        except:
            x = x_default
            zx = zx_default
            zy = zy_default

        self.pic_mapx = interpolate.CloughTocher2DInterpolator(x, zx)
        self.pic_mapy = interpolate.CloughTocher2DInterpolator(x, zy)

        return

    def run(self, bbox):

        throttle = 0.35
        emily = True
        emil = False
        angle = self.path_planning(bbox)
        return angle, throttle, emily, emil

    def path_planning(self, bbox):

        idx = np.argmax(bbox[:,0])
        xpic = bbox[idx, 1]
        ypic = bbox[idx, 2]
        x, y = self.pictoreal(xpic, ypic)
        diameter = (x * x + y * y) / y
        angle = selfdiatoangle(diameter)

        return angle

    def pictoreal(self, xpic, ypic):

        xy = np.array(xpic, ypic)
        x = self.pic_mapx(xy)
        y = self.pic_mapy(xy)

        return x, y

    def diatoangle(self, diameter):

        factor = 1.0
        if diameter < 0:
            factor = -1.0

        if abs(diameter) < 140:
            return factor * 1.0
        if abs(diameter) < 165:
            return factor * 0.9
        if abs(diameter) < 195:
            return factor * 0.8
        if abs(diameter) < 220:
            return factor * 0.7
        if abs(diameter) < 260:
            return factor * 0.6
        if abs(diameter) < 300:
            return factor * 0.5

        return 0.0
