from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms

rfid = PiicoDev_RFID()  # Initialise the RFID module

price = 3  # dollars (whole dollars only)

rfid = PiicoDev_RFID()

print('Place tag near the PiicoDev RFID Module to purchase for $', str(price))
print('')

if rfid.tagPresent():  # apply credit on powerup
    rfid.writeNumber(20)  # Give credit (whole dollars only)
    print('Credit applied! Remove tag...')
    while rfid.tagPresent(): sleep_ms(100)

while True:
    balance_dollars = rfid.readNumber()
    print('Previous Balance: $', str(balance_dollars))

    new_balance = balance_dollars - price