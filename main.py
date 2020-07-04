import webbrowser
import pyautogui
import time
import win32clipboard

webbrowser.open('https://www.naver.com/', new=2)

time.sleep(3)

# target
# x=1250, y=174 ~ x=1363, y=173
pyautogui.click(x=500, y=806)

time.sleep(1)

# pyautogui.mouseDown(x=501, y=807)

# time.sleep(1)

# pyautogui.mouseUp(x=664, y=806)

pyautogui.dragTo(667, 807, 1, button='left')

pyautogui.hotkey('ctrl', 'c')

time.sleep(1)

win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

print(data)
