import keyboard  # using module keyboard
r = open('my-doc.txt', "r")
data = r.read()
while True:
    # Wait for the next event.
    event = keyboard.read_event()
    print(event)
    if event.event_type == keyboard.KEY_DOWN:
        k = event.name
        if k == 'space':
            data += " "
        elif k == 'enter':
            data += "\n"
        elif k == 'backspace':
            data = data[:-1]
        elif k in 'abcdecghijklmnopqrstuvwxyz0123456789~`!@#$%^&*()_+?<>/|\\\'\";:][}{=-':
            data += k
        w = open('my-doc.txt', "w")
        w.write(data)



from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


import keyboard  # using module keyboard
while True:  # making a loop
    if keyboard.is_pressed('a'):  # if key 'q' is pressed
        print('You Pressed A Key!')
        break  # finishing the loop 


while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        print(event.name) # to check key name




import keyboard
import threading

is_programmatic = False

# Define a function to be called when a specific key is pressed
def on_key_press(keyEvent):
    global is_programmatic

    if keyEvent.name == 'a':
        if is_programmatic:
            print("Key press event triggered programmatically")
        else:
            print("Key press event triggered by user input")
    
        is_programmatic = False

# Register listener
keyboard.on_press(on_key_press)

# Start keyboard listener
keyboard.wait()

# or start a thread with the listener (you may want to sleep some seconds to wait the thread)
thread = threading.Thread(target=keyboard.wait)
thread.start()



    import keyboard

    sin = ""
    val = 0.0

    def key_pressed(e, *a, **kw):
            global sin, val
            
            # print(e, a, kw)
            k = e.name
            if k in "0123456789":
                    sin += k
            elif k == 'enter':
                    val += float(sin)/100.0
                    print("Entered: " + sin)
                    print('Value: ', val)
                    sin = ""
    keyboard.on_press(key_pressed)

import keyboard

key_pressed = []

keyboard.press("a")
key_pressed.append("a")

keyboard.press("b")
key_pressed.append("b")

keyboard.press("c")
key_pressed.append("c")

#check if a specific key is pressed
if "a" in key_pressed:
    print ("a pressed")

import keyboard
class CustomKeyboard():
    def __init__(self):
    self.pressed_keys = []

def press(self, key):
    keyboard.press(key)
    self.pressed_keys.append(key)

def is_pressed_programmatically(self, key):
    if key in self.pressed_keys:
        return True
    return False


    import keyboard

    sin = ""
    val = 0.0

    def key_pressed(e, *a, **kw):
            global sin, val
            
            # print(e, a, kw)
            k = e.name
            if k in "0123456789":
                    sin += k
            elif k == 'enter':
                    val += float(sin)/100.0
                    print("Entered: " + sin)
                    print('Value: ', val)
                    sin = ""
    keyboard.on_press(key_pressed)



import keyboard
from functools import partial 

num = ""

def add(i):
    global num
    num += str(i)
    print(num, end='\r')

for i in range(10): # numbers 0...9
    keyboard.add_hotkey(str(i), partial(add, i)) # add hotkeys

keyboard.wait('enter') # block process until "ENTER" is pressed

print("\nNum:{}".format(num))




import keyboard

# Don't do this! This will call `print('space')` immediately then fail when the key is actually pressed.
#keyboard.add_hotkey('space', print('space was pressed'))

# Do this instead
keyboard.add_hotkey('space', lambda: print('space was pressed'))

# or this
def on_space():
    print('space was pressed')
keyboard.add_hotkey('space', on_space)

# or this
while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
        print('space was pressed')
        
import keyboard
while True:
    if keyboard.read_key() == 'enter':
        print('Enter is pressed)
    if keyboard.read_key() == 'q':
        print('Quitting the program)
        break
    if keyboard.read_key() == 's':
        print('Skiping the things')


import keyboard

keyboard.wait('enter')
print('Enter is pressed')

keyboard.wait('q')
print('Quitting the program')

keyboard.wait('s')
print('Skiping the things')




from pynput.keyboard import Key , Listener , Controller

keyboard = Controller()

DoubleShot=False
shot=False
def on_press(key):
    global  DoubleShot
    global  shot

    if Key.num_lock == key:
        print("activate")
        DoubleShot=True
    if DoubleShot:
        if Key.shift == key:
      
            shot = not shot
            if shot:
                keyboard.press(Key.shift)
                keyboard.release(Key.shift)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press , on_release=on_release) as listener:
    listener.join()









