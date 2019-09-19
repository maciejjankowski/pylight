import time
import random
from DmxPy import DmxPy

dmx = DmxPy('/dev/ttyUSB0')

while True:
	for ch1 in range(216, 220):
		ch2 = random.randrange(50, 51)
		ch3 = random.randrange(50, 51)
		ch4 = random.randrange(50, 51)
		dmx.setChannel(0, ch1)
		dmx.setChannel(1, ch2)
		dmx.setChannel(2, ch3)
		print( ch1, ch2, ch3)
		#dmx.setChannel(6, 255)
		dmx.render()
		time.sleep(1.05)
