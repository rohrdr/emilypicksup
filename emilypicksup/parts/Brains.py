import numpy as np

class Brains:

    def __init__(self):
        # need to initialize some stuff

        self.list = list(range(100000))
        self.list.reverse()

        return


    def run(self, bbox):

        throttle = 0.35
        emily = True
        emil = False

        angle = self.path_planning(bbox)
#        angle = 0.0

        return angle, throttle, emily, emil


    def path_planning(self, bbox):

        # idx = np.argmax(bbox[:,0])
        #
        # xpic = bbox[idx, 1]
        # ypic = bbox[idx, 2]
        #
        # xpic = 0.0
        # ypic = 50.0
        #
        # x, y = self.pictoreal(xpic, ypic)
        #
        # diameter = (x * x + y * y) / y
        #
        # angle = diatoangle(diameter)

        cyc = self.list.pop()

        print('cycle = ', cyc)

        angle = np.sin(cyc*0.01)

        return angle


    def pictoreal(self, xpic, ypic):

        return xpic, ypic


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