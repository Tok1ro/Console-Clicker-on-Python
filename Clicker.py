#defualt cps
import pyautogui as pg
from time import sleep
from win32con import *
from win32gui import *
import keyboard
import mouse

key1 = input('клавиша кликера лкм: ')
key2 = input('клавиша кликера пкм: ')

print('кликер активирован!')

while True:
    if keyboard.is_pressed(key1):
        sleep(0.001)
        pg.tripleClick()
    elif keyboard.is_pressed(key2):
        sleep(0.001)
        pg.tripleClick(button='right')
    