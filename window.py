import webbrowser
import pyautogui
import time
import pygetwindow

webbrowser.open('https://www.cultureland.co.kr/', new=2)

time.sleep(3)

# winList = pygetwindow.getAllWindows()



# pyautogui.click(x=501, y=807)
# 컬쳐랜드 - Chrome

win = pygetwindow.getWindowsWithTitle('컬쳐랜드 - Chrome')[0]
win.activate()

pyautogui.scroll(-20000)