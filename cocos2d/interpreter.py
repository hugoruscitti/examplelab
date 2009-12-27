import pyglet
import cocos

from cocos.actions import *
from cocos.layer.python_interpreter import PythonInterpreterLayer 


class Layer(cocos.layer.Layer):

    def __init__(self):
        cocos.layer.Layer.__init__(self)
        image = pyglet.resource.image('player_2.png')
        sprite = cocos.sprite.ActionSprite(image)
        sprite.position = (320, 240)
        self.add(sprite)


if __name__ == '__main__':
    cocos.director.director.init(resizable=True)

    main_layer = Layer()
    interpreter = PythonInterpreterLayer()

    scene = cocos.scene.Scene(main_layer, interpreter)
    cocos.director.director.run(scene)
