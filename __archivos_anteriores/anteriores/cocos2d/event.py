import cocos
from cocos.director import director

class Event(cocos.layer.Layer):

    def __init__(self):
        cocos.layer.Layer.__init__(self)
        text = cocos.text.Label("Text")
        self.add(text)

    def on_key_press(self, symbol, modifiers):
        print "key event:", symbol, modifiers

    def on_mouse_motion(self, x, y, dx, dy):
        print "mouse event, pos:", x, y
        print "mouse event, relative pos:", director.get_virtual_coordinates(x, y)

if __name__ == '__main__':
    director.init(resizable=True)

    event = Event()
    scene = cocos.scene.Scene(event)
    cocos.director.director.run(scene)

