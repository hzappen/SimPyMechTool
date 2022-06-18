import math
from solid import *
from solid.extensions.bosl2 import *

STD_WIDTH = 15
STD_HEIGHT = 2
STD_HOLE_DISTANCE = 10
STD_HOLE_DIAMETER = 5
STD_HOLE_HEIGHT = STD_HEIGHT + 1


class PerforatedStraightBar():
    def __init__(self,length):
        self.numberofHoles = int(math.floor(length)/STD_HOLE_DISTANCE)
        self.holes = []
        bar = cuboid([length,STD_WIDTH,STD_HEIGHT])
        bar = bar.translate([length/2,0,0])
        for index,hole in enumerate(range(0,self.numberofHoles)):
            x_pos = (index + 1)* STD_HOLE_DISTANCE
            myHole = cylinder(h=STD_HOLE_HEIGHT,d=STD_HOLE_DIAMETER,center=True)
            myHole = myHole.translate([x_pos,0,0])
            print(myHole.params)
            self.holes.append(myHole)
            bar = bar - myHole

        self.bar = bar.copy()

    def get(self):
        return self.bar
    


