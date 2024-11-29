from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        r_len = len(grid)
        c_len = len(grid[0])

        queue = deque()

        queue.append((0,0,0))

        visited = set()
        while queue:
            obstacles,r,c = queue.popleft()
            if r==r_len-1 and c==c_len-1:
                return obstacles
            if (r,c) in visited:
                continue
            neighbours = [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]
            for new_r,new_c in neighbours:
                if new_r<0 or new_c<0 or new_r==r_len or new_c==c_len:
                    continue
                if grid[new_r][new_c]:
                    queue.append((obstacles+1,new_r,new_c))
                else:
                    queue.appendleft((obstacles, new_r, new_c))

            visited.add((r,c))

Solution().minimumObstacles([[0,1,1],[1,1,0],[1,1,0]])

