import time
import random
import flask
from DmxPy import DmxPy

def show(msg, timeout=1):
  for t in range(timeout*60):
    j = 0
    for i in msg:
      dmx.setChannel(j, i)
      j = j+1
    dmx.render()
    time.sleep(0.1)


dmx = DmxPy('/dev/ttyUSB1')



