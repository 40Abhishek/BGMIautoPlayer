from pyautogui import *
import time
import keyboard
import win32api, win32con
import time

'''
keys: [

q-sprint
a-left
d-right

p-prone
c-crouch
j-jump

e-exit

timing of playzones:
landing and plane delay:2 min
on clock:
5 min(w)
12 min(blue)

3.20 min(w)
2.20 min(b)

2.20 min(w)
1.25 min(b)

2 min(w)
1 min(b)

2 min(w)
40 sec(b)

2 min

1st:12 min(4664 m)
2nd:5.4min(2967 m)
3rd:4 min()
4th:3 min
5th:2.4 min
6th:2 min
7th:2 min
8th:1.3 min

start_button: bottom left

settins:smooth,low

start_key-0

]

red under map
water image
low health and full health



'''
    
def sprint():
    keyboard.press('q')
    

def maps():
    keyboard.press('m')
    #recoganition

def crouch():
    keyboard.press('c')

def prone():
    keyboard.press('p')

def move():
    keyboard.press('a')#left
    keyboard.press('d')#right

def starter():
    pass

def jump():
    keyboard.press('j')

def main():
    while keyboard.is_pressed('0')== True:
'''#check where the playzone is located
            while True:
                mins, secs=divmod(t,60)
                time.sleep(1)
                t+=1
                now=mins,secs
                if now==(0,3):
                    maps()

    #move towards playzone
            if maps()==True:
                move()

    #sleep mode on

'''

def playzone():
    zone=1
    for i in range(0,7):
    if zone==1:
        #timmer:
            
    
    elif zone==2:
        #timmer:
        zone+=1
    
    elif zone==3:
        #timmer:
        zone+=1
        
    elif zone==4:
        #timmer:
        zone+=1
        
    elif zone==5:
        
        zone+=1
    
    elif zone==6:
        
        zone+=1
    
    elif zone==7:
        
        zone+=1







        
