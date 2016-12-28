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
    global cam
    cam['x'] = 90
    cam['y'] = 90
    ss.set_servo(1, cam['x'])
    ss.set_servo(2, cam['y'])

def cleanup():
    reset_camera()
    ss.cleanup()
    pygame.quit()
    quit()

def pan_tilt(axis, direction, type):
    global cam, steps

    if (cam[axis] <= steps['range_min'] and direction == 'negative') or (cam[axis] >= steps['range_max'] and direction == 'positive'):
        return False

    else:
        if direction == 'positive':
            cam[axis] = (cam[axis] + steps['size']) if type == 'step' else steps['range_max']
        else:
            cam[axis] = cam[axis] - steps['size'] if type == 'step' else steps['range_min']

        servo = 1 if axis == 'x' else 2
        ss.set_servo(servo, cam[axis])
#        percent = (cam[axis] / 180) * 100
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
            type = 'snap' if pygame.key.get_mods() & pygame.KMOD_SHIFT else 'step'
            if event.key == pygame.K_LEFT:
                pan_tilt('x', 'positive', type)
            elif event.key == pygame.K_RIGHT:
                pan_tilt('x', 'negative', type)
            elif event.key == pygame.K_UP:
                pan_tilt('y', 'negative', type)
            elif event.key == pygame.K_DOWN:
                pan_tilt('y', 'positive', type)
            elif event.key == pygame.K_r:
                reset_camera()

cleanup()
