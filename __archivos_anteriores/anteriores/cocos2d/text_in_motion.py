import cocos
from cocos.actions import *


class Text(cocos.layer.Layer):

    def __init__(self):
        cocos.layer.Layer.__init__(self)

        text = cocos.text.Label("Hello world")
        text.position = 100, 100
        scale = RotateBy(360, duration=1)
        text.do(Repeat(scale))

        self.add(text)


if __name__ == '__main__':
    cocos.director.director.init(resizable=True)

    text = Text()
    scene = cocos.scene.Scene(text)
    cocos.director.director.run(scene)
