import direct.directbase.DirectStart
from direct.actor import Actor
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import *


panda = Actor.Actor('models/panda-model', {'walk': 'models/panda-walk4'})
panda.setScale(0.005)
panda.setPos(0, 30, -2)
panda.reparentTo(render)
panda.setHpr(-90, 0, 0)
panda.loop('walk')

interval_1 = panda.posInterval(11, Point3(-10, 30, -2))
interval_1.loop()

run()
