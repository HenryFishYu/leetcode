import heapq
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        len_r = len(maze)
        len_c = len(maze[0])
        queue = []
        visited = set()

        queue.append((0,(entrance[0],entrance[1])))
        while queue:
            distance,(r,c) = queue.pop(0)
            if c<0 or c>=len_c or r<0 or r>=len_r:
                continue

            if maze[r][c]=="+":
                continue

            if (r,c) in visited:
                continue

            if (c==0 or c==len_c-1 or r==0 or r==len_r-1) and (r,c)!=(entrance[0],entrance[1]):
                return distance

            visited.add((r,c))
            queue.append((distance + 1, (r, c + 1)))
            queue.append((distance + 1, (r, c - 1)))
            queue.append((distance + 1, (r + 1, c)))
            queue.append((distance + 1, (r - 1, c)))

        return -1

print(Solution().nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],[1,2]))

