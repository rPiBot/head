import pygame
from pygame.locals import *
import os, sys
from threading import Thread
import time

pygame.init()

screen = pygame.display.set_mode((1, 1)) #Required?

cam_x = 90
cam_y = 90
delay = 0.005

allow_pan_tilt = True

def pan(direction):
    global cam_x, delay, allow_pan_tilt

    print direction, cam_x, allow_pan_tilt

    allow_pan_tilt = True

    while allow_pan_tilt:
        try:
            if (cam_x <= 0 and direction == 'right') or (cam_x >= 180 and direction == 'left'): #Can't move any further
                break;

            if direction == 'left':
                cam_x = cam_x + 1
            else:
                cam_x = cam_x - 1

            print direction, cam_x, allow_pan_tilt
            time.sleep(delay)

        except KeyException:
            break

    print 'Finished moving'


def tilt(direction):
        print direction

def stop():
    global allow_pan_tilt
    allow_pan_tilt = False
    print 's'


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "Exiting"
            pygame.quit()
            quit()
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pan('left')
            elif event.key == pygame.K_RIGHT:
                pan('right')
            elif event.key == pygame.K_UP:
                tilt('up')
            elif event.key == pygame.K_DOWN:
                tilt('down')

        if event.type == pygame.KEYUP:
            stop()

pygame.quit()
quit()
