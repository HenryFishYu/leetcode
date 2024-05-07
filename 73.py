from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        topLeft = False

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        topLeft = True

        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0

        if matrix[0][0]==0:
            for r in range(len(matrix)):
                matrix[r][0] = 0

        if topLeft:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(matrix)
for row in matrix:
    print(row)