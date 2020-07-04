import webbrowser
import pyautogui
import time
import win32clipboard

webbrowser.open('https://www.naver.com/', new=2)

time.sleep(6)

# target
# x=1250, y=174 ~ x=1363, y=173


pyautogui.mouseDown(x=1200, y=174)
pyautogui.mouseUp(x=1413, y=173)

pyautogui.hotkey('ctrl', 'c')

time.sleep(3)

win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

print(data)