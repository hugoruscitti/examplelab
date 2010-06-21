import pyglet
from pyglet.gl import *

document = pyglet.text.decode_text("Hola mundo")
text = pyglet.text.layout.IncrementalTextLayout(document, 200, 200)
img = pyglet.resource.image('undo.png')

window = pyglet.window.Window()

@window.event
def on_draw():
    global text

    glClearColor(1, 1, 1, 1)
    window.clear()
    text.draw()
    img.blit(0, 0)

pyglet.app.run()
