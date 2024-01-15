# Read distance from the PiicoDev Ultrasonic Rangefinder

from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

ranger = PiicoDev_Ultrasonic()  # Initialise the rangefinder

while True:
    print(ranger.distance_mm)

    ranger.led = not ranger.led  # blink the LED every loop
    sleep_ms(100)