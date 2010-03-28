import cocos

class Layer(cocos.layer.Layer):

    def __init__(self):
        cocos.layer.Layer.__init__(self)
        text = cocos.text.Label("This is a example text.", font_size=30)
        self.add(text)


cocos.director.director.init(resizable=True)

scene = cocos.scene.Scene(Layer())
cocos.director.director.run(scene)
