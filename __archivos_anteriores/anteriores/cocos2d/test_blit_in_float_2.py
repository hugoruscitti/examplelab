import cocos
from cocos.actions import *
from pyglet.graphics import Batch


class Test(cocos.scene.Scene):

    def __init__(self):
        super(Test, self).__init__()
        self.layer = cocos.layer.Layer()
        self.add(self.layer)
        self.batch = Batch()

        sprite = cocos.sprite.Sprite('fondo.png')
        sprite.position = -400, 480 - sprite.height / 2 - 50
        sprite.do(Repeat(MoveBy((20, 0), 1)))
        self.layer.add(sprite)

        sprite_2 = cocos.sprite.Sprite('fondo.png')
        sprite_2.position = 320, 100
        self.layer.add(sprite_2)
        self.sprite_2 = sprite_2
        self.x = -100.0
        self.schedule_interval(self.update, 1/20.0)

    def update(self, dt):
        self.x += dt * 20
        self.sprite_2.position = int(self.x), self.sprite_2.position[1]

    def draw(self):
        self.batch.draw()


if __name__ == '__main__':
    cocos.director.director.init(resizable=True)
    cocos.director.director.run(Test())
