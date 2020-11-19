def makeMatrix():
    """
    This function asks the user to input their matrix
    :return: this function returns a list
    """
    rows = int(input("Please input the number of rows you'd like "))
    print(rows)
    columns = int(input("Please input the number of columns you'd like (it has to be the same as your number of rows )"))
    print(columns)
    finalMatrix = []  # List that will include the complete matrix
    for i in range(rows):  # This for loop does a loop for the amount of rows there are
        matrix = []  # List that will contain the rows of the matrix
        for j in range(columns):  # This loop does a loop for the amount of columns there are
            matrix.append(int(input("Please enter the numbers in the rows of the matrix ")))  # This is appending the values the user is inputing
        finalMatrix.append(matrix)  # Appends each row of the matrix
    return finalMatrix


def matrixmultiplication():
    """
    This function adds matrices of same dimensions
    :return: this function returns a list
    """
    print("Please enter your first matrix ")
    firstMatrix = makeMatrix()  # The first matrix is created by the user
    print("This is your first matrix: " + str(firstMatrix))
    print("Please enter your second matrix (This matrixs columns should be the same as your rows in your first matrix ")
    secondMatrix = makeMatrix()  # The second matrix is created by the user
    print("This is your second matrix: "  + str(secondMatrix))
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
        print("This is our final Matrix :) " + str(finalMatrix))
    else:
        print("This operation cannot be done, make sure the rows of the first matrix is the same as the number of columns in the second matrix")
        matrixmultiplication()

matrixmultiplication()
