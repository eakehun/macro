import pyautogui
import time
import win32clipboard

# target
# x=385, y=173 ~ x=431, y=169

# 마우스 좌표
x, y = pyautogui.position()
print('x={0}, y={1}' .format(x, y))


# 드래그
pyautogui.mouseDown(x=385, y=173)
pyautogui.mouseUp(x=431, y=169)


pyautogui.hotkey('ctrl', 'c')

time.sleep(1)

# 클립보드 객체 오픈 안하면 안된다
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

print(data)