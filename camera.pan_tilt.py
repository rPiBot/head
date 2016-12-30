# Calls the Camera.pan_tilt method directly.  Requires three arguments:
# sys.argv[1]       x position      (0 [right] - 180 [left])
# sys.argv[2]       y position      (0 [top]   - 180 [bottom])

from modules.camera import Camera
import sys

camera = Camera('reset')
Camera.pan_tilt(camera, 'x', sys.argv[1], 0)
Camera.pan_tilt(camera, 'y', sys.argv[2], 0)
