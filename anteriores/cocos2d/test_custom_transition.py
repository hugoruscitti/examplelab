import pyglet

import cocos
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.layer.util_layers import ColorLayer

import custom_transition


class Main(Layer):
    
    def __init__(self):
        super(Main, self).__init__()
        color = (56, 56, 128, 255)
        self.add(ColorLayer(*color))
        self.add(cocos.text.Label('Main Scene', font_size=60, y=200, x=100))
        self.add(cocos.text.Label('Press Enter to change scene', y=10))

    def on_key_press(self, symbol, modifiers):
        "Change scene when user hit RETURN key."

        if symbol == pyglet.window.key.RETURN:
            new_scene = Scene(Intro())
            transition = custom_transition.ZoomTransition(director.scene, new_scene)
            director.replace(transition)

class Intro(Layer):

    def __init__(self):
        super(Intro, self).__init__()
        color = (128, 128, 128, 255)
        self.add(ColorLayer(*color))
        self.add(cocos.text.Label('Intro Scene', font_size=40, y=200, x=150))
        self.add(cocos.text.Label('Press Enter to change scene', y=10))

    def on_key_press(self, symbol, modifiers):
        "Change scene when user hit ENTER key."

        if symbol == pyglet.window.key.RETURN:
            new_scene = Scene(Main())
            transition = custom_transition.ZoomTransition(director.scene, new_scene)
            director.replace(transition)

if __name__ == '__main__':
    director.init(resizable=True)
    intro = Intro()
    director.run(Scene(intro))
