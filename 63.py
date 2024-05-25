from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        res = [[0] * (COLS + 1) for _ in range(ROWS+1)]
        res[ROWS - 1][COLS] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    continue
                res[r][c] = res[r + 1][c] + res[r][c + 1]

        return res[0][0]

print(Solution().uniquePathsWithObstacles([[0,0]]))