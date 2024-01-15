# Get an accurate press-count, even when the sample-rate is very slow (3 seconds)
# Try clicking the button multiple times between updates. You ought to see that
# every click is accounted for!

from PiicoDev_Switch import PiicoDev_Switch  # Switch may be used for other types of PiicoDev Switch devices
from PiicoDev_Unified import sleep_ms

button = PiicoDev_Switch()  # Initialise the module

total_presses = 0

while True:
    total_presses += button.press_count  # press_count resets to zero after being read
    print('Total Presses:', total_presses)
    sleep_ms(3000)