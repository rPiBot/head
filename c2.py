import pygame, os, sys, threading, time
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1, 1)) #TODO Required?


# to spam the pygame.KEYDOWN event every 100ms while key being pressed
pygame.key.set_repeat(200, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print 'go forward'
            if event.key == pygame.K_s:
                print 'go backward'
        if event.type == pygame.KEYUP:
            print 'stop'
