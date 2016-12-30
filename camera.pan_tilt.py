# Calls the Camera.pan_tilt method directly.  Requires three arguments:
# sys.argv[1]       axis        (x or y)
# sys.argv[2]       direction   (positive or negative)
# sys.argv[3]       type        (step or snap)

from modules.camera import Camera
import sys

if sys.argv[2] == 'reset':
    camera = Camera('')
else:
    camera = Camera('reset')
    Camera.pan_tilt(camera, sys.argv[1], sys.argv[2], sys.argv[3])
