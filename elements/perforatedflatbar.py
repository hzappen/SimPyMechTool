import math
from solid import *
from solid.extensions.bosl2 import *


STD_WIDTH = 15
STD_HEIGHT = 2
STD_HOLE_DISTANCE = 10
STD_HOLE_DIAMETER = 5
STD_HOLE_HEIGHT = STD_HEIGHT + 1
STD_HOLE_MIN_DIST_EDGE = STD_HOLE_DISTANCE / 4

def calcNumberofHoles(length: float):
    return int(math.floor(length-2*STD_HOLE_MIN_DIST_EDGE)/(STD_HOLE_DISTANCE))


def getPerforatedStraightBar(length: float) -> OpenSCADObject:
    
    numberofHoles = calcNumberofHoles(length)
    holes = []
    bar = cuboid([length,STD_WIDTH,STD_HEIGHT])
    bar = bar.translate([length/2,0,0])
    for index,hole in enumerate(range(0,numberofHoles)):
        x_pos = ((index + 1)* STD_HOLE_DISTANCE)+STD_HOLE_MIN_DIST_EDGE
        myHole = cylinder(h=STD_HOLE_HEIGHT,d=STD_HOLE_DIAMETER,center=True)
        myHole = myHole.translate([x_pos,0,0])
        holes.append(myHole)
        bar = bar - myHole

    bar = bar.translate([-length/2,0,0])
    return bar



