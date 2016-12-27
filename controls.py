import pygame, os, sys, threading, time
from pygame.locals import *
from servosix import ServoSix

pygame.init()
ss = ServoSix()

screen = pygame.display.set_mode((1, 1)) #TODO Required?

steps = { 'size': 10, 'delay': 0.05, 'range_min': 20, 'range_max': 160 }
cam = {'x': 90, 'y': 90}
allow = { 'x': True, 'y': True }

class start_pan_tilt(threading.Thread):
    def __init__(self, type, direction):
        threading.Thread.__init__(self)
        self.type = type
        self.direction = direction
    def run(self):
        pan_tilt(self.type, self.direction)


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

        print type, direction, cam[type]
        servo = 1 if type == 'x' else 2
        ss.set_servo(servo, cam[type])
#        percent = (cam[type] / 180) * 100
#        os.system("echo {}={}% > /dev/servoblaster".format(servo, percent))
        time.sleep(steps['delay'])
    print 'END'
    return True

def stop(type):
    global allow
    allow[type] = False
    print type, 'released'

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
                thread.start_new_thread(pan_tilt, ('x', 'positive',))
                s = start_pan_tilt('x', 'positive')
                #pan_tilt('x', 'positive')
            elif event.key == pygame.K_RIGHT:
                thread.start_new_thread(pan_tilt, ('x', 'negative',))
                s = start_pan_tilt('x', 'negative')
            elif event.key == pygame.K_UP:
                thread.start_new_thread(pan_tilt, ('y', 'negative',))
            elif event.key == pygame.K_DOWN:
                thread.start_new_thread(pan_tilt, ('y', 'positive',))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                stop('x')
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                stop('y')
        s.start

ss.cleanup()
pygame.quit()
quit()
