'''
HIT:  X:682 Y:670

LEFT: X:  651 Y:  437
RIGHT: X:  758 Y:  437

if pyautogui.pixel('coordinates')[0]=='':


BALL: RGB: (146,  26,  25)

X:  694 Y:  470
'''


import pyautogui
#from keyboard import press,is_pressed
#from time import sleep

def click(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.PAUSE=0.2
    pyautogui.click(x,y)

def press():
    while 1:
        click(682,670)

'''
def starter():
    while 1:
        if pyautogui.pixel(694,470)[0]=='146':
            click(682,670)
            return
        else:
            press()
'''
press()
