import pyautogui
import time

for i in range(5, 0, -1):
    print(f"Move mouse to the Person 1 avatar... {i}")
    time.sleep(1)

print("Position:", pyautogui.position())