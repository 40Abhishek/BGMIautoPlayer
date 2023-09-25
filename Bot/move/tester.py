import pyautogui
from keyboard import press,is_pressed
from time import sleep


'''
q - sprint
m - maps
c - crouch
p - prone
a - move left
d - move right
s - start



mins, secs=divmod(t,60)
time.sleep(1)
t+=1
now=mins,secs

'''

def death():
    #check if things on screen are not there
    valu=0
    while 1:
        if pyautogui.locateOnScreen('dead1.png',region=(0,0,1365,250),confidence=0.4)!= None:
            sleep(5)
            press('e')
            print('exit')
            for i in range(4):
                sleep(5)
                press('r')
                print('continue/lobby')
        elif valu==3:
            break
                
        else:
            valu+=1

def find():
    #playzone image checker
    #move 360 to find playzone icon
    press('a')#left
    press('d')#right
    
    if pyautogui.locateOnScreen('start_button.png',region=(0,600,350,100),confidence=0.5)!= None:
            return True




def check():
    pass

def move():
    #move towards playzone
    press('c')
    press('q')
    #move until playzone disapear
    while True:
        sleep(5)
        if check()==False:
            press('q')
            press('p')
            break

def momentum():
    count=1
    while True:
        if count==1:
            #not set
            sleep('time')
            press('c')
            if find(count)==True:
                move()
                count+=1
            death()
            
        elif count==2:
            #not set
            sleep('time')
            press('c')
            if find()==True:
                move()
                count+=1
            death()
            
            
        elif count==3:
            #not set
            sleep('time')
            press('c')
            if find()==True:
                move()
                count+=1
            death()

        elif count==4:
            #not set
            sleep('time')
            press('c')
            if find()==True:
                move()
                count+=1
            death()

        elif count==5:
            #not set
            sleep('time')
            press('c')
            if find()==True:
                move()
                count+=1
            death()

        elif count==6:
            #not set
            sleep('time')
            press('c')
            if find()==True:
                move()
                count+=1
            death()
            
        elif count==7:
            #not set
            sleep('time')
            press('c')
            while True:
                death()

            

        
def playzone(zone):
    pass
    
def timmer(n):
    while True:
        mins, secs=divmod(t,60)
        time.sleep(1)
        t+=1
        now=mins,secs
        if now==(0,3):
            maps()

def sprint():
    keyboard.press('q')

def maps():
    keyboard.press('m')
    #recoganition

def crouch():
    keyboard.press('c')

def prone():
    keyboard.press('p')


    
'''

def main():
    while keyboard.is_pressed('0')== True:
#check where the playzone is located
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

