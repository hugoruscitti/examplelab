# -*- encoding: utf-8 -*-
import pyglet
from pyglet.window import key
from pyglet.gl import *
from pyglet import clock


class Logo(pyglet.sprite.Sprite):
    """Representa una imagen que sigue la posición del mouse."""

    def __init__(self, x=20, y=20):
        image = pyglet.resource.image('sprite.png')
        super(Logo, self).__init__(image)
        self.x = x
        self.y = y

    def update(self, dt):
        pass

    def delta_move(self, dx, dy):
        self.x += dx
        self.y += dy

    def inside(self, x, y):
        "Evalua si un punto está dentro del area del sprite."
        if x > self.x and x < self.x + self.width:
            return y > self.y and y < self.y + self.height

class Window(pyglet.window.Window):
    """Ventana que representa al bucle principal del juego."""

    def __init__(self, *k, **d):
        super(Window, self).__init__(*k, **d)
        self.img = pyglet.resource.image('undo.png')
        self._enable_alpha()
        self._load_cursors()
        clock.schedule_interval(self.update, 1/60.0)
        self.logo = Logo()
        

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.close()

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.logo.inside(x, y):
            self.logo.delta_move(dx, dy)
            self.set_mouse_cursor(self.MOUSE_ON_DRAG)

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.on_mouse_drag(x, y, 0, 0, buttons, modifiers)

    def on_mouse_release(self, x, y, buttons, modifiers):
        if buttons == 1:
            self.on_mouse_motion(x, y, 0, 0)


    def on_mouse_motion(self, x, y, dx, dy):
        if not self.logo.inside(x, y):
            self.set_mouse_cursor(self.MOUSE_DEFAULT)
        else:
            self.set_mouse_cursor(self.MOUSE_DRAG)


    def update(self, dt):
        self.logo.update(dt)

    def on_draw(self):
        self.clear()
        self.logo.draw()

    def _enable_alpha(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def _load_cursors(self):
        img = pyglet.resource.image('drag.png')
        self.MOUSE_DRAG = pyglet.window.ImageMouseCursor(img, 10, 10)
        img = pyglet.resource.image('cursor.png')
        self.MOUSE_DEFAULT = pyglet.window.ImageMouseCursor(img, 0, 20)
        img = pyglet.resource.image('on_drag.png')
        self.MOUSE_ON_DRAG = pyglet.window.ImageMouseCursor(img, 10, 10)

if __name__ == "__main__":
    w = Window(width=320, height=240)
    pyglet.app.run()
