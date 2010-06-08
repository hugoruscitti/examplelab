import pyglet

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

# Genera los Sprites asociados al grupo
image = pyglet.resource.image('sprite.png')
a = pyglet.sprite.Sprite(image, 20, 20, batch=batch)
b = pyglet.sprite.Sprite(image, 20, 300, batch=batch)

@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    a.x += 5

    if a.x > 640:
        a.x = -a.width

    b.x = a.x
    b.rotation += 5

pyglet.clock.schedule_interval(update, 1/100.0)
pyglet.app.run()
