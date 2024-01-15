# Toggle the Button's "Power" LED on every click
from PiicoDev_Switch import PiicoDev_Switch
from PiicoDev_Unified import sleep_ms

button = PiicoDev_Switch()

while True:
    if button.was_pressed:
        button.led = not button.led
    sleep_ms(100)