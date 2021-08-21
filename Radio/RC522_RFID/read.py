import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

rfid = SimpleMFRC522()

try:

	id, text = rfid.read()

	print(id)
	print(text)

finally:

	GPIO.cleanup()
