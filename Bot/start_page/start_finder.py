import pyautogui
from keyboard import press
from time import sleep

'''
X:   39 Y:  616 RGB:

X:   36 Y:  617 RGB:

X:   47 Y:  623 RGB: ( up left)
X:  227 Y:  623 RGB: (up right)
X:  227 Y:  697 RGB: (d right)
X:   47 Y:  697 RGB: (d left)

import time
import pyautogui
time.sleep(20)
pyautogui.displayMousePosition()


time.sleep(20)
img=pyautogui.screenshot(region=(47,623,180,74))

h=79
w=192
'''

while 1:
    sleep(5)
    if pyautogui.locateOnScreen('start_button.png',region=(36,616,200,85),confidence=0.5)!= None:
        press('s')
        sleep(1)
