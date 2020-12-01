def makeMatrix():
    """
    This function asks the user to input their matrix
    :return: this function returns a list
    """
    rows = int(input("Please input the number of rows you'd like "))
    columns = int(input("Please input the number of columns you'd like (it has to be the same as your number of rows) "))
    finalMatrix = []  # List that will include the complete matrix
    for i in range(rows):  # This for loop does a loop for the amount of rows there are
        matrix = []  # List that will contain the rows of the matrix
        for j in range(columns):  # This loop does a loop for the amount of columns there are
            columnNum = int(input("Please enter the first " + str(j) + " numbers of row " + str(i + 1) + " in the matrix "))
            matrix.append(columnNum)  # This is appending the values the user is inputing
        finalMatrix.append(matrix)  # Appends each row of the matrix
    return finalMatrix


def matrixaddition():
    """
    This function adds matrices of same dimensions
    :return: this function returns a list
    """
    print("Please enter your first matrix ")
    firstMatrix = makeMatrix()  # The first matrix is created by the user
    print("Please enter your second matrix ")
    secondMatrix = makeMatrix()  # The second matrix is created by the user
    if len(firstMatrix) == len(secondMatrix):  # Checks whether the matrices can be added or not
        print(firstMatrix)
        print(secondMatrix)
        finalMatrix = []  # Vector that will contain the full matrix
        for i in range(len(firstMatrix)):  # Will through each row in the matrix
            matrix = []  # Vector that will get all the rows in the matrix
            for j in range(len(secondMatrix[0])):  # Will go through each column
                sumNum = firstMatrix[i][j] + secondMatrix[i][j]  # Will add each individual cell
                matrix.append(sumNum)
                print(matrix)
            finalMatrix.append(matrix)
        print("The sum of the two matrices is: " + str(finalMatrix))
    else:
        print("This operation cannot be done because the dimensions of the matrices are not the same. "
              "Try again :)")
        matrixaddition()


matrixaddition()
