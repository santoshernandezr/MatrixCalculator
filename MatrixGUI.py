from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from MatrixClass import Matrices, matrixAddition, matrixSubtraction, matrixMultiplication


class MainWindow(Screen):
    pass

class TransposeWindow(Screen):
    transCols = ObjectProperty(None)
    transRows = ObjectProperty(None)

    def makeTransposeGrid(self):
        """ 
        This function will make the Transposed Grid and check if the user left something blank.
        If they do it will warn them, if not it will call makeMatrix 
        """
        if self.transCols.text == "" or self.transRows.text == "":
            errorModal('You left something blank. Please fill everything out.')
        else:
            makeMatrix(int(self.transCols.text), int(self.transRows.text), "Transpose")
    
        self.transCols.text = ""
        self.transRows.text = ""

class InverseWindow(Screen):
    invCols = ObjectProperty(None)
    invRows = ObjectProperty(None)

    def makeInvGrid(self):
        """
        This function will make the Inverse Grid and check if the user left something blank or if the matrix is not a square matrix.
        If something is blank or it's not a square matrix then it will warn them. If everything is fine then it will call makeMatrix
        """
        if self.invCols.text == "" or self.invRows.text == "":
            errorModal('You left something blank. Please fill everything out.')
        elif int(self.invCols.text) != int(self.invRows.text):
            errorModal('This is not a square matrix, so this matrix has no inverse.')
        else:
            makeMatrix(int(self.invCols.text), int(self.invRows.text), "Invert")

        print(self.invCols.text, self.invRows.text)
        self.invCols.text = ""
        self.invRows.text = ""

class RowReduceWindow(Screen):
    reduceCols = ObjectProperty(None)
    reduceRows = ObjectProperty(None)

    def makeRowReduceGrid(self):
        """
        This function will make the Row Reduce Grid.
        """
        makeMatrix(int(self.reduceCols.text), int(self.reduceRows.text), "Row Reduce")
        print(self.reduceCols.text, self.reduceRows.text)
        self.reduceCols.text = ""
        self.reduceRows.text = ""

class AdditionWindow(Screen):
    colsMatrix1 = ObjectProperty(None)
    rowsMatrix1 = ObjectProperty(None)
    colsMatrix2 = ObjectProperty(None)
    rowsMatrix2 = ObjectProperty(None)

    def makeAddGrid(self):
        if self.colsMatrix1.text == "" or self.rowsMatrix1.text == "" or self.colsMatrix2.text == "" or self.rowsMatrix2.text == "":
            errorModal('You left something blank. Please fill everything out.')
        elif int(self.colsMatrix1.text) != int(self.colsMatrix2.text) or int(self.rowsMatrix1.text) != int(self.rowsMatrix2.text):
            errorModal('In order to add matrices they have to be the same \ndimension. Re-enter new dimensions.')
        else:
            makeDoubleMatrix(None, int(self.colsMatrix1.text), int(self.rowsMatrix1.text), None, None, "First Matrix", True, False, False)

        print(self.colsMatrix1.text, self.rowsMatrix1.text, self.colsMatrix2.text, self.rowsMatrix2.text)
        self.colsMatrix1.text = ""
        self.rowsMatrix1.text = ""
        self.colsMatrix2.text = ""
        self.rowsMatrix2.text = ""

class SubtractionWindow(Screen):
    colsMatrix1 = ObjectProperty(None)
    rowsMatrix1 = ObjectProperty(None)
    colsMatrix2 = ObjectProperty(None)
    rowsMatrix2 = ObjectProperty(None)

    def makeSubGrid(self):
        if self.colsMatrix1.text == "" or self.rowsMatrix1.text == "" or self.colsMatrix2.text == "" or self.rowsMatrix2.text == "":
            errorModal('You left something blank. Please fill everything out.')
        elif int(self.colsMatrix1.text) != int(self.colsMatrix2.text) or int(self.rowsMatrix1.text) != int(self.rowsMatrix2.text):
            errorModal('In order to subtract matrices they have to be the same \ndimension. Re-enter new dimensions.')
        else:
            makeDoubleMatrix(None, int(self.colsMatrix1.text), int(self.rowsMatrix1.text), None, None, "First Matrix", False, True, False)

        print(self.colsMatrix1.text, self.rowsMatrix1.text, self.colsMatrix2.text, self.rowsMatrix2.text)
        self.colsMatrix1.text = ""
        self.rowsMatrix1.text = ""
        self.colsMatrix2.text = ""
        self.rowsMatrix2.text = ""

class MultiplicationWindow(Screen):
    colsMatrix1 = ObjectProperty(None)
    rowsMatrix1 = ObjectProperty(None)
    colsMatrix2 = ObjectProperty(None)
    rowsMatrix2 = ObjectProperty(None)

    def makeMultGrid(self):
        if self.colsMatrix1.text == "" or self.rowsMatrix1.text == "" or self.colsMatrix2.text == "" or self.rowsMatrix2.text == "":
            errorModal('You left something blank. Please fill everything out.')
        elif int(self.colsMatrix1.text) != int(self.rowsMatrix2.text):
            errorModal("The columns of the first matrix has to be equal \nto the rows in the second Matrix.")
        else:
            makeDoubleMatrix(None, int(self.colsMatrix1.text), int(self.rowsMatrix1.text), int(self.colsMatrix2.text), int(self.rowsMatrix2.text), "First Matrix", False, False, True)

        print(self.colsMatrix1.text, self.rowsMatrix1.text, self.colsMatrix2.text, self.rowsMatrix2.text)
        self.colsMatrix1.text = ""
        self.rowsMatrix1.text = ""
        self.colsMatrix2.text = ""
        self.rowsMatrix2.text = ""

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

def makeDoubleMatrix(matrix, myCols, myRows, myCols1, myRows1, operation, add, sub, mult):
    """ 
    This function will take in the users input of columns, rows, and the operation they are doing. 
    It will make a grid that will represent the Matrix and allow the user to input their matrix.
    """
    if mult == True:
        if operation == "First Matrix":
            userInputs = []
            layout = GridLayout(cols = 1)
            inside = GridLayout(cols = myCols)
            for i in range(myRows * myCols):
                gridNums = TextInput(text = "")
                userInputs.append(gridNums)
                inside.add_widget(gridNums)
        else:
            userInputs = []
            layout = GridLayout(cols = 1)
            inside = GridLayout(cols = myCols1)
            for i in range(myRows1 * myCols1):
                gridNums = TextInput(text = "")
                userInputs.append(gridNums)
                inside.add_widget(gridNums)
    else: 
        userInputs = []
        layout = GridLayout(cols = 1)
        inside = GridLayout(cols = myCols)
        for i in range(myRows * myCols):
            gridNums = TextInput(text = "")
            userInputs.append(gridNums)
            inside.add_widget(gridNums)

    layout.add_widget(inside)
    closeBtn = Button(text = operation, size_hint = (1, 0.3))

    if add == True:
        if operation == "First Matrix":
            closeBtn.bind(on_press = lambda x: getDoubleMatrix(userInputs, myCols, myRows, myCols1, myRows1, None, operation, True, False, False))
        else:
            closeBtn.bind(on_press = lambda x: getDoubleMatrix(userInputs, myCols, myRows, myCols1, myRows1, matrix, operation, True, False, False))
    elif sub == True:
        if operation == "First Matrix":
            closeBtn.bind(on_press = lambda x: getDoubleMatrix(userInputs, myCols, myRows, myCols1, myRows1, None, operation, False, True, False))
        else:
            closeBtn.bind(on_press = lambda x: getDoubleMatrix(userInputs, myCols, myRows, myCols1, myRows1, matrix, operation, False, True, False))
    elif mult == True:
        if operation == "First Matrix":
            closeBtn.bind(on_press = lambda x: getDoubleMatrix(userInputs, myCols, myRows, myCols1, myRows1, None, operation, False, False, True))
        else:
            closeBtn.bind(on_press = lambda x: getDoubleMatrix(userInputs, myCols, myRows, myCols1, myRows1, matrix, operation, False, False, True))

    layout.add_widget(closeBtn)
    box = BoxLayout(orientation = "horizontal")
    box.add_widget(layout)
    popupWindow = Popup(title = "Your first Matrix", content = box, auto_dismiss = True,
                        size_hint = (None, None), size = (400, 400))
    popupWindow.open()

def getDoubleMatrix(userInputs, myCols, myRows, myCols1, myRows1, secondMatrix, operation, add, sub, mult):
    """ 
    This function will iterate through the users inputs and make a matrix so we can do operations.
    This function will only take care of the following operations: addition, subtraction, and multiplication.
    If the user left something blank it will warn them and they will get the oportunity to go back and change their matrix.
    """
    matrix = []
    for nums in userInputs:
        if nums.text == "":
            break
        else:
            matrix.append(int(nums.text))
    if mult == True:
        if secondMatrix == None:
            if len(matrix) != (myCols * myRows):
                errorModal('You left something blank. Please fill everything out.')
            else:
                makeDoubleMatrix(matrix, myCols, myRows, myCols1, myRows1, "Multiply", False, False, True)
        else:
            if len(matrix) != (myCols1 * myRows1):
                errorModal('You left something blank. Please fill everything out.')
            else:
                first = Matrices(secondMatrix, myCols, myRows)
                second = Matrices(matrix, myCols1, myRows1)
                getResult(myCols1, myRows, matrixMultiplication(first.Matrix, second.Matrix))
    else:
        if len(matrix) != (myCols * myRows):
            errorModal('You left something blank. Please fill everything out.')
        else:
            if add == True:
                if operation == "First Matrix":
                    makeDoubleMatrix(matrix, myCols, myRows, None, None, "Add", True, False, False)
                else:
                    first = Matrices(secondMatrix, myCols, myRows)
                    second = Matrices(matrix, myCols, myRows)
                    getResult(myCols, myRows, matrixAddition(first.Matrix, second.Matrix))
            
            if sub == True:
                if operation == "First Matrix":
                    makeDoubleMatrix(matrix, myCols, myRows, None, None, "Subtract", False, True, False)
                else:
                    first = Matrices(secondMatrix, myCols, myRows)
                    second = Matrices(matrix, myCols, myRows)
                    getResult(myCols, myRows, matrixSubtraction(first.Matrix, second.Matrix))

def getMatrix(userInputs, myCols, myRows, operation):
    """ 
    This function will iterate through the users inputs and make a matrix so we can do operations.
    This function will only take care of the following operations: transpose, inverse, Row Reduction.
    If the user left something blank it will warn them and they will get the oportunity to go back and change their matrix.
    """
    matrix = []
    for nums in userInputs:
        if nums.text == "":
            break
        else:
            matrix.append(int(nums.text))
    if len(matrix) != (myCols * myRows):
        errorModal('You left something blank. Please fill everything out.')
    else:
        first = Matrices(matrix, myCols, myRows)
        if operation == "Transpose":
            getResult(myCols, myRows, first.transpose())
        elif operation == "Invert":
            if first.inverse() == "Determinant":
                errorModal('The determinant is 0, so this matrix has no inverse')
            else: 
                getResult(myCols, myRows, first.inverse())
        elif operation == "Row Reduce":
            myMatrix = first.rowReduce()
            tempMatrix = []
            mainMatrix = []
            for i in range(1, len(myMatrix) + 1):
                if i % myCols == 0:
                    tempMatrix.append(int(myMatrix[i-1]))
                    mainMatrix.append(tempMatrix)
                    tempMatrix = []
                else:
                    tempMatrix.append(int(myMatrix[i-1]))
            getResult(myCols, myRows, mainMatrix)

def getResult(myCols, myRows, myMatrix):
    """
    This function will make the popup with the results of whatever operation they did
    """
    layout = GridLayout(cols = 1)
    inside = GridLayout(cols = myCols)
    for matrix in myMatrix:
        for nums in matrix:
            gridNums = Label(text = str(format(nums, '.2f')))
            inside.add_widget(gridNums)

    layout.add_widget(inside)
    closeBtn = Button(text = "Close", size_hint = (1, 0.3))
    layout.add_widget(closeBtn)

    box = BoxLayout(orientation = "horizontal")
    box.add_widget(layout)

    popupWindow = Popup(title = "Your first Matrix", content = box, auto_dismiss = True,
                        size_hint = (None, None), size = (400, 400))

    closeBtn.bind(on_press = popupWindow.dismiss)
    popupWindow.open()

def makeMatrix(myCols, myRows, operation):
    """ 
    This function will take in the users input of columns, rows, and the operation they are doing. 
    It will make a grid that will represent the Matrix and allow the user to input their matrix.
    """
    userInputs = []
    layout = GridLayout(cols = 1)
    inside = GridLayout(cols = myCols)
    for i in range(myRows * myCols):
        gridNums = TextInput(text = "")
        userInputs.append(gridNums)
        inside.add_widget(gridNums)
    
    print("This is the list: ", userInputs)

    layout.add_widget(inside)

    closeBtn = Button(text = operation, size_hint = (1, 0.3))
    closeBtn.bind(on_press = lambda x: getMatrix(userInputs, myCols, myRows, operation))
    layout.add_widget(closeBtn)

    box = BoxLayout(orientation = "horizontal")
    box.add_widget(layout)

    popupWindow = Popup(title = "Your first Matrix", content = box, auto_dismiss = True,
                        size_hint = (None, None), size = (400, 400))

    popupWindow.open()

def errorModal(msg):
    """
    This function will make a popup with the message of the users choice
    """
    box = BoxLayout(orientation = "vertical")
    box.add_widget(Label(text = msg))
    closeBtn = Button(text = 'Close', size_hint = (1, 0.3))
    box.add_widget(closeBtn)
    popupWindow = Popup(title = "Oops!", content = box, auto_dismiss = False,
                        size_hint = (None, None), size = (400, 400))
    closeBtn.bind(on_press = popupWindow.dismiss)
    popupWindow.open()

kv = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    app = MainApp()
    app.run()