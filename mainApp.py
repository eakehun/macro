import sys
import threading
import pyautogui
import win32clipboard
import eventManager
import sequence
import json
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QLabel, QGridLayout, QComboBox, QLineEdit, QPushButton, QScrollArea, QRadioButton, QButtonGroup, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot, QThread
from pynput import keyboard


class ButtonReleaseManager(QObject):
    store = set()

    MY_HOTKEY = {
        "mouse_position_copy": set([keyboard.Key.ctrl_l, keyboard.Key.alt_l, keyboard.KeyCode(67)])
    }
    
    released = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._listener = keyboard.Listener(on_press=self._key_pressed, on_release = self._key_released)
        self._listener.start()

    def _key_pressed(self, key):
        self.store.add( key )        
        
        for functionName in self.MY_HOTKEY:
            if all(k in self.store for k in self.MY_HOTKEY.get(functionName)):
                self.released.emit()
            
    def _key_released(self, key):
        if key in self.store:
            self.store.remove( key )
        

class mainApp(QWidget):

    eventStarted = pyqtSignal(eventManager.eventManager)

    def __init__(self):
        super().__init__()
        self.initUI()
        self.manager = ButtonReleaseManager()
        self.manager.released.connect(self.show_position)

        self.eventThread = eventManager.eventThread(parent=self)
        self.eventManager = eventManager.eventManager(self.eventThread)
        

    def initUI(self):

        mainLayout = QGridLayout()

        # 제일 위

        currentCoTextLabel = QLabel('현재 좌표: ', self)
        
        self.currentCoLabel = QLabel('', self)                
        self.currentCoLabel.setStyleSheet("border :1px solid grey;")
       
        # fixCoTextLabel = QLabel('클릭 좌표: ', self)
        
        # self.fixCoLabel = QLabel('', self)
        # self.fixCoLabel.setStyleSheet("border :1px solid grey;")


        headerGroup = QButtonGroup(self)
        pinRadio = QRadioButton('PIN 입력')
        cashRadio = QRadioButton('기프트 구입')

        headerGroup.addButton(pinRadio)
        headerGroup.addButton(cashRadio)

        pinRadio.setChecked(True)

        # 중간
        
        inputTypeTextLabel = QLabel('동작 구분: ', self)

        self.inputTypeCombobox = QComboBox(self)
        self.inputTypeCombobox.addItem('클릭')
        self.inputTypeCombobox.addItem('드래그')
        self.inputTypeCombobox.addItem('텍스트')
        self.inputTypeCombobox.addItem('핫키')
        self.inputTypeCombobox.addItem('브라우저')

        self.inputTypeCombobox.activated[str].connect(self.onActivated)

        self.startCoTextLabel = QLabel('시작 좌표', self)

        self.startCoText = QLineEdit(self)

        self.endCoTextLabel = QLabel('종료 좌표', self)
        self.endCoText = QLineEdit(self)        

        self.typoTextLabel = QLabel('텍스트', self)        
        self.typoText = QLineEdit(self)

        self.browserLabel = QLabel('URL', self)        
        self.browserText = QLineEdit(self)
        
        hotkeyGroup = QButtonGroup(self)
        self.copyRadio = QRadioButton('복사')
        self.pasteRadio = QRadioButton('붙여넣기')

        hotkeyGroup.addButton(self.copyRadio)
        hotkeyGroup.addButton(self.pasteRadio)



        delayTextLabel = QLabel('지연 시간', self)

        self.delayText = QLineEdit(self)

        actionTypeTextLabel = QLabel('동작 횟수', self)

        self.actionTypeCombobox = QComboBox(self)
        self.actionTypeCombobox.addItem('한번만')
        self.actionTypeCombobox.addItem('반복')

        self.addButton = QPushButton(self)
        self.addButton.setText('추가')
        self.addButton.clicked.connect(self.eventAdd)

        self.startButton = QPushButton(self)
        self.startButton.setText('시작')
        self.startButton.clicked.connect(self.macroStart)

        self.typoTextLabel.hide()
        self.typoText.hide()
        self.browserLabel.hide()
        self.browserText.hide()
        self.copyRadio.hide()
        self.pasteRadio.hide()
        self.endCoText.setEnabled(False)

        self.copyRadio.setChecked(True)

        # 아래
        
        self.pinLabel = QLabel()
        self.pinLabel.setStyleSheet("border :1px solid grey;")

        self.eventLabelScrollArea = QScrollArea()
        self.eventLabelScrollArea.setWidgetResizable(True)

        self.scrollWidget = QWidget(self)

        # scrollLayout = QVBoxLayout(self)
        scrollLayout = QGridLayout(self)
        

        self.scrollWidget.setLayout(scrollLayout)

        # self.eventLabel = QLabel()
        self.eventLabelScrollArea.setWidget(self.scrollWidget)
        

        # 그리드에 쌓기
        
        mainLayout.addWidget(currentCoTextLabel, 0, 0)
        mainLayout.addWidget(self.currentCoLabel, 0, 1, 1, 3)
        # mainLayout.addWidget(fixCoTextLabel, 0, 4)
        # mainLayout.addWidget(self.fixCoLabel, 0, 5, 1, 3)
        mainLayout.addWidget(pinRadio, 0, 10)
        mainLayout.addWidget(cashRadio, 0, 11, 1, 2)

        mainLayout.addWidget(inputTypeTextLabel, 1, 0)
        mainLayout.addWidget(self.inputTypeCombobox, 1, 1)
        mainLayout.addWidget(self.startCoTextLabel, 1, 2)
        mainLayout.addWidget(self.startCoText, 1, 3)
        mainLayout.addWidget(self.endCoTextLabel, 1, 4)
        mainLayout.addWidget(self.endCoText, 1, 5)

        mainLayout.addWidget(self.typoTextLabel, 1, 2)
        mainLayout.addWidget(self.typoText, 1, 3, 1, 3)
        mainLayout.addWidget(self.browserLabel, 1, 2)
        mainLayout.addWidget(self.browserText, 1, 3, 1, 3)

        mainLayout.addWidget(self.copyRadio, 1, 2)
        mainLayout.addWidget(self.pasteRadio, 1, 3, 1, 3)

        mainLayout.addWidget(delayTextLabel, 1, 6)
        mainLayout.addWidget(self.delayText, 1, 7)
        mainLayout.addWidget(actionTypeTextLabel, 1, 8)
        mainLayout.addWidget(self.actionTypeCombobox, 1, 9)
        mainLayout.addWidget(self.addButton, 1, 10)
        mainLayout.addWidget(self.startButton, 1, 11)

        mainLayout.addWidget(self.pinLabel, 2, 0, 10, 10)
        mainLayout.addWidget(self.eventLabelScrollArea, 13, 0, 1, 10)

        # mouseTrackThread = threading.Thread(target=self.mouseTrack, args=())
        # mouseTrackThread.daemon = True
        # mouseTrackThread.start()
        
        self.setLayout(mainLayout)

        self.setWindowTitle('Sample Macro')
        self.setFixedSize(1024, 768)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())        
        self.show()


        # with open('eventScenario.json', encoding='UTF8') as json_file:
        #     json_data = json.load(json_file)
        #     # print(json_data)
        #     self.jsonEventAdd(json_data)
        #     self.buildEventLayout()

        

    def mouseTrack(self):
        while 1:
            x, y = pyautogui.position()
            self.currentCoLabel.setText('x={0}, y={1}' .format(x, y))

    

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            if self.eventThread.isRun:
                self.eventThread.isRun = False
                print('loop end')
            else:
                with open("eventScenario.json", "w") as json_file:
                    json.dump(self.eventManager.eventScenarioJson, json_file)
                print('app end')
                self.close()

    def onActivated(self, text):
        self.startCoTextLabel.hide()
        self.startCoText.hide()
        self.endCoTextLabel.hide()
        self.endCoText.hide()
        self.typoTextLabel.hide()
        self.typoText.hide()
        self.browserLabel.hide()
        self.browserText.hide()
        self.copyRadio.hide()
        self.pasteRadio.hide()

        self.startCoText.setText('')
        self.typoText.setText('')
        self.browserText.setText('')
        self.endCoText.setText('')
        self.delayText.setText('')


        if text == '클릭':
            self.startCoTextLabel.show()
            self.startCoText.show()
            self.endCoTextLabel.show()
            self.endCoText.show()
            self.endCoText.setEnabled(False)
            
        elif text == '드래그':
            self.startCoTextLabel.show()
            self.startCoText.show()
            self.endCoTextLabel.show()
            self.endCoText.show()
            self.endCoText.setEnabled(True)

        elif text == '텍스트':
            self.typoTextLabel.show()
            self.typoText.show()

        elif text == '핫키':
            self.copyRadio.show()
            self.pasteRadio.show()
            self.copyRadio.setChecked(True)
        
        elif text == '브라우저':
            self.browserLabel.show()
            self.browserText.show()
            
    def eventAdd(self):
        # print('add click')

        eventType = self.inputTypeCombobox.currentText()
        startXy = self.startCoText.text()
        endXy = self.endCoText.text()
        typoText = self.typoText.text()
        url = self.browserText.text()
        hotkey = 'copy'

        if self.copyRadio.isChecked():
            hotkey = 'copy'
        else:
            hotkey = 'paste'


        delay = self.delayText.text()
        actionType = self.actionTypeCombobox.currentIndex()

        self.clearEventLayout()

        
        newSeq = sequence.sequence(startXy, eventType, endXy, typoText, url, hotkey, delay, actionType)
        self.eventManager.addEvent(newSeq, actionType)
        self.buildEventLayout()

        # print(json.dumps(self.eventManager))

    def jsonEventAdd(self, jsonData):
        # print('add click')

        eventList = jsonData['eventList']
        repeatEventList = jsonData['repeatEventList']

        for eventSeq in eventList:
            eventType = eventSeq['eventType']
            startXy = eventSeq['startXy']
            endXy = eventSeq['endXy']
            typoText = eventSeq['text']
            url = eventSeq['url']
            hotkey = eventSeq['command']

            delay = eventSeq['delayTime']
            actionType = eventSeq['actionType']
            
            newSeq = sequence.sequence(startXy, eventType, endXy, typoText, url, hotkey, delay, actionType)
            self.eventManager.addEvent(newSeq, actionType)

        for eventSeq in repeatEventList:
            eventType = eventSeq['eventType']
            startXy = eventSeq['startXy']
            endXy = eventSeq['endXy']
            typoText = eventSeq['text']
            url = eventSeq['url']
            hotkey = eventSeq['command']

            delay = eventSeq['delayTime']
            actionType = eventSeq['actionType']
            
            newSeq = sequence.sequence(startXy, eventType, endXy, typoText, url, hotkey, delay, actionType)
            self.eventManager.addEvent(newSeq, actionType)


    def clearEventLayout(self):
        while self.scrollWidget.layout().count():
            item = self.scrollWidget.layout().takeAt(0)
            widget = item.widget()
            widget.deleteLater()
       
    def buildEventLayout(self):
        for idx, eventSeq in enumerate(self.eventManager.eventList):

            seqString = '동작구분={0}, 시작좌표={1}, 끝좌표={2}, 텍스트={3}, 단축키={4}, 지연시간={5}, 반복구분={6}\n' .format(eventSeq.eventType, eventSeq.startXy, eventSeq.endXy, eventSeq.text, eventSeq.command, eventSeq.delayTime, eventSeq.actionType)

            eventLabel = QLabel(seqString)
            eventEditButton = QPushButton()
            eventEditButton.setText('수정')

            eventDeleteButton = QPushButton()
            eventDeleteButton.setText('삭제')

            eventEditButton.clicked.connect(lambda checked, _idx = idx : self.eventEdit(_idx, eventSeq.actionType))
            eventDeleteButton.clicked.connect(lambda checked, _idx = idx : self.eventDelete(_idx, eventSeq.actionType))

            self.scrollWidget.layout().addWidget(eventLabel, idx, 0)
            self.scrollWidget.layout().addWidget(eventEditButton, idx, 1)
            self.scrollWidget.layout().addWidget(eventDeleteButton, idx, 2)

        for idx, repeatEventSeq in enumerate(self.eventManager.repeatEventList, len(self.eventManager.eventList)):

            seqString = '동작구분={0}, 시작좌표={1}, 끝좌표={2}, 텍스트={3}, 단축키={4}, 지연시간={5}, 반복구분={6}\n' .format(repeatEventSeq.eventType, repeatEventSeq.startXy, repeatEventSeq.endXy, repeatEventSeq.text, repeatEventSeq.command, repeatEventSeq.delayTime, repeatEventSeq.actionType)
            
            eventLabel = QLabel(seqString)
            eventEditButton = QPushButton()
            eventEditButton.setText('수정')

            eventDeleteButton = QPushButton()
            eventDeleteButton.setText('삭제')

            eventEditButton.clicked.connect(lambda checked, _idx = idx - len(self.eventManager.eventList) : self.eventEdit(_idx, repeatEventSeq.actionType))
            eventDeleteButton.clicked.connect(lambda checked, _idx = idx - len(self.eventManager.eventList) : self.eventDelete(_idx, repeatEventSeq.actionType))

            self.scrollWidget.layout().addWidget(eventLabel, idx, 0)
            self.scrollWidget.layout().addWidget(eventEditButton, idx, 1)
            self.scrollWidget.layout().addWidget(eventDeleteButton, idx, 2)
        
    
    def macroStart(self):
        # print('start click')

        self.eventManager.executeEvent()

    # def on_click(self, x, y, button, pressed):
    #     if pressed == True:
    #         print(x,y)

    def eventEdit(self, _index, actionType):
        print('actionType:{0} index:{1} edit click'.format(actionType, _index))

    def eventDelete(self, _index, actionType):
        print('actionType:{0} index:{1} delete click'.format(actionType, _index))

    @pyqtSlot()
    def show_position(self):
        x, y = pyautogui.position()
        coordText = '{0}, {1}' .format(x, y)
        win32clipboard.OpenClipboard()        
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(coordText, win32clipboard.CF_TEXT)
        win32clipboard.CloseClipboard()

        self.currentCoLabel.setText(coordText)
            

    # def inputInit(self):
    #     with mouse.Listener(on_click=self.on_click) as listener:
    #         listener.join()

# def main():
#     thread2 = threading.Thread(target=takeScreenshot, args=())
#     thread2.start()

#     with Listener(on_press=getKey) as listener:
#         listener.join()


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = mainApp()
    
    with open('eventScenario.json', encoding='UTF8') as json_file:
        try:
            json_data = json.load(json_file)        
            ex.jsonEventAdd(json_data)
            ex.buildEventLayout()
        except json.decoder.JSONDecodeError:
            pass
        
    
    sys.exit(app.exec_())



