# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Square.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowSquare(object):
    def setupUi(self, WindowSquare):
        WindowSquare.setObjectName("WindowSquare")
        WindowSquare.setEnabled(True)
        WindowSquare.resize(497, 540)
        WindowSquare.setMinimumSize(QtCore.QSize(497, 540))
        WindowSquare.setMaximumSize(QtCore.QSize(497, 540))
        self.centralwidget = QtWidgets.QWidget(WindowSquare)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCircle = QtWidgets.QLabel(self.centralwidget)
        self.labelCircle.setGeometry(QtCore.QRect(20, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(36)
        self.labelCircle.setFont(font)
        self.labelCircle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelCircle.setStyleSheet("font: 36pt \"American Typewriter\";\n"
"color:rgb(15, 128, 255)")
        self.labelCircle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCircle.setObjectName("labelCircle")
        self.pushMSquare = QtWidgets.QPushButton(self.centralwidget)
        self.pushMSquare.setGeometry(QtCore.QRect(140, 200, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushMSquare.setFont(font)
        self.pushMSquare.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushMSquare.setObjectName("pushMSquare")
        self.labelSides = QtWidgets.QLabel(self.centralwidget)
        self.labelSides.setGeometry(QtCore.QRect(110, 150, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(13)
        self.labelSides.setFont(font)
        self.labelSides.setObjectName("labelSides")
        self.sides = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.sides.setGeometry(QtCore.QRect(190, 150, 201, 21))
        self.sides.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.sides.setObjectName("sides")
        self.pushMainS = QtWidgets.QPushButton(self.centralwidget)
        self.pushMainS.setGeometry(QtCore.QRect(140, 410, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushMainS.setFont(font)
        self.pushMainS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushMainS.setObjectName("pushMainS")
        self.numSquare = QtWidgets.QLabel(self.centralwidget)
        self.numSquare.setGeometry(QtCore.QRect(20, 300, 461, 121))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(96)
        self.numSquare.setFont(font)
        self.numSquare.setStyleSheet("font: 96pt \"American Typewriter\";\n"
"color:rgb(15, 128, 255)")
        self.numSquare.setAlignment(QtCore.Qt.AlignCenter)
        self.numSquare.setObjectName("numSquare")
        self.textSquare = QtWidgets.QLabel(self.centralwidget)
        self.textSquare.setGeometry(QtCore.QRect(20, 240, 461, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        self.textSquare.setFont(font)
        self.textSquare.setAlignment(QtCore.Qt.AlignCenter)
        self.textSquare.setWordWrap(True)
        self.textSquare.setObjectName("textSquare")
        self.groupBoxC = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxC.setGeometry(QtCore.QRect(50, 80, 401, 41))
        self.groupBoxC.setTitle("")
        self.groupBoxC.setObjectName("groupBoxC")
        self.radioAreaS = QtWidgets.QRadioButton(self.groupBoxC)
        self.radioAreaS.setGeometry(QtCore.QRect(70, 10, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioAreaS.setFont(font)
        self.radioAreaS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioAreaS.setChecked(False)
        self.radioAreaS.setObjectName("radioAreaS")
        self.radioPerimeterS = QtWidgets.QRadioButton(self.groupBoxC)
        self.radioPerimeterS.setGeometry(QtCore.QRect(230, 10, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioPerimeterS.setFont(font)
        self.radioPerimeterS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioPerimeterS.setChecked(True)
        self.radioPerimeterS.setObjectName("radioPerimeterS")
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
        WindowSquare.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowSquare)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 24))
        self.menubar.setObjectName("menubar")
        WindowSquare.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowSquare)
        self.statusbar.setObjectName("statusbar")
        WindowSquare.setStatusBar(self.statusbar)

        self.retranslateUi(WindowSquare)
        QtCore.QMetaObject.connectSlotsByName(WindowSquare)

    def retranslateUi(self, WindowSquare):
        _translate = QtCore.QCoreApplication.translate
        WindowSquare.setWindowTitle(_translate("WindowSquare", "Square"))
        self.labelCircle.setText(_translate("WindowSquare", "SQUARE COMPUTATION"))
        self.pushMSquare.setText(_translate("WindowSquare", "Measure Shape"))
        self.labelSides.setText(_translate("WindowSquare", "Side(s) :"))
        self.pushMainS.setText(_translate("WindowSquare", "Go Back"))
        self.numSquare.setText(_translate("WindowSquare", "0"))
        self.textSquare.setText(_translate("WindowSquare", "The _________ of the Square is..."))
        self.radioAreaS.setText(_translate("WindowSquare", "Area"))
        self.radioPerimeterS.setText(_translate("WindowSquare", "Perimeter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowSquare = QtWidgets.QMainWindow()
    ui = Ui_WindowSquare()
    ui.setupUi(WindowSquare)
    WindowSquare.show()
    sys.exit(app.exec_())
