import pyautogui
from keyboard import press,is_pressed
from time import sleep

'''
START:
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

'''
LOBBY:
region=(36,616,200,85)
'''

'''
EXIT:
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
4. continue(r bottom)(10)
5. lobby(r bottom)
6. start

'''
def starter():
    while 1:
        sleep(5)
        if pyautogui.locateOnScreen('start_button.png',region=(0,600,350,100),confidence=0.4)!= None:
            #clicking
            click('s')
            print('found start')
            sleep(1)
            return

def lobby():
    print('entering lobby')
    sleep(20)
    while 1:
        if pyautogui.locateOnScreen('killed.png',region=(0,0,290,70),confidence=0.5)!= None:
            sleep(50)
            press('j')
            print('jumped')
            break
    while 1:
        #change for fast landing
        sleep(70)
        press('p')
        print('now prone')
        sleep(30)
        return


def death():
    #check if things on screen are not there
    valu=0
    while 1:
        if pyautogui.locateOnScreen('dead1.png',region=(0,0,1365,250),confidence=0.4)!= None:
            sleep(5)
            #clicking
            press('e')
            print('exit')
            for i in range(4):
                sleep(5)
                press('r')
                print('continue/lobby')
                return 1
    
def game():
    while 1:
        starter()
        lobby()
        death()
        sleep(3)


if __name__=='__main__':
    game()

'''
if maps()== True:
sleep(20)
elif maps()==False:
move()
'''

    
