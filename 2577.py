import heapq
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1]>1 and grid[1][0]>1:
            return -1


        r_len = len(grid)
        c_len = len(grid[0])

        queue = []
        queue.append((0,0,0))

        visited = set()
        while queue:
            time,r,c = heapq.heappop(queue)
            if r == r_len-1 and c==c_len-1:
                return time

            neighbours = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]
            for new_r, new_c in neighbours:
                if new_r < 0 or new_c < 0 or new_r == r_len or new_c == c_len or (new_r,new_c) in visited:
                    continue
                difference = abs(grid[new_r][new_c]-time)
                wait = 1
                if difference&1:
                    wait=0


                heapq.heappush(queue,(max(time+1,grid[new_r][new_c]+wait),new_r,new_c))
                visited.add((new_r, new_c))

