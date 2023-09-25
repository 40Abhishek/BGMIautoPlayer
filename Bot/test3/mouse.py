from pynput.mouse import Button,Controller
import time
mouse=Controller()
#moving left
#X: 1167 Y:  458
time.sleep(3)
mouse.position=(1167,458)
mouse.press(Button.left)
#X:  906 Y:  458
mouse.move(-300,0)
mouse.release(Button.left)
