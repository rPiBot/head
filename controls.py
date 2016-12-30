import pygame, os, sys, time
from pygame.locals import *
from modules.camera import Camera
#from modules.body import Body

pygame.init()
screen = pygame.display.set_mode((1, 1)) #TODO Required?
pygame.key.set_repeat(50, 50)

#b = Body()
c = Camera()

def cleanup():
    ss.cleanup()
    pygame.quit()
    quit()

def monitor_inputs():
    global state

    keys = {
        pygame.K_LEFT:  ['x', 'positive'],
        pygame.K_RIGHT: ['x', 'negative'],
        pygame.K_UP:    ['y', 'negative'],
        pygame.K_DOWN:  ['y', 'positive'],

        pygame.K_w:     ['forwards'],
        pygame.K_s:     ['backwards'],
        pygame.K_a:     ['left'],
        pygame.K_d:     ['right']
    }

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print "Exiting"
                cleanup()
                break

            if event.type == pygame.KEYDOWN:
                type = 'snap' if pygame.key.get_mods() & pygame.KMOD_SHIFT else 'step'
                if event.key in {pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN}:
                    variables = keys.get(event.key, 'NO KEY SET')
                    Camera.pan_tilt(c, variables[0], variables[1], type)
                elif event.key == pygame.K_r:
                    Camera.__init__(c)
                elif event.key in {pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d}:
                    variables = keys.get(event.key, 'NO KEY SET')
                    if variables[0] != state['body']:
                        move(variables[0])

            if event.type == pygame.KEYUP:
                if event.key in {pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d}:
                    move('stop')

monitor_inputs()
cleanup()
