from sympy import Matrix
import numpy as np

class Matrices:
    def __init__(self, columns, rows):

        self.rows = rows
        self.columns = columns
        self.Matrix = []
        self.Transpose = []
        self.Inverse = []
        self.RowReduced = []
        
        for i in range(self.rows):  # This for loop does a loop for the amount of rows there are
            matrix = []  # List that will contain the rows of the matrix
            for j in range(self.columns):  # This loop does a loop for the amount of columns there are
                columnNum = int(input("Please enter the " + str(j + 1) + "st/nd/rd/th number of row " + str(i + 1) + " in the matrix "))
                matrix.append(columnNum)  # This is appending the values the user is inputing
            self.Matrix.append(matrix)  # Appends each row of the matrix
        print(self.Matrix)
        
    def transpose(self):
        """
        This function returns the transpose of the Matrix that the user created
        """
        for i in range(self.columns): # This for loop makes the rows we need in our transposed matrix
            matrix = [] # List that will contain the rows of the transpose matrix
            for j in range(self.rows): # This for loop makes the columns we need in our transposed matrix
                    matrix.append(self.Matrix[j][i]) 
            self.Transpose.append(matrix) # Appending the rows into the bigger list we created
        print("This is your transposed matrix: ", self.Transpose)
        
    def inverse(self):
        """ 
        This will find return the inverse of the users matrix if there is one
        """
        myMatrix = np.array(self.Matrix)
        if np.linalg.det(myMatrix) == 0:
            print("This matrix has a determinant of 0, meaning it has no inverse")
        else:
            self.Inverse = np.linalg.inv(myMatrix)
            print("This is the inverse to your matrix: ", self.Inverse)

    def rowReduce(self):
        """
        This function will row reduce the users matrix
        """
        myMatrix = Matrix(self.Matrix)
        print("This is the row reduced echelon form of your matrix: \n", myMatrix.rref())
        
def matrixAddition(firstMatrix, secondMatrix):
    """
    This function adds matrices of same dimensions
    :return: this function returns a list
    """
    if len(firstMatrix) == len(secondMatrix):  # Checks whether the matrices can be added or not
        print(firstMatrix)
        print(secondMatrix)
        additionMatrix = []  # Vector that will contain the full matrix
        for i in range(len(firstMatrix)):  # Will through each row in the matrix
            matrix = []  # Vector that will get all the rows in the matrix
            for j in range(len(secondMatrix[0])):  # Will go through each column
                sumNum = firstMatrix[i][j] + secondMatrix[i][j]  # Will add each individual cell
                matrix.append(sumNum)
                print(matrix)
            additionMatrix.append(matrix)
        print("The sum of the two matrices is: " + str(additionMatrix))
    else:
        print("This operation cannot be done because the dimensions of the matrices are not the same. "
            "Try again :)")

def matrixSubtraction(firstMatrix, secondMatrix):
    """
    This function subtracts matrices of same dimensions
    :return: this function returns a list
    """
    if len(firstMatrix) == len(secondMatrix):  # Checks whether the matrices can be subtracted or not
        print(firstMatrix)
        print(secondMatrix)
        subtractionMatrix = []  # Vector that will contain the full matrix
        for i in range(len(firstMatrix)):  # Will through each row in the matrix
            matrix = []  # Vector that will get all the rows in the matrix
            for j in range(len(secondMatrix[0])):  # Will go through each column
                sumNum = firstMatrix[i][j] - secondMatrix[i][j]  # Will add each individual cell
                matrix.append(sumNum)
                print(matrix)
            subtractionMatrix.append(matrix)
        print("The difference of the two matrices is: " + str(subtractionMatrix))
    else:
        print("This operation cannot be done because the dimensions of the matrices are not the same. "
            "Try again :)")

def matrixMultiplication(firstMatrix, secondMatrix):
    """
    This function adds matrices of same dimensions
    :return: this function returns a list
    """
    if len(firstMatrix[0]) == len(secondMatrix):  # Checks whether the matrices can be multiplied or not or not
        finalMatrix = []
        for y in range(len(firstMatrix)): # 2
            currentMatrix = []
            for i in range(len(secondMatrix[0])):
                currentSum = 0
                for j in range(len(secondMatrix)):
                    currentSum += secondMatrix[j][i] * firstMatrix[y][j]
                currentMatrix.append(currentSum)
                print("This is my current matrix: " + str(currentMatrix))
            finalMatrix.append(currentMatrix)
        print("This product of the two matrices is :) " + str(finalMatrix))
    else:
        print("This operation cannot be done, make sure the rows of the first matrix is the same as the number of columns in the second matrix")

# first = Matrices(3, 2)
# second = Matrices(4, 3)

# matrixMultiplication(first.Matrix, second.Matrix)
# # first.inverse()


def main():
    operation = input("What operation would you like to do today? \n (Addition, Subtraction, Multiplication, Row Reduce, Transpose, Inverse) ")
    if operation == "Row Reduce" or operation == "Transpose" or operation == "Inverse":
        columns = int(input("Number of columns? "))
        rows = int(input("Number of rows? "))
        first = Matrices(columns, rows)
        first.Matrix
        if operation == "Row Reduce":
            first.rowReduce()
        elif operation == "Transpose":
            first.transpose()
        else:
            first.inverse()
    else:
        columns = int(input("Number of columns for your first Matrix? "))
        rows = int(input("Number of rows for your first Matrix? "))
        first = Matrices(columns, rows)
        print("This is your first Matrix: ", first.Matrix)
        columns2 = int(input("Number of columns for your second Matrix? "))
        rows2 = int(input("Number of rows for your second Matrix? "))
        second = Matrices(columns2, rows2)
        print("This is your second Matrix: ", second.Matrix)
        if operation == "Addition":
            matrixAddition(first, second)
        elif operation == "Subtraction":
            matrixSubtraction(first, second)
        else:
            matrixMultiplication(first, second)

main()