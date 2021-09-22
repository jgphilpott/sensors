import RPi.GPIO as GPIO
from datetime import datetime
import matplotlib.pyplot as pyplot

RECEIVE_PIN = 23
MAX_DURATION = 5
RECEIVED_SIGNAL = [[], []]

GPIO.setmode(GPIO.BCM)
GPIO.setup(RECEIVE_PIN, GPIO.IN)

cumulative_time = 0
beginning_time = datetime.now()
print('Started recording...')

while cumulative_time < MAX_DURATION:

    time_delta = datetime.now() - beginning_time

    RECEIVED_SIGNAL[0].append(time_delta)
    RECEIVED_SIGNAL[1].append(GPIO.input(RECEIVE_PIN))

    cumulative_time = time_delta.seconds

print('Ended recording,', len(RECEIVED_SIGNAL[0]), 'samples recorded.')

GPIO.cleanup()

print('Processing results...')

for i in range(len(RECEIVED_SIGNAL[0])):

    RECEIVED_SIGNAL[0][i] = RECEIVED_SIGNAL[0][i].seconds + RECEIVED_SIGNAL[0][i].microseconds/1000000.0

print('Plotting results...')

pyplot.plot(RECEIVED_SIGNAL[0], RECEIVED_SIGNAL[1])
pyplot.axis([0, MAX_DURATION, -1, 2])
pyplot.show()
