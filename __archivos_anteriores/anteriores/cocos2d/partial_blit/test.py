# -*- encoding: utf-8 -*-
import os
import pyglet
import cocos

cocos.director.director.init(resizable=True)


#load = pyglet.resource.image
load = pyglet.image.load

class PartialImage:

    def __init__(self, directory):
        names_list = [f for f in os.listdir(directory) if 'png' in f]
        names_list.sort()
        self.images = [load(name) for name in names_list]
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


ima = PartialImage("./")
x = 0

class Layer(cocos.layer.Layer):

    def __init__(self, ima):
        cocos.layer.Layer.__init__(self)
        self.position = 0, 0
        self.image = ima
        
    def draw(self):
        #x, y = self.position
        self.image.blit((12, 0), (0, 0), 500)


scene = cocos.scene.Scene(Layer(ima))

cocos.director.director.run(scene)
