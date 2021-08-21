import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

rfid = SimpleMFRC522()

try:

	data = input("Enter new data:")
	print("Now place your tag to write.")
	rfid.write(data)
	print("Written!")

finally:

	GPIO.cleanup()
