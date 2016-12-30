import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()  # Cleanup any existing use
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

class Body:
    state = ''


    def move(self, direction):
        if direction != self.state:
            GPIO.output(35, False)
            GPIO.output(36, False)
            GPIO.output(37, False)
            GPIO.output(38, False)

            self.state = direction

            if direction == 'forwards':
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
