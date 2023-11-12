import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #  Transpose the matrix
        c = len(matrix[0])
        r = len(matrix)
        mid = c//2
        # print(mid)
        # n = len(matrix)
        # for i in range(n):
        #     for j in range(i, n):
        #         matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        matrix[:] = np.transpose(matrix)
        
        print(matrix)
        # print(matrix)

        for i, rows in enumerate(matrix):
            k = 0 
            while (k < mid):
                temp = matrix[i][k]
                matrix[i][k] = matrix[i][c-1-k]
                matrix[i][c-1-k] = temp
                k = k + 1
        print(matrix)    
        
        