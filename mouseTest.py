import mouse

from pynput.mouse import Button, Controller

import time

import pyautogui
# import time

# from pynput import mouse
# def on_click(x, y, button, pressed):
#     if pressed == True:
#         print(x,y)
# with mouse.Listener(on_click=on_click) as listener:
#      listener.join()

# target
# x=384, y=150 ~ x=431, y=153

# 마우스 좌표
# x, y = pyautogui.position()
# print('x={0}, y={1}' .format(x, y))


# 마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right')

# # 드래그
# pyautogui.mouseDown(x=384, y=150)
# pyautogui.mouseUp(x=431, y=153)

# # 복붙 

# pyautogui.hotkey('ctrl', 'c')

# time.sleep(1)
# pyautogui.click(x=1266, y=248)
# time.sleep(1)

# pyautogui.hotkey('ctrl', 'v')

# mouse.drag(26, 803, 480, 872, absolute=True, duration=1)


# pyautogui.moveTo(27, 629)
# pyautogui.mouseDown(button='left')
# pyautogui.moveTo(500, 629)


# mouse = Controller()
# mouse.position = (27, 629)
# time.sleep(1)
# mouse.click(Button.left)
# time.sleep(1)
# mouse.press(Button.left)
# time.sleep(1)
# mouse.move(500, 0)
# time.sleep(1)
# mouse.release(Button.left)

pyautogui.moveTo(x=27, y=629)
pyautogui.dragTo(x=527, y=629, duration=1, button='left')

# pyautogui.moveTo(27, 629)
# pyautogui.mouseDown(button='left')
# pyautogui.moveTo(500, 900)
# # pyautogui.mouseUp(button='left')
# time.sleep(1)
# pyautogui.moveTo(600, 990)
# pyautogui.mouseUp(button='left')
# time.sleep(10)