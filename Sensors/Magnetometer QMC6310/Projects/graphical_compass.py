# Similar to the compass example, this demo uses a PiicoDev OLED module to show a compass graphic

from PiicoDev_QMC6310 import PiicoDev_QMC6310
from PiicoDev_SSD1306 import create_PiicoDev_SSD1306, WIDTH, HEIGHT
from PiicoDev_Unified import sleep_ms
from math import sin, cos, radians # for calculating the compass-needle co-ordinates

compass = PiicoDev_QMC6310(range=1200) # Initialise the sensor with the most sensitive range. Valid ranges: 200, 800, 1200, 3000 uT
oled = create_PiicoDev_SSD1306()
# compass.calibrate() # only need to calibrate once

# Declination is the difference between magnetic-north and true-north ("heading") and depends on location
compass.setDeclination(12.5) # Found with: https://www.magnetic-declination.com/Australia/Newcastle/122944.html

centreX = int(WIDTH/2)
centreY = int(HEIGHT/2)

# This function draws the artwork onto the OLED display. It takes a heading and draws a line at that angle from the centre of the display - along with some other nice stuff.
def drawCompass(heading):
    rads = radians(heading + 180) # convert heading to radians and offset by 180 degrees (to account for y increasing down the display)
    length = 25 # compass needle length (in pixels) from centre

    # Convert polar coordinates (length, angle) to cartesian coordinates (x,y) for plotting on display. Offset the coordinates by half the screen width/height to draw from the centre - rather than the top-left of the display.
    x = int( length * sin(rads) + WIDTH/2 )
    y = int( length * cos(rads) + HEIGHT/2 )

    # Plot the compass on the display
    oled.fill(0)
    oled.line(centreX, centreY, x, y, 1) # draw the compass needle
    oled.circ(x,y,4)                     # put a north-indicator on the end
    oled.text(str(heading),100,57)       # show the heading in the bottom-right corner
    oled.show()

while True:
    heading = compass.readHeading()
    if compass.dataValid(): # only draw for valid data - prevents errors
        heading = round(heading)
        drawCompass(heading)
    print(heading)

    sleep_ms(100)