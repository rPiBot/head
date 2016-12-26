from servosix import ServoSix
import time

ss = ServoSix()

speed = 0.015

stop_moving = False

for x in range(0, 180):
    if stop_moving:
        stop_moving = False
        break
    ss.set_servo(1, x)
    time.sleep(speed)

ss.cleanup()
