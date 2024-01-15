# Use multiple PiicoDev Buttons to increment / decrement a counter

from PiicoDev_Switch import PiicoDev_Switch
from PiicoDev_Unified import sleep_ms

button_up = PiicoDev_Switch(id=[0, 0, 0, 0])  # Initialise the 1st module
button_down = PiicoDev_Switch(id=[1, 0, 0, 0])  # Initialise the 2nd module

count = 0

while True:
    count += button_up.press_count
    count -= button_down.press_count

    print("Count", count)

    sleep_ms(1000)