import time
#import pygame

#screen = pygame.display.set_mode((320, 240))

FPS = 2
TICK_STEP = 1000 / FPS

def get_tick():
    "Retorna el tiempo actual en milisegundos."
    return int(time.time() * 1000)

def update():
    print "update"


next_tick = get_tick()


while True:

    frame_skip = -1

    while get_tick() > next_tick:
        update()
        next_tick += TICK_STEP
        frame_skip += 1

    if frame_skip > 0:
        print "SALTO:", frame_skip

    #pygame.display.flip()
