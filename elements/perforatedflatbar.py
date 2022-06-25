import math
from solid import *
from solid.extensions.bosl2 import *


STD_WIDTH = 28.5
STD_HEIGHT = 4.3
STD_HOLE_DISTANCE = 30
STD_HOLE_DIAMETER = 10
STD_HOLE_HEIGHT = STD_HEIGHT + 1
STD_HOLE_MIN_DIST_EDGE = STD_HOLE_DISTANCE / 3

def calcNumberofHoles(length: float):
    
    return int(math.floor(length-2*STD_HOLE_MIN_DIST_EDGE)/(STD_HOLE_DISTANCE))


def getPerforatedStraightBar(length: float,zOffset: int = 0, forceCenterHole = True) -> OpenSCADObject:
    
    numberofHoles = calcNumberofHoles(length)
    holes = []
    bar = cuboid([length,STD_WIDTH,STD_HEIGHT])
    
    bar = bar.translate([length/2,0,0])
    for index,hole in enumerate(range(0,numberofHoles)):
        if forceCenterHole == True:
            remainLength = (length/2-STD_HOLE_MIN_DIST_EDGE) % STD_HOLE_DISTANCE
            print(remainLength)
            x_pos = (index* STD_HOLE_DISTANCE)+STD_HOLE_MIN_DIST_EDGE+remainLength
        else:    
            remainLength = (length - STD_HOLE_MIN_DIST_EDGE) % STD_HOLE_DISTANCE       
            x_pos = (index* STD_HOLE_DISTANCE)+STD_HOLE_MIN_DIST_EDGE+remainLength
        
        myHole = cylinder(h=STD_HOLE_HEIGHT,d=STD_HOLE_DIAMETER,center=True)
        myHole = myHole.translate([x_pos,0,0])
        holes.append(myHole)
        bar = bar - myHole

    bar = bar.translate([(-length/2),0,zOffset]) # First hole at origin
    
    print(bar)
    return bar



