# A self-calibrating tripwire that looks for gross changes in distance
# Slowly calibrates for new distances - no manual tuning required.

from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

ranger = PiicoDev_Ultrasonic()  # Initialise the rangefinder

tuning = 0.1  # a tuning parameter that affects how quickly new distances are calibrated
sensitivity = 50  # [mm] any change greater than this amount will count as a trip
average = ranger.distance_mm  # Initialise the moving average with a range sample

sleep_ms(1000)

while True:

    distance = ranger.distance_mm
    print(distance, average)

    # check if the wire has been tripped
    if abs(average - distance) > sensitivity:
        print("Trip!")
        ranger.led = True  # Indicate a trip
    else:
        ranger.led = False

    # update the moving average https://en.wikipedia.org/wiki/Exponential_smoothing
    average = tuning * distance + (1 - tuning) * average

    sleep_ms(100)