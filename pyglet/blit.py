# -*- encoding: utf-8 -*-
import pyglet

window = pyglet.window.Window()
img = pyglet.resource.image('undo.png')

@window.event
def on_draw():
    window.clear()
    img.blit(40, 40)

pyglet.app.run()
