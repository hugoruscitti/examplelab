# -*- encoding: utf-8 -*-
import pygame
from common import *


screen = pygame.display.set_mode((320, 150))


restore(screen)

color = (100, 255, 100)
points = [(20, 20), (250, 50), (10, 70)]
pygame.draw.polygon(screen, color, points)

draw_code(screen,
'''
color = (100, 255, 100)
points = [(20, 20), (250, 50), (10, 70)]
pygame.draw.polygon(screen, color, points)
''')

save_screen("polygon")




restore(screen)

color = (200, 200, 100)
pygame.draw.circle(screen, color, (160, 40), 30)

draw_code(screen,
'''
color = (200, 200, 100)
pygame.draw.circle(screen, color, (160, 40), 30)
''')

save_screen("circle")




'''
restore(screen)
color = (100, 100, 200)
rect = (20, 20, 50, 80)
pygame.draw.arc(screen, color, rect, 30, 10, 5)
save_screen("arc")
'''

#pygame.draw.lines(screen, color, closed, pointlist, width=1)

restore(screen)
color = (100, 100, 200)
p1 = (10, 10)
p2 = (310, 60)
pygame.draw.aaline(screen, color, p1, p2, 1)
draw_code(screen,
'''
color = (100, 100, 200)
p1 = (10, 10)
p2 = (310, 60)
pygame.draw.aaline(screen, color, p1, p2, 1)
''')
save_screen("aaline")


restore(screen)
color = (100, 200, 200)
points = [(160, 20), (300, 70), (20, 60)]
pygame.draw.aalines(screen, color, True, points, 1)

draw_code(screen,
'''
color = (100, 200, 200)
points = [(160, 20), (300, 70), (20, 60)]
pygame.draw.aalines(screen, color, True, points, 1)
''')
save_screen("aalines")
