# -*- encoding: utf-8 -*-
import pygame

class Control:

    def __init__(self):
        pygame.joystick.init()
        self.key_map = {
            'left': [pygame.K_LEFT, pygame.K_h],
            }

    def update(self):
        pygame_map_key = pygame.key.get_pressed()

        for name in self.key_map:
            keys = self.key_map[key]

            for key in keys:
                if pygame_map_key[key]:
                    setattr(object, name, True)



if __name__ == '__main__':
    pygame.display.init()
    quit = False
    screen = pygame.display.set_mode((320, 240))

    control = Control()

    while not quit:
        control.update()

        for e in pygame.event.get():
            print e

            if e.type == pygame.QUIT:
                quit = True

            if e.type == pygame.KEYDOWN:
                if e.key in [pygame.K_q, pygame.K_ESCAPE]:
                    quit = True
        
        pygame.time.wait(10)
