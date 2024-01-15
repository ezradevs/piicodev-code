# A non-contact musical instrument. Hold your hand near the rangefinder and move
# closer or farther to play different notes.

from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Buzzer import PiicoDev_Buzzer
from PiicoDev_Unified import sleep_ms

ranger = PiicoDev_Ultrasonic()  # Initialise the rangefinder
buzzer = PiicoDev_Buzzer()


def get_note_from_distance(distance):
    """Converts a distance [mm] to a note [Hz] from a supplied scale"""
    scale_Hz = [523, 587, 659, 698, 784, 880, 988, 1047]  # Cmajor scale
    note_number = round((distance - 100) / 50)  # spaces notes 50mm apart, starting 100mm away from the rangefinder

    # make sure the note stays within bounds
    if 0 <= note_number < len(scale_Hz):
        return scale_Hz[note_number]
    else:
        return 0  # silence if not being actively played


note_duration = 250  # [ms]
while True:
    distance = ranger.distance_mm
    note = get_note_from_distance(distance)
    buzzer.tone(note, note_duration)

    print(distance, note)

    sleep_ms(note_duration)