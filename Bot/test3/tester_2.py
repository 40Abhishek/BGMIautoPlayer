import pyautogui
from keyboard import press,is_pressed
from time import sleep
import win32api, win32con
'''
sleep(3)
pyautogui.moveTo(1250,500)
#pyautogui.drag(400,0,0.7,button='left')

while 1:
    if pyautogui.locateOnScreen('landed.png',region=(1016,65,70,70),confidence=0.3)!= None:
        print('landed')
        click(1257,602)
        print('now prone')
        #sleep(30)
        sleep(30)
        break
    sleep(1)

pyautogui.PAUSE=0.2
pyautogui.click(1320,0)
'''
def finder():
    for i in range(5):

        #X:  671 Y:  521
        sleep(2)
        #0= red,1=green,2=blue
        #rgb, RGB: (177, 132,   0)(Y)    RGB: (116, 144,  98)(G)
        pyautogui.moveTo(671,521)
        if pyautogui.pixel(671,521)[1]==132 or pyautogui.pixel(671,628)[2]==98:
            print('found slot')
            sleep(1)
            return
        elif pyautogui.pixel(671,628)[1]==132 or pyautogui.pixel(671,628)[2]==98:
            print('found slot')
            sleep(1)
            return
while 1:
    finder()
