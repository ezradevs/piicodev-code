from PiicoDev_Transceiver import PiicoDev_Transceiver
from PiicoDev_Unified import sleep_ms

radio = PiicoDev_Transceiver(group=2, radio_address=1) # Initialise this Transceiver in Group:2, as Radio Address 1

radio.send("This is a broadcast to everyone in group two")

sleep_ms(50)

radio.send("whisper to address three", address=3) # within my group!