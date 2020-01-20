import pyglet
import cocos
from cocos.director import director
from cocos.layer import Layer

class Background(Layer):

    def __init__(self):
        Layer.__init__(self)
        self.image = pyglet.resource.image('background.png')

    def on_draw(self):
        self.image.blit(0, 0)

if __name__ == '__main__':
    director.init(resizable=True)
    layer = Background()
    scene = cocos.scene.Scene(layer)
    director.run(scene)
