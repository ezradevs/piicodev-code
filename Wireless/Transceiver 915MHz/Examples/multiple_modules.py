# Demonstrate how to use multiple PiicoDev Transceivers on the same bus

from PiicoDev_Transceiver import PiicoDev_Transceiver
from PiicoDev_Unified import sleep_ms
from math import sin

# Initialise two separate radios
transmitter = PiicoDev_Transceiver(id=[0, 0, 0, 0])  # each radio needs a unique ID switch setting
receiver = PiicoDev_Transceiver(id=[1, 0, 0, 0])

x = 0  # generates a sine wave

while True:
    # TRANSMIT a new value from one Transceiver
    y = sin(x)  # generate a new number
    transmitter.send(('sine wave', y))  # send the number
    x += 0.2  # increment the control variable

    sleep_ms(50)

    # RECEIVE any incoming messages and print
    if receiver.receive():
        message = receiver.message
        print(message)