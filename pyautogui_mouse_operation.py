import pyautogui  
import time
time.sleep(2)  # Wait for 5 seconds before starting the automation
#pyautogui.moveTo(100, 100, duration=1)  # Move the mouse to (100, 100) over 1 second
#pyautogui.click(100, 100)  # Click the mouse at the current position
#pyautogui.typewrite("Hello, world!", interval=0.1)  # Type "Hello, world!" with a 0.1 second delay between each character
#pyautogui.rightClick(100, 100)  # Right-click the mouse at the current position
#pyautogui.leftClick(100, 100)  # Left-click the mouse at the current position
#pyautogui.dragto(200, 200, duration=1)  # Drag the mouse to (200, 200) over 1 second
pyautogui.scroll(-500)
time.sleep(2)  # Wait for 2 seconds before ending the script
pyautogui.scroll(500)