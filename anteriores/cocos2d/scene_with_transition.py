# -*- encoding: utf-8 -*-
import pyglet

import cocos
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.actions import *
from cocos.scenes import *


# Layers y Scenes para el menu

class MenuBackground(Layer):

    def __init__(self):
        Layer.__init__(self)
        self.image = pyglet.resource.image('menu.jpg')

    def on_draw(self):
        self.image.blit(0, 0)

class Menu(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.add(MenuBackground())


# Layers y Scenes para la introducción

class Background(Layer):

    def __init__(self):
        Layer.__init__(self)
        self.image = pyglet.resource.image('background.png')

    def on_draw(self):
        self.image.blit(0, 0)


class FrontLayer(Layer):
    
    def __init__(self):
        Layer.__init__(self)
        self.image = pyglet.resource.image('player_2.png')
        self.image.scale = 2.0

    def on_draw(self):
        self.image.blit(0, 0)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ENTER:
            scene = Menu()
            #effect = SlideInBTransition(director.scene, scene, duration=1)
            #effect = ShrinkAndGrowTransition(director.scene, scene, duration=1)
            effect = FlipX3D(director.scene, scene, duration=1)
            director.replace(effect)

class Intro(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.add(Background(), z=0)  # 'z' es inversa de profundidad
        self.add(FrontLayer(), z=1)
        self.scale = 0.0001
        self.rotation = 180
        self.do(RotateBy(180, duration=1))
        self.do(ScaleTo(1, duration=1))

        
def Other(Scene):

    def __init__(self):
        Scene.__init__(self)


if __name__ == '__main__':
    window = director.init(resizable=True)

    scene = Intro()
    director.run(scene)
