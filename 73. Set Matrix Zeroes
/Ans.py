from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = len(matrix)
    col = len(matrix[0])
    zero_rowi=[]
    zero_colj=[]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                zero_rowi.append(i)
                zero_colj.append(j)
    for i in range(row):
        for j in range(col):
            if i in zero_rowi or j in zero_colj:
                matrix[i][j] = 0
    return matrix            


print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))