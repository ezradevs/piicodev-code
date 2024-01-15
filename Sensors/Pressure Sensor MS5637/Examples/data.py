# PiicoDev MS5637 minimal example code
# This program temperature and pressure data from the PiicoDev MS5637 pressure sensor
# and displays the result

from PiicoDev_MS5637 import PiicoDev_MS5637
from PiicoDev_Unified import sleep_ms

pressure = PiicoDev_MS5637()

while True:
    press_hPa = pressure.read_pressure()
    altitude_m = pressure.read_altitude()

    # Print Pressure
    print(str(press_hPa) + " hPa")
    
    # Print Altitude (metres)
#     print(str(altitude_m) + " m")
    sleep_ms(100)
    
