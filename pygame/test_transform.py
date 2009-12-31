# -*- encoding: utf-8 -*-
import pygame
from common import *

screen = pygame.display.set_mode((320, 200))
background = pygame.image.load('background.bmp')



test_codes = [
    ('flip',  "pygame.transform.flip(image, True, False)"),
    ('scale', "pygame.transform.scale(image, (121, 50))"),
    ('rotate', "pygame.transform.rotate(image, 190)"),
    ('rotozoom', "pygame.transform.rotozoom(image, 45, 0.5)"),
    ('scale2x', "pygame.transform.scale2x(image)"),
    ('smoothscale', "pygame.transform.smoothscale(image, (121, 50))"),
    ('chop', "pygame.transform.chop(image, (20, 20, 30, 30))"),
    ('laplacian', "pygame.transform.laplacian(image)"),
    ]


for (name, code) in test_codes:
    restore(screen, background)
    converted_image = eval(code)
    save_screenshot(screen, name, converted_image, code)

'''

restore(screen,background)
convert = 

restore(screen,background)
convert = 
save_screenshot(screen, "rotate", convert, "pygame.transform.rotate(image, 190)")


restore(screen,background)
convert = 
save_screenshot(screen, "rotozoom", convert, "pygame.transform.rotozoom(image, 45, 0.5)")


restore(screen,background)
convert = 
save_screenshot(screen, "scale2x", convert, "pygame.transform.scale2x(image)")


restore(screen,background)
convert = 
save_screenshot(screen, "smoothscale", convert, "pygame.transform.smoothscale(image, (121, 50))")


restore(screen,background)
convert = 
save_screenshot(screen, "chop", convert, "pygame.transform.chop(image, (20, 20, 30, 30))")


restore(screen,background)
convert = 
save_screenshot(screen, "laplacian", convert, "pygame.transform.laplacian(image)")
'''
