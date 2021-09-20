import RPi.GPIO as GPIO

count = 0
signal = 0

data_input_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(data_input_pin, GPIO.IN)

while count < 10:

    if GPIO.input(data_input_pin):

        signal = 0

    else:

        if signal == 0:

            count += 1
            signal = 1

            print("\nSignal detected!")
            print("Count = %s" % count)
