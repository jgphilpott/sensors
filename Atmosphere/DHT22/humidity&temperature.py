import time
import Adafruit_DHT

DHT_PIN = 4
DHT_SENSOR = Adafruit_DHT.DHT22

try:

    while True:

        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:

            print("Temperature={0:0.1f}°C  Humidity={1:0.1f}%".format(temperature, humidity))

        else:

            print("Failed to retrieve data from humidity sensor!")

        time.sleep(0.5)

except KeyboardInterrupt:

    print("Keyboard Interrupt!")
