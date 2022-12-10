from PyQt5.QtWidgets import *
from GUIMain import *
from Circle import *
from Rectangle import *
from Triangle import *
from Square import *

# learn how to change color of GUI

class Shapes(QMainWindow, Ui_Main):
    '''
    STARTER WINDOW
        - Hub for all four shapes
        - Each button will move you to a diffrent window when clicked
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        '''
        When any shape button is clicked it will lead to function to open a new window of information
        '''
        self.buttonCircle.clicked.connect(lambda: self.bCircle())
        self.buttonRectangle.clicked.connect(lambda: self.bRectangle())
        self.buttonTriangle.clicked.connect(lambda: self.bTriangle())
        self.buttonSquare.clicked.connect(lambda: self.bSquare())
        print('car')

    def bCircle(self):
        '''
        ACTIONS ON THE SHAPE WINDOW
            - pushMain{SHAPE LETTER} will direct you to the main window and hide the SHAPE window
            -pushM{SHAPE} will go to class Measure{SHAPE LETTER} and calculate the amount to display
        '''
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowCircle()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.pushMainC.clicked.connect(lambda: self.goBack())
        self.ui.pushMCircle.clicked.connect(lambda: self.MeasureC())
        print('fish')

    def MeasureC(self):

        '''
            CIRCLE MEASUREMENTS PER & AREA
                - When clicking on shape needed from the main screen, it will lead into a new window
                - shows the perimeter and area radio buttons and an inout section which will computed
                - Try and Except statements for Value Errors and if there ia a negative or 0 input given
                - if statement made for correct inputs which will preform button task of area or perimeter
                - measure{SHAPE}  value will be displayed in num{SHAPE} and text{SHAPE} will change accordingly
        '''

        try: # --------------------------------- PERIMETER  ----------------------------------------------
            if self.ui.radioPerimeterC.isChecked():
                pi = 3.14
                radius = float(self.ui.radius.toPlainText())

                '''
                                If given an input of a zero or negative number there will be an error
                '''
                if float(radius) <= 0:  # Not a Zero Division Error (loop hole, unable to use custmized name)
                    print('phone')
                    raise ZeroDivisionError

                measureCircle = 2 * (pi * radius)  # perimeter
                measureCircle = "{:.2f}".format(measureCircle)
                self.ui.numCircle.setText(str(measureCircle))
                self.ui.textCircle.setText(str('The Perimeter of the Circle is...'))

        except (ValueError, TypeError, ZeroDivisionError):
            self.ui.textCircle.setText(str('ERROR : Type in positive numerical value(s) needed for the computation'))
            self.ui.numCircle.setText(str('ERROR'))

        try:  # --------------------------------- AREA ----------------------------------------------
            if self.ui.radioAreaC.isChecked():
                #  CIRCLE MEASUREMENTS AREA
                #  sets the amount and display text
                pi = 3.14
                radius = float(self.ui.radius.toPlainText())

                '''
                If given an input of a zero or negative number there will be an erro
                '''
                if float(radius) <= 0:  #Not a Zero Division Error (loop hole, unable to use custmized name)
                    print('phone')
                    raise ZeroDivisionError

                measureCircle = pi * (radius * radius)  # area
                measureCircle = "{:.2f}".format(measureCircle)
                print(measureCircle)
                self.ui.numCircle.setText(str(measureCircle))
                self.ui.textCircle.setText(str('The Area of the Circle is...'))
                print(measureCircle)

        except (ValueError, TypeError,ZeroDivisionError):
            self.ui.textCircle.setText(str('ERROR : Type in positive numerical value(s) needed for the computation'))
            self.ui.numCircle.setText(str('ERROR'))

    def bRectangle(self):
        '''
            ACTIONS ON THE SHAPE WINDOW
                - pushMain{SHAPE LETTER} will direct you to the main window and hide the SHAPE window
                -pushM{SHAPE} will go to class Measure{SHAPE LETTER} and calculate the amount to display
        '''
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowRectangle()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.pushMainR.clicked.connect(lambda: self.goBack())
        self.ui.pushMRectangle.clicked.connect(lambda: self.MeasureR())
        print('dog')

    def MeasureR(self):
        # RECTANGLE INPUTS
        '''
            RECTANGLE MEASUREMENTS PER & AREA
                - When clicking on shape needed from the main screen, it will lead into a new window
                - shows the perimeter and area radio buttons and an inout section which will computed
                - Try and Except statements for Value Errors and if there ia a negative or 0 input given
                - if statement made for correct inputs which will preform button task of area or perimeter
                - measure{SHAPE}  value will be displayed in num{SHAPE} and text{SHAPE} will change accordingly
        '''

        try: # --------------------------------- PERIMETER ----------------------------------------------
            if self.ui.radioPerimeterR.isChecked():
                length = float(self.ui.length.toPlainText())
                width = float(self.ui.width.toPlainText())
                #  RECTANGLE MEASUREMENTS PER
                measureRectangle = 2 * (length + width)

                if float(length) <= 0:  #Not a Zero Division Error (loop hole, unable to use custmized name)
                    raise ZeroDivisionError
                elif float(width) <= 0:  #Not a Zero Division Error (loop hole, unable to use custmized name)
                    raise ZeroDivisionError

                measureRectangle = "{:.2f}".format(measureRectangle)
                self.ui.numRectangle.setText(str(measureRectangle))
                self.ui.textRectangle.setText(str('The Perimeter of the Rectangle is...'))


        except (ValueError, TypeError, ZeroDivisionError):
            self.ui.textRectangle.setText(str('ERROR : Type in positive numerical value(s) needed for the computation'))
            self.ui.numRectangle.setText(str('ERROR'))

        try: # --------------------------------- AREA ----------------------------------------------
            if self.ui.radioAreaR.isChecked():
                length = float(self.ui.length.toPlainText())
                width = float(self.ui.width.toPlainText())
                measureRectangle = length * width

                if float(length) <= 0:  # Not a Zero Division Error (loop hole, unable to use custmized name)
                    raise ZeroDivisionError
                elif float(width) <= 0:  # Not a Zero Division Error (loop hole, unable to use custmized name)
                    raise ZeroDivisionError

                measureRectangle = "{:.2f}".format(measureRectangle)
                self.ui.numRectangle.setText(str(measureRectangle))
                self.ui.textRectangle.setText(str('The Area of the Rectangle is...'))

        except (ValueError, TypeError, ZeroDivisionError):
            self.ui.textRectangle.setText(str('ERROR : Type in positive numerical value(s) needed for the computation'))
            self.ui.numRectangle.setText(str('ERROR'))

    def bTriangle(self):
        '''
            ACTIONS ON THE SHAPE WINDOW
                - pushMain{SHAPE LETTER} will direct you to the main window and hide the SHAPE window
                -pushM{SHAPE} will go to class Measure{SHAPE LETTER} and calculate the amount to display
        '''
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowTriangle()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.pushMainT.clicked.connect(lambda: self.goBack())
        self.ui.pushMTriangle.clicked.connect(lambda: self.MeasureT())

    def MeasureT(self):
        #  TRIANGLE INPUTS
        '''
            TRIANGLE MEASUREMENTS PER & AREA
                - When clicking on shape needed from the main screen, it will lead into a new window
                - shows the perimeter and area radio buttons and an inout section which will computed
                - Try and Except statements for Value Errors and if there ia a negative or 0 input given
                - if statement made for correct inputs which will preform button task of area or perimeter
                - measure{SHAPE}  value will be displayed in num{SHAPE} and text{SHAPE} will change accordingly
        '''


        try: # --------------------------------- PERIMETER ----------------------------------------------
            if self.ui.radioPerimeterT.isChecked():
                side1 = float(self.ui.side1.toPlainText())
                side2 = float(self.ui.side2.toPlainText())
                side3 = float(self.ui.side3.toPlainText())

                if float(side1) <= 0:  #Not a Zero Division Error (loop hole, unable to use custmized name)
                    raise ZeroDivisionError
                elif float(side2) <= 0:  #Not a Zero Division Error (loop hole, unable to use custmized name)
                    raise ZeroDivisionError
                elif float(side3) <= 0:  #Not a Zero Division Error (loop hole, unable to use custmized name)
                    raise ZeroDivisionError

                #  CIRCLE MEASUREMENTS PER
                measureTriangle = (side1 + side2 + side3)  # perimeter
                measureTriangle = "{:.2f}".format(measureTriangle)
                self.ui.numTriangle.setText(str(measureTriangle))
                self.ui.textTriangle.setText(str('The Perimeter of the Triangle is...'))


        except (ValueError, TypeError, ZeroDivisionError):
            self.ui.textTriangle.setText(str('ERROR : Type in positive numerical value(s) needed for the computation'))
            self.ui.numTriangle.setText(str('ERROR'))

        try: #--------------------------------- AREA ----------------------------------------------

            if self.ui.radioAreaT.isChecked():
                base = float(self.ui.base.toPlainText())
                height = float(self.ui.height.toPlainText())

                if float(base) <= 0:  #Not a Zero Division Error (loop hole, unable to use custmized name)
                    raise ZeroDivisionError
                elif float(height) <= 0:  #Not a Zero Division Error (loop hole, unable to use custmized name)
                    raise ZeroDivisionError

                #  CIRCLE MEASUREMENTS AREA
                measureTriangle = 0.5 * (base * height)  # area
                measureTriangle = "{:.2f}".format(measureTriangle)
                self.ui.numTriangle.setText(str(measureTriangle))
                self.ui.textTriangle.setText(str('The Area of the Triangle is...'))

        except (ValueError, TypeError, ZeroDivisionError):
            self.ui.textTriangle.setText(str('ERROR : Type in positive numerical value(s) needed for the computation'))
            self.ui.numTriangle.setText(str('ERROR'))

    def bSquare(self):
        '''
            ACTIONS ON THE SHAPE WINDOW
                - pushMain{SHAPE LETTER} will direct you to the main window and hide the SHAPE window
                -pushM{SHAPE} will go to class Measure{SHAPE LETTER} and calculate the amount to display
        '''
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowSquare()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.pushMainS.clicked.connect(lambda: self.goBack())
        self.ui.pushMSquare.clicked.connect(lambda: self.MeasureS())

    def MeasureS(self):
        #  SQUARE INPUTS
        '''
            SQUARE MEASUREMENTS PER & AREA
                - When clicking on shape needed from the main screen, it will lead into a new window
                - shows the perimeter and area radio buttons and an inout section which will computed
                - Try and Except statements for Value Errors and if there ia a negative or 0 input given
                - if statement made for correct inputs which will preform button task of area or perimeter
                - measure{SHAPE}  value will be displayed in num{SHAPE} and text{SHAPE} will change accordingly
        '''


        try: #--------------------------------- PERIMETER ----------------------------------------------
            if self.ui.radioPerimeterS.isChecked():
                sides = float(self.ui.sides.toPlainText())
                #  SQUARE MEASUREMENTS PER

                if float(sides) <= 0:  #Not a Zero Division Error (loop hole, unable to use custmized name)
                    raise ZeroDivisionError

                measureSquare = 4 * sides  # perimeter
                measureSquare = "{:.2f}".format(measureSquare)
                self.ui.numSquare.setText(str(measureSquare))
                self.ui.textSquare.setText(str('The Perimeter of the Square is...'))


        except (ValueError, TypeError, ZeroDivisionError):
            self.ui.textSquare.setText(str('ERROR : Type in positive numerical value(s) needed for the computation'))
            self.ui.numSquare.setText(str('ERROR'))

        try: #--------------------------------- AREA ----------------------------------------------
            if self.ui.radioAreaS.isChecked():
                sides = float(self.ui.sides.toPlainText())
                #  SQUARE MEASUREMENTS AREA

                if float(sides) <= 0:  #Not a Zero Division Error (loop hole, unable to use custmized name)
                    raise ZeroDivisionError

                measureSquare = sides * sides  # area
                measureSquare = "{:.2f}".format(measureSquare)
                self.ui.numSquare.setText(str(measureSquare))
                self.ui.textSquare.setText(str('The Area of the Square is...'))

        except (ValueError, TypeError, ZeroDivisionError):
            self.ui.textSquare.setText(str('ERROR : Type in positive numerical value(s) needed for the computation'))
            self.ui.numSquare.setText(str('ERROR'))

    def goBack(self):
        '''
        GOES BACK TO MAIN WINDOW WHILE CLOSING THE SHAPE WINDOW
            - All shape windows will lead back to the main window
            - code to go to this class are all listed in class b{SHAPE}
            - THIS CODE ALSO ALLOWS THE CODE TO 'LOOP' AND RE-CLICK ALL BUTTONS WHEN GOING BACK TO THE MAIN
        '''
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.buttonCircle.clicked.connect(lambda: self.bCircle())
        self.ui.buttonRectangle.clicked.connect(lambda: self.bRectangle())
        self.ui.buttonTriangle.clicked.connect(lambda: self.bTriangle())
        self.ui.buttonSquare.clicked.connect(lambda: self.bSquare())

#  Made by Nia L. and Riley F.