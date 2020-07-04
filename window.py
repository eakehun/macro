import webbrowser
import pyautogui
import time

webbrowser.open('https://www.cultureland.co.kr/', new=2)

time.sleep(3)

pyautogui.click(x=501, y=807)

pyautogui.scroll(-20000)