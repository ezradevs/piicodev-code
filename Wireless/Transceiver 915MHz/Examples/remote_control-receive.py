# Listen for LED control messages
# Valid messages set the state of the on-board LED

from PiicoDev_Transceiver import PiicoDev_Transceiver
from PiicoDev_Unified import sleep_ms

radio = PiicoDev_Transceiver()

while True:
    if radio.receive():
        message = radio.message
        print(message)

        if message == 'LED:ON': radio.led = True
        if message == 'LED:OFF': radio.led = False
    sleep_ms(50)