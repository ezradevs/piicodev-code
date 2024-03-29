from PiicoDev_LIS3DH import PiicoDev_LIS3DH
from PiicoDev_Unified import sleep_ms

# Initialise two devices, A and B
accelerometer_A = PiicoDev_LIS3DH(asw=0) # initialise the first device with ASW: OFF
accelerometer_B = PiicoDev_LIS3DH(asw=1) # initialise the first device with ASW: ON

# Or be explicit about the I2C address, if you prefer
# accelerometer_A = PiicoDev_LIS3DH(address=0x19) # initialise the first device with ASW: OFF
# accelerometer_B = PiicoDev_LIS3DH(address=0x18) # initialise the first device with ASW: ON

# Now each device can be read independently
xA, yA, zA = accelerometer_A.acceleration
xB, yB, zB = accelerometer_B.acceleration