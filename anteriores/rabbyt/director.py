import pygame
import rabbyt

class Director:

    def __init__(self, width=640, height=480, title=""):
        pygame.init()
        self._create_display(width, height)
        pygame.display.set_caption(title)
        self._quit = False

    def _create_display(self, width, height):
        size = width, height
        flags = pygame.OPENGL | pygame.DOUBLEBUF

        self.screen = pygame.display.set_mode(size, flags)
        rabbyt.set_viewport(size)
        rabbyt.set_default_attribs()

    def run(self, scene):
        self.change_scene(scene)


