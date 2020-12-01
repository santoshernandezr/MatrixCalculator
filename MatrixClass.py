class Matrix:
    def __init__(self, columns, rows):

        self.rows = rows
        self.columns = columns
        self.Matrix = []
        self.Transpose = []
        
        for i in range(self.rows):  # This for loop does a loop for the amount of rows there are
            matrix = []  # List that will contain the rows of the matrix
            for j in range(self.columns):  # This loop does a loop for the amount of columns there are
                columnNum = int(input("Please enter the " + str(j + 1) + "st/nd/rd/th number of row " + str(i + 1) + " in the matrix "))
                matrix.append(columnNum)  # This is appending the values the user is inputing
            self.Matrix.append(matrix)  # Appends each row of the matrix
        print("This is your Matrix: ", self.Matrix)
        
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

def matrixMultiplication(firstMatrix, secondMatrix):
    """
    This function adds matrices of same dimensions
    :return: this function returns a list
    """
    if len(firstMatrix[0]) == len(secondMatrix):  # Checks whether the matrices can be multiplied or not or not
        finalMatrix = []
        for y in range(len(firstMatrix)): # 2
            currentMatrix = []
            for i in range(len(firstMatrix)):
                currentSum = 0
                for j in range(len(secondMatrix)):
                    currentSum += secondMatrix[j][y] * firstMatrix[i][j]
                currentMatrix.append(currentSum)
                print("This is my current matrix: " + str(currentMatrix))
            finalMatrix.append(currentMatrix)
        print("This product of the two matrices is :) " + str(finalMatrix))
    else:
        print("This operation cannot be done, make sure the rows of the first matrix is the same as the number of columns in the second matrix")

print("This is your First Matrix")
first = Matrix(3, 2)
first.transpose()

# print("This is your Second Matrix")
# second = Matrix(3, 3)
# print("This is first.Matrix ", first.Matrix)
# print("This is second.Matrix ", second.Matrix)
# matrixAddition(first.Matrix, second.Matrix)
# matrixMultiplication(first.Matrix, second.Matrix)