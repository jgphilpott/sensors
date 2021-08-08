import sys
import time
import RPi.GPIO as GPIO

LedPin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.output(LedPin, GPIO.HIGH)

on_time = int(sys.argv[1]) / 1000 if len(sys.argv) > 1 else 1
off_time = int(sys.argv[2]) / 1000 if len(sys.argv) > 2 else 1

def loop():

	while True:

		GPIO.output(LedPin, GPIO.LOW) # ON
		time.sleep(on_time)

		GPIO.output(LedPin, GPIO.HIGH) # OFF
		time.sleep(off_time)

def stop():

	GPIO.output(LedPin, GPIO.HIGH)
	GPIO.cleanup()

try:

	loop()

except KeyboardInterrupt:

	stop()
