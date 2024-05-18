from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        number_of_rows = len(board)
        number_of_columns = len(board[0])
        visited = set()
        def backtrack(r: int, c: int, i: int):
            if i==len(word):
                return True
            if (r,c) in visited:
                return False
            if r>=number_of_rows or r<0 or c>=number_of_columns or c<0:
                return False
            if board[r][c] == word[i]:
                visited.add((r,c))
                if backtrack(r+1,c,i+1) or backtrack(r - 1, c, i + 1) or backtrack(r, c+1, i + 1) or backtrack(r, c-1, i + 1):
                    return True
                visited.remove((r,c))
                return False

        for r in range(number_of_rows):
            for c in range(number_of_columns):

                if backtrack(r,c,0):
                    return True
        return False

print(Solution().exist([["a","a","a"],["A","A","A"],["a","a","a"]],"aAaaaAaaA"))





