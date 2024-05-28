from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = [[0] * (COLS+1) for _ in range(ROWS+1)]
        res = 0
        for r in range(ROWS-1,-1,-1):
            for c in range(COLS - 1, -1, -1):
                if matrix[r][c] == "1":
                    cache[r][c] = 1+ min(cache[r+1][c],cache[r][c+1],cache[r+1][c+1])
                    res = max(res,cache[r][c])

        return res*res


