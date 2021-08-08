# SunFounder Laser

**Supply:** [Amazon](https://www.amazon.ca/gp/product/B013QSHMSU/ref=ppx_yo_dt_b_asin_title_o06_s01?ie=UTF8&psc=1)

**Tutorial:** [SunFounder](https://learn.sunfounder.com/lesson-5-laser-emitter-module)

**Setup:** Connect the laser **VCC pin to 3.3V power** and the **SIG pin to GPIO #17** on the PI.

**Usage:** Use the command `python3 laser.py` to start the script and `Ctrl + C` to stop. You can optionally pass in two arguments for on time and off time (in milliseconds). For example use the command `python3 laser.py 3000 500` to have the laser flash on for 3 seconds and off for half a second, the default is 1000 (one second).
