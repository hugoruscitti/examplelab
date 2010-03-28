import pyglet
import cocos

from cocos.actions import *

class Layer(cocos.layer.Layer):

    def __init__(self):
        cocos.layer.Layer.__init__(self)
        image = pyglet.resource.image('player_2.png')
        sprite = cocos.sprite.ActionSprite(image)
        sprite.position = (320, 240)
        rotate = RotateBy(360, 1)
        sprite.do(Repeat(rotate))
        self.add(sprite)


if __name__ == '__main__':
    cocos.director.director.init(resizable=True)

    scene = cocos.scene.Scene(Layer())
    cocos.director.director.run(scene)
