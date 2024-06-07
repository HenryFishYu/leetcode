from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """



        def valid_set(r,c):
            occupied = set()
            occupied.update(board[r])
            for i in range(9):
                occupied.add(board[i][c])
            new_r = 3*(r//3)
            new_c = 3*(c//3)
            for i_r in range(new_r,new_r+3):
                for i_c in range(new_c,new_c+3):
                    occupied.add(board[i_r][i_c])
            return occupied

        def dfs(r,c):
            if r==9:
                return True
            if c==9:
                return dfs(r+1,0)
            if board[r][c]!=".":
                return dfs(r, c+1)
            else:
                for i in range(1,10):
                    s_i = str(i)
                    if s_i not in valid_set(r,c):
                        board[r][c] = s_i
                        if dfs(r,c+1):
                            return True
                        else:
                            board[r][c] = "."
                return False

        dfs(0,0)

res = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(res)
print(res)