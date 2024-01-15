# Drive a Continuous Rotation (a.k.a. 360 degree) servo.

from PiicoDev_Unified import sleep_ms
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

controller = PiicoDev_Servo_Driver()

continuous_servo = PiicoDev_Servo(controller, 1, midpoint_us=1500, range_us=1800) # Connect a 360° servo to channel 2

continuous_servo.speed = 1    # fast
sleep_ms(1000)
continuous_servo.speed = 0.2  # slow
sleep_ms(1000)

continuous_servo.speed = -0.2 # slow reverse
sleep_ms(1000)
continuous_servo.speed = -1   # fast reverse
sleep_ms(1000)

continuous_servo.speed = 0    # stop