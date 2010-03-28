import pyglet
import cocos


import cocos.actions

class Sprite(cocos.sprite.Sprite):

    def __init__(self):
        image = pyglet.resource.image('player_2.png')
        cocos.sprite.Sprite.__init__(self, image)



class Layer(cocos.layer.Layer):

    def __init__(self):
        cocos.layer.Layer.__init__(self)

        girl = Sprite()
        girl.position = 200, 200


        #other = Sprite()
        #other.position = 300, 300
        #kkother.do( Repeat(RotateBy(45, 1)))

        self.add(girl)
        #self.add(other)



if __name__ == '__main__':
    cocos.director.director.init(resizable=True)

    scene = cocos.scene.Scene(Layer())
    image = pyglet.resource.image('player_2.png')
    cocos.sprite.Sprite(image)
    cocos.director.director.run(scene)
