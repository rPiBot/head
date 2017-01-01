import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

TRIG = 33
ECHO = 31
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

class Body:
    state = ''

    def check_distance(self):
        sleep(0.005) # Wait for sensor to be ready
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
          start = time.time()

        while GPIO.input(ECHO) == 1:
          end = time.time()

        duration = end - start
        distance = round((duration * 17150), 2)
        print "Distance:",distance,"cm"

    def move(self, direction):
        if direction != self.state:
            GPIO.output(35, False)
            GPIO.output(36, False)
            GPIO.output(37, False)
            GPIO.output(38, False)

            GPIO.output(TRIG, False)

            self.state = direction

            if direction == 'forwards':
                check_distance(self)
                GPIO.output(35, True)
                GPIO.output(36, True)
            elif direction == 'backwards':
                GPIO.output(37, True)
                GPIO.output(38, True)
            elif direction == 'left':
                GPIO.output(38, True)
                GPIO.output(35, True)
            elif direction == 'right':
                GPIO.output(36, True)
                GPIO.output(37, True)

            print direction
