from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a,b) for a,b in connections}
        map = {city:[] for city in range(n)}
        for a,b in edges:
            map[a].append(b)
            map[b].append(a)
        visited = set()
        res = 0

        def dfs(city:int):
            nonlocal res
            for dest in map[city]:
                if dest in visited:
                    continue
                if (dest,city) not in edges:
                    res+=1
                visited.add(dest)
                dfs(dest)
        visited.add(0)
        dfs(0)

        return res

print(Solution().minReorder(3,[[1,0],[2,0]]))
