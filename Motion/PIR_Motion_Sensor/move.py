import time
import RPi.GPIO as GPIO

SENSOR_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def action(event):

    print("There was a movement!")

try:

    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=action)

    while True:

        time.sleep(100)

except KeyboardInterrupt:

    print("Keyboard Interrupt!")

GPIO.cleanup()
