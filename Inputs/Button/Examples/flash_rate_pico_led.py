# Use a PiicoDev Button to control the flash-rate of RPi Pico's onboard LED
from machine import Pin
from PiicoDev_Switch import PiicoDev_Switch  # Switch may be used for other types of PiicoDev Switch devices
from PiicoDev_Unified import sleep_ms

button = PiicoDev_Switch()  # Initialise the module
led = Pin('LED', Pin.OUT)  # Initialise the onboard LED

index = 0
delays = [100, 200, 500, 1000]  # a pool of delay values

while True:
    if button.was_pressed:  # change the flash rate by
        index += 1  # incrementing the index
        index = index % len(delays)  # wrap the index back to zero when it goes out of bounds
        print("index: ", index)

    led.toggle()
    delay = delays[index]  # select the current delay duration
    sleep_ms(delay)