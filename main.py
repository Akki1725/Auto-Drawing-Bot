import pyautogui
import time

# Mouse Position: X:  228 Y:  265

def sl(s):
    time.sleep(s)

sl(3)

pyautogui.press('win')
sl(0.5)
pyautogui.typewrite('paint', 0.1)
sl(0.5)
pyautogui.keyDown('enter')
sl(0.5)
pyautogui.hotkey('win' + 'up')
sl(0.1)

pyautogui.moveTo(228, 265)

sl(1)

distance=300

while distance > 0:
    pyautogui.dragRel(distance,0,duration=0.1) #move right
    distance=distance-5 #decrement in distance
    pyautogui.dragRel(0, distance, duration=0.1) #move down
    pyautogui.dragRel(-distance, 0, duration=0.1) #move left
    distance = distance - 5 #again decrement
    pyautogui.dragRel(0, -distance, duration=0.1) #move up