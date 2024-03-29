# hello_app_from_ui_mult.py

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic, QtCore, QtGui
import sys
import myEpicsHome
import time

# Load UI Files
Ui_Form_telaInicial, QtBaseClass = uic.loadUiType("telaInicial.ui")
Ui_Form_epicsInterface, QtBaseClass = uic.loadUiType("epicsInterface.ui")
Ui_Form_EPSInterface, QtBaseClass = uic.loadUiType("EPSInterface.ui")
Ui_Form_TempScreen, QtBaseClass = uic.loadUiType("TempScreen.ui")

# Window #1 Class
class TelaInicial(QMainWindow, Ui_Form_telaInicial):
    def __init__(self, parent=None):
        super(TelaInicial, self).__init__(parent)
        super(Ui_Form_telaInicial, self).__init__()
        self.setupUi(self)

        # Add things to my TelaInicial

        # Bind signal to slot
        self.LinkButtonEPICS.clicked.connect(self.openEPICS)
        self.LinkButtonEPS.clicked.connect(self.openEPS)
        self.LinkButtonTempScreen.clicked.connect(self.openTempScreen)


    # My slot's
    def openEPICS(self):
        self.epicsInterface = EpicsInterface()
        self.epicsInterface.show()
        self.close()

    def openEPS(self):
        self.EPSInterface = EPSInterface()
        self.EPSInterface.show()
        self.close()
    
    def openTempScreen(self):
        self.TempScreen = TempScreen()
        self.TempScreen.show()
        self.close()

# Window #2 Class
class EpicsInterface(QWidget, Ui_Form_epicsInterface):
    def __init__(self, parent=None):
        super(EpicsInterface, self).__init__(parent)
        super(Ui_Form_epicsInterface, self).__init__()
        self.setupUi(self)

        # Bind signal to slot
        self.LinkButtonBack.clicked.connect(self.onClickBack)
        self.pushButton_readPv.clicked.connect(self.readPv)
        
    # My slots
    def onClickBack(self):
        self.close()
        self.window = TelaInicial()
        self.window.show()
        
    def readPv(self):
         nome_da_pv = self.lineEdit_readPv.text()
         if nome_da_pv != '':
             pv = PV(nome_da_pv)
             if pv.connected:
                      pv_value = str(float(pv.value/10))
                      self.lineEdit_PvValue.setText(pv_value)
             else:
                      self.lineEdit_PvValue.setText('PV not connected')  

        
# Window #3 Class
class EPSInterface(QWidget, Ui_Form_EPSInterface):
    def __init__(self, parent=None):
        super(EPSInterface, self).__init__(parent)
        super(Ui_Form_EPSInterface, self).__init__()
        self.setupUi(self)

        # Add things to my Window
        self.threadclass = ThreadClass()
        self.threadclass.start()

       # Set things to my Window

        
       # Bind signal to method
        self.threadclass.sig.connect(self.updateAI)
    
    def onClickBack(self):
        self.close()
        self.window = TelaInicial()
        self.window.show()

    def updateAI(self, AI1, AI2, AI3, AI4,AI5, AI6, AI7, AI8,AI9, AI10, AI11, AI12,AI13, AI14, AI15, AI16,AI17, AI18, AI19, AI20,AI21, AI22, AI23, AI24,AI25, AI26, AI27, AI28,AI29, AI30, AI31, AI32):
        self.lineEditAI1.setText(str(AI1))
        self.lineEditAI2.setText(str(AI2))
        self.lineEditAI3.setText(str(AI3))
        self.lineEditAI4.setText(str(AI4))
        self.lineEditAI5.setText(str(AI5))
        self.lineEditAI6.setText(str(AI6))
        self.lineEditAI7.setText(str(AI7))
        self.lineEditAI8.setText(str(AI8))
        self.lineEditAI9.setText(str(AI9))
        self.lineEditAI10.setText(str(AI10))
        self.lineEditAI11.setText(str(AI11))
        self.lineEditAI12.setText(str(AI12))
        self.lineEditAI13.setText(str(AI13))
        self.lineEditAI14.setText(str(AI14))
        self.lineEditAI15.setText(str(AI15))
        self.lineEditAI16.setText(str(AI16))
        self.lineEditAI17.setText(str(AI17))
        self.lineEditAI18.setText(str(AI18))
        self.lineEditAI19.setText(str(AI19))
        self.lineEditAI20.setText(str(AI20))
        self.lineEditAI21.setText(str(AI21))
        self.lineEditAI22.setText(str(AI22))
        self.lineEditAI23.setText(str(AI23))
        self.lineEditAI24.setText(str(AI24))
        self.lineEditAI25.setText(str(AI25))
        self.lineEditAI26.setText(str(AI26))
        self.lineEditAI27.setText(str(AI27))
        self.lineEditAI28.setText(str(AI28))
        self.lineEditAI29.setText(str(AI29))
        self.lineEditAI30.setText(str(AI30))
        self.lineEditAI31.setText(str(AI31))
        self.lineEditAI32.setText(str(AI32))
        
# Window #4 Class
class TempScreen(QWidget, Ui_Form_TempScreen):
    def __init__(self, parent=None):
        super(TempScreen, self).__init__(parent)
        super(Ui_Form_TempScreen, self).__init__()
        self.setupUi(self)

        # Add things to my Window
        self.threadtempscreen = ThreadTempScreen()
        self.threadtempscreen.start()
        
        # Set things to my Window

        # Bind signal to method
        self.threadtempscreen.sig.connect(self.updateTempScreen)
        self.pushButtonBackTempScreen.clicked.connect(self.onClickBack)

        # My slots
    def onClickBack(self):
        self.close()
        self.window = TelaInicial()
        self.window.show()
        
    def updateTempScreen(self, A1, myList):
        self.lineEditWprFitValue.setText(str(A1))
        
        #Update Booleans variables (0 - failure/red) (1 - normal/green)
        if myList[0] == 1:
            self.labelWprFitBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelWprFitBool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if myList[1] == 1:
            self.labelBpBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelBpBool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if myList[2] == 1:
            self.labelEpsStatusBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelEpsStatusBool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if myList[3] == 1:
            self.labelPpsStatusBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelPpsStatusBool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if myList[4] == 1:
            self.lineEditShutter.setText("CLOSED")
        else:
            self.lineEditShutter.setText("OPEN")
        if myList[5] == 1:
            self.lineEditBeamStatus.setText("ON")
        else:
            self.lineEditBeamStatus.setText("OFF")

    
class ThreadTempScreen(QtCore.QThread):
    # Create the signal
    sig = QtCore.pyqtSignal(float, list)
    
    def __init__(self, parent=None):
        super(ThreadTempScreen, self).__init__(parent)
        
    def run(self):
        myList = list(range(6))
        while 1:
            A1 = myEpicsHome.getRandom()
            myList[0] = myEpicsHome.getBool()
            myList[1] = myEpicsHome.getBool()
            myList[2] = myEpicsHome.getBool()
            myList[3] = myEpicsHome.getBool()
            myList[4] = myEpicsHome.getBool()
            myList[4] = myEpicsHome.getBool()
            myList[5] = myEpicsHome.getBool()
            time.sleep(0.4)
            print (myList) # Debugg



            
            # Emit the signal
            self.sig.emit(A1,myList)
        
class ThreadClass(QtCore.QThread):
    # Create the signal
    sig = QtCore.pyqtSignal(float, float, float, float,float, float, float, float,float, float, float, float,float, float, float, float,float, float, float, float,float, float, float, float,float, float, float, float,float, float, float, float)
    
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        
    def run(self):
        while 1:
            AI1 = myEpicsHome.getRandom()
            AI2 = myEpicsHome.getRandom()
            AI3 = myEpicsHome.getRandom()
            AI4 = myEpicsHome.getRandom()
            AI5 = myEpicsHome.getRandom()
            AI6 = myEpicsHome.getRandom()
            AI7 = myEpicsHome.getRandom()
            AI8 = myEpicsHome.getRandom()
            AI9 = myEpicsHome.getRandom()
            AI10 = myEpicsHome.getRandom()
            AI11 = myEpicsHome.getRandom()
            AI12 = myEpicsHome.getRandom()
            AI13 = myEpicsHome.getRandom()
            AI14 = myEpicsHome.getRandom()
            AI15 = myEpicsHome.getRandom()
            AI16 = myEpicsHome.getRandom()
            AI17 = myEpicsHome.getRandom()
            AI18 = myEpicsHome.getRandom()
            AI19 = myEpicsHome.getRandom()
            AI20 = myEpicsHome.getRandom()
            AI21 = myEpicsHome.getRandom()
            AI22 = myEpicsHome.getRandom()
            AI23 = myEpicsHome.getRandom()
            AI24 = myEpicsHome.getRandom()
            AI25 = myEpicsHome.getRandom()
            AI26 = myEpicsHome.getRandom()
            AI27 = myEpicsHome.getRandom()
            AI28 = myEpicsHome.getRandom()
            AI29 = myEpicsHome.getRandom()
            AI30 = myEpicsHome.getRandom()
            AI31 = myEpicsHome.getRandom()
            AI32 = myEpicsHome.getRandom()
            

            time.sleep(0.4)


            
            # Emit the signal
            self.sig.emit(AI1, AI2, AI3, AI4,AI5, AI6, AI7, AI8,AI9, AI10, AI11, AI12,AI13, AI14, AI15, AI16,AI17, AI18, AI19, AI20,AI21, AI22, AI23, AI24,AI25, AI26, AI27, AI28,AI29, AI30, AI31, AI32)

# Init interface
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TelaInicial()
    window.show()
    sys.exit(app.exec_())
