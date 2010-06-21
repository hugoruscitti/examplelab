import pyglet
from pyglet.gl import *

import cocos
from cocos.actions import *

class Layer(cocos.layer.Layer):

    def __init__(self, path):
        cocos.layer.Layer.__init__(self)
        self.image = pyglet.resource.image(path)

    def on_draw(self):
        glColor4f(1, 1, 1, self.opacity / 255.0)
        self.image.blit(0, 0)
        glColor4f(1, 1, 1, 1)


        #sprite = cocos.sprite.ActionSprite(image)
        #sprite.position = (320, 240)
        #rotate = RotateBy(360, 1)
        #sprite.do(Repeat(rotate))
        #self.add(sprite)

class Scene(cocos.scene.Scene):

    def __init__(self):
        super(Scene, self).__init__()
        layer1 = Layer('background.png')
        layer2 = Layer('player_2.png')
        
        layer1.opacity = 255
        layer2.do(FadeOut(2))

        self.add(layer1, z=0)
        self.add(layer2, z=1)



if __name__ == '__main__':
    cocos.director.director.init(resizable=True)
    scene = Scene()
    cocos.director.director.run(scene)
