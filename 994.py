from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        len_r = len(grid)
        len_c = len(grid[0])
        queue = deque()
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c]==2:
                    queue.append((0,(r,c)))
                    grid[r][c]=1

        while queue:
            min,(r,c) = queue.popleft()
            if r<0 or r==len_r or c<0 or c==len_c or grid[r][c]!=1:
                continue
            res = min
            grid[r][c]=2
            queue.append((min+1,(r+1,c)))
            queue.append((min + 1, (r - 1, c)))
            queue.append((min + 1, (r, c+1)))
            queue.append((min + 1, (r, c-1)))

        for r in grid:
            for e in r:
                if e==1:
                    return -1

        return res


print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))


