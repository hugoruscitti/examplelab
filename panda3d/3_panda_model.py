import direct.directbase.DirectStart
from direct.actor import Actor


panda = Actor.Actor('models/panda-model')
panda.setScale(0.005)
panda.setPos(0, 10, -2)
panda.reparentTo(render)
#panda.place()
#print panda.ls()

run()
