from typing import List


class Solution:
    def rotate_matrix(self, matrix):
        """
        Rotates a 2D matrix by 90 degrees clockwise.

        Args:
            matrix (list of lists): The input matrix to be rotated.

        Returns:
            list of lists: The rotated matrix.
        """
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]

        return matrix

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rotated_board = self.rotate_matrix(board)
        def match(word:str, board: List[List[str]]):
            for item in board:
                if word in "".join(item):
                    return True
            return False
        res = []
        for word in words:
            if match(word,board) or match(word,rotated_board):
                res.append(word)

        return res
