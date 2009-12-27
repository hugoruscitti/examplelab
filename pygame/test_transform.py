# -*- encoding: utf-8 -*-
import pygame
from common import *

screen = pygame.display.set_mode((320, 200))
background = pygame.image.load('background.bmp')

restore(screen, background)
convert = pygame.transform.flip(image, True, True)
save_screenshot("flip", convert, "pygame.transform.flip(image, True, True)")


restore(screen,background)
convert = pygame.transform.scale(image, (121, 50))
save_screenshot("scale", convert, "pygame.transform.scale(image, (121, 50))")



restore(screen,background)
convert = pygame.transform.rotate(image, 190)
save_screenshot("rotate", convert, "pygame.transform.rotate(image, 190)")


restore(screen,background)
convert = pygame.transform.rotozoom(image, 45, 0.5)
save_screenshot("rotozoom", convert, "pygame.transform.rotozoom(image, 45, 0.5)")


restore(screen,background)
convert = pygame.transform.scale2x(image)
save_screenshot("scale2x", convert, "pygame.transform.scale2x(image)")


restore(screen,background)
convert = pygame.transform.smoothscale(image, (121, 50))
save_screenshot("smoothscale", convert, "pygame.transform.smoothscale(image, (121, 50))")


restore(screen,background)
convert = pygame.transform.chop(image, (20, 20, 30, 30))
save_screenshot("chop", convert, "pygame.transform.chop(image, (20, 20, 30, 30))")


restore(screen,background)
convert = pygame.transform.laplacian(image)
save_screenshot("laplacian", convert, "pygame.transform.laplacian(image)")
