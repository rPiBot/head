import pygame, os, sys, thread, time
from pygame.locals import *
from servosix import ServoSix

pygame.init()
ss = ServoSix()

screen = pygame.display.set_mode((1, 1)) #TODO Required?

steps = { 'size': 10, 'delay': 0.05, 'range_min': 20, 'range_max': 160 }
cam = {'x': 90, 'y': 90}
allow = { 'x': True, 'y': True }

def pan_tilt(type, direction):
    global cam, steps, allow

    allow[type] = True

    while allow[type]:
        if (cam[type] <= steps['range_min'] and direction == 'negative') or (cam[type] >= steps['range_max'] and direction == 'positive'):
            print 'Limit reached'
            break;

        if direction == 'positive':
            cam[type] = cam[type] + steps['size']
        else:
            cam[type] = cam[type] - steps['size']

    #    print type, direction, cam[type]
        servo = 1 if type == 'x' else 2
        ss.set_servo(servo, cam[type])
        time.sleep(steps['delay'])

def stop(type):
    global allow
    allow[type] = False
#    print type, 'released'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "Exiting"
            ss.cleanup()
            pygame.quit()
            quit()
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print 'left'
                #thread.start_new_thread(pan_tilt, ('x', 'positive',))
            elif event.key == pygame.K_RIGHT:
                print 'right'
                #thread.start_new_thread(pan_tilt, ('x', 'negative',))
            elif event.key == pygame.K_UP:
                print 'up'
                #thread.start_new_thread(pan_tilt, ('y', 'negative',))
            elif event.key == pygame.K_DOWN:
                print 'down'
                #thread.start_new_thread(pan_tilt, ('y', 'positive',))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                stop('x')
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                stop('y')
ss.cleanup()
pygame.quit()
quit()
