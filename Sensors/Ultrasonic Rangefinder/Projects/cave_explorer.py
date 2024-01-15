# Cave explorer game. Use the ultrasonic rangefinder to control the position of the player as you
# fly through a narrow, winding cave. Don't crash into the walls!

import math
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Buzzer import PiicoDev_Buzzer
from PiicoDev_Unified import sleep_ms

ranger = PiicoDev_Ultrasonic()  # Initialise the rangefinder
buzzer = PiicoDev_Buzzer()  # Initialise the buzzer


def generate_cave():
    """generate a new cave floor and ceiling based of the frame number. Changing these constants will affect game difficulty"""
    floor = range + \
            range / 2 * math.sin(2 * math.pi * frame / 200) + \
            range / 4 * math.cos(2 * math.pi * frame / 88) + \
            range / 4 * math.sin(2 * math.pi * frame / 33)

    ceiling = floor + cave_size
    return floor, ceiling


def player_in_bounds():
    return player > cave_floor and player < cave_ceiling


def play_start_sound():
    buzzer.tone(1200, 300)


def play_crash_sound():
    buzzer.tone(1200, 300)
    sleep_ms(300)
    buzzer.tone(600, 300)


#################
# Game Variables
#################

cave_size = 150  # height of the cave
cave_floor = 150  # starting floor height
range = 150  # how much room the player needs to move around
frame = 0  # frame counter is used to generate the cave, and keep score

bound_counter = 0  # how many frames the player was out of bounds. glitches happen, so we look for consecutive out-of-bounds to trigger a crash

state = 'prestart'
print("Game starts when player is in bounds")
sleep_ms(1000)

while True:

    # Update the game
    cave_floor, cave_ceiling = generate_cave()
    player = ranger.distance_mm

    # Check for out-of-bounds
    if player_in_bounds():
        bound_counter = 0
        if state == 'prestart':
            state = 'play'
            play_start_sound()
    else:
        bound_counter += 1

    # Plot the game state
    print(f"{player} {cave_ceiling} {cave_floor} 0 {2 * range + cave_size}")

    # Crash when out of bounds for consecutive frames
    if bound_counter > 2 and state == 'play':
        print(f"You crashed! Score: {frame}")
        play_crash_sound()
        break;

    frame += 1
    sleep_ms(100)