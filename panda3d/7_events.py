import sys

import direct.directbase.DirectStart
from direct.showbase import DirectObject
from direct.actor import Actor


class World(DirectObject.DirectObject):

    def __init__(self):
        panda = Actor.Actor('models/panda-model')
        panda.setScale(0.005)
        panda.setPos(0, 30, -2)
        panda.reparentTo(render)
        self.panda = panda

        # Control's boolean state.
        self.do_right = False
        self.do_left = False

        # State
        self.last_time_value = 0

        # Event manager
        self.accept('escape', sys.exit)
        self.accept('arrow_left', self.on_left, [True])
        self.accept('arrow_right', self.on_right, [True])

        self.accept('arrow_left-up', self.on_left, [False])
        self.accept('arrow_right-up', self.on_right, [False])

        # Update handler
        taskMgr.add(self.update, "update")

    def on_left(self, state):
        self.do_left = state
        
    def on_right(self, state):
        self.do_right = state

    def update(self, task):
        dt = task.time - self.last_time_value

        speed = 300

        if self.do_left:
            self.panda.setH(self.panda, dt * speed)
        
        if self.do_right:
            self.panda.setH(self.panda, -dt * speed)

        self.last_time_value = task.time

        return task.cont



World()
run()
