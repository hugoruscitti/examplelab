import sys
import pygame
from vector2 import Vector2 as Vector


class Sprite:

    def __init__(self):
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(30, 100, 30, 30)
        self.x = 0.0
        self.y = 0.0
        self.go_to(320, 240)

    def render(self):
        global screen
        screen.fill(self.color, self.rect)

    def update(self, dt):
        speed = 10
        self.x += speed * dt * self.direction.x
        self.y += speed * dt * self.direction.y

        self.rect.center = (self.x, self.y)


    def go_to(self, x, y):
        actual = (self.x, self.y)
        to = (x, y)
        self.direction = Vector.from_points(actual, to)
        self.direction.normalise()
        print self.direction.x

screen = pygame.display.set_mode((320, 240))
time_counter = 0
rectangle = Sprite()

clock = pygame.time.Clock()
fps = 0
rectangle.rect.right=0

while True:

    dt = clock.tick(100) / 1000.0
    pygame.display.set_caption(str(int(clock.get_fps())))
    #rectangle.update(dt)
    rectangle.rect.x += 320 * dt

    for event in pygame.event.get():
        if event.type in [pygame.QUIT, pygame.KEYDOWN]:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rectangle.go_to(*event.pos)

    screen.fill((100, 100, 100))
    rectangle.render()
    pygame.display.flip()
