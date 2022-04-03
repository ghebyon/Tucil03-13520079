from App import *
import webbrowser
import sys
import os
from PyQt5 import QtTest
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Puzzle import *
from Puzzle import Puzzle

linkedinURL = "https://www.linkedin.com/in/ghebyon-nainggolan-5002ab218/"
githubURL = "https://github.com/ghebyon/Tucil03-Stima"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Remove window tittle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Shadow effect style
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        self.setWindowTitle("15-PUZZLE WITH BNB")
        QSizeGrip(self.ui.unusedFrame)
        QSizeGrip(self.ui.unusedFrame2)
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        self.ui.quitButton.clicked.connect(lambda: self.close())
        self.ui.exitButton.clicked.connect(lambda: self.close())
        self.ui.fullscreenButton.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.slideMenuButton.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.socmediaButton.clicked.connect(lambda: webbrowser.open(linkedinURL))
        self.ui.githubButton.clicked.connect(lambda: webbrowser.open(githubURL))
        self.ui.inputFileTxtButton.clicked.connect(lambda : self.browseFiles())
        self.ui.fastSlider.valueChanged.connect(lambda : self.updateSliderValue())
        self.ui.searchButton.clicked.connect(lambda : self.search())
        def moveWindow(e):
                if self.isMaximized() == False: #Not maximized
                    if e.buttons() == Qt.LeftButton:  
                        self.move(self.pos() + e.globalPos() - self.clickPosition)
                        self.clickPosition = e.globalPos()
                        e.accept()
        self.ui.headerFrame.mouseMoveEvent = moveWindow
        self.show()

    def search(self):
        context = self.ui.plainTextEdit.toPlainText()
        elementContent = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
        arrayContext = context.split()
        
        for x in arrayContext:
            if x in elementContent:
                elementContent.remove(x)
        
        if (len(elementContent) != 0 or len(arrayContext) > 16):
            self.ui.boxSolusi.setPlainText("Invalid input")
        else:
            for i in range(len(arrayContext)):
                arrayContext[i] = int(arrayContext[i])
            root = Puzzle(0,arrayContext,"")
            if(root.reachable()):
                self.ui.boxSolusi.setPlainText("Calculating...")
                start = time.time()
                initPuzzleList = []
                initPuzzleList.append(root)
                count, solution = BranchnBound(initPuzzleList)
                end = time.time()
                self.ui.boxSolusi.setPlainText(solution)
                print(f"SOLUTION : {solution}")
                print(f"TOTAL ACCESS : {count}")
                print(f"TIME EXECUTION : {end-start} s")
                self.ui.TE.setText(f"TIME EXECUTION : {end-start} s")
                self.ui.TA.setText(f"TOTAL ACCESS : {count}")
                self.animatePuzzle(arrayContext, solution)
            else:
                self.ui.boxSolusi.setPlainText("Not Reachable")
                self.ui.TE.setText("TIME EXECUTION : -")
                self.ui.TA.setText("TOTAL ACCESS : - ")

    def animatePuzzle(self, arrayContext, solution):
        slot = [self.ui.slot01,self.ui.slot02,self.ui.slot03,self.ui.slot04,
                self.ui.slot05,self.ui.slot06,self.ui.slot07,self.ui.slot08,
                self.ui.slot09,self.ui.slot10,self.ui.slot11,self.ui.slot12,
                self.ui.slot13,self.ui.slot14,self.ui.slot15,self.ui.slot16,]
        for i in range(16):
            slot[i].setText(str(arrayContext[i]))
            if(str(arrayContext[i]) == "16"):
                slot[i].setStyleSheet('background-color: rgb(34, 40, 49); font: 75 26pt "Comic Sans MS";color: rgb(230, 5, 64);')
            else:
                slot[i].setStyleSheet('background-color: rgb(9, 5, 13); font: 75 26pt "Comic Sans MS";color: rgb(230, 5, 64);')
        QtTest.QTest.qWait(1000)
        for command in solution:
            for i in range(16):
                if slot[i].text() == "16":
                    if(command == "L"):
                        temp = slot[i-1].text()
                        slot[i-1].setText(str(slot[i].text()))
                        slot[i].setText(temp)
                        slot[i].setStyleSheet('background-color: rgb(9, 5, 13); font: 75 26pt "Comic Sans MS";color: rgb(230, 5, 64);')
                        slot[i-1].setStyleSheet('background-color: rgb(34, 40, 49); font: 75 26pt "Comic Sans MS";color: rgb(230, 5, 64);')
                    elif(command == "U"):
                        temp = slot[i-4].text()
                        slot[i-4].setText(str(slot[i].text()))
                        slot[i].setText(temp)
                        slot[i].setStyleSheet('background-color: rgb(9, 5, 13); font: 75 26pt "Comic Sans MS";color: rgb(230, 5, 64);')
                        slot[i-4].setStyleSheet('background-color: rgb(34, 40, 49); font: 75 26pt "Comic Sans MS";color: rgb(230, 5, 64);')
                    elif(command == "D"):
                        temp = slot[i+4].text()
                        slot[i+4].setText(str(slot[i].text()))
                        slot[i].setText(temp)
                        slot[i].setStyleSheet('background-color: rgb(9, 5, 13); font: 75 26pt "Comic Sans MS";color: rgb(230, 5, 64);')
                        slot[i+4].setStyleSheet('background-color: rgb(34, 40, 49); font: 75 26pt "Comic Sans MS";color: rgb(230, 5, 64);')
                    elif(command == "R"):
                        temp = slot[i+1].text()
                        slot[i+1].setText(str(slot[i].text()))
                        slot[i].setText(temp)
                        slot[i].setStyleSheet('background-color: rgb(9, 5, 13); font: 75 26pt "Comic Sans MS";color: rgb(230, 5, 64);')
                        slot[i+1].setStyleSheet('background-color: rgb(34, 40, 49); font: 75 26pt "Comic Sans MS";color: rgb(230, 5, 64);')
                    break
            percentage = int(self.ui.sliderValue.text())
            QtTest.QTest.qWait(int((1/percentage)*1000))
            
   
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()  

    def updateSliderValue(self):
        newValue = str(self.ui.fastSlider.value())
        self.ui.sliderValue.setText(newValue)

    def browseFiles(self):
        txtPath = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', 'txt files (*.txt)')
        fp = open(txtPath[0], 'r')
        text = fp.read()
        fp.close()
        self.ui.plainTextEdit.setPlainText(text)
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.fullscreenButton.setIcon(QtGui.QIcon(u":/newPrefix/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.fullscreenButton.setIcon(QtGui.QIcon(u":/newPrefix/icons/minimize-2.svg"))
    
    def slideLeftMenu(self):
        width = self.ui.slidemenu.width()
        # If minimized
        if width == 0:
            newWidth = 300
            self.ui.slideMenuButton.setIcon(QtGui.QIcon(u":/newPrefix/icons/chevron-left.svg"))
        # If maximized
        else:
            # Restore menu
            newWidth = 0
            self.ui.slideMenuButton.setIcon(QtGui.QIcon(u":/newPrefix/icons/align-left.svg"))

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.slidemenu, b"maximumWidth")#Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
