# -*- encoding: utf-8 -*-
import os
import pyglet

window = pyglet.window.Window()

class PartialImage:

    def __init__(self, directory):
        names_list = [f for f in os.listdir(directory) if 'png' in f]
        names_list.sort()
        self.images = [pyglet.resource.image(name) for name in names_list]
        self.width = self.images[0].width
        self.height = self.images[0].height

    def blit(self, (x, y), (dst_x, dst_y), width):

        while width > 0:
            index = x / self.width
            index = int(index)
            delta_x = x % self.width

            try:
                self.images[index].blit(dst_x - delta_x, dst_y)
            except IndexError:
                print "Error de indice", index

            width -= self.width
            dst_x += self.width
            x += self.width


img = PartialImage("./")
x = 0

@window.event
def on_key_press(symbol, modifiers):
    global x

    if symbol == pyglet.window.key.RIGHT:
        x += 10.1
    elif symbol == pyglet.window.key.LEFT:
        x -= 10.1

@window.event
def on_draw():
    global x
    window.clear()
    img.blit((x, 0), (300, 10), 201)

pyglet.app.run()
