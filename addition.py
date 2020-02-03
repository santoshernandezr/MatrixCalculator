def makeMatrix():
    """
    This function asks the user to input their matrix
    :return: this function returns a list
    """
    rows = int(input("Please input the number of rows you'd like "))
    columns = int(input("Please input the number of columns you'd like (it has to be the same as your number of rows "))
    finalMatrix = []
    for i in range(rows):
        matrix = []
        for j in range(columns):
            matrix.append(int(input("Please enter the numbers in the rows of the matrix ")))
        finalMatrix.append(matrix)
    return finalMatrix


def matrixaddition():
    """
    This function adds matrices of same dimensions
    :return: this function returns a list
    """
    print("Please enter your first matrix ")
    firstMatrix = makeMatrix()
    print("Please enter your second matrix ")
    secondMatrix = makeMatrix()
    if len(firstMatrix) == len(secondMatrix):
        print(firstMatrix)
        print(secondMatrix)
        finalMatrix = []
        for i in range(len(firstMatrix)):
            matrix = []
            for j in range(len(secondMatrix[0])):
                sumNum = firstMatrix[i][j] + secondMatrix[i][j]
                matrix.append(sumNum)
                print(matrix)
            finalMatrix.append(matrix)
        print(finalMatrix)
    else:
        print("This operation cannot be done because the dimensions of the matrices are not the same. "
              "Try again :)")
        matrixaddition()


matrixaddition()
