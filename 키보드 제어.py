# -*- coding: utf-8 -*- 
import pyautogui

import time


'''
press_S = pyautogui.moveTo(x = 90, y = 840)

press_D = pyautogui.moveTo(x = 120, y = 840)

press_F = pyautogui.moveTo(x = 150, y = 840)
'''

#https://blankspace-dev.tistory.com/417

def rightATK():
    attack = pyautogui.click(x = 60, y = 840,clicks=1,interval=1)
    move_right_1 = pyautogui.mouseDown(x = 375, y = 890)
    time.sleep(1)
    move_right_2 = pyautogui.mouseUp(x = 375, y = 890)
def leftATK():
    attack = pyautogui.click(x = 60, y = 840,clicks=1,interval=1)
    move_left_1 = pyautogui.mouseDown(x = 320, y = 890)
    time.sleep(1)
    move_left_2 = pyautogui.mouseUp(x = 320, y = 890)


while(1):
    leftATK()
    leftATK()
    leftATK()
    leftATK()
    leftATK()
    leftATK()
    rightATK()
    rightATK()
    rightATK()
    rightATK()
    rightATK()
    rightATK()
    
