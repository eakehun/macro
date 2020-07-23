import pyautogui
import time
import win32clipboard

class sequence:
    def __init__(self, startXy, eventType, endXy, text, command, delayTime, actionType):
        # print(eventType)

        self.eventType = eventType
        self.startXy = startXy
        self.endXy = endXy
        self.text = text
        self.command = command
        self.delayTime = delayTime
        self.actionType = actionType

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
        win32clipboard.OpenClipboard()        
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text, win32clipboard.CF_TEXT)
        win32clipboard.CloseClipboard()

        pyautogui.hotkey('ctrl', 'v')

        # pyautogui.write(text, interval=0.1)

    def commandCopy(self):
        pyautogui.hotkey('ctrl', 'c')

    def commandPaste(self):
        pyautogui.hotkey('ctrl', 'v')

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

        time.sleep(int(self.delayTime))