# PiicoDev Atmospheric Sensor BME280 - Using multiple sensors
# Connect two sensors, each with a different address. They can be initialised and read independently.

from PiicoDev_BME280 import PiicoDev_BME280
from PiicoDev_Unified import sleep_ms  # cross-platform compatible sleep function

sensorA = PiicoDev_BME280()  # initialise the first sensor (defaults to 0x77). This is identical to "PiicoDev_BME280(address=0x77)"
sensorB = PiicoDev_BME280(address=0x76)  # initialise the second sensor at address 0x76

while True:
    dataA = sensorA.values()  # read all data from the first sensor
    dataB = sensorB.values()  # read all data from the second sensor

    myString = "A: "
    str(dataA)
    "   B: "
    str(dataB)  # create output string with both data

    print(myString)

    sleep_ms(100)