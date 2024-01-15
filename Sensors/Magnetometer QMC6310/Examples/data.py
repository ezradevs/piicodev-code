# Prints the raw axis readings in micro-Tesla

from PiicoDev_QMC6310 import PiicoDev_QMC6310
from PiicoDev_Unified import sleep_ms

magSensor = PiicoDev_QMC6310() # Initialise the sensor (defaults to range=3000uT)
magSensor.setRange(1200)

while True:
    raw_data = magSensor.read() # Read the field strength on each axis in uT
    # raw_data = magSensor.read(raw=True) # Read the raw, unscaled data on each axis
    print(raw_data)             # Print the data
    sleep_ms(200)