from typing import final

import pyautogui 
import time
import pyscreeze
time.sleep(5)  # switch to Notepad (or your target window) during this delay
pyautogui.typewrite("Udhaya Sankar", interval=0.1)  # Type "Hello, world!" with a 0.1 second delay between each characterHello, world!Hello, world!Hello, world!Hello, world!

#hot Keys
pyautogui.press('enter')
pyautogui.keyDown('shift')
pyautogui.typewrite("Devipriya", interval=0.1)
pyautogui.keyUp('shift')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'i')          # turn Italic on
pyautogui.typewrite('Prithoon', interval=0.1)
pyautogui.hotkey('ctrl', 'i')          # turn Italic off
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'b')
pyautogui.typewrite("Prithvik", interval=0.1)
pyautogui.hotkey('ctrl', 'b')
pyautogui.press('enter')
#pyautogui.hotkey('cmd','c' )
#pyautogui.press('enter')
#pyautogui.hotkey('cmd','V' )

screenshot = pyautogui.screenshot()
screenshot.save(r"C:\Users\udhayasankar.n\Documents\GitHub\new_assignment\final.jpeg")
