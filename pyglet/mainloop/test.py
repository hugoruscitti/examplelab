import pyglet

class EventLoop(pyglet.app.EventLoop):

    def __init__(self):
        pyglet.app.EventLoop.__init__(self)


window = pyglet.window.Window()
sprite1 = pyglet.sprite.Sprite(pyglet.resource.image('bg.png'))
sprite2 = pyglet.sprite.Sprite(pyglet.resource.image('bg.png'))
sprite2.y = 300


@window.event
def on_draw():
    global sprite1
    global sprite2

    sprite1.draw()
    sprite2.draw()

def update(dt):
    sprite1.x -= dt * 100

pyglet.clock.schedule(update)
eventloop = EventLoop()
eventloop.run()
