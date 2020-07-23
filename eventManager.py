import sequence
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread, QObject

class eventManager(QObject):

    eventStarted = pyqtSignal(list)

    def __init__(self, eventThread):
        super().__init__()
        self.eventList = []
        self.repeatEventList = []
        self.eventThread = eventThread

        self.eventStarted.connect(self.eventThread.setEventList)
        
        # print('event manager')

    def addEvent(self, sequence, actionType):
        if actionType == 0:
            self.eventList.append(sequence)
        else:            
            self.repeatEventList.append(sequence)

    def clearEvent(self):
        self.eventList.clear()
        self.repeatEventList.clear()

    def deleteEventByIndex(self, actionType):
        if actionType == 0:
            del self.eventList[-1]
        else:            
            del self.repeatEventList[-1]

    def executeEvent(self):

        

        for seq in self.eventList:
            seq.launch()
        if len(self.repeatEventList) > 0:
            self.eventStarted.emit(self.repeatEventList)
            self.eventThread.isRun = True
            self.eventThread.start()

            # while True:
                
            #         for seq in self.repeatEventList:
            #             seq.launch()
            #     except KeyboardInterrupt:
            #         break

    


class eventThread(QThread):

    def __init__(self, parent=None):
       super().__init__() 
       self.isRun = False
       

    
    def run(self):
        while self.isRun:
            # self.eventManager.executeEvent()

            for seq in self.repeatEventList:
                seq.launch()

    @pyqtSlot(list)
    def setEventList(self, repeatEventList):
        self.repeatEventList = repeatEventList


