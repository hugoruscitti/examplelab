import pygame
import rabbyt

size = 640, 480

pygame.init()
pygame.display.set_mode(size, pygame.OPENGL | pygame.DOUBLEBUF)
rabbyt.set_viewport(size)
rabbyt.set_default_attribs()

quit = False



class Sprite(rabbyt.Sprite):

    def __init__(self, texture, size=None):
        if size:
            rabbyt.Sprite.__init__(self, texture, size)
        else:
            rabbyt.Sprite.__init__(self, texture)

    def __cmp__(self, other):
        if other.y > self.y:
            return 1
        else:
            return -1



image, size = rabbyt.pygame_load_texture('shaolin.png')

sprite1 = Sprite(image, size)
sprite2 = Sprite('fat.png')

sprites = [sprite1, sprite2]

while not quit:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit = True


    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        sprite1.y += 2
    elif keys[pygame.K_DOWN]:
        sprite1.y -= 2

    if keys[pygame.K_LEFT]:
        sprite1.x -= 2
    elif keys[pygame.K_RIGHT]:
        sprite1.x += 2


    rabbyt.set_time(pygame.time.get_ticks())
    rabbyt.clear((12, 23, 23))
    rabbyt.render_sorted(sprites)
    pygame.display.flip()
    pygame.time.delay(1)
