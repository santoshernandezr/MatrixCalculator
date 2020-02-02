firstMatrix = [[1, 2, 3],
               [4, 5, 6],
               [5, 6, 7]]
secondMatrix = [[4, 7, 3],
                [8, 6, 8],
                [9, 1, 7]]
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
