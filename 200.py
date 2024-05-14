from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != "1":
                return
            grid[x][y] = "0"
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for i in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[i][k] == "1":
                    res += 1
                    dfs(i, k)

        return res
