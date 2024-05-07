from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []

        for i in range(9):
            for k in range(9):
                element = board[i][k]
                if element!='.':
                    res.append((element,i))
                    res.append((k,element))
                    res.append((element,i//3,k//3))
        return len(res) == len(set(res))


print(Solution().isValidSudoku(board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))