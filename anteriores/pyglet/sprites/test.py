# -*- encoding: utf-8 -*-
import pyglet
import window


class Player(pyglet.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()



class Window(window.Window):
    """Representa la ventana principal el programa."""

    def __init__(self):
        super(Window, self).__init__()


if __name__ == '__main__':
    w = Window()
    pyglet.app.run()
