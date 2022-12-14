# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Circle.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowCircle(object):
    def setupUi(self, WindowCircle):
        WindowCircle.setObjectName("WindowCircle")
        WindowCircle.setEnabled(True)
        WindowCircle.resize(497, 540)
        WindowCircle.setMinimumSize(QtCore.QSize(497, 540))
        WindowCircle.setMaximumSize(QtCore.QSize(497, 540))
        self.centralwidget = QtWidgets.QWidget(WindowCircle)
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
        self.pushMCircle = QtWidgets.QPushButton(self.centralwidget)
        self.pushMCircle.setGeometry(QtCore.QRect(140, 200, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushMCircle.setFont(font)
        self.pushMCircle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushMCircle.setObjectName("pushMCircle")
        self.labelRadius = QtWidgets.QLabel(self.centralwidget)
        self.labelRadius.setGeometry(QtCore.QRect(110, 150, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(13)
        self.labelRadius.setFont(font)
        self.labelRadius.setObjectName("labelRadius")
        self.radius = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.radius.setGeometry(QtCore.QRect(190, 150, 201, 21))
        self.radius.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.radius.setObjectName("radius")
        self.pushMainC = QtWidgets.QPushButton(self.centralwidget)
        self.pushMainC.setGeometry(QtCore.QRect(140, 410, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushMainC.setFont(font)
        self.pushMainC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushMainC.setObjectName("pushMainC")
        self.numCircle = QtWidgets.QLabel(self.centralwidget)
        self.numCircle.setGeometry(QtCore.QRect(20, 290, 461, 121))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(96)
        self.numCircle.setFont(font)
        self.numCircle.setStyleSheet("font: 96pt \"American Typewriter\";\n"
"color:rgb(15, 128, 255)")
        self.numCircle.setAlignment(QtCore.Qt.AlignCenter)
        self.numCircle.setObjectName("numCircle")
        self.textCircle = QtWidgets.QLabel(self.centralwidget)
        self.textCircle.setGeometry(QtCore.QRect(20, 230, 461, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        self.textCircle.setFont(font)
        self.textCircle.setAlignment(QtCore.Qt.AlignCenter)
        self.textCircle.setWordWrap(True)
        self.textCircle.setObjectName("textCircle")
        self.groupBoxC = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxC.setGeometry(QtCore.QRect(50, 80, 401, 41))
        self.groupBoxC.setTitle("")
        self.groupBoxC.setObjectName("groupBoxC")
        self.radioAreaC = QtWidgets.QRadioButton(self.groupBoxC)
        self.radioAreaC.setGeometry(QtCore.QRect(70, 10, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioAreaC.setFont(font)
        self.radioAreaC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioAreaC.setChecked(False)
        self.radioAreaC.setObjectName("radioAreaC")
        self.radioPerimeterC = QtWidgets.QRadioButton(self.groupBoxC)
        self.radioPerimeterC.setGeometry(QtCore.QRect(230, 10, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioPerimeterC.setFont(font)
        self.radioPerimeterC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioPerimeterC.setChecked(True)
        self.radioPerimeterC.setObjectName("radioPerimeterC")
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
        WindowCircle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowCircle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 24))
        self.menubar.setObjectName("menubar")
        WindowCircle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowCircle)
        self.statusbar.setObjectName("statusbar")
        WindowCircle.setStatusBar(self.statusbar)

        self.retranslateUi(WindowCircle)
        QtCore.QMetaObject.connectSlotsByName(WindowCircle)

    def retranslateUi(self, WindowCircle):
        _translate = QtCore.QCoreApplication.translate
        WindowCircle.setWindowTitle(_translate("WindowCircle", "Circle"))
        self.labelCircle.setText(_translate("WindowCircle", "CIRCLE COMPUTATION"))
        self.pushMCircle.setText(_translate("WindowCircle", "Measure Shape"))
        self.labelRadius.setText(_translate("WindowCircle", "Radius :"))
        self.pushMainC.setText(_translate("WindowCircle", "Go Back"))
        self.numCircle.setText(_translate("WindowCircle", "0"))
        self.textCircle.setText(_translate("WindowCircle", "The _________ of the Circle is..."))
        self.radioAreaC.setText(_translate("WindowCircle", "Area"))
        self.radioPerimeterC.setText(_translate("WindowCircle", "Perimeter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowCircle = QtWidgets.QMainWindow()
    ui = Ui_WindowCircle()
    ui.setupUi(WindowCircle)
    WindowCircle.show()
    sys.exit(app.exec_())
