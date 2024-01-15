#The PiicoDev RTC features an External Event Interrupt pin (EVI) and Time Stamp function that can capture the time of an external event. The example below configures the EVI pin to capture the timestamp of a falling edge. If multiple events occur before the event time is queried, only the most recent timestamp is returned.
# Read the EVI pin event time.
# The program will continue listening for an event until one is detected.
from PiicoDev_RV3028 import PiicoDev_RV3028
from PiicoDev_Unified import sleep_ms

rtc = PiicoDev_RV3028()

rtc.resetEventInterrupt(edge = 'falling')

rtc.getDateTime()
print('Monitoring started at: ' + rtc.timestamp())

while (rtc.getEventInterrupt() is False):
    print('Waiting for 10 seconds.  If there is a falling edge on EVI pin the time will be recorded.')
    sleep_ms(10000)
print('Event occurred at: ', end='')
rtc.getDateTime(eventTimestamp=True)
print(rtc.timestamp(eventTimestamp=True))