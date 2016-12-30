# Calls the Body.move method directly.  Requires one argument:
# sys.argv[1]       direction        (forwards, backwards, left, right or stop)

from modules.body import Body
import sys

body = Body()
Body.move(body, sys.argv[1])
