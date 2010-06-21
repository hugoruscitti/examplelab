import pyglet

window = pyglet.window.Window()
window.set_fullscreen(True)

fps_display = pyglet.clock.ClockDisplay()
batch = pyglet.graphics.Batch()
image_1 = pyglet.resource.image('fondo.png')
sprite = pyglet.sprite.Sprite(image_1, batch=batch)
x = 0.0


def update(dt):
    global sprite, x

    x += dt * 20
    sprite.x = int(x)



@window.event
def on_draw():
    window.clear()
    batch.draw()
    fps_display.draw()

pyglet.clock.schedule(update)
pyglet.app.run()
