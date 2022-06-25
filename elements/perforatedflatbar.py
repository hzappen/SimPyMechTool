import math
from solid import *
from solid.extensions.bosl2 import *


STD_WIDTH = 15
STD_HEIGHT = 2
STD_HOLE_DISTANCE = 10
STD_HOLE_DIAMETER = 5
STD_HOLE_HEIGHT = STD_HEIGHT + 1
STD_HOLE_MIN_DIST_EDGE = STD_HOLE_DISTANCE / 4

class PerforatedStraightBar(cuboid):
    def __init__(self,length):
        self.name = "cuboid"
        self.params = {"size": length}
        super().__init__(self.name,self.params)

        self.numberofHoles = int(math.floor(length-2*STD_HOLE_MIN_DIST_EDGE)/(STD_HOLE_DISTANCE))
        self.holes = []
        bar = cuboid([length,STD_WIDTH,STD_HEIGHT])
        bar = bar.translate([length/2,0,0])
        for index,hole in enumerate(range(0,self.numberofHoles)):
            x_pos = ((index + 1)* STD_HOLE_DISTANCE)+STD_HOLE_MIN_DIST_EDGE
            myHole = cylinder(h=STD_HOLE_HEIGHT,d=STD_HOLE_DIAMETER,center=True)
            myHole = myHole.translate([x_pos,0,0])
            print(myHole.params)
            self.holes.append(myHole)
            bar = bar - myHole

        bar = bar.translate([-length/2,0,0])
        self.bar = bar.copy()


    def getSCADobj(self):
        return self.bar

    def getHolePositions(self,holeIndex: int):
        if holeIndex > self.numberofHoles-1:
            return [0, 0, 0]
        else:
            pos = self.holes[holeIndex].params['v']
            return pos

    



