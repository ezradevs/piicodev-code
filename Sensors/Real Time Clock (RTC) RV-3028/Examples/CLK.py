# Set the CLK output pin frequency
#The PiicoDev RTC features a clock output pin (CLK) that generates a square wave - the frequency is user configurable. Valid frequencies are: 0Hz (off, Low), 1, 32, 64, 1024, 8192 and 32,768Hz

from PiicoDev_RV3028 import PiicoDev_RV3028

rtc = PiicoDev_RV3028()
rtc.configClockOutput(1) # The frequency, in Hz, of the square wave on the CLK output pin. Valid values are: 32768, 8192, 1024, 64, 32, 1, and 0 (always low).