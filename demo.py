from servosix import ServoSix
import time

ss = ServoSix()

period = 0.05

try:
    while (True):
        for x in range(0, 36):
          if x <= 18:
            ss.set_servo(1, (x*10))

            if x > 2 and x < 17:
              ss.set_servo(2, (x*10))

            time.sleep(period)

            if x == 12:

              time.sleep(period*10)
              ss.set_servo(2, 30)
              time.sleep(period*20)
              ss.set_servo(2, 60)
              time.sleep(period*30)
              ss.set_servo(1, 90)
              time.sleep(period*20)

              ss.set_servo(2, 30)
              ss.set_servo(1, 70)
              time.sleep(period*5)
              ss.set_servo(2, 160)
              time.sleep(period*5)
              ss.set_servo(2, 30)
              time.sleep(period*3)
              ss.set_servo(2, 160)
              ss.set_servo(1, 100)
              time.sleep(period*8)
              ss.set_servo(2, 30)
              time.sleep(period*10)
              time.sleep(period*10)




          else:

            y = 180-((x-18)*10)
            ss.set_servo(1, y)
            if y > 20 and y < 170:
              ss.set_servo(2, y)

            time.sleep(period)




finally:
    ss.cleanup()
