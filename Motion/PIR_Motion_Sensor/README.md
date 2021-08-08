# PIR Motion Sensor

**Supply:** [Amazon](https://www.amazon.ca/gp/product/B07GJDJV63/ref=ppx_yo_dt_b_asin_title_o06_s01?ie=UTF8&psc=1)

**Tutorial:** [Raspberry Pi Tutorials](https://tutorials-raspberrypi.com/connect-and-control-raspberry-pi-motion-detector-pir)

**Setup:** To orient the sensor see the image below, the **left pin is power**, the **center pin is control** and the **right pin is ground**.

<p align="center"><img width="300" height="400" src="https://github.com/jgphilpott/sensors/blob/main/Motion/PIR_Motion_Sensor/PIR_Motion_Sensor.jpg"></p>

**Usage:** Use the command `python3 move.py` to start the script and `Ctrl + C` to stop. Once the script is running try waving your hand in front of the sensor, you should see the message `There was a movement!` printed in the terminal, after a short delay you can repeat this process.
