# Drive an angular servo with generally safe-to-use default properties

from PiicoDev_Unified import sleep_ms
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

# Initialise the Servo Driver Module
controller = PiicoDev_Servo_Driver()

# Simple setup: Attach a servo to channel 1 of the controller with default properties
servo = PiicoDev_Servo(controller, 1)

# Customised setup - Attach a servo to channel 1 of the controller with the following properties:
#    - min_us: the minimum expected pulse length (microsecconds)
#    - max_us: the maximum expected pulse length (microsecconds)
#    - degrees: the angular range of the servo in degrees
# Uncomment the line below to use customised properties
# servo = PiicoDev_Servo(controller, 1, min_us=600, max_us=2400, degrees=180)

# Step the servo
servo.angle = 0
sleep_ms(1000)
servo.angle = 90
sleep_ms(1000)
servo.angle = 180
sleep_ms(1000)
servo.angle = 0
sleep_ms(2000)

# Sweep the servo slowly 0->180°
for x in range(0,180,5):
    servo.angle = x
    sleep_ms(40)