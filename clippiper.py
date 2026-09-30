import pyperclip
import pyautogui
import time
# ... after your Ctrl+C line:
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
print("Clipboard content:", pyperclip.paste())