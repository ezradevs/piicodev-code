from PiicoDev_Switch import PiicoDev_Switch
from PiicoDev_Unified import sleep_ms
button = PiicoDev_Switch(double_press_duration=400)
while True:
    print('Double Press:', button.was_double_pressed)
    sleep_ms(1000)