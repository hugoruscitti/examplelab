# -*- encoding: utf-8 -*-
import pyglet

class BigImage:

    def __init__(self, filename):
        pass

window = pyglet.window.Window()
img = pyglet.image.load('sky.png')
x = 0

@window.event
def on_draw(dt=0):
    global img, x
    x += 10
    img.blit(x, 0)

# fail as well as:
#       img = pyglet.resource.image('sky.png')

pyglet.clock.schedule_interval(on_draw, 1 / 60.0)
pyglet.app.run()
