from PiicoDev_ENS160 import PiicoDev_ENS160
from PiicoDev_Unified import sleep_ms

sensor = PiicoDev_ENS160()  # Initialise the ENS160 module

while True:
    print('Operational Mode: ' + str(sensor.operation))
    sleep_ms(1000)