# PiicoDev Capacitive Touch Sensor CAP1203 demo code
# Read the touch sensor buttons and print the result

from PiicoDev_CAP1203 import PiicoDev_CAP1203
from PiicoDev_Unified import sleep_ms # cross-platform-compatible sleep

touchSensor = PiicoDev_CAP1203()
# touchSensor = PiicoDev_CAP1203(touchmode='single')
# touchSensor = PiicoDev_CAP1203(sensitivity=6)
# touchSensor = PiicoDev_CAP1203(touchmode='single', sensitivity=6)

while True:
    # Example: Display touch-pad statuses
    status = touchSensor.read()
    print("Touch Pad Status: " + str(status[1]) + "  " + str(status[2]) + "  " + str(status[3]))

    sleep_ms(100)