from pyautogui import press
from keyboard import is_pressed
from time import sleep
def DCC(s, e):
    for i in range(s, e+1):
        for j in str(i):
            press(j)
            sleep(0.05)
        press('enter')

while not is_pressed('enter'):
    pass
DCC(2747, 2800)
