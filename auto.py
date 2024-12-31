# Code originally created by maksimKorzh on Github https://github.com/maksimKorzh
# Code adjusted by BlazingGlitch007222 on Github https://github.com/Xi-v
#
# Note from BlazingGlitch007222:
# Thank you to the original owner for creating the process, I adjusted it so that it could handle
# special characters and uppercase, so it would work for all scripts.
# please enjoy, and don't forget to favourite and watch the repo!
#
# There is a way to change the tempo down below, in a variable called delay

# packages
import time
from pynput.keyboard import Controller, Key

# Initialize the keyboard controller
keyboard = Controller()


print("Quickly head over to your desired choice of playing")
print('Music will start playing in 5 seconds...')
time.sleep(2)

# Change the temp here (in seconds 1 = 1 second, 0.5 = Half a second)
delay = 0.13

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
