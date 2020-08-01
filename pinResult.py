import pyautogui
import time
import os.path


from bs4 import BeautifulSoup

# time.sleep(3)

# fileExist = os.path.isfile('C:/Users/gnogu/OneDrive/Documents/컬쳐랜드.htm')

# pyautogui.hotkey('ctrl', 's')

# time.sleep(1)

# pyautogui.press('enter')

# if fileExist:
#     time.sleep(1)

#     pyautogui.press('left')
#     time.sleep(1)
#     pyautogui.press('enter')

# time.sleep(5)

f = open("C:/Users/gnogu/OneDrive/Documents/해피머니상품권 충전실패-해피머니_hm.txt", 'r', encoding='UTF8')
data = f.read()

soup = BeautifulSoup(data, 'html.parser')

name = soup.select('#contents > div.contents > div.section.sec-form > div > div.article > table > tbody')

print(name[0].text)