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
from MatrixClass import Matrices


class MainWindow(Screen):
    pass

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
            makeMatrix(int(self.colsMatrix1.text), int(self.rowsMatrix1.text), "Add")

        print(self.colsMatrix1.text, self.rowsMatrix1.text, self.colsMatrix2.text, self.rowsMatrix2.text)
        self.colsMatrix1.text = ""
        self.rowsMatrix1.text = ""
        self.colsMatrix2.text = ""
        self.rowsMatrix2.text = ""

class TransposeWindow(Screen):
    transCols = ObjectProperty(None)
    transRows = ObjectProperty(None)

    def makeTransposeGrid(self):
        if self.transCols.text == "" or self.transRows.text == "":
            errorModal('You left something blank. Please fill everything out.')
        else:
            makeMatrix(int(self.transCols.text), int(self.transRows.text), "Transpose")

        print(self.transCols.text, self.transRows.text)
        self.transCols.text = ""
        self.transRows.text = ""

class InverseWindow(Screen):
    invCols = ObjectProperty(None)
    invRows = ObjectProperty(None)

    def makeInvGrid(self):
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
        makeMatrix(int(self.reduceCols.text), int(self.reduceRows.text), "Row Reduce")
        print(self.reduceCols.text, self.reduceRows.text)
        self.reduceCols.text = ""
        self.reduceRows.text = ""

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

def getText(userInputs, myCols, myRows, operation):
    matrix = []
    for nums in userInputs:
        if nums.text == "":
            break
        else:
            matrix.append(int(nums.text))
        print("This is the text: ", nums.text)
    print("This is my matrix: ", matrix)
    print("This is the length of the matrix: ", len(matrix))
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
    userInputs = []
    layout = GridLayout(cols = 1)
    inside = GridLayout(cols = myCols)
    for i in range(myRows * myCols):
        gridNums = TextInput(text = "", id = str(i))
        userInputs.append(gridNums)
        inside.add_widget(gridNums)
    
    print("This is the list: ", userInputs)

    layout.add_widget(inside)

    closeBtn = Button(text = operation, size_hint = (1, 0.3))
    closeBtn.bind(on_press = lambda x: getText(userInputs, myCols, myRows, operation))
    layout.add_widget(closeBtn)

    box = BoxLayout(orientation = "horizontal")
    box.add_widget(layout)

    popupWindow = Popup(title = "Your first Matrix", content = box, auto_dismiss = True,
                        size_hint = (None, None), size = (400, 400))

    popupWindow.open()

def errorModal(msg):
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