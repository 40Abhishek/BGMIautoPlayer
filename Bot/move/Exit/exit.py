import time
import pyautogui
import time
from keyboard import press
'''
X:   10 Y:   37
X:   10 Y:  161
X: 1150 Y:    0

area:
h:84
w:978

X: 1365 Y:    0 
X: 1364 Y:  194

region=(0,0,1365,200),



1. exit(l bottom)
2. continue(right bottom)
3. continue(right bottom)(30 sec)
4. continue()(10)
5. lobby(r bottom)
6. start

'''

while 1:
    if pyautogui.locateOnScreen('dead1.png',region=(0,0,1365,250),confidence=0.4)!= None:
        press('e')
        time.sleep(5)
