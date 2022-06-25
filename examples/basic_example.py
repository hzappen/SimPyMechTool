from solid import *
import viewscad
from solid.extensions.bosl2 import *
from elements.perforatedflatbar import getPerforatedStraightBar,STD_HEIGHT,STD_HOLE_DISTANCE

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    metric_screws: OpenSCADObject = None

def two_crossed_bars(render: bool=True):
    myobj1 = getPerforatedStraightBar(length=200,forceCenterHole=True)
    myobj2 = getPerforatedStraightBar(length=250,zOffset=1,forceCenterHole=True) 

    #bolt = metric_screws.metric_bolt(size=5, headtype='hex', l=10).translate([0,0,2*STD_HEIGHT])
    #nut = metric_screws.metric_nut(size=5, hole=True, pitch=1.5, details=False, center=True).translate([0,0,-10+2*STD_HEIGHT])

#    assembly = myobj1 + myobj2 + bolt + nut
    assembly = myobj1 + myobj2

    if render == True:
        r=viewscad.Renderer()
        r.render(assembly)
    
    return assembly



