from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        neighbours = [[i+1] for i in range(n)]

        def bfs():
            visited = set()
            queue = deque()
            queue.append((0,0))

            while queue:
                current,distance = queue.popleft()
                if current==n-1:
                    return distance
                for neighbour in neighbours[current]:
                    if neighbour in visited:
                        continue

                    queue.append((neighbour,distance+1))
                    visited.add(neighbour)

        res = []
        for src,desc in queries:
            neighbours[src].append(desc)
            res.append(bfs())

        return res