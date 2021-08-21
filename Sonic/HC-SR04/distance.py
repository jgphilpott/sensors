import time
import RPi.GPIO as GPIO

GPIO_ECHO = 24
GPIO_TRIGGER = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)

def measure_distance():

    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(GPIO_ECHO) == 0:

        start_time = time.time()

    while GPIO.input(GPIO_ECHO) == 1:

        stop_time = time.time()

    elapsed_time = stop_time - start_time

    distance = (elapsed_time * 34300) / 2

    return distance

try:

    while True:

        distance = measure_distance()
        print("Measured Distance = %.1f cm" % distance)
        time.sleep(1)

except KeyboardInterrupt:

    print("Keyboard Interrupt!")
    GPIO.cleanup()
