import pyautogui
import time

class Sequence:
    def __init__(self, startXy, eventType, endXy, text, command):        
        print(eventType)

        if eventType == 'click':
            self.mouseDown(startXy)
        elif eventType == 'drag':
            self.mouseDrag(startXy, endXy)
        elif eventType == 'text':
            self.textTypo(text)
        elif eventType == 'hotkey':
            if command == 'copy':
                self.commandCopy()
            elif command == 'paste':
                self.commandPaste()
            else:
                print('{} 는 단축 명령이 아님'.format(command))
        else:
            print('{} 는 이벤트 타입이 아님'.format(eventType))
        

    def mouseDown(self, startXy):
        print(startXy)
        pyautogui.click(startXy)



    def mouseDrag(self, startXy, endXy):
        print(startXy)
        print(endXy)

        pyautogui.click(startXy)
        pyautogui.dragTo(endXy, duration=1, button='left')


    
    def textTypo(self, text):
        print(text)

    def commandCopy(self):
        pyautogui.hotkey('ctrl', 'c')

    def commandPaste(self):
        pyautogui.hotkey('ctrl', 'v')