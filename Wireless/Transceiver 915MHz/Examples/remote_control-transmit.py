# Send LED control messages to a listening receiver

from PiicoDev_Transceiver import PiicoDev_Transceiver
from PiicoDev_Unified import sleep_ms

radio = PiicoDev_Transceiver()

state = True
while True:
    if state:
        radio.send('LED:ON')
    else:
        radio.send('LED:OFF')
    state = not state
    sleep_ms(1000)
