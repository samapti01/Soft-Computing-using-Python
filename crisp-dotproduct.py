# -*- coding: utf-8 -*-
//crisp relation dot product
def inputMatrix(which):
    row = int(input(f"Enter the number of rows for the {which} matrix:\n"))
    matrix = []
    for i in range(0, row):
        mat_row = [int(a) for a in input(
            f"Enter {i+1}th row as space separated list:\n").split(" ")]
        matrix.append(mat_row)
    return matrix


matrix1 = inputMatrix("first")
print("")
matrix2 = inputMatrix("second")


def dotproduct(matrix1, matrix2):
    row1 = len(matrix1)
    col2 = len(matrix2[0])
    row2 = len(matrix2)

    matrix3 = []
    for i in range(0, row1):
        li = []
        for j in range(0, col2):
            res = 0
            for k in range(0, row2):
                res = max(res, (matrix1[i][k]*matrix2[k][j]))
            li.append(res)
        matrix3.append(li)
    return matrix3


print("\nThe resultant matrix:\n",dotproduct(matrix1, matrix2))