from sympy import Matrix
import numpy as np

class Matrices:
    def __init__(self, myMatrix, columns, rows):

        self.rows = rows
        self.columns = columns
        self.Matrix = []
        self.Transpose = []
        self.Inverse = []
        self.RowReduced = []
        
        columns = []
        for i in range(1, len(myMatrix) + 1):
            if i % self.columns == 0:
                columns.append(myMatrix[i-1])
                self.Matrix.append(columns)
                columns = []
            else:
                columns.append(myMatrix[i-1])
        
        print("This is my matrix: ", self.Matrix)
        
    def transpose(self):
        """
        This function returns the transpose of the Matrix that the user created
        """
        for i in range(self.columns): # This for loop makes the rows we need in our transposed matrix
            matrix = [] # List that will contain the rows of the transpose matrix
            for j in range(self.rows): # This for loop makes the columns we need in our transposed matrix
                    matrix.append(self.Matrix[j][i]) 
            self.Transpose.append(matrix) # Appending the rows into the bigger list we created

        return self.Transpose
        
    def inverse(self):
        """ 
        This will find return the inverse of the users matrix if there is one
        """
        myMatrix = np.array(self.Matrix)
        if np.linalg.det(myMatrix) == 0:
            # print("This matrix has a determinant of 0, meaning it has no inverse")
            return "Determinant"
        else:
            self.Inverse = np.linalg.inv(myMatrix)
        return self.Inverse

    def rowReduce(self):
        """
        This function will return the row reduceed form of the users matrix
        """
        myMatrix = Matrix(self.Matrix)
        myMatrix = myMatrix.rref()
        print("This is the row reduced echelon form of your matrix: \n", myMatrix)
        return myMatrix[0]
        
def matrixAddition(firstMatrix, secondMatrix):
    """
    This function adds matrices of same dimensions
    :return: this function returns a list
    """
    additionMatrix = []  # Vector that will contain the full matrix
    for i in range(len(firstMatrix)):  # Will through each row in the matrix
        matrix = []  # Vector that will get all the rows in the matrix
        for j in range(len(secondMatrix[0])):  # Will go through each column
            sumNum = firstMatrix[i][j] + secondMatrix[i][j]  # Will add each individual cell
            matrix.append(sumNum)
            print(matrix)
        additionMatrix.append(matrix)
    return additionMatrix

def matrixSubtraction(firstMatrix, secondMatrix):
    """
    This function subtracts matrices of same dimensions
    :return: this function returns a list
    """
    subtractionMatrix = []  # Vector that will contain the full matrix
    for i in range(len(firstMatrix)):  # Will through each row in the matrix
        matrix = []  # Vector that will get all the rows in the matrix
        for j in range(len(secondMatrix[0])):  # Will go through each column
            sumNum = firstMatrix[i][j] - secondMatrix[i][j]  # Will add each individual cell
            matrix.append(sumNum)
            print(matrix)
        subtractionMatrix.append(matrix)
    return subtractionMatrix

def matrixMultiplication(firstMatrix, secondMatrix):
    """
    This function adds matrices of same dimensions
    :return: this function returns a list
    """
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
    return finalMatrix