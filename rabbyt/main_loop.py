import pygame
import rabbyt

size = (640, 480)

# Create Display
pygame.init()
pygame.display.set_mode(size, pygame.OPENGL | pygame.DOUBLEBUF)
rabbyt.set_viewport(size)
rabbyt.set_default_attribs()

# Main loop
quit = False
last_tick = pygame.time.get_ticks()
last_fps = last_tick
fps_dt = 0.0
frames = 0

while not quit:
    actual = pygame.time.get_ticks()
    dt = (actual - last_tick) / 1000.0
    last_tick = actual

    fps_dt += dt

    frames += 1

    if fps_dt > 1.0:
        fps_dt -= 1.0
        print frames, fps_dt
        frames = 0


    # Handle events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit = True

    # Logic update
    #self._scene.update(dt)

    # Graphic update
    #self.screen.fill((50, 50, 50))
    #self._scene.draw(self.screen)

    pygame.display.flip()
    pygame.time.delay(1)

