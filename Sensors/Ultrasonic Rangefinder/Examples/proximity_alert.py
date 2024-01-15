# Turn on the LED when range is less than 100mm

from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

ranger = PiicoDev_Ultrasonic()  # Initialise the rangefinder

while True:
    print(ranger.distance_mm)

    ranger.led = (ranger.distance_mm < 100)
    sleep_ms(100)