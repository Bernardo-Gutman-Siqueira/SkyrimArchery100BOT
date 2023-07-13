import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

START_STOP_KEY = KeyCode(char="o")
mouse = Controller()

def press_and_release():
    mouse.press(Button.left)
    time.sleep(2.2)
    mouse.release(Button.left)

def on_press(key):
    if key == START_STOP_KEY:
        toggle_clicking()

def toggle_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        threading.Thread(target=click_loop).start()

def click_loop():
    while clicking:
        press_and_release()
        time.sleep(0.1)

clicking = False

with Listener(on_press=on_press) as listener:
    listener.join()
