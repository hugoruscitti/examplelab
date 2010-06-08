# -*- encoding: utf-8 -*-
import pyglet
from pyglet.window.key import LEFT, RIGHT, UP, DOWN
from pyglet.gl import *

def enable_alpha():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

window = pyglet.window.Window()
enable_alpha()
img = pyglet.resource.image('undo.png')

@window.event
def on_draw():
    window.clear()
    img.blit(40, 40)
    img.blit(200, 200)

pyglet.app.run()
