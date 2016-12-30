import os, sys, time
from modules.camera import Camera
from modules.keys import Keys
from modules.body import Body

keys = Keys()
body = Body()
camera = Camera('')

Keys.monitor_inputs(keys, body, camera)
