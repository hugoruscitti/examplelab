import pygame
import rabbyt


size = 640, 480

pygame.init()
pygame.display.set_mode(size, pygame.OPENGL | pygame.DOUBLEBUF)
rabbyt.set_viewport(size)
rabbyt.set_default_attribs()

quit = False


image, size = rabbyt.pygame_load_texture('big.png')

sprite = rabbyt.Sprite(image, size)
#"../cocos2d/player.png")

sprites = [sprite]

#sprite.x = rabbyt.ease(0, 200, dt=4000, method='sine')

anim = rabbyt.chain(
        rabbyt.ease(0, 360, dt=1000, method='sine'),
        rabbyt.ease(360, 0, dt=1000, method='sine'),
        )
sprite.rot = anim 

scheduler = rabbyt.Scheduler()

def saludar():
    print "Hola mundo"
    return True


scheduler.add(2001, saludar)


while not quit:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            quit = True


    rabbyt.set_time(pygame.time.get_ticks())
    rabbyt.clear()
    rabbyt.render_sorted(sprites)
    scheduler.pump(pygame.time.get_ticks())
    pygame.display.flip()

print rabbyt.get_gl_vendor()
