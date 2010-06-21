import os
import pyglet

window = pyglet.window.Window()

image_1 = pyglet.image.load('0.png')
image_2 = pyglet.resource.image('0.png')

@window.event
def on_draw():
    window.clear()

    for x in range(0, 400, image_1.width):
        image_1.blit(x, 200)

    for x in range(0, 400, image_2.width):
        image_2.blit(x, 0)


print image_1.width
print image_2.width
pyglet.app.run()
