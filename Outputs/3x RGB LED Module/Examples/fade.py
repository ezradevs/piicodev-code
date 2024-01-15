from PiicoDev_RGB import PiicoDev_RGB
from PiicoDev_Unified import sleep_ms  # Cross-platform compatible sleep function

leds = PiicoDev_RGB()  # initialise the LED module with conservative default brightness

while True:
    for x in range(255):  # glow on
        leds.fill([x, 0, 0])  # fill() will automatically show()
        sleep_ms(2)

    for x in range(255, 0, -1):  # glow off
        leds.fill([x, 0, 0])  # fill() will automatically show()
        sleep_ms(2)