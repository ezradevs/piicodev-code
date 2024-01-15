#Set the temperature and humidity properties for compensated data.
from PiicoDev_ENS160 import PiicoDev_ENS160
from PiicoDev_Unified import sleep_ms

sensor = PiicoDev_ENS160() # Initialise the ENS160 module
sensor.temperature = 25.0  # [degC]
sensor.humidity = 50.0     # [%RH]