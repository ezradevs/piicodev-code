# Lighting controller example
# One Pot controls the Hue (0 -> 1), one pot controls Brightness (0 -> 255)

from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_RGB import PiicoDev_RGB, wheel
from PiicoDev_Unified import sleep_ms

colour = PiicoDev_Potentiometer(minimum=0, maximum=1, id=[0, 0, 0, 0])
brightness = PiicoDev_Potentiometer(minimum=0, maximum=255, id=[1, 0, 0, 0])
leds = PiicoDev_RGB(id=[0, 1, 0,
                        0])  # all devices with 'id' switches require a unique 'id' switch setting - even if they're a different type of module.

while True:
    # Sample the pots for colour and brightness
    c = colour.value
    b = int(brightness.value)

    print(c * 255, b)  # print a line for each pot (scale up the colour)

    # Set the LED colour and brightness
    leds.fill(wheel(c))
    leds.setBrightness(b)

    sleep_ms(50)