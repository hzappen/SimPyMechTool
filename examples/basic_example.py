from solid import *
import viewscad
from elements.perforatedflatbar import PerforatedStraightBar,STD_HEIGHT,STD_HOLE_DISTANCE


def two_crossed_bars(render: bool=True):
    myobj1 = PerforatedStraightBar(60).get()
    myobj2 = PerforatedStraightBar(70).get().rotate(0,0,90).translate([0,-1*STD_HOLE_DISTANCE/2,STD_HEIGHT])

    assembly = myobj1+myobj2
    if render == True:
        r=viewscad.Renderer()
        r.render(assembly)
    
    return assembly

