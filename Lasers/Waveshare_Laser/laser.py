import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# define data pins on breakout board of Raspberry Pi Model B
# ... corresponds to 'dout' pin on laser module
data_input_pin = 18

# define data_input_pin as input to Raspberry Pi
GPIO.setup(data_input_pin,GPIO.IN)

icount=0
icount_signal = 0

while icount_signal < 10:

    if GPIO.input(data_input_pin):
        icount += 1
        input_save=1
    else:
        if input_save==1:
            icount_signal += 1
            print("\n GPIO.input(data_input_pin) = 0!")
            print(' icount_signal = %s' % icount_signal)
            input_save=0
            print('\n -- end --\n')
