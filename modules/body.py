import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

TRIG_FRONT = 33
TRIG_REAR = 31
ECHO_FRONT = 40
ECHO_REAR = 32

GPIO.setup(TRIG_FRONT,GPIO.OUT)
GPIO.setup(TRIG_REAR,GPIO.OUT)
GPIO.setup(ECHO_FRONT,GPIO.IN)
GPIO.setup(ECHO_REAR,GPIO.IN)

class Body:
    state = ''

    def check_distance(self, trigger, echo):
        time.sleep(0.005) # Wait for sensor to be ready
        GPIO.output(trigger, True)
        time.sleep(0.00001)
        GPIO.output(trigger, False)

        while GPIO.input(echo) == 0:
            start = time.time()

        while GPIO.input(echo) == 1:
            end = time.time()

        duration = end - start
        return round((duration * 17150), 2)

    def move(self, direction):
        if direction != self.state:
            GPIO.output(35, False)
            GPIO.output(36, False)
            GPIO.output(37, False)
            GPIO.output(38, False)

            GPIO.output(TRIG_FRONT, False)
            GPIO.output(TRIG_REAR, False)

            self.state = direction

            print 'checking distance'

            if direction == 'forwards':
                while self.check_distance(TRIG_FRONT, ECHO_FRONT) > 20: # AND state == forwards FROM CONFIG FILE
                  GPIO.output(35, True)
                  GPIO.output(36, True)
                else:
                  print 'Not safe to drive forwards'
                  GPIO.output(35, False)
                  GPIO.output(36, False)
            elif direction == 'backwards':
                while self.check_distance(TRIG_REAR, ECHO_REAR) > 20: # AND state == backwards FROM CONFIG FILE
                    GPIO.output(37, True)
                    GPIO.output(38, True)
                else:
                    print 'Not safe to drive backwards'
                    GPIO.output(37, False)
                    GPIO.output(38, False)
            elif direction == 'right':
                GPIO.output(38, True)
                GPIO.output(35, True)
            elif direction == 'left':
                GPIO.output(36, True)
                GPIO.output(37, True)

            print direction
