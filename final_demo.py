import subprocess
import time
import pyautogui

subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"--profile-directory=Default"])
time.sleep(3)

pyautogui.hotkey('ctrl', 'l')
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
time.sleep(0.3)
pyautogui.write('https://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/204108?type=locality&city=bengaluru', interval=0.05)
pyautogui.press('enter')
time.sleep(6)

# Click somewhere on the page body first so Ctrl+A selects page content, not the address bar
pyautogui.click(600, 400)
time.sleep(1)

# Select the whole page and copy
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

# Open Notepad and paste
subprocess.Popen('notepad.exe')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')