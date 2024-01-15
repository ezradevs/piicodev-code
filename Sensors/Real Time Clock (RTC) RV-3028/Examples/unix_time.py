#The PiicoDev RTC features a UNIX time register that can be set independently of the date-time. UNIX time is represented as the number of seconds since the last epoch. When reset to zero, this timer can be useful for keeping uptime or a mission-timer for data logging

from PiicoDev_RV3028 import PiicoDev_RV3028
from PiicoDev_Unified import sleep_ms

rtc = PiicoDev_RV3028() # Initialise the RTC module
rtc.setUnixTime(0) # reset UNIX time

while True:
    print(rtc.getUnixTime()) # display UNIX time
    sleep_ms(1500)