from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        original | new | flag
        0        |  0  |  0
        1        |  0  |  1
        0        |  1  |  2
        1        |  1  |  3
        """

        def count_neighbors(i_r,i_c):
            res = 0
            for r in range(i_r-1,i_r+2):
                for c in range(i_c-1,i_c+2):
                    if r<0 or c<0 or r==len_r or c==len_c or (r==i_r and c==i_c):
                        continue
                    if board[r][c] in [1,3]:
                        res += 1
            return res

        len_r = len(board)
        len_c = len(board[0])

        for r in range(len_r):
            for c in range(len_c):
                neighbors = count_neighbors(r,c)
                if board[r][c]:
                    if neighbors in [2,3]:
                        board[r][c]=3
                    continue

                if neighbors==3:
                    board[r][c] = 2

        for r in range(len_r):
            for c in range(len_c):
                if board[r][c]==1:
                    board[r][c]=0
                    continue

                if board[r][c] in [2,3]:
                    board[r][c] = 1








