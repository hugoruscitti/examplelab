import pyglet
from pyglet.gl import *

class Window(pyglet.window.Window):

    def __init__(self, *args, **kargs):
        super(Window, self).__init__(resizable=True, *args, **kargs)

        self._window_original_width = self.width
        self._window_original_height = self.height
        self._window_aspect =  self.width / float(self.height)

        # Enable blend
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


    def on_resize(self, width, height):
        width, height = self.width, self.height
        ow, oh = self._window_original_width, self._window_original_height

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, 1.0*width/height, 0.1, 3000.0)
        glMatrixMode(GL_MODELVIEW)

        glLoadIdentity()
        gluLookAt(ow/2.0, oh/2.0, oh/1.1566, ow / 2.0, oh / 2.0, 0, 0.0, 1.0, 0.0)


if __name__ == '__main__':
    window = Window()
    img = pyglet.resource.image('undo.png')

    @window.event
    def on_draw():
        window.clear()
        img.blit(40, 40)
        img.blit(200, 200)

    pyglet.app.run()
