from servosix import ServoSix
import time

ss = ServoSix()

smoothness = 0.05

for x in range(0, 90):
  ss.set_servo(1, x)
  time.sleep(smoothness*10)

ss.cleanup()
