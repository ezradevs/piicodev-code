# PiicoDev Real Time Clock RV-3028
# An example of how to set and read the date, time, and weekday

from PiicoDev_RV3028 import PiicoDev_RV3028
from PiicoDev_Unified import sleep_ms

rtc = PiicoDev_RV3028() # Initialise the RTC module, enable charging

# Set the time by assigning values to rtc's attributes
# Replace the following values with the current date/time
rtc.day = 6
rtc.month = 5
rtc.year = 2022
rtc.hour = 11
rtc.minute = 57
rtc.second = 00
rtc.ampm = '24' # 'AM','PM' or '24'. Defaults to 24-hr time
rtc.weekday = 4 # Rolls over at midnight, works independently of the calendar date
rtc.setDateTime() # Sets the time with the above values

# Get the current time
rtc.getDateTime()

# Print the current time, and today's name
# You can read from individual time attributes eg hour, minute, weekday.
print("The time is " + str(rtc.hour) + ":" + str(rtc.minute))
print("Today is " + str(rtc.weekdayName) + "\n") # weekdayName assumes counting from 0=Monday.

while True:
    print(rtc.timestamp()) # timestamp() automatically updates time, and returns a pre-formatted string. Useful for printing and datalogging!
    sleep_ms(1000)