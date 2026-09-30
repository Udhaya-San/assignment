import subprocess
import time
import re
import pyautogui
import pyperclip
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

today_date = datetime.now().strftime("%Y-%m-%d")
today_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ---------- Step 1: Open Chrome and fetch weather data ----------
subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"--profile-directory=Default"])
time.sleep(3)

pyautogui.hotkey('ctrl', 'l')
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
time.sleep(0.3)
pyautogui.write('https://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/204108?type=locality&city=bengaluru', interval=0.05)
pyautogui.press('enter')
time.sleep(8)  # was 6

pyautogui.click(600, 400)   # click page body so Ctrl+A selects content, not the address bar
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

page_text = pyperclip.paste()
print("First 300 chars of copied text:", page_text[:300])
match = re.search(r'\d{1,3}\s?°', page_text)   # find the first "NN°" pattern on the page
fetched_data = match.group() if match else "Data not found"
print("Fetched data:", fetched_data)

# ---------- Step 2: Open Excel and enter the row ----------
subprocess.Popen([r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"])
time.sleep(5)

pyautogui.typewrite(today_datetime, interval=0.03)
pyautogui.press('tab')
pyautogui.typewrite(fetched_data, interval=0.03)
pyautogui.press('tab')
pyautogui.typewrite("Good for outdoor activities", interval=0.03)
pyautogui.press('enter')
time.sleep(1)

# ---------- Save the Excel file with today's date in the filename ----------
pyautogui.hotkey('ctrl', 's')
time.sleep(2)
pyautogui.typewrite(f"daily_report_{today_date}", interval=0.05)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')  # confirms "Keep current format" dialog if it appears
time.sleep(2)

# ---------- Step 3: Screenshot of the final sheet ----------
screenshot = pyautogui.screenshot()
screenshot.save(f"daily_report_screenshot_{today_date}.png")
print("Done. Excel file and screenshot saved.")