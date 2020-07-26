import pyautogui
import time
import win32clipboard
import webbrowser
from collections import deque

class sequence:
    def __init__(self, startXy, eventType, endXy, text, _url, command, delayTime, actionType, pinList):
        # print(eventType)

        self.eventType = eventType
        self.startXy = startXy
        self.endXy = endXy
        self.text = text
        self._url = _url
        self.command = command
        self.delayTime = delayTime
        self.actionType = actionType
        self.pinList = pinList

        # if eventType == 'click':
        #     self.mouseDown(startXy)
        # elif eventType == 'drag':
        #     self.mouseDrag(startXy, endXy)
        # elif eventType == 'text':
        #     self.textTypo(text)
        # elif eventType == 'hotkey':
        #     if command == 'copy':
        #         self.commandCopy()
        #     elif command == 'paste':
        #         self.commandPaste()
        #     else:
        #         print('{} 는 단축 명령이 아님'.format(command))
        # else:
        #     print('{} 는 이벤트 타입이 아님'.format(eventType))

    def mouseDown(self, startXy):
        # print(startXy)

        data = startXy.split(',')

        pyautogui.click(x=int(data[0]), y=int(data[1]))
        

    def mouseDrag(self, startXy, endXy):
        # print(startXy)
        # print(endXy)

        data = startXy.split(',')
        data2 = endXy.split(',')

        pyautogui.click(x=int(data[0]), y=int(data[1]))
        pyautogui.dragTo(x=int(data2[0]), y=int(data2[1]), duration=1, button='left')
    
    def textTypo(self, text):
        # print(text)
        # win32clipboard.OpenClipboard()
        # win32clipboard.EmptyClipboard()
        # win32clipboard.SetClipboardText(text, win32clipboard.CF_TEXT)
        # win32clipboard.CloseClipboard()

        # pyautogui.hotkey('ctrl', 'v')

        pyautogui.write(text, interval=0.2)

    def commandCopy(self):
        pyautogui.hotkey('ctrl', 'c')

    def commandPaste(self):
        pyautogui.hotkey('ctrl', 'v')

    def mouseMove(self, startXy):
        data = startXy.split(',')
        pyautogui.moveTo(x=int(data[0]), y=int(data[1]))

    def loggingResult(self):
        win32clipboard.OpenClipboard()                
        resultString = win32clipboard.GetClipboardData()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()

        resultString = resultString.replace('null')
        resultString = resultString.replace('추가 충전하기다 쓴 문상이벤트 바로가기')

        # print(resultString)

        logFile = open('log.txt', 'a', encoding='utf-8')
        logFile.write(resultString)
        logFile.close

    def launch(self):

        if self.eventType == '클릭':
            self.mouseDown(self.startXy)
        elif self.eventType == '드래그':
            self.mouseDrag(self.startXy, self.endXy)
        elif self.eventType == '텍스트':
            self.textTypo(self.text)
        elif self.eventType == '핫키':
            if self.command == 'copy':
                self.commandCopy()
            elif self.command == 'paste':
                self.commandPaste()
        elif self.eventType == '브라우저':
            webbrowser.open(self._url, new=2)
        elif self.eventType == '이동' or self.eventType == '마우스이동':
            self.mouseMove(self.startXy)
        elif self.eventType == '핀입력':
            self.inputPinCount = 0
            while len(self.pinList):
                self.inputPinCount += 1

                self.textTypo(self.pinList.popleft())

                if self.inputPinCount == 5:
                    break
        elif self.eventType == '결과확인':
            self.commandCopy()
            self.loggingResult()
            

            # if len(self.pinList) == 0 and self.inputPinCount != 5:
            #     for i in range(5 - self.inputPinCount):
            #         self.textTypo('000000000000000000')
                

        time.sleep(int(self.delayTime))