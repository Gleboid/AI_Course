import pyautogui
import time

print("Быстро наведи мышку на точку ПЕРЕД динозавром!")
time.sleep(4)

pyautogui.press('space')

while True:
    if not pyautogui.pixelMatchesColor(100,-245,(0,0,0)):
        pyautogui.press('space')
        print("Вижу кактус!") 
print (pyautogui.position())