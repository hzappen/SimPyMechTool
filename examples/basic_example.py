from solid import *
import viewscad
from solid.extensions.bosl2 import *
from elements.perforatedflatbar import PerforatedStraightBar,STD_HEIGHT,STD_HOLE_DISTANCE

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    metric_screws: OpenSCADObject = None

def two_crossed_bars(render: bool=True):
    myobj1 = PerforatedStraightBar(60)
    myobj2 = PerforatedStraightBar(70)
    print(myobj1.getHolePositions(2))
    myobj1.getSCADobj().rotate(0,0,90).translate([0,-1*STD_HOLE_DISTANCE/2,STD_HEIGHT])
    print(myobj1.getHolePositions(2))
    bolt = metric_screws.metric_bolt(size=5, headtype='hex', l=10).translate([0,0,2*STD_HEIGHT])
    nut = metric_screws.metric_nut(size=5, hole=True, pitch=1.5, details=False, center=True).translate([0,0,-10+2*STD_HEIGHT])

    assembly = myobj1.getSCADobj()+myobj2.getSCADobj()+bolt+nut
    if render == True:
        r=viewscad.Renderer()
        r.render(assembly)
    
    return assembly

def test_scadchild():
    myobj1 = PerforatedStraightBar(60).translate([1,1,1])
    r=viewscad.Renderer()
    r.render(myobj1)
    return myobj1
    


