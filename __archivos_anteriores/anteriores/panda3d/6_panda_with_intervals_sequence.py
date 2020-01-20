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

interval_1 = panda.posInterval(1, Point3(-5, 30, -2))
rotate_right = panda.hprInterval(1, Point3(90, 0, 0))
interval_2 = panda.posInterval(1, Point3(0, 30, -2))
rotate_left = panda.hprInterval(1, Point3(-90, 0, 0))

sequence = Sequence(interval_1, rotate_right, interval_2, rotate_left)
sequence.loop()

run()
