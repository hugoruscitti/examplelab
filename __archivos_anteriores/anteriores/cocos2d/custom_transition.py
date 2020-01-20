import pyglet
import cocos
from cocos.scenes.transitions import *
from cocos.actions import *
from cocos.sprite import ActionSprite


class ZoomTransition(TransitionScene):
    """Zoom and FadeOut the outgoing scene."""

    def __init__(self, *args, **kwargs):
        super(ZoomTransition, self ).__init__( *args, **kwargs)

    def start(self):
        screensprite = self._create_out_screenshot()
        self.add(screensprite, z=1)
        self.add(self.in_scene, z=0)

    def _create_out_screenshot(self):
        # TODO: try to use `pyglet.image.get_buffer_manager().get_color_buffer()`
        #       instead of create a new BufferManager... note that pyglet uses
        #       a BufferManager singleton that fail when you change the window
        #       size.
        buffer = pyglet.image.BufferManager()
        image = buffer.get_color_buffer()

        director = cocos.director.director

        width, height = director.window.width, director.window.height 
        actual_width, actual_height = cocos.director.director.get_window_size()

        out = ActionSprite(image)
        out.position = actual_width / 2, actual_height / 2
        out.scale = max(actual_width / float(width), actual_height / float(height))

        zoom = ScaleBy(2, self.duration) | FadeOut(self.duration)
        restore = CallFunc(self.restore_out)

        out.do(zoom + restore)
        return out

    def finish(self):
        pass
