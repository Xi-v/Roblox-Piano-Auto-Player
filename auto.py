# Code originally created by maksimKorzh on Github https://github.com/maksimKorzh
# Code adjusted by Xi-v on Github https://github.com/Xi-v
#
# Note from Xi-v:
# Thank you to the original owner for creating the process, I adjusted it so that it could handle
# special characters and uppercase, so it would work for all scripts.
# please enjoy, and don't forget to star and watch the repo!
#
# Tempo-adjustable version with user input for BPM.

# packages
import time
from pynput.keyboard import Controller, Key

# Initialize the keyboard controller
keyboard = Controller()

# Ask the user for the tempo in BPM
print("Enter the tempo in BPM (beats per minute):")
try:
    tempo = float(input())
    if tempo <= 0:
        raise ValueError("Tempo must be greater than 0.")
except ValueError as e:
    print(f"Invalid input: {e}. Setting default tempo to 120 BPM.")
    tempo = 120

# Calculate the delay in seconds for each beat
delay = 60 / tempo

print(f"Tempo set to {tempo} BPM. Delay between notes is {delay:.3f} seconds.")
print("Quickly head over to the window you want to play in.")
print('Auto will start playing in 3 seconds...')
time.sleep(3)

# Mapping for special characters that require Shift
special_characters = {
    '!': '1', '@': '2', '#': '3', '$': '4', '%': '5',
    '^': '6', '&': '7', '*': '8', '(': '9', ')': '0',
    '_': '-', '+': '=', '{': '[', '}': ']', ':': ';',
    '"': "'", '<': ',', '>': '.', '?': '/'
}

def press_key(note):
    if note in special_characters:  
        keyboard.press(Key.shift)
        keyboard.press(special_characters[note])
        keyboard.release(special_characters[note])
        keyboard.release(Key.shift)
    elif note.isupper():
        keyboard.press(Key.shift)
        keyboard.press(note.lower())
        keyboard.release(note.lower())
        keyboard.release(Key.shift)
    else: 
        keyboard.press(note)
        keyboard.release(note)

with open('sheet.txt') as f:
    notes = f.read()

    index = 0

    while index in range(len(notes)):
        if notes[index].isalnum() or notes[index] in special_characters:
            press_key(notes[index])
            print("pressed key:", notes[index])
        
        else:
            if notes[index] == '|': 
                time.sleep(delay * 8)

            if notes[index] == '[':
                chord = []

                while notes[index] != ']':
                    if notes[index].isalnum() or notes[index] in special_characters:
                        chord.append(notes[index])
                    
                    index += 1

                for note in chord:
                    press_key(note)

                print("pressed keys:", chord)

        time.sleep(delay)

        index += 1
