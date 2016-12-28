import pygame, os, sys, time
from pygame.locals import *
from servosix import ServoSix

pygame.init()
screen = pygame.display.set_mode((1, 1)) #TODO Required?
pygame.key.set_repeat(50, 50)

ss = ServoSix()

steps = { 'size': 10, 'range_min': 20, 'range_max': 160 }
cam = {'x': 90, 'y': 90}

def reset_camera():
    ss.set_servo(1, 90)
    ss.set_servo(2, 90)

def cleanup():
    reset_camera()
    ss.cleanup()
    pygame.quit()
    quit()

def pan_tilt(type, direction):
    global cam, steps

    if (cam[type] <= steps['range_min'] and direction == 'negative') or (cam[type] >= steps['range_max'] and direction == 'positive'):
        print 'Limit reached'

    else:
        if direction == 'positive':
            cam[type] = cam[type] + steps['size']
        else:
            cam[type] = cam[type] - steps['size']

        servo = 1 if type == 'x' else 2
        ss.set_servo(servo, cam[type])
#        percent = (cam[type] / 180) * 100
#        os.system("echo {}={}% > /dev/servoblaster".format(servo, percent))
    return True

reset_camera()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "Exiting"
            cleanup()
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pan_tilt('x', 'positive')
            elif event.key == pygame.K_RIGHT:
                pan_tilt('x', 'negative')
            elif event.key == pygame.K_UP:
                pan_tilt('y', 'negative')
            elif event.key == pygame.K_DOWN:
                pan_tilt('y', 'positive')

cleanup()
