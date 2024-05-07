from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)
        halfLength = length//2
        def transpose():
            for i in range(length):
                for k in range(i,length):
                    matrix[i][k],matrix[k][i] = matrix[k][i],matrix[i][k]

        def reverse_row():
            for i in range(length):
                for k in range(halfLength):
                    matrix[i][k],matrix[i][-(k+1)] = matrix[i][-(k+1)],matrix[i][k]

        transpose()
        reverse_row()

matrix = [[1,2,3],[4,5,6],[7,8,9]]

Solution().rotate(matrix)
print(matrix)