import pygame, os, sys, time
import RPi.GPIO as GPIO
from pygame.locals import *
from servosix import ServoSix

pygame.init()
screen = pygame.display.set_mode((1, 1)) #TODO Required?
pygame.key.set_repeat(50, 50)

ss = ServoSix()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

cam = {'x': 90, 'y': 90}
state = {'cam': 'reset', 'body': 'reset'}

def initialise():
    global state
    pan_tilt('x', 'reset', type)
    pan_tilt('y', 'reset', type)

def cleanup():
    ss.cleanup()
    pygame.quit()
    quit()

def pan_tilt(axis, direction, type):
    global cam, state

    defaults = { 'size': 10, 'range_min': 20, 'range_max': 160, 'x': 90, 'y': 90 }

    if (cam[axis] <= defaults['range_min'] and direction == 'negative') or (cam[axis] >= defaults['range_max'] and direction == 'positive'):
        return False

    else:
        if direction == 'positive':
            cam[axis] = cam[axis] + defaults['size'] if type == 'step' else defaults['range_max']
        elif direction == 'negative':
            cam[axis] = cam[axis] - defaults['size'] if type == 'step' else defaults['range_min']
        elif direction == 'reset':
            cam[axis] = defaults[axis]

        state['cam'] = direction

        print axis, direction, cam[axis]

        servo = 1 if axis == 'x' else 2
        ss.set_servo(servo, cam[axis])
#        percent = (cam[axis] / 180) * 100
#        os.system("echo {}={}% > /dev/servoblaster".format(servo, percent))
    return True

def move(direction):
    global state

    print direction

    GPIO.output(35, False)
    GPIO.output(36, False)
    GPIO.output(37, False)
    GPIO.output(38, False)

    state['body'] = direction
    if direction == 'forwards':
        GPIO.output(35, True)
        GPIO.output(37, True)
    elif direction == 'backwards':
        GPIO.output(36, True)
        GPIO.output(38, True)
    elif direction == 'left':
        GPIO.output(36, True)
    elif direction == 'right':
        GPIO.output(38, True)

    print direction

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
                    pan_tilt(variables[0], variables[1], type)
                elif event.key == pygame.K_r and state['cam'] != 'reset':
                    initialise()
                elif event.key in {pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d}:
                    variables = keys.get(event.key, 'NO KEY SET')
                    if variables[0] != state['body']:
                        move(variables[0])

            if event.type == pygame.KEYUP:
                if event.key in {pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d}:
                    move('stop')

initialise()
monitor_inputs()
cleanup()
