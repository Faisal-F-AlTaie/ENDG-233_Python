# ENDG 233 Fall 2025
# Programming with Data
# Hardware Project
# Faisal Al-Taie

import machine
import time

# CONSTANTS AND PIN DEFINITIONS

TIME_UNIT = 0.1
DOT = 1
DASH = 3
SPACE = 7


test_string = "SR255G0B0D3R0G255B0D3R0G0B255D3S"

led_pin = machine.Pin('LED', machine.Pin.OUT)
output_pin = machine.Pin(0, machine.Pin.OUT)

# HELPER FUNCTIONS

def char_to_morse(character):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }
    return morse_code.get(character, -1)

def dot():
    led_pin.on()
    output_pin.on()
    time.sleep(TIME_UNIT * DOT)
    led_pin.off()
    output_pin.off()
    time.sleep(TIME_UNIT)

def dash():
    led_pin.on()
    output_pin.on()
    time.sleep(TIME_UNIT * DASH)
    led_pin.off()
    output_pin.off()
    time.sleep(TIME_UNIT)

def space():
    led_pin.off()
    output_pin.off()
    time.sleep(TIME_UNIT * SPACE)

# DRIVER CODE

def main():
    time.sleep(3)  # leave this as is

    while True:
        for char in test_string:
            morse_code = char_to_morse(char.upper())

            if morse_code == -1:
                continue

            if morse_code == "/":
                space()
                continue

            for symbol in morse_code:
                if symbol == ".":
                    dot()
                elif symbol == "-":
                    dash()

            time.sleep(0.3)


if __name__ == "__main__":
    main()
