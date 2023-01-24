#speed cps
import pyautogui as pb
from time import sleep
import keyboard
import mouse

key1 = input('клавиша кликера лкм: ')
key2 = input('клавиша кликера пкм: ')

print('кликер активирован!')

while True:
    if keyboard.is_pressed(key1):
        sleep(0.001)
        mouse.double_click(button='left')
    elif keyboard.is_pressed(key2):
        sleep(0.001)
        mouse.double_click(button='right')