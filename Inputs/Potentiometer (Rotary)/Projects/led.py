# Remix: Control the brightness of the Pico's LED with a PiicoDev Potentiometer
from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms
from machine import Pin, PWM

led = PWM(Pin(25))  # Initialise the pin connected to the onboard LED as a PWM channel

pot = PiicoDev_Potentiometer(minimum=0, maximum=65534)  # Scale the pot to the duty cycle range for a Raspberry Pi Pico

while True:
    duty = round(pot.value)
    led.duty_u16(duty)
    sleep_ms(20)
