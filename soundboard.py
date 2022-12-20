# import everything we need
import json, os
from pynput import keyboard
from playsound import playsound

# define basic variables
soundboardLocation = os.path.dirname(__file__)
jsonLocation = soundboardLocation + "/sounds.json"

# load sounds.json as a dictionary
with open(jsonLocation, 'r') as jsonFile:
    jsonDict = json.load(jsonFile)

def on_press(key):
    if key == keyboard.Key.esc:
        return False # stop listener
    try:
        k = key.char # single-char keys
    except:
        k = key.name # other keys
    if k in ['1', '2', '3', '4', '5', '6', '7', '8', '9']: # no 10th sound for you
        print('Key pressed: ' + k)
        global keyPressed
        keyPressed = k
        return False # refer to line 12 for this comment

# start listener
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

# find path of right sound
soundToPlay = "/sounds/" + jsonDict.get("sound" + keyPressed, None)

# if the sound exists, play it. otherwise, say that it doesn't exist.
if soundToPlay != None and os.path.exists(soundToPlay):
    playsound(soundToPlay)
else:
    print("sound" + keyPressed + " does not exist!")

# this is so janky, but it works so i don't care
