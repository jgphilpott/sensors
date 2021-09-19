import time
from pulsesensor import Pulsesensor

sensor = Pulsesensor()
sensor.startAsyncBPM()

try:

    while True:

        bpm = sensor.BPM

        if bpm > 0:

            print("BPM: %d" % bpm)

        else:

            print("No Heartbeat found.")

        time.sleep(1)

except:

    sensor.stopAsyncBPM()
