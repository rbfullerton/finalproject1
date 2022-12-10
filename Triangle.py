# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Triangle.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowTriangle(object):
    def setupUi(self, WindowTriangle):
        WindowTriangle.setObjectName("WindowTriangle")
        WindowTriangle.setEnabled(True)
        WindowTriangle.resize(497, 540)
        WindowTriangle.setMinimumSize(QtCore.QSize(497, 540))
        WindowTriangle.setMaximumSize(QtCore.QSize(497, 540))
        self.centralwidget = QtWidgets.QWidget(WindowTriangle)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTriangle = QtWidgets.QLabel(self.centralwidget)
        self.labelTriangle.setGeometry(QtCore.QRect(20, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(36)
        self.labelTriangle.setFont(font)
        self.labelTriangle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelTriangle.setStyleSheet("font: 36pt \"American Typewriter\";\n"
"color:rgb(15, 128, 255)")
        self.labelTriangle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTriangle.setObjectName("labelTriangle")
        self.pushMTriangle = QtWidgets.QPushButton(self.centralwidget)
        self.pushMTriangle.setGeometry(QtCore.QRect(140, 220, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushMTriangle.setFont(font)
        self.pushMTriangle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushMTriangle.setObjectName("pushMTriangle")
        self.labelBase = QtWidgets.QLabel(self.centralwidget)
        self.labelBase.setGeometry(QtCore.QRect(50, 130, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(13)
        self.labelBase.setFont(font)
        self.labelBase.setObjectName("labelBase")
        self.base = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.base.setGeometry(QtCore.QRect(110, 130, 121, 21))
        self.base.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.base.setObjectName("base")
        self.pushMainT = QtWidgets.QPushButton(self.centralwidget)
        self.pushMainT.setGeometry(QtCore.QRect(140, 410, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushMainT.setFont(font)
        self.pushMainT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushMainT.setObjectName("pushMainT")
        self.numTriangle = QtWidgets.QLabel(self.centralwidget)
        self.numTriangle.setGeometry(QtCore.QRect(20, 300, 461, 121))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(96)
        self.numTriangle.setFont(font)
        self.numTriangle.setStyleSheet("font: 96pt \"American Typewriter\";\n"
"color:rgb(15, 128, 255)")
        self.numTriangle.setAlignment(QtCore.Qt.AlignCenter)
        self.numTriangle.setObjectName("numTriangle")
        self.textTriangle = QtWidgets.QLabel(self.centralwidget)
        self.textTriangle.setGeometry(QtCore.QRect(20, 250, 461, 71))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        self.textTriangle.setFont(font)
        self.textTriangle.setAlignment(QtCore.Qt.AlignCenter)
        self.textTriangle.setWordWrap(True)
        self.textTriangle.setObjectName("textTriangle")
        self.groupBoxC = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxC.setGeometry(QtCore.QRect(50, 80, 401, 41))
        self.groupBoxC.setTitle("")
        self.groupBoxC.setObjectName("groupBoxC")
        self.radioAreaT = QtWidgets.QRadioButton(self.groupBoxC)
        self.radioAreaT.setGeometry(QtCore.QRect(70, 10, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioAreaT.setFont(font)
        self.radioAreaT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioAreaT.setChecked(False)
        self.radioAreaT.setObjectName("radioAreaT")
        self.radioPerimeterT = QtWidgets.QRadioButton(self.groupBoxC)
        self.radioPerimeterT.setGeometry(QtCore.QRect(230, 10, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioPerimeterT.setFont(font)
        self.radioPerimeterT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioPerimeterT.setChecked(True)
        self.radioPerimeterT.setObjectName("radioPerimeterT")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(10, 60, 481, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setEnabled(True)
        self.line_2.setGeometry(QtCore.QRect(10, 0, 481, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.labelHeight = QtWidgets.QLabel(self.centralwidget)
        self.labelHeight.setGeometry(QtCore.QRect(50, 160, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(13)
        self.labelHeight.setFont(font)
        self.labelHeight.setObjectName("labelHeight")
        self.height = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.height.setGeometry(QtCore.QRect(110, 160, 121, 21))
        self.height.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.height.setObjectName("height")
        self.labelSide2 = QtWidgets.QLabel(self.centralwidget)
        self.labelSide2.setGeometry(QtCore.QRect(270, 160, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(13)
        self.labelSide2.setFont(font)
        self.labelSide2.setObjectName("labelSide2")
        self.side2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.side2.setGeometry(QtCore.QRect(330, 160, 121, 21))
        self.side2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.side2.setObjectName("side2")
        self.labelSide1 = QtWidgets.QLabel(self.centralwidget)
        self.labelSide1.setGeometry(QtCore.QRect(270, 130, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(13)
        self.labelSide1.setFont(font)
        self.labelSide1.setObjectName("labelSide1")
        self.side1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.side1.setGeometry(QtCore.QRect(330, 130, 121, 21))
        self.side1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.side1.setObjectName("side1")
        self.labelSide3 = QtWidgets.QLabel(self.centralwidget)
        self.labelSide3.setGeometry(QtCore.QRect(270, 190, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(13)
        self.labelSide3.setFont(font)
        self.labelSide3.setObjectName("labelSide3")
        self.side3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.side3.setGeometry(QtCore.QRect(330, 190, 121, 21))
        self.side3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.side3.setObjectName("side3")
        WindowTriangle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowTriangle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 24))
        self.menubar.setObjectName("menubar")
        WindowTriangle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowTriangle)
        self.statusbar.setObjectName("statusbar")
        WindowTriangle.setStatusBar(self.statusbar)

        self.retranslateUi(WindowTriangle)
        QtCore.QMetaObject.connectSlotsByName(WindowTriangle)

    def retranslateUi(self, WindowTriangle):
        _translate = QtCore.QCoreApplication.translate
        WindowTriangle.setWindowTitle(_translate("WindowTriangle", "Triangle"))
        self.labelTriangle.setText(_translate("WindowTriangle", "TRIANGLE COMPUTATION"))
        self.pushMTriangle.setText(_translate("WindowTriangle", "Measure Shape"))
        self.labelBase.setText(_translate("WindowTriangle", "Base :"))
        self.pushMainT.setText(_translate("WindowTriangle", "Go Back"))
        self.numTriangle.setText(_translate("WindowTriangle", "0"))
        self.textTriangle.setText(_translate("WindowTriangle", "The _________ of the Triangle is..."))
        self.radioAreaT.setText(_translate("WindowTriangle", "Area"))
        self.radioPerimeterT.setText(_translate("WindowTriangle", "Perimeter"))
        self.labelHeight.setText(_translate("WindowTriangle", "Height :"))
        self.labelSide2.setText(_translate("WindowTriangle", "Side 2 :"))
        self.labelSide1.setText(_translate("WindowTriangle", "Side 1 :"))
        self.labelSide3.setText(_translate("WindowTriangle", "Side 3 :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowTriangle = QtWidgets.QMainWindow()
    ui = Ui_WindowTriangle()
    ui.setupUi(WindowTriangle)
    WindowTriangle.show()
    sys.exit(app.exec_())
