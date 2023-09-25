import pyautogui
from keyboard import press
from time import sleep
'''
region=(36,616,200,85)

text: players in cabin
high blue ocean
jump button(time to jump:30 sec)
killed 0(top left)
open map and find plane/orange
'''

def maps():
    return True

while 1:
    #time.sleep(5)
    if pyautogui.locateOnScreen('plane.png',confidence=0.5)!= None:
        #keyboard.press('s')
        t=0
        while True:
            mins, secs=divmod(t,60)
            sleep(1)
            t+=1
            now=mins,secs
            print(now)
            if now==(0,50):
               press('j')
            break
        
        t=0
        while True:
            mins, secs=divmod(t,60)
            sleep(1)
            t+=1
            now=mins,secs
            #1 min approx
            if now==(1,10):
                press('p')
                sleep(30)
                if maps()== True:
                    sleep(20)
                elif maps()==False:
                    move()
                    
            break

        
