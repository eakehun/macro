import webbrowser
import pyautogui
import time
import pygetwindow
import os

iexplore = os.path.join(os.environ.get("PROGRAMFILES", "C:/Program Files"),"Internet Explorer/IEXPLORE.EXE")
ie = webbrowser.BackgroundBrowser(iexplore)
ie.open('https://www.cultureland.co.kr/', new=2)

# webbrowser.get(webbrowser.iexplore).open('https://www.cultureland.co.kr/', new=2)

# webbrowser.open('https://www.cultureland.co.kr/', new=2)

# webbrowser.get('chrome %s').open_new_tab('http://www.google.com')

# time.sleep(3)

# winList = pygetwindow.getAllWindows()



# pyautogui.click(x=501, y=807)
# 컬쳐랜드 - Chrome

# win = pygetwindow.getWindowsWithTitle('컬쳐랜드 - Chrome')[0]
# win.activate()

# pyautogui.scroll(-20000)