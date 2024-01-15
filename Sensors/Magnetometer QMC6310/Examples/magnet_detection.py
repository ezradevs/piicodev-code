# Read the magnetic field strength and determine if a magnet is nearby

from PiicoDev_QMC6310 import PiicoDev_QMC6310
from PiicoDev_Unified import sleep_ms

magSensor = PiicoDev_QMC6310(range=3000)  # initialise the magnetometer
# magSensor.calibrate()

threshold = 120  # microTesla or 'uT'.

while True:

    strength = magSensor.readMagnitude()  # Reads the magnetic-field strength in microTesla (uT)
    myString = str(strength) + ' uT'  # create a string with the field-strength and the unit
    print(myString)  # Print the field strength

    if strength > threshold:  # Check if the magnetic field is strong
        print('Strong Magnet!')

    sleep_ms(1000)