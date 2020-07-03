import pyautogui
import time

# target
# x=384, y=150 ~ x=431, y=153

# 마우스 좌표
x, y = pyautogui.position()
print('x={0}, y={1}' .format(x, y))


# 마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right')

# 드래그
pyautogui.mouseDown(x=384, y=150)
pyautogui.mouseUp(x=431, y=153)

# 복붙 

pyautogui.hotkey('ctrl', 'c')

time.sleep(1)
pyautogui.click(x=1266, y=248)
time.sleep(1)

pyautogui.hotkey('ctrl', 'v')

