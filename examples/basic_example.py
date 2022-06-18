from solid import *
import viewscad
from elements.perforatedflatbar import PerforatedStraightBar,STD_HEIGHT

myobj1 = PerforatedStraightBar(67).get()
myobj2 = PerforatedStraightBar(73).get().rotate(0,0,90).up(STD_HEIGHT)

assembly = myobj1+myobj2
r=viewscad.Renderer()
r.render(assembly)

#assembly.save_as_scad()