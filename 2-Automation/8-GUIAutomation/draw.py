# Draws a nice pattern using pyautogui's mose controlling function

import pyautogui

pyautogui.click() # click to put program in focus
distance = 200
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=1) # move right
    distance -= 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=1) # move down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=1) # move left
    distance -= 25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=1) # move up
